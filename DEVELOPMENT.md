# Seungmin Shin · 신승민

LLM · AI Agent · Agentic Memory · Evaluation

- **한국어**: [이력서 웹페이지](./index.html) · [텍스트 버전](./resume-ko.md)
- **English**: [CV webpage](./en.html) · [Text version](./resume-en.md)

The website is published at https://seummin.github.io/CV/ (Korean) and https://seummin.github.io/CV/en.html (English). GitHub Pages uses the public repository’s main branch and root directory. The README also renders the Korean CV directly, and `resume-en.md` renders the English CV.

## Preview and edit

No package installation or frontend build tool is required. The generated HTML is complete and can be read without JavaScript. JavaScript only enables the print button.

```sh
python3 build.py
python3 -m http.server 8000
```

Open `http://localhost:8000/`. Edit the Korean and English records in `content.json`, run `python3 build.py`, and commit the generated HTML and Markdown along with the source. The generator validates section counts, anchor targets, and relative links.

Use **인쇄 / PDF 저장** or **Print / Save PDF** to open the browser print dialog. The print stylesheet uses A4 pages, hides navigation, and preserves text and links. Choose “Save as PDF” in the browser dialog to export.

## GitHub Pages

The site works at a repository subpath such as `/CV/`; assets and language links are relative.

When Pages is available for the repository's current visibility and plan, choose **Settings → Pages → Deploy from a branch → main → / (root)**. No build step is needed. Keep the repository's existing visibility unless its owner chooses to change it.

## Editorial basis

- Primary content: the owner's existing Overleaf CV, `Academic_CV_Template_v2`, especially `main_1.tex`, read on 2026-10-18.
- Supporting evidence: the owner's local project summaries, used to clarify evaluation populations, failure types, individual contributions, and measurement scope.
- Writing guidance: `토스_AI직무_이력서_작성가이드_체크리스트.md`, supplied by the owner. Projects describe the problem and constraints, direct responsibilities, technical choices, validation, and outcomes. Requirements for unrelated roles were not treated as mandatory experience.
- Visual reference: [Kwangho Lee's CV](https://khlee369.github.io/CV/). The green accent, restrained typography, language navigation, and main-column / sidebar structure informed an independently implemented design. No biography, photograph, logos, or source code were copied. The self-hosted Pretendard Variable font is from the official orioncactus/pretendard distribution, with its SIL OFL license in `OFL-Pretendard.txt`. The reference-inspired typography and photo / introduction layout use text-only navigation and headings. Body and section-navigation emoji are removed. Language flags and header contact icons are retained as clarified by the owner.

- Profile photograph: supplied and approved by the owner for this CV.

### Consistency decisions

- Memory benchmark: **50 source users → 44 users with acronym cases → 326 acronyms / 454 conversations**. These are different populations, not conflicting sample counts.
- Memory accuracy: **68.94% → 80.40%, +11.46 percentage points**. Batch processing **33.31 s → 19.77 s** is a separate experiment.
- Structured-output tests: **4 JSON errors + 27 null-input errors out of 698 tests**. Four JSON errors do not mean only four total failures.
- Security inference: **642 requests / 58.706 s aggregate recorded test time**. Hardware, batching, and p95 were not verified; the figure is not presented as an operational latency guarantee. The reported **+7.3 percentage point** accuracy gain is retained from the original CV; an exact evaluation split and hardware comparison were not supplied.
- ORAK: leaderboard positions and the Track 2 overall award are team results. Direct contribution is limited to the **Pokémon Red agent**.
- The search-agent paper is **under review**, not accepted. The publication title and AAAI 2027 under-review status were updated from the owner’s explicit correction on 2026-10-19; project periods follow `main_1.tex`. Conflicting correlation coefficients and certified-accuracy figures in other local drafts were omitted. The alternate title in `cv-reference-en.tex` was not silently substituted.
- Duplicate ORAK material under the original CV's Teaching section was consolidated under projects and awards; no teaching experience was inferred.
- Teaching and training experience comes from the owner’s screenshot supplied on 2026-10-19. Listed directly below awards as a flat list with dates transcribed from the owner’s screenshot. New-hire and experienced-hire AI onboarding TA assignments are separate; training attendance, outcomes and additional responsibilities are not inferred.
- No unverified revenue, online lift, user adoption, team size, or production traffic figures were added.

Last content update: October 2026.


## Readability system

Guidance: [Typography skill by petekp](https://github.com/petekp/agent-skills/blob/main/skills/typography/SKILL.md), including its fluid typography and internationalization references. Used as a design reference for this task; no external code or global skill installation is required.

- Headline sizes retain the earlier type scale. Reading density takes priority over mathematical column ratios: the sheet is capped at 1200px, with a 240px supporting sidebar and a 32px gutter.
- Primary text remains 16–17px. Korean leading is 1.6 with a 48ic measure cap; English leading is 1.55 with a 78ch cap. At widths up to 960px, the main content uses one column. Mobile gutters are 20px.
- Entry spacing is 32px, section spacing 48px, and bullet margins 6px. Titles, dates and role metadata form one visual group. Result strips use 22px values and 12px vertical padding.
- Editorial review: shorten the opening profile to specialization, scope and one academic credential. Keep project problem statements, individual responsibilities, alternatives, evaluation populations and measured outcomes explicit. Do not replace evidence with unsupported summary claims.
- Maintain text-only section navigation, language flags and header contact icons, visible keyboard focus, contrast, 200% text support and awards below publications.

## Experience timeline

The Experience section uses a green dot and a continuous vertical rail for each role. The rail is CSS-only and decorative; headings and dates remain normal text for screen readers. Print styling removes the rail to conserve page width. The Korean and English section labels are 경험 and Experience.

## Publication layout

Publication entries present a compact venue badge, title, authors, then a [Paper] link when the source record includes a URL. The title remains plain text so entries without a public paper link do not appear clickable. The AAAI 2027 manuscript carries a separate grey under review badge beside the authors to avoid implying acceptance.
