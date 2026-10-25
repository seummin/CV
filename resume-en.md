[English CV website](https://seummin.github.io/CV/en.html), [한국어 웹 이력서](https://seummin.github.io/CV/ko.html)

[한국어 텍스트](./README.md), [English text](./resume-en.md)

<img src="./portrait.png" alt="Portrait of Seungmin Shin" width="108" align="right">

# SEUNGMIN SHIN

AI Engineer, LLM & AI Agents

seungminshin00@gmail.com, +82 10 4522 0340, https://github.com/seummin

I am an AI Engineer who turns problems encountered in services into research questions and applies experimentally validated methods to those services. I develop AI agents and user memory systems, analyzing real user requests and execution traces to identify failures missed by existing evaluations and design solutions that fit service goals and operational constraints. I published first-author research on controllable dialogue generation at EMNLP 2025 Main Conference.

## Experience

### LOTTE INNOVATE | Feb 2025 – Present

AI Engineer, AI Tech Lab

Developed LLM-powered capabilities and AI agents for the group’s internal AI platform and client services. Analyzed business requirements to define the problems to solve and the scope of service deployment.

- Designed agent architectures for internal services and client PoCs. Implemented MCP-based tools that connect databases and external APIs, along with personalization based on user information. Defined agent roles and execution flows around task characteristics and the reasoning capabilities of the models.
- Analyzed research contributions and limitations, and validated their applicability in service environments. Adapted methods to limited data and operational constraints, connecting model training and evaluation with serving and operations to translate research into deployed services.
- Designed task-specific evaluation datasets, metrics, and comparative experiments to quantitatively validate AI services. Analyzed errors missed by existing evaluations and failures during execution to improve evaluation methods and AI services.

### Sungkyunkwan University, NLP Lab | Mar 2023 – Feb 2025

Graduate Research Assistant

Built a foundation in natural language structure and semantic representation, language modeling, and contextual processing in Transformers, and applied it to dialogue generation and reasoning evaluation research.

- Researched methods for controlling response attributes, including emotion and dialogue acts, to generate dialogue aligned with user requirements and conversational goals.
- Conducted a project on output control to suppress harmful responses from dialogue models.

## Selected Projects



### User Profile Memory, Conversation-Based Personalization | 2025 – 2026

Memory proposal, evaluation design, service implementation and operations

Applied profile memory to an internal chat service and confirmed an 11.46 percentage-point improvement in acronym interpretation accuracy in an evaluation based on real conversations. Taking the internal platform’s characteristics into account, I structured memory to reuse users’ occupations, interests, and technical information across sessions and implemented operations for bulk updates and retries of failed segments.

- I identified the need for users to repeatedly explain their backgrounds and proposed profile memory to preserve reusable information separately from conversation history. I structured the user information used in responses into occupations, interests, and technical information.
- The existing memory architecture suffered from delayed updates due to repeated LLM calls and accumulated information that was not used in responses. To test whether stored information actually contributed to personalization, I selected acronym interpretation, where the correct meaning depends on user context, as the evaluation task.
- To reduce duplicate storage of differently worded information and incorrect updates, I configured Chroma to retrieve the five most similar memories before deciding whether to add, update, delete, or retain information. Rather than comparing the entire profile on every update, I narrowed model input to relevant candidates to improve operational stability.
- In an evaluation based on real conversations, acronym interpretation accuracy improved from 68.94% to 80.40%, an increase of 11.46 percentage points.
- I split bulk updates into user-level jobs and asynchronous conversation-segment tasks, and limited concurrent calls to fit the serving API’s processing constraints. Completed work was retained and only failed segments were retried, reducing the need to rerun entire batches. I deployed the system to the internal platform and operated it.

Python / FastAPI / Structured Output / User Profile Memory / Asynchronous Processing

### Long-Term Memory for Work Context and Execution Experience | Aug 2026 – Present

Led framework proposal, memory design and comparative evaluation

Designed a long-term memory framework for the internal platform that combines precise facts with integrated work context, leading the structural proposal and comparative evaluation. The framework combines Facts preserving information and sources, Wikis integrating work context, and experience memory recording execution processes and lessons learned, enabling information and execution results from multiple conversations to be reused in subsequent tasks.

- Retrieving past conversations alone required reconstructing work change histories and currently applicable rules, while Wiki-based summaries omitted values, effective dates, and conditions. I concluded that fact preservation should be separated from context integration and designed a graph connecting work Wikis to Facts that preserve entities, values, dates, speakers, and sources. New information integrates changes and effective dates while retaining existing evidence.
- Retrieving individual Facts alone can miss the overall work context, while retrieving only integrated Wikis can miss precise values and conditions. I structured retrieval to identify relationships and current state in Wikis, then consult linked Facts for detailed evidence, combining contextual understanding with specific facts as required by the question.
- Passing all retrieved information to the answer model reduces space for the current conversation and risks mixing values or conditions from different events. I introduced a Curating stage that selects evidence based on the relationships and time constraints relevant to the question. Selected evidence is passed as stored sentences with sources rather than summarized again, controlling input volume while preserving necessary values and conditions.
- I evaluated recall of facts and temporal context across conversations with LoCoMo, and multi-hop reasoning across documents with MuSiQue. Compared with memory frameworks using different ingestion approaches, including Mem0 and HippoRAG 2, the framework achieved the highest F1 in both evaluations, exceeding the best comparison scores by 2.42 and 10.07 percentage points, respectively. These scores supported the effectiveness of the design direction of combining precise facts with integrated work context for conversational memory and evidence linking.

Long-term Memory / LLM Wiki / Search Strategy / Benchmark Evaluation

### ORAK Game Agent Challenge, Pokémon Red Agent | Feb 2026 – Apr 2026

Pokémon Red observation preprocessing, progress state and action design

Developed a Pokémon Red game agent designed to achieve progress objectives within 200 steps by accounting for the model’s reasoning capabilities. I owned input preprocessing, progress state management, and action-decision architecture for exploration, movement, dialogue, and battle under a limited action budget.

- Asking small models to perform the compound reasoning handled by frontier models led to coordinate errors and repeated actions. I identified the burden of jointly determining the current objective, movement route, and next action from raw game state as a major cause.
- To reduce the scope of each decision, I separated objective setting, movement, dialogue, and battle. I designed the agent workflow to provide the current subgoal and completion criteria, with state-specific information and tools so the model could focus on one task at a time.
- Even after task decomposition, small models made errors in judging traversability and routes and failed to reach the objective within the step budget. I precomputed movement candidates with graph search and reformulated the task as selecting a candidate suited to the current objective. After the change, small models could select valid moves and progress, reaching the objective within 200 steps.
- I found cases where successful tool calls produced no actual movement or progress. I compared coordinates, screen state, battle state, and inventory before and after execution to identify invalid actions and repeated failures, then incorporated the previous action and observed state changes into the next decision.
- I adjusted decision scope, input information, and computations handled by code to match model reasoning capabilities. I owned observation preprocessing, state management, and action selection for the Pokémon Red agent, contributing to the team’s first-place competition finish.

Long-Horizon Agent / Agent Workflow / LLM Agent / State Memory / MCP
[Competition](https://www.aicrowd.com/challenges/orak-game-agent-challenge-2025)

### Shopping Concierge Agent PoC, Data-Driven Recommendations | May 2025 – Jul 2025

Client scenario alignment, evaluation metrics, DB tools and agent workflow

Connected a client’s customer profiles, purchase history, and product database to recommend products from natural-language requests. Designed the flow to clarify missing constraints rather than let the model invent them.

- I determined that purchase history alone could not adequately reflect the current request or a gift recipient’s needs, so I configured the agent to use member information and the current request separately. For recommendations to the account holder, I preloaded member information and enabled product, brand, and promotion lookups based on the request. I applied category and price constraints to popular products by gender, age, and customer segment, and grounded recommendation explanations in retrieved product attributes and member information.
- The client did not want internal customer-segment information disclosed in responses. I worked with them to define rules prohibiting direct references and the acceptable scope of indirect descriptions. I incorporated the agreed rules into the response-generation guidelines and reviewed recommendation-scenario outputs with the client to check compliance and the appropriateness of recommendation explanations.
- Successful tool calls still produced unsuitable recommendations when the model invented missing price constraints or gift-recipient information. Prompt revisions did not resolve the recurring issue, so I separated DB-verifiable information from details requiring user input. I distinguished the account holder from the gift recipient and changed the workflow to end the current run and return a clarification question when recipient information was missing.
- Although clarification adds conversational turns, I prioritized reducing recommendations based on unverified assumptions. I passed the user’s answer into the next turn’s conversation history to continue the recommendation flow reducing errors caused by model assumptions in scenarios with insufficient information and improving recommendation accuracy by 11.17 percentage points.

Python / Smolagents / MCP / Tool Calling / Customer/Product DB / Agent Workflow

### Additional Projects

#### Security-Monitoring LLM & Inference Service | Apr 2025 – Jul 2025

Trained an LLM that jointly generates attack classifications, attack payloads, and supporting explanations, and implemented confidence scoring and an inference API.

#### Financial & Economic Agent | Apr 2025 – Oct 2025

Developed and operated a financial and economic agent for an internal AI assistant that identifies companies and statistical series from natural-language requests and answers using Korean stock prices, financial statements, and macroeconomic indicators retrieved through external APIs.

## Research Experience

### Search Agent, Requirement-Aware Trajectory Evaluation | Feb 2026 – Jun 2026

AAAI 2027, Problem definition, rubric design, baseline reproduction and analysis

Research on diagnosing missing condition verification in search agents that final-answer accuracy alone does not reveal. I defined the problem, designed evaluation criteria, reproduced baseline agents, and analyzed the experiments.

- I initially explored memory to coordinate redundant parallel searches, but found that sequential agents also used unverified candidates as premises for further search. I reframed the research question around diagnosing missing verification before addressing parallel coordination.
- An agent can reach the correct answer without verifying all necessary conditions. I designed evaluation criteria that decompose each question into target entities, linking entities, and atomic requirements. I separated clue discovery from condition satisfaction, using an LLM to interpret evidence and code to aggregate cumulative fulfillment and scores.
- Considering web search and crawling costs, I selected 150 questions and evaluated 10 agent configurations over three runs. I preserved the baseline methods’ search-result selection and summarization rules, and found a gap between mean answer accuracy of 17.5% and evidence-certified accuracy of 2.5%.
- To check whether the findings arose from judge errors, I refined missing and duplicated requirements. Across 180 entity–requirement pairs, judge decisions agreed with the majority vote of three human evaluators in 90.6% of cases. I also tested whether the gap between correct answers and complete evidence persisted when replacing the judge.
- Based on the analysis, I proposed tracking unresolved requirements and verifying them before further search as targets for subsequent training. I developed an evaluation framework that diagnoses verification failures hidden by final-answer accuracy and submitted the research to AAAI 2027 as first author.

Python / LLM-as-a-Judge / Entity Graph / Benchmark Design / Trajectory Evaluation

### ECO Decoding, Entropy-Based Dialogue Control | 2023 – 2025

EMNLP 2025 Main Conference first author, Problem definition, algorithm, experiments and writing

Research on controlling emotion and dialogue acts while preserving grammatical quality. I defined the problem, designed the algorithm, conducted comparative experiments, and wrote the paper, published at EMNLP 2025 Main Conference as first author.

- Existing weighted decoding degraded grammar and fluency as control strength increased. I attributed this limitation to fixed weights that did not account for uncertainty at each generation step and chose token-wise control instead of additional training of the base language model.
- I hypothesized that preserving confident language-model outputs while strengthening attribute control at uncertain steps could improve control accuracy while retaining grammatical quality. Based on this hypothesis, I designed ECO Decoding to determine token-wise weights using entropy from both the language model and the attribute classifier.
- To check whether higher control accuracy came at the expense of grammatical quality, I compared methods at similar grammar scores. In the DialoGPT-based FUDGE setting for emotion control on DailyDialog, accuracy increased from 76.98% to 81.03%, a gain of 4.05 percentage points, while the grammar score remained comparable at 90.30 versus 90.34.
- To test whether the performance gains followed from the proposed hypothesis, I conducted part-of-speech entropy analysis, component ablations, and experiments with reversed weight directions. These experiments confirmed that adjusting control strength according to token-wise uncertainty contributed to the gains, while automatic and human evaluations validated improvements in generation quality.
- I consolidated the performance comparisons and hypothesis-testing results into a paper published at EMNLP 2025 Main Conference as first author.

Controllable Generation / Decoding Strategy / Weighted Decoding / Entropy Analysis
[Paper](https://aclanthology.org/2025.emnlp-main.1437/)
[Code](https://github.com/seummin/ECODecoding)

## Publications

- [ECO Decoding: Entropy-Based Control for Controllability and Fluency in Controllable Dialogue Generation](https://arxiv.org/abs/2511.01568)
  Seungmin Shin, Dooyoung Kim, Youngjoong Ko. EMNLP 2025 Main Conference. Published.

- Diagnosing Premature Downstream Expansion in Multi-Hop Search Agents via Requirement Closure
  Seungmin Shin, Hyunmook Cha. AAAI 2027. Under Review.

- Acronym Meaning Selection for Improving Ambiguous Query Answering with User Profile Memory
  Seungmin Shin, Kwangryun Kim, Kihun Lee, Jiwon Jeong, Junghwan Kim, Junye Park, Wonchul Kim. IEIE 2026 Summer Conference.

- Unified Inference and Confidence Calibration Method Using Large Language Models
  Seungmin Shin, Daegun Kim, Ungi Lee, Kwangryun Kim, Ilho Choi, Kihun Lee, Bongji Jeon. HCLT-KACL 2025.

## Awards

### ORAK Game Agent Challenge, 1st place

117 teams developed MCP-connected LLM agents that interpret textual and visual game states to plan actions, use tools, and complete objectives across multiple games.

[Link](https://www.aicrowd.com/challenges/orak-game-agent-challenge-2025/winners)

## Teaching

- AI application training for LOTTE Group executives, Aug 2026
- TA, AI onboarding for new hires at LOTTE Group companies, Sep 2025, Apr, Jun, Oct 2026 (4 sessions)
- TA, AI onboarding for experienced hires at LOTTE Group companies, Dec 2025, Apr 2026 (2 sessions)
- Workflow automation training for new employees at LOTTE INNOVATE, Jun 2026
- Lecture on AI applications, Chosun University, Dec 2025
- Teaching assistant, Natural Language Processing: Theory and Applications, Mar – Jun 2024
- Teaching assistant, Introduction to Artificial Intelligence, Mar 2017 – Feb 2023

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
