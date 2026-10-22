[한국어 웹 이력서](https://seummin.github.io/CV/) · [English CV website](https://seummin.github.io/CV/en.html)

[한국어 텍스트](./README.md) · [English text](./resume-en.md)

<img src="./portrait.png" alt="Portrait of Seungmin Shin" width="108" align="right">

# SEUNGMIN SHIN

AI Engineer · LLM & AI Agents

seungminshin00@gmail.com · +82 10 4522 0340 · https://github.com/seummin

AI Engineer building LLM and AI Agent systems. I work across problem definition, evaluation, API development, and inference serving for user memory, agent tools, and security LLMs. At LOTTE INNOVATE AI Tech Lab, I connect research with implementation. I hold an M.S. in AI from Sungkyunkwan University and published first-author research on controllable dialogue generation at EMNLP 2025 Main Conference.

## Experience

### LOTTE INNOVATE | Feb 2025 – Present

AI Engineer · AI Tech Lab

Develop LLM-powered capabilities and AI agents for the group’s internal AI platform and client services. Analyze business requirements to define the problems to solve and the scope of service deployment.

- Design agent architectures for internal services and client PoCs. Implement MCP-based tools that connect databases and external APIs, along with personalization based on user information. Define agent roles and execution flows around task characteristics and the reasoning capabilities of the models.
- Analyze research contributions and limitations, and validate their applicability in service environments. Adapt methods to limited data and operational constraints, connecting model training and evaluation with serving and operations to translate research into deployed services.
- Design task-specific evaluation datasets, metrics, and comparative experiments to quantitatively validate AI services. Analyze errors missed by existing evaluations and failures during execution to improve evaluation methods and AI services.

### Sungkyunkwan University · NLP Lab | Mar 2023 – Feb 2025

Graduate Research Assistant

Studied controllable dialogue generation grounded in natural language processing theory.

- Proposed ECO Decoding to adjust attribute-control strength using token-level entropy; validated it with automatic metrics, ablations, and human evaluation.

## Selected Projects

### User Profile Memory · Conversation-Based Personalization | 2025 – 2026

LOTTE Innovate · Memory proposal, evaluation design, service implementation and operations

Designed and deployed profile memory for an internal chat service so user roles and interests remain useful across sessions. Evaluated personalization on real conversations and made bulk updates recoverable when individual tasks fail.

- Across sessions, the chat service could not reuse a user’s role and interests. Re-sending the entire history increased context length and latency, so I proposed structured profile memory for reusable information.
- An existing memory design caused repeated LLM calls, delayed updates, and accumulated unused facts. I first asked which memories actually improve responses and designed an evaluation around that question.
- Structured job, interest, and technical details from real work conversations; selected user-dependent acronym interpretation as the personalization task.
- On 454 evaluation conversations from real logs, acronym interpretation accuracy rose from 68.94% to 80.40% with profiles. I used the result to support service adoption.
- When updates timed out, completion was unclear and the entire batch had to be rerun. I added asynchronous user/conversation-level jobs and progress tracking to retry only failed segments, while limiting concurrency to the serving API capacity.

Python / FastAPI / Structured Output / User Profile Memory / Asynchronous Processing

### Security-Monitoring LLM & Inference Service | Apr 2025 – Jul 2025

LOTTE INNOVATE · Data/task design, fine-tuning, confidence scoring, and inference APIs

Developed an LLM that generates an attack decision, suspicious payload, and explanation together, addressing disagreement between separate classification and explanation pipelines and making supporting evidence available to security analysts.

- Identified mislabeled records and inconsistent evidence through model-error analysis, requested relabeling from data owners, and compared and trained models on cleaned data with a unified JSON task. Improved attack-detection accuracy by 7.3 percentage points over the existing classifier.
- Without risk-probability labels or latency headroom for repeated inference, derived single-pass confidence from attack-label token log probabilities. Fixed the output schema with Guided Decoding and integrated vLLM / FastAPI with the security system.
- Recorded aggregate inference time: 642 requests in 58.706 s in a single test. Published the method as a first-author HCLT-KACL 2025 paper.

PyTorch / Hugging Face / Guided Decoding / Token Log Probability / vLLM / FastAPI

### ORAK Game Agent Challenge · Pokémon Red Agent | Feb 2026 – Apr 2026

LOTTE Innovate · Pokémon Red observation preprocessing, progress state and action design

Built a Pokémon Red agent for game objectives under a strict action budget. Code organizes environmental state and valid moves; the model selects actions aligned with the current objective.

- The agent had 200 steps to achieve seven goals, while a small model struggled to infer objectives and routes directly from raw observations. I separated valid-candidate computation in code from model selection.
- I combined maps, coordinates, inventory, and screen text into progress state, encoded subgoals and completion conditions in a playbook, computed moves with graph search, and exposed only tools relevant to each state.
- A successful tool call did not establish a successful action, so I evaluated execution logs against actual changes in position, screen, battle, and inventory to identify loops and stalled progress.
- I fed previous actions and observed state changes into the next decision, and constrained state-specific tools and map transitions. I owned the Pokémon Red agent; the team placed first on both Lightweight and Open Track leaderboards.

Python / LLM Agent / MCP / PyBoy / Graph Search / State Memory
[Competition](https://www.aicrowd.com/challenges/orak-game-agent-challenge-2025)

### Financial & Economic Data Tools for an AI Assistant | Apr 2025 – Oct 2025

LOTTE INNOVATE · Agent tool design, development, and operation

Mapped natural-language company names, dates, and economic concepts to external API identifiers so an internal AI assistant could retrieve Korean equities, financial statements, and macroeconomic indicators.

- Integrated sources including KRX and the Bank of Korea's ECOS. Added company-name mapping, candidate search, date-range and market-calendar checks, and schema constraints to handle invalid arguments before data retrieval.
- Implemented caching, historical backfill, retry/fallback logic, and error isolation; verified core retrieval and exception paths with pytest. Converted the tools to MCP interfaces to ground agent responses in retrieved data.

Python / MCP / KRX / ECOS / API Validation / pytest

### Shopping Concierge Agent PoC · Data-Driven Recommendations | May 2025 – Jul 2025

LOTTE Innovate · Client scenario alignment, evaluation metrics, DB tools and agent workflow

Connected a client’s customer profiles, purchase history, and product database to recommend products from natural-language requests. Designed the flow to clarify missing constraints rather than let the model invent them.

- Existing recommendations leaned on past purchases or similar users and struggled to reflect both the current request and product attributes. I scoped a PoC to test personalized recommendations across customer and product data.
- With the client, I defined expected outcomes for initial and follow-up requests; I built separate Smolagents tools for customer and product data. Evaluation criteria distinguished successful tool calls from satisfaction of user constraints.
- Evaluation found successful tool calls that still produced unsuitable recommendations. Tracing call order and inputs showed the model inventing missing price ranges and product conditions.
- Prompt instructions against guessing were insufficient. I separated DB-verifiable facts from conditions requiring user input and changed the flow to interrupt, ask a clarifying question, then resume with the answer.

Python / Smolagents / MCP / Tool Calling / Customer/Product DB / Agent Workflow

## Research Experience

### Search Agent · Requirement-Aware Trajectory Evaluation | Feb 2026 – Jun 2026

LOTTE Innovate · Problem definition, rubric design, baseline reproduction and analysis · First author, AAAI 2027 under review

Studied how multi-hop web search agents skip condition checks even when their final answers appear correct. Compared question requirements against evidence gathered during search to diagnose failures hidden by answer accuracy.

- I initially explored memory to coordinate parallel searches, but found that sequential agents also used unverified candidates as premises. I shifted the research question from search coordination to diagnosing missing verification.
- Because final answers alone could not reveal this failure, I developed a Requirement Closure Rubric that separates target entities, linking entities, and atomic conditions, and evaluates clue discovery, condition satisfaction, and evidence completeness.
- Preserving the baseline’s result selection and summarization rules, I evaluated 150 questions across 10 agent configurations with three runs each. Mean answer accuracy was 17.5%, while evidence-certified accuracy was 2.5%.
- I refined missing or duplicated requirements and separated evidence interpretation from score aggregation. The resulting analysis motivates tracking unresolved conditions and verifying them before downstream search; the paper was submitted to AAAI 2027.

Python / LLM-as-a-Judge / Entity Graph / Benchmark Design / Trajectory Evaluation

### ECO Decoding · Entropy-Based Dialogue Control | 2023 – 2025

Sungkyunkwan University NLP Lab · Problem definition, algorithm, experiments and writing · First author, EMNLP 2025 Main Conference

Studied how to control emotion and dialogue acts while preserving grammatical quality. Proposed token-wise control strength and tested the mechanism through automatic and human evaluation and component experiments.

- With existing weighted decoding, stronger control degraded grammar and fluency. I attributed this tradeoff to a fixed weight that ignored uncertainty at each generation step and chose a token-wise method without additional language-model training.
- I designed ECO Decoding to use entropy from the language model and attribute classifier to decide when to preserve the base distribution and when to strengthen attribute control.
- On DailyDialog and MultiWOZ, I evaluated single and multiple emotion/dialogue-act attributes, compared control accuracy under similar grammatical quality, and checked generation quality with human evaluation.
- To test the proposed mechanism, I analyzed entropy by part of speech and ran component removal and reversed-weight experiments. I strengthened validation after review and published the first-author paper at EMNLP 2025 Main Conference.

Python / PyTorch / Hugging Face Transformers / Weighted Decoding / Entropy Analysis / Ablation / Human Evaluation
[Paper](https://aclanthology.org/2025.emnlp-main.1437/)
[Code](https://github.com/seummin/ECODecoding)

## Publications

- [ECO Decoding: Entropy-Based Control for Controllability and Fluency in Controllable Dialogue Generation](https://arxiv.org/abs/2511.01568)
  Seungmin Shin, Dooyoung Kim, Youngjoong Ko. EMNLP 2025 · Main Conference. Published.

- Diagnosing Premature Downstream Expansion in Multi-Hop Search Agents via Requirement Closure
  Seungmin Shin, Hyunmook Cha. AAAI 2027. Under Review.

- Acronym Meaning Selection for Improving Ambiguous Query Answering with User Profile Memory
  Seungmin Shin, Kwangryun Kim, Kihun Lee, Jiwon Jeong, Junghwan Kim, Junye Park, Wonchul Kim. IEIE 2026 Summer Conference.

- Unified Inference and Confidence Calibration Method Using Large Language Models
  Seungmin Shin, Daegun Kim, Ungi Lee, Kwangryun Kim, Ilho Choi, Kihun Lee, Bongji Jeon. HCLT-KACL 2025.

## Awards

### ORAK Game Agent Challenge [Link](https://www.aicrowd.com/challenges/orak-game-agent-challenge-2025/winners)

A real-game LLM agent challenge with 117 teams and 497 participants, evaluating planning, tool use, and goal completion across Pokémon Red, StarCraft II, Super Mario, and 2048.

**1st place overall · Track 2**

1st on both Track 1 & 2 leaderboards · Team award, 2026

## Teaching

- AI application training for LOTTE Group executives · Aug 2026
- TA, AI onboarding for new hires at LOTTE Group companies · Sep 2025 · Apr, Jun, Oct 2026 (4 sessions)
- TA, AI onboarding for experienced hires at LOTTE Group companies · Dec 2025 · Apr 2026 (2 sessions)
- Workflow automation training for new employees at LOTTE INNOVATE · Jun 2026
- Lecture on AI applications, Chosun University · Dec 2025
- Teaching assistant, Natural Language Processing: Theory and Applications · Mar – Jun 2024
- Teaching assistant, Introduction to Artificial Intelligence · Mar 2017 – Feb 2023

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
- Agents & Evaluation: Agent Orchestration, Agentic Search, Agentic Memory, Memory Augmented Generation, Tool Calling, MCP, Smolagents, Benchmark Design, LLM-as-a-Judge, Evaluation Framework
- Serving & Data: vLLM, FastAPI, Structured Output, Database / Cache Integration, Async Processing, pytest

## Research Interests

Large Language Models, AI Agents, Agentic Memory, Agentic Search, Evaluation Frameworks, Controllable Generation
