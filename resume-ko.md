[한국어 웹 이력서](https://seummin.github.io/CV/) · [English CV website](https://seummin.github.io/CV/en.html)

[한국어 텍스트](./README.md) · [English text](./resume-en.md)

<img src="./portrait.png" alt="신승민 프로필 사진" width="108" align="right">

# 신승민

AI Engineer · LLM & AI Agents

seungminshin00@gmail.com · +82 10 4522 0340 · https://github.com/seummin

LLM과 AI Agent를 개발하는 AI Engineer입니다. 사용자 메모리·Agent 도구·보안관제 LLM의 문제 정의와 평가부터 API 구현·추론 서빙까지 담당합니다. 롯데이노베이트 AI Tech Lab에 재직 중이며, 성균관대학교 인공지능 석사로 제어 가능한 대화 생성 연구를 EMNLP 2025 Main Conference에 제1저자로 발표했습니다.

## 경험

### 롯데이노베이트 | 2025.02 – 현재

AI Engineer · AI Tech Lab

그룹사 내부 AI 플랫폼과 고객사 서비스를 위한 LLM 기반 기능과 AI Agent를 개발합니다. 현업 요구를 분석해 해결할 문제와 서비스 적용 범위를 구체화합니다.

- 사내 서비스와 고객사 PoC의 목적에 맞는 Agent 구조를 설계합니다. DB와 외부 API를 연동하는 MCP 기반 도구와 사용자 정보 기반 개인화를 구현하고 태스크의 특성과 모델의 추론 역량에 맞춰 Agent의 역할과 실행 흐름을 설계합니다.
- 연구의 기여점과 한계를 분석하고 서비스 환경에서의 유효성을 검증합니다. 제한된 데이터와 운영 제약에 맞게 방법을 재설계하고 모델 학습과 평가부터 서빙과 운영까지 연결해 연구 결과를 실제 서비스로 구현합니다.
- 태스크에 맞는 평가 데이터와 지표 및 비교 실험을 설계해 AI 서비스를 정량적으로 검증합니다. 기존 평가에서 드러나지 않는 오류와 실행 과정의 실패를 분석하고 평가 방식과 AI 서비스를 개선합니다.

### 성균관대학교 자연어처리 연구실 | 2023.03 – 2025.02

석사과정 연구원

자연어처리 이론을 바탕으로 제어 가능한 대화 생성을 연구했습니다.

- 토큰별 엔트로피로 속성 제어 강도를 조정하는 ECO Decoding을 제안하고, 자동 평가·ablation·사람 평가로 검증했습니다.

## 주요 프로젝트

### User Profile Memory · 대화 기반 개인화 메모리 | 2025 – 2026

롯데이노베이트 · 메모리 도입 제안·평가 설계·서비스 구현 및 운영

세션이 달라져도 사용자 직무와 관심사를 응답에 활용할 수 있도록 사내 챗 서비스에 프로필 메모리를 설계·적용했습니다. 실제 대화로 개인화 효과를 평가하고, 대량 갱신 중 일부 작업이 실패해도 복구할 수 있도록 운영 구조를 개선했습니다.

- 대화 세션이 바뀌면 이전 대화에서 알게 된 사용자의 직무·관심사를 응답에 이어 쓰기 어려웠습니다. 매번 전체 대화를 입력하면 길이와 처리 시간이 늘어나므로, 반복 활용할 정보를 저장하는 프로필 메모리 도입을 제안했습니다.
- 사내 챗 서비스에 기존 메모리 구조를 적용하자 반복적인 LLM 호출로 갱신이 지연되고 활용되지 않는 정보가 쌓였습니다. 유용한 맥락을 보존하기 위해 무엇을 기억해야 응답이 개선되는지부터 평가하기로 했습니다.
- 실제 업무 대화에서 직무·관심사·기술 정보를 프로필로 구조화하고, 사용자에 따라 뜻이 달라지는 약어 해석을 개인화 평가 과제로 선정했습니다.
- 실제 로그로 구성한 평가 대화 454건에서 프로필 사용 여부를 비교한 결과, 약어 해석 정확도가 68.94%에서 80.40%로 개선됐습니다. 이 결과를 근거로 구조화된 프로필을 서비스에 적용했습니다.
- 갱신 요청이 시간 초과되면 완료 범위를 알 수 없어 전체를 재실행해야 했습니다. 사용자·대화 구간별 비동기 처리와 작업 상태 추적을 구현해 실패 구간만 재처리하고, 서빙 API 제한에 맞춰 동시 호출 수를 조절했습니다.

Python / FastAPI / Structured Output / User Profile Memory / 비동기 처리

### 보안관제 LLM과 추론 서비스 | 2025.04 – 2025.07

롯데이노베이트 · 데이터·과제 설계, 파인튜닝, 신뢰도 산출, 추론 API

별도 분류기와 설명 생성기의 판단이 어긋나는 문제를 줄이고 관제사가 판단 근거를 함께 확인할 수 있도록, 공격 여부·공격 구문·설명을 한 번에 생성하는 LLM을 개발했습니다.

- 모델별 오답에서 오라벨과 근거 불일치를 찾아 데이터 담당자에게 재라벨링을 요청하고, 정제된 데이터와 통합 JSON 과제로 모델을 비교·학습했습니다. 기존 분류 모델 대비 공격 탐지 정확도 +7.3%p를 기록했습니다.
- 위험도 확률 라벨과 반복 추론에 쓸 지연 여유가 없어, 공격 라벨 토큰의 로그 확률로 단일 추론 기반 신뢰도를 산출했습니다. Guided Decoding으로 출력 스키마를 고정하고 vLLM·FastAPI를 보안 시스템과 연동했습니다.
- 기록된 추론 테스트에서 642건을 총 58.706초에 처리했습니다(해당 테스트의 총 처리 시간 기준). 방법론을 HCLT-KACL 2025 제1저자 논문으로 발표했습니다.

PyTorch / Hugging Face / Guided Decoding / Token Log Probability / vLLM / FastAPI

### ORAK Game Agent Challenge · Pokémon Red Agent | 2026.02 – 2026.04

롯데이노베이트 · Pokémon Red의 입력 전처리·진행 상태 관리·행동 결정 설계 및 구현

제한된 행동 횟수 안에 Pokémon Red의 진행 목표를 수행하는 게임 Agent를 개발했습니다. 환경 상태와 이동 후보는 코드로 정리하고, 모델이 현재 목표에 맞는 행동을 선택하도록 설계했습니다.

- 200 step 안에 7개 목표를 달성해야 했지만 소형 모델은 원시 관측만으로 목표와 경로를 함께 판단하기 어려웠습니다. 코드가 유효한 행동 후보를 계산하고 모델이 선택하도록 역할을 나눴습니다.
- 지도·좌표·소지품·화면 텍스트로 진행 상태를 구성하고 Playbook에 하위 목표와 완료 조건을 명시했습니다. 그래프 탐색으로 이동 후보를 계산하고 상황별로 필요한 도구만 제공했습니다.
- 도구 호출의 정상 반환만으로는 행동 성공을 알 수 없어 실행 로그와 실제 상태 변화를 함께 평가했습니다. 좌표·화면·전투·소지품 변화를 근거로 반복 행동과 진행 실패를 확인했습니다.
- 실패 분석을 반영해 직전 행동과 상태 변화를 다음 판단에 제공하고, 상태별 유효 도구와 맵 전환 후보를 제한했습니다. 본인은 Pokémon Red를 담당했으며 팀은 Lightweight·Open Track 리더보드에서 모두 1위를 기록했습니다.

Python / LLM Agent / MCP / PyBoy / Graph Search / State Memory
[대회 페이지](https://www.aicrowd.com/challenges/orak-game-agent-challenge-2025)

### 사내 AI 비서의 금융·경제 데이터 도구 | 2025.04 – 2025.10

롯데이노베이트 · Agent 도구 설계·개발·운영

사용자의 기업명·날짜·경제 용어를 외부 API가 요구하는 식별자로 연결해, 사내 AI 비서가 국내 주식·재무제표·거시경제 정보를 조회하도록 개발했습니다.

- KRX·한국은행 ECOS 등과 연동하고, 기업명 매핑·후보 검색·날짜 범위와 거래일 검증·스키마 제약으로 잘못된 인자가 실제 조회로 이어지는 경로를 다뤘습니다.
- 캐싱, 과거 데이터 보충, 재시도·fallback과 오류 격리를 구현하고 pytest로 주요 조회·예외 경로를 검증했습니다. MCP 인터페이스로 전환해 Agent가 조회 결과를 근거로 답변할 수 있도록 연결했습니다.

Python / MCP / KRX / ECOS / API Validation / pytest

### 쇼핑 컨시어지 Agent PoC · 고객 데이터 기반 개인화 추천 | 2025.05 – 2025.07

롯데이노베이트 · 고객사 추천 시나리오 조율·평가 지표 설계·DB Tool 및 Agent 워크플로우 구현

고객사의 회원·구매 이력과 상품 DB를 연결해 자연어 요청에 맞는 상품을 추천하는 Agent PoC입니다. 필수 조건이 불명확할 때 모델이 값을 추측하는 대신 사용자에게 확인한 뒤 추천을 이어가도록 실행 흐름을 설계했습니다.

- 기존 추천 방식은 과거 구매 이력이나 유사 사용자 데이터에 치우쳐 현재 질의의 맥락과 상품 속성을 함께 반영하기 어려웠습니다. 고객 프로필·구매 이력·상품 DB를 연결해 개인화 추천의 가능성을 검증하는 PoC로 문제를 정의했습니다.
- 고객사와 일반 추천·후속 조건 질의의 기대 결과를 정리하고, Smolagents 기반으로 사용자 정보와 상품 정보를 조회하는 Tool을 분리해 구현했습니다. 고객 데이터 기반 평가 지표를 설계해 호출 성공과 개인화 조건 충족을 구분했습니다.
- 평가에서 Tool 호출은 성공해도 사용자 조건에 맞지 않는 추천을 확인했습니다. 호출 순서와 입력값을 추적해 모델이 누락된 가격대·상품 조건을 임의로 채우는 문제를 원인으로 파악했습니다.
- 추측을 막는 프롬프트를 보강해도 문제가 반복돼, DB에서 확인할 정보와 사용자에게 물어야 할 조건을 분리했습니다. 필수 정보가 부족하면 실행 중단 → 추가 질문 → 답변 반영 후 재개하도록 워크플로우를 바꿨습니다.

Python / Smolagents / MCP / Tool Calling / 사용자·상품 DB 연동 / Agent 워크플로우

## 연구 경험

### Search Agent · 요구조건 기반 검색 과정 평가 | 2026.02 – 2026.06

롯데이노베이트 · 문제 정의·평가 기준 설계·기준 모델 재현·실험 분석 · 제1저자, AAAI 2027 심사 중

다단계 웹 검색 Agent의 최종 정답 뒤에 숨은 조건 검증 누락을 측정하는 연구입니다. 질문별 필수 요구조건을 검색 과정의 근거와 대조해, 정답률만으로 드러나지 않는 실패를 진단했습니다.

- 병렬 검색의 중복을 메모리로 조정하려 했으나, 순차 검색에서도 미검증 후보를 다음 탐색의 전제로 삼는 실패를 발견했습니다. 연구 문제를 검색 간 조율에서 조건 검증 누락의 진단으로 바꿨습니다.
- 최종 정답만으로는 이 실패를 구분할 수 없어 질문을 대상·연결 개체·세부 조건으로 분해하는 Requirement Closure Rubric을 설계했습니다. 단서 발견과 조건 충족, 근거 완결성을 각각 평가했습니다.
- 기존 방법의 검색 결과 선택·요약 규칙을 유지하며 10개 Agent 설정으로 150문항을 설정별 3회 반복 평가했습니다. 평균 정답률 17.5%와 필수 근거를 확인한 인증 정확도 2.5%의 차이를 확인했습니다.
- 요구조건의 누락·중복을 정제하고 근거 해석과 점수 집계를 분리해 평가 절차를 보완했습니다. 미해결 조건을 추적하고 다음 탐색 전에 검증하는 행동을 후속 학습 목표로 제안해 AAAI 2027에 제출했습니다.

Python / LLM-as-a-Judge / Entity Graph / Benchmark Design / Trajectory Evaluation

### ECO Decoding · 엔트로피 기반 대화 생성 제어 | 2023 – 2025

성균관대학교 자연어처리 연구실 · 문제 정의·알고리즘 설계·실험 및 논문 작성 · EMNLP 2025 Main Conference 제1저자

대화 응답의 감정·대화행위를 제어하면서 문법 품질을 유지하기 위한 생성 방법을 연구했습니다. 토큰마다 제어 강도를 조절하는 ECO Decoding을 제안하고 자동·사람 평가와 구성 요소 실험으로 검증했습니다.

- 기존 weighted decoding은 제어 강도를 높일수록 문법·유창성이 저하됐습니다. 고정 가중치가 생성 단계별 불확실성을 반영하지 못한다고 보고 추가 언어모델 학습 없이 토큰별 제어 강도를 바꾸는 방법을 선택했습니다.
- 언어모델과 속성 분류기의 엔트로피로 가중치를 조절하는 ECO Decoding을 설계해, 생성 단계마다 언어모델의 출력을 보존할지 속성 제어를 강화할지 결정했습니다.
- DailyDialog·MultiWOZ에서 감정·대화행위의 단일·복수 속성 제어를 평가했습니다. 유사한 문법 품질 조건에서 기존 방법과 제어 정확도를 비교하고 사람 평가로 생성 품질을 점검했습니다.
- 개선이 제안한 원리에서 비롯됐는지 확인하려고 품사별 엔트로피 분석, 구성 요소 제거와 반대 가중치 실험을 수행했습니다. 심사 의견에 따라 검증을 보강해 EMNLP 2025 Main Conference에 제1저자로 게재했습니다.

Python / PyTorch / Hugging Face Transformers / Weighted Decoding / Entropy Analysis / Ablation / Human Evaluation
[논문](https://aclanthology.org/2025.emnlp-main.1437/)
[코드](https://github.com/seummin/ECODecoding)

## 논문

- [ECO Decoding: Entropy-Based Control for Controllability and Fluency in Controllable Dialogue Generation](https://arxiv.org/abs/2511.01568)
  Seungmin Shin, Dooyoung Kim, Youngjoong Ko. EMNLP 2025 · Main Conference. 게재.

- Diagnosing Premature Downstream Expansion in Multi-Hop Search Agents via Requirement Closure
  Seungmin Shin, Hyunmook Cha. AAAI 2027. Under Review.

- Acronym Meaning Selection for Improving Ambiguous Query Answering with User Profile Memory
  Seungmin Shin, Kwangryun Kim, Kihun Lee, Jiwon Jeong, Junghwan Kim, Junye Park, Wonchul Kim. IEIE 2026 Summer Conference.

- Unified Inference and Confidence Calibration Method Using Large Language Models
  Seungmin Shin, Daegun Kim, Ungi Lee, Kwangryun Kim, Ilho Choi, Kihun Lee, Bongji Jeon. HCLT-KACL 2025.

## 수상

ORAK Game Agent Challenge

Track 2 종합 1위

Track 1·2 리더보드 모두 1위 · 팀 수상, 2026

## 강의·교육

- 롯데 그룹사 임원 대상 AI 활용 교육 · 2026.08
- 롯데 그룹사 신입사원 AI 입문 교육 TA · 2025.09 · 2026.04·06·10 (4회)
- 롯데 그룹사 경력사원 AI 입문 교육 TA · 2025.12 · 2026.04 (2회)
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
