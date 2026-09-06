<div align="center">

# 서명석 · Myungseok Seo

### DevOps / GitLab Engineer · 7년차

**배포 이후의 세계를 담당합니다** — 온프렘부터 클라우드, 그리고 폐쇄망까지

**플래티어** IDT · 경기 성남

[![외주 문의](https://img.shields.io/badge/외주_·_기술자문_문의하기-2EA043?style=for-the-badge&logo=github&logoColor=white)](https://github.com/smshack/smshack/issues/new/choose)
[![포트폴리오](https://img.shields.io/badge/포트폴리오-000000?style=for-the-badge&logo=Notion&logoColor=white)](https://northern-breath-ec3.notion.site/a567896700704dcb9c642913a76d6fa6)
[![데모](https://img.shields.io/badge/라이브_데모-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://welfare-navigator.vercel.app)

</div>

---

개발자는 코드를 알고, 저는 **그 코드가 실제로 도는 곳**을 압니다.
코드 리뷰에서는 안 보이고 새벽 3시에 보이는 층입니다.

```mermaid
flowchart LR
    A["코드<br/>개발자"] --> B["CI<br/>GitLab CI"] --> C["배포<br/>ArgoCD · Helm"] --> D["런타임<br/>K8s · 모니터링"] --> E["장애<br/>Grafana · 로그"]
    style A fill:#e8e8e8,stroke:#999,color:#333
    style B fill:#FC6D26,stroke:#FC6D26,color:#fff
    style C fill:#FC6D26,stroke:#FC6D26,color:#fff
    style D fill:#FC6D26,stroke:#FC6D26,color:#fff
    style E fill:#FC6D26,stroke:#FC6D26,color:#fff
```

<sub>주황색 구간이 제가 7년간 서 있던 자리입니다. 대부분의 개발자는 첫 칸까지만 봅니다.</sub>

<br>

## 이런 일을 맡기실 수 있습니다

<table>
<tr><th width="26%">무엇을</th><th width="46%">실제로 해본 것</th><th width="28%">어디서</th></tr>
<tr>
<td><b>🔒 폐쇄망 · 망분리 환경</b><br/><sub>검색으로는 안 나오는 영역</sub></td>
<td>Air-Gapped 개발·배포 인프라 구성<br/>내부 Package/Container Registry, 오프라인 Artifact 관리<br/>사설 CA 및 내부 DNS/네트워크 구성<br/>소스·Artifact 반출입을 고려한 형상관리·배포 구조</td>
<td>와트<br/>플래티어</td>
</tr>
<tr>
<td><b>📡 WebRTC 실시간 통신 인프라</b></td>
<td>STUN / TURN / ICE 환경 구성 및 Coturn 운영<br/>Janus · Jitsi · Kurento · aiortc 미디어 서버 검토·구축<br/>실시간 영상·음성 연결 및 네트워크 문제 분석</td>
<td>와트</td>
</tr>
<tr>
<td><b>⚙️ GitLab · CI/CD 구축·운영</b></td>
<td>GitLab CE <b>직접 구축·운영</b> (SaaS 아님)<br/>GitLab Runner + Docker CI 구성 및 트러블슈팅<br/>Jenkins Pipeline 빌드·배포 자동화<br/>ArgoCD + Kustomize 배포 자동화<br/>SonarQube 품질 게이트 · Black Duck 취약점 관리<br/>Harbor / Nexus 사내 Registry 운영</td>
<td>플래티어<br/>와트<br/>라온피플</td>
</tr>
<tr>
<td><b>☸️ 쿠버네티스 환경 구축</b><br/><sub>온프렘 · 클라우드 · 폐쇄망</sub></td>
<td>kubespray · kubeadm로 온프렘 클러스터 <b>밑바닥부터</b> 구축<br/>ingress-nginx · rook-ceph · Helm 구성<br/>Azure AKS 리소스 및 계정 권한 설계<br/>Pod · Service · PVC · NetworkPolicy 운영 및 장애 분석</td>
<td>와트<br/>오베네프<br/>라온피플</td>
</tr>
<tr>
<td><b>📊 모니터링 · 관측 스택</b></td>
<td>Prometheus · Grafana · Thanos 구성<br/>cAdvisor · Node Exporter 기반 컨테이너/호스트 관측<br/>Grafana API로 대시보드 배포 자동화</td>
<td>와트<br/>라온피플</td>
</tr>
<tr>
<td><b>🖥️ 서버 · DB · 인프라 운영</b></td>
<td>Ubuntu 서버 구축, Nginx Reverse Proxy 및 LB 구성<br/>AWS EC2 · Naver Cloud · GCP · 코로케이션<br/>PostgreSQL · MySQL · MSSQL · MongoDB · Redis 운영</td>
<td>와트<br/>오베네프</td>
</tr>
<tr>
<td><b>🌐 웹 서비스 개발</b><br/><sub>기획부터 배포까지</sub></td>
<td>React · Next.js · TypeScript · Tailwind · MUI · shadcn/ui<br/>Express · NestJS · Spring Boot(Java 17) · gRPC<br/>Keycloak SSO · JWT 인증 연동<br/>Figma 기획 → Vercel 배포까지 단독 진행</td>
<td>와트<br/>엔아이<br/>오베네프</td>
</tr>
</table>

> **혼자서 기획부터 운영까지 닫을 수 있습니다.**
> LMS 백엔드 단독 전담, 온프렘 K8s 단독 구축, 홈페이지 기획–배포 단독 진행 — 전부 혼자 끝냈습니다.
>
> **드문 조합 두 가지를 갖고 있습니다.** 하나는 **폐쇄망**, 하나는 **WebRTC**입니다.
> 둘 다 문서를 읽어서는 안 되고, 실제로 안 되는 걸 붙잡고 있어 본 사람만 합니다.

<br>

## 만든 것

<details open>
<summary><b>복지 내비게이터</b> — 자기 조건을 모르는 사람을 위한 복지 안내 &nbsp;<a href="https://welfare-navigator.vercel.app">🔗 라이브</a></summary>

<br>

자기가 중위소득 몇 %인지 몰라도, 상황을 일상어로 적으면 받을 수 있는 지원을 찾아줍니다.

> 정부 서비스는 **조건을 정확히 아는 사람**에게 답합니다.
> 이건 **자기 조건을 모르는 사람**에게 답합니다.

기존 서비스를 직접 클릭해 측정하고, 그 숫자를 목표로 잡았습니다.

| | 기존 서비스 (실측) | 복지 내비게이터 |
|---|---|---|
| 결과까지 상호작용 | 11회 | **1회** |
| 결과 전 필수 입력 | 4종 | **0종** |
| 결과 건수 | 50개 | **5~8개** (근거·예상 금액 포함) |

`Next.js 16` `React 19` `TypeScript` `Tailwind` `Vercel`

</details>

<details>
<summary><b>kuber-resource / docker-resource</b> — 운영하며 실제로 쓴 Helm 차트와 리소스 설정</summary>

<br>

검색해도 안 나와서 직접 정리한 것들입니다. 예제가 아니라 **실서비스에 올라간 설정**입니다.

- [kuber-resource](https://github.com/smshack/kuber-resource) — Helm 및 사용 리소스 정리
- [docker-resource](https://github.com/smshack/docker-resource) — 컨테이너 리소스 설정 정리

</details>

<details>
<summary><b>devops-portfolio</b> — 오픈소스를 <i>운영 관점</i>에서 뜯어보는 기록 <sub>(진행 중)</sub></summary>

<br>

기능이 아니라 **붙였을 때 뭐가 터지는지**를 봅니다. 현재 Keycloak.
→ [저장소](https://github.com/smshack/devops-portfolio)

</details>

<br>

## 경력 · 7년

<sub>펼쳐서 보실 수 있습니다.</sub>

<details open>
<summary><b>(주)플래티어</b> · DevOps / GitLab 엔지니어 · <code>2026.07 ~ 재직중</code></summary>

<br>

IDT 부서. 사내 GitLab / CI 플랫폼 운영.
모든 팀의 파이프라인이 지나가는 자리라, 조직이 어디서 반복해서 넘어지는지가 보입니다.

</details>

<details>
<summary><b>주식회사 와트</b> (WATTCO) · Software / DevOps Engineer · <code>2024.07 ~ 2026.07</code> <sub>(2년 1개월)</sub></summary>

<br>

**가장 넓은 층을 다룬 2년입니다.** 개발과 인프라를 동시에 맡았습니다.

**CI/CD · DevOps 환경 구축·운영**
- GitLab CE 기반 형상관리 및 CI/CD 환경 구축·운영
- Jenkins Pipeline을 활용한 빌드·배포 자동화
- GitLab Runner 및 Docker 기반 CI 환경 구성 및 트러블슈팅
- Docker Compose 기반 개발·운영 환경 구성
- SonarQube 코드 품질 관리 / Black Duck 오픈소스·보안 취약점 관리
- Harbor · Nexus 사내 Artifact 및 Container Registry 운영

**실시간 통신 / WebRTC 인프라**
- WebRTC 기반 실시간 통신 서비스 인프라 구축 및 운영
- STUN / TURN / ICE 환경 구성 및 Coturn 운영
- Janus, Jitsi, Kurento, aiortc 등 미디어 서버 검토·구축
- 실시간 영상·음성 통신 환경의 네트워크 및 연결 문제 분석

**망분리 · 폐쇄망 환경 대응**
- Air-Gapped 환경을 고려한 개발·배포 인프라 구성
- 내부 Package / Container Registry 및 오프라인 Artifact 관리 환경 검토
- 사설 CA 및 내부 DNS / 네트워크 환경을 고려한 서비스 구성
- 망분리 환경에서 소스코드·Artifact 반출입을 고려한 형상관리·배포 구조 검토

**컨테이너 · 쿠버네티스**
- kubeadm 및 Minikube 기반 클러스터 구성
- Pod, Service, PVC, Network Policy 등 리소스 운영 및 장애 분석

**서버 · 인프라**
- Ubuntu 서버 환경 구축 및 운영, Nginx Reverse Proxy 및 Load Balancer 구성
- AWS EC2 및 Naver Cloud 기반 인프라 구성
- PostgreSQL, MySQL, MSSQL, MongoDB, Redis 운영
- Prometheus, Grafana, cAdvisor, Node Exporter 모니터링 환경 구성

**웹 애플리케이션 개발**
- React, Next.js, TypeScript 프론트엔드 / Express, NestJS, Spring Boot(Java 17) 백엔드
- Context API, Tailwind CSS, MUI, shadcn/ui 기반 UI 구현

**장애 분석 및 기술 지원**
- GitLab, GitLab Runner, Jenkins, Docker, Kubernetes 등 개발 인프라 장애 원인 분석·해결
- 네트워크, DNS, 권한, 인증서, Container Registry, WebSocket 운영 이슈 트러블슈팅
- 개발팀의 빌드·배포 및 개발환경 기술 지원

</details>

<details>
<summary><b>라온피플 주식회사</b> · DevOps · AI 플랫폼팀 · <code>2024.01 ~ 2024.06</code></summary>

<br>

- Azure AKS 리소스 활용 및 계정 권한 관리
- Prometheus, Grafana, Thanos를 활용한 모니터링 세팅
- 모니터링 시스템 배포 자동화 (ArgoCD, Kustomize, Job + Grafana API 활용)

</details>

<details>
<summary><b>주식회사 엔아이</b> · 웹마스터 / 개발팀장 · <code>2023.05 ~ 2024.01</code></summary>

<br>

- **개발 프로세스 수립** — git flow 기반 개발문화 세팅, Notion·Slack 업무 체계
- **[자사 홈페이지 구축](https://www.nimarketing.co.kr/)** — Figma 기획부터 Vercel 배포까지 단독 진행, SEO 고려한 설계, 채널톡 연동
- **크롤링 및 댓글 자동화 시스템** — 광고 댓글 자동화 및 로깅

</details>

<details>
<summary><b>(주)판도플랫폼</b> · 음성인식 미들웨어 · <code>2022.09 ~ 2023.05</code></summary>

<br>

- STT / TTS를 활용한 주문 시스템 엔티티 생성 로직 미들웨어
- gRPC를 이용한 음성 데이터 중간 처리 및 S3 저장
- 배달 주소 검색 가중치 로직 구현
- 기존 로직 및 코드 최적화

</details>

<details>
<summary><b>주식회사 오베네프</b> · 웹마스터 / 백엔드 단독 · <code>2020.10 ~ 2022.04</code> <sub>(1년 7개월)</sub></summary>

<br>

**가장 넓은 층을 혼자 다룬 시기입니다.**

- **온프렘 K8s 환경 구축** (2021.09~) — kubespray로 직접 구축, ingress-nginx · rook-ceph를 Helm으로 구성, Prometheus & Grafana 모니터링
- **실습실 시스템** — `kubernetes/client-node`로 API 개발, 유저별 namespace 할당, 생성 시 Secret·PV 할당 및 Pod 생성, ingress-nginx로 웹 접근 제공
- **LMS 백엔드 전부 단독 개발** (Express + MongoDB) — 강의·수강생·강사 CRUD, 진도율 체크 API, `aggregate` 기반 admin 통계 API, video.js와 연동해 5초 단위 진도 저장 (React 측도 함께)
- **Keycloak SSO** (2021.08) — Docker + react-keycloak으로 학사 사이트 ↔ LMS 사이트 SSO 연동
- **DB 마이그레이션 시스템** — 대학교 학사 DB ↔ LMS DB, 생성·수정·삭제 비교 로직으로 주기적 연동
- **도메인 및 서버 관리** — GCP, 코로케이션 서버, nginx
- JWT + Redux 로그인, React 초기 구조 설계

</details>

<details>
<summary><b>(주)엔리치소프트</b> · SQA · KT 과금팀 · <code>2018.08 ~ 2020.01</code> <sub>(1년 6개월)</sub></summary>

<br>

- 서버 모니터링, 장애 초기 대응 및 전파
- 오라클 데이터 사용량 조회

<sub>장애가 실제로 어떻게 터지고 어떻게 번지는지를 여기서 배웠습니다.</sub>

</details>

<br>

## 일하는 방식

<table>
<tr><td width="26%"><b>계약 형태</b></td><td>프로젝트 단위 · 시간제 자문 · 단발성 트러블슈팅 모두 가능합니다.</td></tr>
<tr><td><b>진행 방식</b></td><td>원격 기본. 폐쇄망처럼 <b>현장에 가야만 되는 일</b>은 방문합니다 — 반입 절차가 있는 환경을 여러 번 겪었습니다.</td></tr>
<tr><td><b>시작할 때</b></td><td>먼저 <b>지금 뭐가 안 되는지</b>부터 봅니다. 구성도와 범위를 문서로 먼저 맞추고 손을 댑니다.<br/>기획이 덜 된 상태로 들어가면 왕복만 늘어난다는 걸 비싸게 배웠습니다.</td></tr>
<tr><td><b>남기는 것</b></td><td>작업이 끝나면 <b>다음 사람이 읽고 운영할 수 있는 문서</b>를 같이 드립니다. 저 없이 굴러가야 끝난 겁니다.</td></tr>
<tr><td><b>안 맡는 일</b></td><td>제가 안 해본 영역은 안 해봤다고 말씀드립니다. 되는 척하고 배우면서 하는 게 제일 비쌉니다.</td></tr>
</table>

<br>

## 다뤄본 것

<sub>배지 나열 대신 <b>어디서 굴려봤는지</b>로 적습니다.</sub>

| 층 | 무엇을 | 어디서 |
|---|---|---|
| **CI/CD** | GitLab CE·GitLab CI·GitLab Runner, Jenkins, ArgoCD, Kustomize, Helm | 사내 전 개발팀 파이프라인 운영, GitLab CE 직접 구축 |
| **품질·보안** | SonarQube, Black Duck, Harbor, Nexus, 사설 CA | 납품 대응 품질 게이트 및 사내 Registry 운영 |
| **인프라** | Kubernetes(kubespray·kubeadm·AKS·Minikube), Docker, Docker Compose, rook-ceph, ingress-nginx | 온프렘 클러스터 단독 구축, 폐쇄망 반입 |
| **관측** | Prometheus, Grafana, Thanos, cAdvisor, Node Exporter | AI 플랫폼·실서비스 모니터링 스택 구성 |
| **실시간 통신** | WebRTC, Coturn(STUN/TURN/ICE), Janus, Jitsi, Kurento, aiortc | 실시간 영상·음성 서비스 인프라 구축·운영 |
| **서버·네트워크** | Ubuntu, Nginx(Reverse Proxy·LB), DNS, 인증서, WebSocket | 서비스 운영 및 장애 트러블슈팅 |
| **클라우드** | AWS(EC2·S3), Azure, GCP, Naver Cloud, Vercel, 코로케이션 | 서비스 운영·배포 |
| **백엔드** | Node.js, NestJS, Express, Spring Boot(Java 17), gRPC | LMS 단독 개발, 음성 미들웨어, 사내 API |
| **DB** | PostgreSQL, MySQL, MSSQL, MongoDB, Redis, Oracle | 다중 DB 환경 운영 |
| **프론트** | React, Next.js, TypeScript, Redux, Tailwind, MUI, shadcn/ui | LMS, 자사 홈페이지, 복지 내비게이터 |
| **인증** | Keycloak(SSO), JWT | 두 사이트 간 SSO 연동 |

<br>

---

<div align="center">

**외주 · 기술자문 문의를 받고 있습니다.**

폐쇄망 구축 · WebRTC 인프라 · GitLab/CI-CD 이관 · 쿠버네티스 · 모니터링,<br/>또는 기획부터 배포까지 통째로.

[![문의하기](https://img.shields.io/badge/문의_남기기-2EA043?style=for-the-badge&logo=github&logoColor=white)](https://github.com/smshack/smshack/issues/new/choose)
[![Email](https://img.shields.io/badge/5432tat@naver.com-555555?style=for-the-badge&logo=maildotru&logoColor=white)](mailto:5432tat@naver.com)
[![Notion](https://img.shields.io/badge/상세_포트폴리오-000000?style=for-the-badge&logo=Notion&logoColor=white)](https://northern-breath-ec3.notion.site/a567896700704dcb9c642913a76d6fa6)

</div>
