[한국어 웹 이력서](https://seummin.github.io/CV/) · [English CV website](https://seummin.github.io/CV/en.html)

[한국어 텍스트](./README.md) · [English text](./resume-en.md)

<img src="./portrait.png" alt="Portrait of Seungmin Shin" width="108" align="right">

# SEUNGMIN SHIN

AI Engineer · LLM & AI Agents

seungminshin00@gmail.com · +82 10 4522 0340 · https://github.com/seummin

I am an AI Engineer researching and building LLMs and AI agents. I turn problems found in services into research questions, and research results into systems people can use. At LOTTE INNOVATE, I work on user profile memory, agent tools and workflows, and security-monitoring LLMs, from problem definition and evaluation to backend implementation and inference serving. I earned an M.S. in Artificial Intelligence from Sungkyunkwan University, where I studied natural language processing, and published a first-author paper on controllable dialogue generation at the EMNLP 2025 Main Conference.

## Work Experience

### LOTTE INNOVATE | Feb 2025 – Present

AI Engineer · AI Tech Lab

Develop context-aware LLM services and agent systems, covering data and task design, model evaluation and fine-tuning, API implementation, and integration with operational systems.

- Defined the problem and evaluation tasks for user profile memory; implemented extraction, storage, retrieval APIs, and asynchronous processing.
- Unified attack classification, evidence extraction, and explanation for security monitoring; developed confidence scoring and vLLM / FastAPI inference services.
- Built agent tools connecting financial and economic data and user/product databases, with input validation, clarification, and error recovery.

### Sungkyunkwan University · NLP Lab | Mar 2023 – Feb 2025

Graduate Research Assistant

Researched controllable dialogue generation and LLM reasoning evaluation.

- Proposed ECO Decoding to adjust attribute-control strength using token-level entropy; validated it with automatic metrics, ablations, and human evaluation.
- Built a Twenty Questions reasoning benchmark with 1,000 samples and a BERT environment model, and registered it as a software asset.

## Selected Projects

### Conversation-Based User Profile Memory | 2025 – 2026

LOTTE INNOVATE · Problem definition, evaluation, memory APIs, and asynchronous processing

Built structured profiles of stable user occupations, interests, and preferences to preserve context across sessions while addressing the cost and latency of repeatedly supplying entire conversation histories.

- Analyzed real queries and selected domain-dependent acronym interpretation as an evaluation task. From 50 source users, constructed a benchmark of 44 users, 326 acronyms, and 454 conversations, checking for answer leakage and duplicate cases.
- Compared full-history versus user-only extraction and system versus user message injection. On the same acronym benchmark, improved GPT-4.1-mini accuracy from 68.94% without profiles to 80.40% (+11.46 percentage points).
- Split long updates into jobs and per-user conversation-chunk tasks. Implemented progress queries, partial-success reporting, chunk-level retries, and per-user write locks. Coordinated post-update cache refresh with the backend to address stale profiles.
- In a separate batch performance experiment, parallel processing reduced mean processing time from 33.31 s to 19.77 s (40.6%). Classified failures in 698 structured-output tests into 4 JSON errors and 27 null-input errors to identify distinct improvement targets.

Python / Structured Output / FastAPI / Job / Worker / DB / Cache / HMAC

### Security-Monitoring LLM & Inference Service | Apr 2025 – Jul 2025

LOTTE INNOVATE · Data/task design, fine-tuning, confidence scoring, and inference APIs

Developed an LLM that generates an attack decision, suspicious payload, and explanation together, addressing disagreement between separate classification and explanation pipelines and making supporting evidence available to security analysts.

- Identified mislabeled records and inconsistent evidence through model-error analysis, requested relabeling from data owners, and compared and trained models on cleaned data with a unified JSON task. Improved attack-detection accuracy by 7.3 percentage points over the existing classifier.
- Without risk-probability labels or latency headroom for repeated inference, derived single-pass confidence from attack-label token log probabilities. Fixed the output schema with Guided Decoding and integrated vLLM / FastAPI with the security system.
- Recorded aggregate inference time: 642 requests in 58.706 s in a single test. Published the method as a first-author HCLT-KACL 2025 paper.

PyTorch / Hugging Face / Guided Decoding / Token Log Probability / vLLM / FastAPI

### ORAK Game Agent · Pokémon Red | Feb 2026 – Apr 2026

LOTTE INNOVATE · Pokémon Red planning, observation processing, state memory, and action selection

Analyzed repeated failures when a small LLM had to interpret coordinates, movement, dialogue, and battles together in a partially observed game. Designed an agent that turns this reasoning burden into state-specific action selection.

- Used a playbook to constrain the current story objective; preprocessed field, dialogue, and battle observations. Generated valid movement candidates with graph search and checked action outcomes against previous/current state and map memory.
- The team ranked 1st on both Track 1 (Lightweight) and Track 2 (Open) leaderboards and received 1st place overall in Track 2. My direct contribution was the Pokémon Red agent within the multi-game team.

LLM Agent / MCP / PyBoy / Graph Search / State Memory
[Competition](https://www.aicrowd.com/challenges/orak-game-agent-challenge-2025)

### Financial & Economic Data Tools for an AI Assistant | Apr 2025 – Oct 2025

LOTTE INNOVATE · Agent tool design, development, and operation

Mapped natural-language company names, dates, and economic concepts to external API identifiers so an internal AI assistant could retrieve Korean equities, financial statements, and macroeconomic indicators.

- Integrated sources including KRX and the Bank of Korea's ECOS. Added company-name mapping, candidate search, date-range and market-calendar checks, and schema constraints to handle invalid arguments before data retrieval.
- Implemented caching, historical backfill, retry/fallback logic, and error isolation; verified core retrieval and exception paths with pytest. Converted the tools to MCP interfaces to ground agent responses in retrieved data.

Python / MCP / KRX / ECOS / API Validation / pytest

### Personalized Shopping Concierge Agent PoC | May 2025 – Jul 2025

LOTTE INNOVATE · Requirements, database tools, and interrupt/resume workflows

Connected user profiles, purchase histories, and product databases in a three-month PoC. Addressed errors in which the model invented tool arguments such as price ranges or product constraints that the user had never supplied.

- Worked with the client and internal collaborators to define recommendation and follow-up filtering scenarios, separating user lookup, product retrieval, and conversation-state responsibilities.
- Chose workflow changes over additional training within the short development period. Interrupted execution when required arguments were missing, asked targeted clarification questions, and resumed with validated user answers. Checked that user constraints were reflected in general and follow-up query scenarios.

Python / Smolagents / Tool Calling / DB Integration / Interrupt / Resume

## Research Experience

### Requirement-Aware Search Agent Trajectory Evaluation | Feb 2026 – Jun 2026

First author · Manuscript under review

Final-answer-only evaluation can miss agents moving to dependent entities before verifying the current entity's constraints. Defined this failure as Premature Downstream Expansion and proposed a framework that checks whether evidence actually satisfies question-derived requirements.

- Designed a Requirement Closure Rubric separating target/bridge entities and atomic requirements. Implemented requirement refinement, dependency-graph construction and pruning, clue resolution, and turn-level evidence verification with LLM-as-a-Judge.
- Evaluated 150 questions, 10 sequential/parallel agent configurations, and 1,500 trajectories from GAIA, FRAMES, and BrowseComp in a common tool environment. Distinguished answer accuracy from evidence satisfaction to analyze correct answers with incomplete verification.

Benchmark Design / LLM-as-a-Judge / Entity Graph / Agent Evaluation

### ECO Decoding · Controllable Dialogue Generation | 2023 – 2025

Sungkyunkwan University · First author, EMNLP 2025 Main Conference

Analyzed how fixed-strength guidance can unnecessarily alter next-token choices or harm fluency. Proposed a decoding method that adjusts control strength using token-level entropy without additional training or changes to the model architecture.

- Compared DialoGPT and LLaMA2 on DailyDialog and MultiWOZ across emotion, dialogue-act, and multi-attribute conditions. Validated the method through token/POS analysis, ablations, automatic metrics, and human evaluation.
- Improved attribute-control performance by 3.1 percentage points on average while maintaining fluency. Published at the EMNLP 2025 Main Conference.

PyTorch / Controllable Generation / Entropy / Decoding
[Paper](https://arxiv.org/abs/2511.01568)

### Twenty Questions Benchmark for LLM Reasoning | 2023 – 2024

Sungkyunkwan University · Benchmark, environment model, and state tracking

Built an interactive evaluation loop in which an LLM asks questions and a BERT environment model responds Yes/No/Unknown. Compared answer accuracy and question efficiency on 1,000 controlled samples, analyzed recurring failures, and registered the benchmark as a software asset.


BERT / WordNet / Interactive Evaluation

## Publications

- [ECO Decoding: Entropy-Based Control for Controllability and Fluency in Controllable Dialogue Generation](https://arxiv.org/abs/2511.01568)
  Seungmin Shin, Dooyoung Kim, Youngjoong Ko. EMNLP 2025 · Main Conference. Published.

- Do Search Agents Verify Before They Search? A Requirement-Aware Framework for Trajectory Evaluation
  Seungmin Shin et al.. 2026 · Manuscript under review. Under review.

- Acronym Meaning Selection for Improving Ambiguous Query Answering with User Profile Memory
  Seungmin Shin et al.. IEIE Summer Conference · 2026. Presented.

- Unified Inference and Confidence Calibration Method Using Large Language Models
  Seungmin Shin et al.. HCLT-KACL · 2025. Presented.

## Awards

ORAK Game Agent Challenge

1st place overall · Track 2

1st on both Track 1 & 2 leaderboards · Team award, 2026

## Education

### Sungkyunkwan University

M.S. in Artificial Intelligence | Mar 2023 – Feb 2025

- GPA 4.17 / 4.5
- Natural Language Processing Lab
- Advisor: Youngjoong Ko

### Inha University

B.S. in Computer Science and Engineering | Mar 2017 – Feb 2023

- GPA 3.89 / 4.5
- Major GPA 4.24 / 4.5

## Technical Skills

- Programming: Python
- Modeling: PyTorch, Hugging Face Transformers, PEFT / LoRA
- Agents & Evaluation: Tool Calling, MCP, Smolagents, Graph Search, Benchmark Design, LLM-as-a-Judge
- Serving & Data: vLLM, FastAPI, Structured Output, Database / Cache Integration, Async Processing, pytest

## Research Interests

Large Language Models, AI Agents, Agentic Memory, Agentic Search, Evaluation Frameworks, Controllable Generation
