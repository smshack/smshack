"""README 의 <!-- x starts --> ~ <!-- x ends --> 구간을 GitHub 활동으로 갈아끼운다.

GitHub Actions 에서 매일 돌린다. 외부 의존성 없이 표준 라이브러리만 쓴다.
"""

import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta

USER = "smshack"
README = "README.md"
KST = timezone(timedelta(hours=9))
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-profile-builder",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        print(f"  ! {path} -> HTTP {e.code}")
        return []


def ago(iso):
    """ISO8601 을 '3일 전' 같은 한국어로."""
    t = datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    d = (datetime.now(timezone.utc) - t).days
    if d == 0:
        return "오늘"
    if d == 1:
        return "어제"
    if d < 30:
        return f"{d}일 전"
    if d < 365:
        return f"{d // 30}개월 전"
    return f"{d // 365}년 전"


def active_repos(limit=8):
    """최근 푸시된 공개 저장소 (아카이브·포크·프로필 저장소 제외)."""
    out = []
    for r in api(f"/users/{USER}/repos?sort=pushed&per_page=100"):
        if r.get("archived") or r.get("fork") or r["name"] == USER:
            continue
        out.append(r)
        if len(out) == limit:
            break
    return out


def build_activity():
    """저장소별 최신 커밋을 모아 시간순으로.

    events API 의 payload.commits 는 API 경유 커밋에서 비어 있는 경우가 있어
    저장소마다 최신 커밋을 직접 읽는다.
    """
    items = []
    for r in active_repos(6):
        commits = api(f"/repos/{USER}/{r['name']}/commits?per_page=1")
        if not commits:
            continue
        c = commits[0]
        msg = c["commit"]["message"].split("\n")[0].strip()
        if msg.startswith("chore: README 자동 갱신"):
            continue
        when = c["commit"]["author"]["date"]
        items.append((when, r["name"], msg))

    items.sort(reverse=True)
    lines = []
    for when, name, msg in items[:5]:
        if len(msg) > 50:
            msg = msg[:50] + "…"
        lines.append(
            f"**[{name}](https://github.com/{USER}/{name})** · {ago(when)}<br/>"
            f"<sub>{msg}</sub>"
        )
    return "\n\n".join(lines) if lines else "_아직 공개 활동이 없습니다._"


def build_repos():
    """최근 푸시된 공개 저장소."""
    lines = []
    for r in active_repos(5):
        desc = (r.get("description") or "").split("—")[0].strip()
        if len(desc) > 46:
            desc = desc[:46] + "…"
        lines.append(
            f"**[{r['name']}]({r['html_url']})** · {ago(r['pushed_at'])}<br/>"
            f"<sub>{desc}</sub>"
        )
    return "\n\n".join(lines) if lines else "_저장소가 없습니다._"


def replace(text, marker, body):
    pat = re.compile(
        rf"(<!-- {marker} starts -->).*?(<!-- {marker} ends -->)", re.DOTALL
    )
    if not pat.search(text):
        print(f"  ! 마커 '{marker}' 를 찾지 못했다")
        return text
    return pat.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(2)}", text)


def main():
    with open(README, encoding="utf-8") as f:
        text = original = f.read()

    print("최근 활동 수집…")
    text = replace(text, "activity", build_activity())
    print("저장소 목록 수집…")
    text = replace(text, "repos", build_repos())

    stamp = datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")
    text = re.sub(
        r"마지막 갱신 시각을 보시면 제가 살아 있는지 아실 수 있습니다\.[^<]*",
        f"마지막 갱신 시각을 보시면 제가 살아 있는지 아실 수 있습니다. 최종 갱신 {stamp}",
        text,
    )

    if text == original:
        print("변경 없음")
        return
    with open(README, "w", encoding="utf-8") as f:
        f.write(text)
    print("README 갱신됨")


if __name__ == "__main__":
    main()
