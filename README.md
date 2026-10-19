[한국어 웹 이력서](https://seummin.github.io/CV/) · [English CV website](https://seummin.github.io/CV/en.html)

[한국어 텍스트](./README.md) · [English text](./resume-en.md)

<img src="./portrait.png" alt="신승민 프로필 사진" width="108" align="right">

# 신승민

AI Engineer · LLM & AI Agents

seungminshin00@gmail.com · +82 10 4522 0340 · https://github.com/seummin

LLM과 AI Agent를 개발하는 AI Engineer입니다. 사용자 메모리·Agent 도구·보안관제 LLM의 문제 정의와 평가부터 API 구현·추론 서빙까지 담당합니다. 롯데이노베이트 AI Tech Lab에 재직 중이며, 성균관대학교 인공지능 석사로 제어 가능한 대화 생성 연구를 EMNLP 2025 Main Conference에 제1저자로 발표했습니다.

## 경력

### 롯데이노베이트 | 2025.02 – 현재

AI Engineer · AI Tech Lab

사용자 맥락을 활용하는 LLM 서비스와 Agent 시스템을 개발합니다. 데이터·과제 설계, 모델 평가·파인튜닝, API 구현 및 운영 시스템 연동을 담당합니다.

- 사용자 프로필 메모리의 문제·평가 과제를 정의하고 추출·저장·조회 API와 비동기 처리 구조를 구현했습니다.
- 보안관제의 공격 분류·근거 추출·설명을 통합하고, 신뢰도 산출과 vLLM·FastAPI 추론 서비스를 개발했습니다.
- 금융·경제 데이터와 사용자·상품 DB를 연결하는 Agent 도구를 개발하고, 입력 검증·재질의·오류 복구 흐름을 설계했습니다.

### 성균관대학교 자연어처리 연구실 | 2023.03 – 2025.02

석사과정 연구원

제어 가능한 대화 생성과 LLM 추론 평가를 연구했습니다.

- 토큰별 엔트로피로 속성 제어 강도를 조정하는 ECO Decoding을 제안하고, 자동 평가·ablation·사람 평가로 검증했습니다.
- 1,000개 샘플과 BERT 환경 모델로 스무고개형 추론 벤치마크를 구축하고 소프트웨어 자산으로 등록했습니다.

## 주요 프로젝트

### 대화 기반 사용자 프로필 메모리 | 2025 – 2026

롯데이노베이트 · 문제 정의, 평가 설계, 메모리 API·비동기 처리 구현

세션이 바뀌면 사라지는 사용자 맥락과 전체 대화 입력의 비용·지연 문제를 해결하기 위해, 장기간 재사용할 직무·관심·선호를 구조화된 프로필로 저장하고 응답에 주입하는 시스템을 개발했습니다.

- 실제 질의를 분석해 직무에 따라 의미가 달라지는 약어 해석을 평가 과제로 선정했습니다. 원천 사용자 50명 중 약어가 등장한 44명·326개 약어·454개 대화로 평가셋을 구성하고, 정답 노출과 중복 사례를 점검했습니다.
- 전체 히스토리와 사용자 발화만을 이용한 추출, system/user 메시지 주입을 비교했습니다. 동일 약어 평가셋에서 GPT-4.1-mini 정확도를 프로필 미사용 68.94% → 80.40% (+11.46%p)로 개선했습니다.
- 긴 갱신 작업을 job과 사용자·대화 청크별 task로 분리했습니다. 진행 상태 조회, 부분 성공, 실패 청크 재시도와 사용자별 쓰기 잠금을 구현하고, 백엔드와 갱신 후 캐시 재조회 흐름을 맞춰 오래된 프로필이 사용되는 문제를 해결했습니다.
- 별도 배치 성능 실험에서 병렬 처리로 평균 처리 시간을 33.31초 → 19.77초 (40.6% 단축)로 줄였습니다. 구조화 출력 테스트 698건의 실패를 JSON 오류 4건과 null 입력 27건으로 분리해 개선 대상을 구체화했습니다.

Python / Structured Output / FastAPI / Job / Worker / DB / Cache / HMAC

### 보안관제 LLM과 추론 서비스 | 2025.04 – 2025.07

롯데이노베이트 · 데이터·과제 설계, 파인튜닝, 신뢰도 산출, 추론 API

별도 분류기와 설명 생성기의 판단이 어긋나는 문제를 줄이고 관제사가 판단 근거를 함께 확인할 수 있도록, 공격 여부·공격 구문·설명을 한 번에 생성하는 LLM을 개발했습니다.

- 모델별 오답에서 오라벨과 근거 불일치를 찾아 데이터 담당자에게 재라벨링을 요청하고, 정제된 데이터와 통합 JSON 과제로 모델을 비교·학습했습니다. 기존 분류 모델 대비 공격 탐지 정확도 +7.3%p를 기록했습니다.
- 위험도 확률 라벨과 반복 추론에 쓸 지연 여유가 없어, 공격 라벨 토큰의 로그 확률로 단일 추론 기반 신뢰도를 산출했습니다. Guided Decoding으로 출력 스키마를 고정하고 vLLM·FastAPI를 보안 시스템과 연동했습니다.
- 기록된 추론 테스트에서 642건을 총 58.706초에 처리했습니다(해당 테스트의 총 처리 시간 기준). 방법론을 HCLT-KACL 2025 제1저자 논문으로 발표했습니다.

PyTorch / Hugging Face / Guided Decoding / Token Log Probability / vLLM / FastAPI

### ORAK Game Agent · Pokémon Red | 2026.02 – 2026.04

롯데이노베이트 · Pokémon Red 계획·관측 전처리·상태 메모리·행동 선택

소형 LLM이 부분 관측 게임에서 좌표·이동·대화·전투를 한 번에 판단하며 실패를 반복하는 문제를 분석했습니다. 복합 추론을 현재 상태에 맞는 행동 후보 선택으로 바꾸는 Agent를 설계했습니다.

- Playbook으로 현재 스토리 목표를 제한하고, 필드·대화·전투 상태별 관측을 전처리했습니다. 그래프 탐색으로 유효한 이동 후보를 만들고 이전·현재 상태와 맵 메모리로 행동 결과를 확인했습니다.
- 팀은 Track 1 (Lightweight)·Track 2 (Open) 리더보드 모두 1위를 기록하고 Track 2 종합 1위를 수상했습니다. 직접 기여 범위는 여러 게임 중 Pokémon Red Agent입니다.

LLM Agent / MCP / PyBoy / Graph Search / State Memory
[대회 페이지](https://www.aicrowd.com/challenges/orak-game-agent-challenge-2025)

### 사내 AI 비서의 금융·경제 데이터 도구 | 2025.04 – 2025.10

롯데이노베이트 · Agent 도구 설계·개발·운영

사용자의 기업명·날짜·경제 용어를 외부 API가 요구하는 식별자로 연결해, 사내 AI 비서가 국내 주식·재무제표·거시경제 정보를 조회하도록 개발했습니다.

- KRX·한국은행 ECOS 등과 연동하고, 기업명 매핑·후보 검색·날짜 범위와 거래일 검증·스키마 제약으로 잘못된 인자가 실제 조회로 이어지는 경로를 다뤘습니다.
- 캐싱, 과거 데이터 보충, 재시도·fallback과 오류 격리를 구현하고 pytest로 주요 조회·예외 경로를 검증했습니다. MCP 인터페이스로 전환해 Agent가 조회 결과를 근거로 답변할 수 있도록 연결했습니다.

Python / MCP / KRX / ECOS / API Validation / pytest

### 개인 맞춤형 쇼핑 컨시어지 Agent PoC | 2025.05 – 2025.07

롯데이노베이트 · 고객 요구 구체화, DB 도구·중단 및 재개 흐름 구현

3개월의 PoC 기간에 사용자 프로필·구매 이력·상품 DB를 연결했습니다. 사용자가 말하지 않은 가격대나 상품 조건을 모델이 도구 인자로 만들어내는 오류를 해결했습니다.

- 고객사·내부 구성원과 추천 및 후속 필터링 시나리오를 정리하고, 사용자 조회·상품 조회·대화 상태의 책임을 분리했습니다.
- 짧은 개발 기간을 고려해 추가 학습보다 워크플로 개선을 선택했습니다. 필수 인자가 없으면 실행을 중단하고 구체적인 추가 질문을 한 뒤, 검증된 사용자 답변으로 재개하도록 수정했습니다. 일반·후속 질의 시나리오에서 사용자 조건의 반영을 확인했습니다.

Python / Smolagents / Tool Calling / DB Integration / Interrupt / Resume

## 연구 경험

### 검색 Agent의 요구조건 충족과 탐색 궤적 평가 | 2026.02 – 2026.06

Requirement-Aware Search Agent Trajectory Evaluation · 제1저자, 심사 중

최종 정답만으로는 중간 개체의 조건을 검증하지 않은 채 다음 개체로 탐색을 확장하는 실패를 놓칩니다. 이 현상을 Premature Downstream Expansion으로 정의하고, 질문의 요구조건이 실제 근거로 충족됐는지 평가하는 프레임워크를 제안했습니다.

- 목표·중간 개체와 원자적 요구조건을 분리하는 Requirement Closure Rubric을 설계했습니다. 요구조건 정제, 의존성 그래프 구성·가지치기, 단서 해결과 LLM-as-a-Judge 기반 턴별 근거 검증 파이프라인을 구현했습니다.
- GAIA·FRAMES·BrowseComp의 150문항, 10개 순차·병렬 Agent 설정, 1,500개 궤적을 공통 도구 환경에서 평가했습니다. 정답 정확도와 근거 충족을 구분해, 답이 맞아도 요구조건 검증이 빠질 수 있는 오류를 분석했습니다.

Benchmark Design / LLM-as-a-Judge / Entity Graph / Agent Evaluation

### ECO Decoding · 제어 가능한 대화 생성 | 2023 – 2025

성균관대학교 · 제1저자, EMNLP 2025 Main Conference

고정된 제어 강도가 불필요하게 다음 토큰을 바꾸거나 문장 유창성을 해치는 문제를 분석했습니다. 추가 학습이나 모델 구조 변경 없이 토큰별 엔트로피로 제어 강도를 조정하는 디코딩 방법을 제안했습니다.

- DailyDialog·MultiWOZ에서 DialoGPT와 LLaMA2를 감정·대화행위·다중 속성 조건으로 비교하고, 토큰·품사별 분석, ablation, 자동 지표와 사람 평가로 검증했습니다.
- 유창성을 유지하면서 속성 제어 성능을 평균 3.1%p 개선했습니다. 논문은 EMNLP 2025 Main Conference에 게재됐습니다.

PyTorch / Controllable Generation / Entropy / Decoding
[논문](https://arxiv.org/abs/2511.01568)

### 스무고개 기반 LLM 추론 벤치마크 | 2023 – 2024

성균관대학교 · 벤치마크·환경 모델·상태 추적 구현

LLM이 질문하고 BERT 환경 모델이 Yes/No/Unknown으로 답하는 상호작용형 평가를 구성했습니다. 1,000개 통제 샘플에서 정답률과 질문 효율을 비교하고 반복 실패 유형을 분석했으며, 결과물을 소프트웨어 자산으로 등록했습니다.


BERT / WordNet / Interactive Evaluation

## 논문

- [ECO Decoding: Entropy-Based Control for Controllability and Fluency in Controllable Dialogue Generation](https://arxiv.org/abs/2511.01568)
  Seungmin Shin, Dooyoung Kim, Youngjoong Ko. EMNLP 2025 · Main Conference. 게재.

- Diagnosing Premature Downstream Expansion in Multi-Hop Search Agents via Requirement Closure
  Seungmin Shin et al.. 2027 AAAI. Under Review.

- Acronym Meaning Selection for Improving Ambiguous Query Answering with User Profile Memory
  Seungmin Shin et al.. IEIE Summer Conference · 2026. 발표.

- Unified Inference and Confidence Calibration Method Using Large Language Models
  Seungmin Shin et al.. HCLT-KACL · 2025. 발표.

## 수상

ORAK Game Agent Challenge

Track 2 종합 1위

Track 1·2 리더보드 모두 1위 · 팀 수상, 2026

## Education

- 롯데 그룹사 임원 대상 AI 활용 교육 · 2026.08
- 롯데 그룹사 신입사원 AI 입문 교육 TA · 2025.09 / 2026.04 / 2026.06 / 2026.10
- 롯데 그룹사 경력사원 AI 입문 교육 TA · 2025.12 / 2026.04
- 롯데이노베이트 신입사원 대상 업무 자동화 교육 · 2026.06
- 조선대학교 AI 활용 강의 · 2025.12
- 「자연어처리 이론 및 응용」 수업 조교 · 2024.03 – 2024.06
- 「인공지능개론」 수업 조교 · 2017.03 – 2023.02

## 학력

### 성균관대학교

인공지능학과 석사 | 2023.03 – 2025.02

- GPA 4.17 / 4.5
- 자연어처리 연구실
- 지도교수 고영중

### 인하대학교

컴퓨터공학 학사 | 2017.03 – 2023.02

- GPA 3.89 / 4.5
- 전공 GPA 4.24 / 4.5

## 기술

- Programming: Python
- Modeling: PyTorch, Hugging Face Transformers, PEFT / LoRA
- Agents & Evaluation: Agent Orchestration, Agentic Search, Agentic Memory, Memory Augmented Generation, Tool Calling, MCP, Smolagents, Benchmark Design, LLM-as-a-Judge, Evaluation Framework
- Serving & Data: vLLM, FastAPI, Structured Output, DB·캐시 연동, 비동기 처리, pytest

## 연구 관심 분야

Large Language Models, AI Agents, Agentic Memory, Agentic Search, Evaluation Frameworks, Controllable Generation
