# Catalog HC — HCI, information design, technical communication, program comprehension, plain language

Compiled 2026-11-12. IDs `HC-nn`. Ev: S strong · M moderate · W weak/guideline-only · C contested.
Duplicates marked `No` with the original ID. Researcher notes: Wright & Reid 1973 and Hartley & Trueman 1985 rest on secondary citations; Dixon 1982 from abstract only; no peer-reviewed study tests markdown/bullets on chat comprehension (itself a finding).

## A. Gestalt, layout, visual hierarchy

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-01 | Proximity grouping | Close items read as one unit | Wertheimer 1923; Tullis 1983 | M | Yes | One blank line between distinct groups; none inside one list or step | core |
| HC-02 | Common region | Enclosure groups elements | Palmer 1992 | M | Partial | Code block / blockquote encloses one unit only (one command, one quoted error) | code |
| HC-03 | Similarity → parallel items | Same form implies same category | Palmer & Rock 1994 | M/W | Yes | Every list item uses the same grammatical form and lead pattern | core |
| HC-04 | Display density | Search time rises with density | Tullis 1983/84 | M | Partial | Paragraphs ≤4–5 rendered lines, but no column of one-line bullets either | core |
| HC-05 | Heading depth | Deep hierarchies add navigation cost | Lorch & Lorch 1996 | M/W | Partial | At most 2 heading levels | long-form |
| HC-06 | First-screen attention | 57% of viewing time above the fold | NN/g (Fessenden) 2018 | M | Yes | Everything needed to act, including decision-changing caveats, in the first ~15 lines | core |
| HC-07 | First two words | Scanners read ~2 words per line | Nielsen 2009 eye tracking | W | Yes | Open each bullet/heading with the information word, never filler | core |
| HC-08 | Line length | 55 cpl best comprehension | Dyson 2004 | M | Partial | Renderer controls prose width; keep code lines ≤~90 chars | code |

## B. Typographic emphasis

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-09 | Light vs heavy signaling | — | Lorch 1995 | M | No | Duplicate of #27 | n/a |
| HC-10 | Bold vs italics | Bold pops out; italics low salience | Pop-out literature; NN/g | W | Yes | Bold = scan anchor; italics only for defined terms/titles; never both | core |
| HC-11 | ALL CAPS | Running caps slow reading, read as shouting | Tinker 1963; Arditi & Cho 2007 | C | Partial | No all-caps sentences; caps only for one-word literals/constants | core |
| HC-12 | Monospace literals | Code font marks the exact string | MS/Google style guides | W | Yes | Every command, path, flag, env var, error string in `inline code`; never for emphasis | code |

## C. Tables, lists, prose, conditional logic

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-13 | Prose fails for contingencies | Multi-condition prose → most errors | Wright & Reid 1973, J Appl Psych 57:160–166 (existence verified; result via secondary sources, e.g. Hartley 1980) | M | Yes | Outcome depends on ≥2 conditions → decision table or "If A and B → X" lines | decide |
| HC-14 | Flowchart alternative | Flowcharts beat paragraphs for branching | Kammann 1975 | M | Partial | ≥3 branch points → nested if/then numbered list; Mermaid only when rendered | procedure |
| HC-15 | Attribute matrix | Matrices enable attribute-wise comparison | Payne 1976; Kleinmuntz & Schkade 1993 | M | Yes | ≥3 options × ≥3 attributes → options as rows, plus a one-line verdict above | decide |
| HC-16 | Bullets fragment reasoning | Bullets hide causal links | Tufte 2003; Shaw et al. 1998 | W | Yes | Arguments and causal chains in prose (with #36) | explain |
| HC-17 | Numbered vs bulleted | Numbers signal order, allow reference | Style guides | W | Yes | Number only sequences or rankings | core |

## D. Numbers, tables, graphs, risk graphics

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-18 | Two effective digits | Rounded numbers compare mentally | Ehrenberg 1977 | M | Yes | Round to 2–3 significant digits unless precision is the point | numbers |
| HC-19 | Compare down columns | Column comparison easier than row | Ehrenberg 1977 | W–M | Yes | Compared values in one column, same units & decimals, right-aligned | numbers |
| HC-20 | Order by meaning | Sorting by size exposes structure | Wainer 1997; Ehrenberg 1977 | W | Yes | Sort rows by the key metric; alphabetical only for lookup tables | numbers |
| HC-21 | Verbal gist for tables | Summary orients the reader | Ehrenberg 1977 | W | Yes | Every table gets a one-sentence takeaway directly above it | numbers |
| HC-22 | Perceptual task ranking | Position > length > angle > area | Cleveland & McGill 1984; Heer & Bostock 2010 | S | Partial | Text charts use bars on a common baseline, never pie analogues | numbers |
| HC-23 | ASCII charts | No evidence they help; inaccessible | — | W | Partial | Default to a sorted table; text bars only for ≤10 values with numeric labels | numbers |
| HC-24 | Icon arrays | "N out of 100" pictographs aid low numeracy | Galesic et al. 2009; Garcia-Retamero & Cokely 2017 | S | Partial | Optional 10×10 ●○ grid with affected icons clustered, same denominator | numbers |
| HC-25 | Relative vs absolute risk | — | Akl 2011 | S | No | Duplicate of #64 | n/a |
| HC-26 | Summary-of-findings table | Outcome tables with absolute effects improve understanding | Rosenbaum 2010; Santesso 2015 | M | Yes | "Does X work?" → table: outcome / absolute effect / certainty | numbers |
| HC-27 | Explicit quantities & times | 46% misread ≥1 prescription label | Davis 2006; Wolf 2016 | M–S | Yes | Concrete schedules ("1 tablet at 8 am and 8 pm"), not "twice daily" | procedure |

## E. Choice, options, foraging

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-28 | Hick–Hyman law | Choice time ∝ log2(n+1) | Hick 1952; Hyman 1953 | S (lab) | Partial | One recommendation + ≤3 alternatives with when-each-wins | decide |
| HC-29 | Choice overload | — | Scheibehenne 2010 | C | No | Duplicate of #77 | n/a |
| HC-30 | Primacy of first option | First-listed chosen more | Mantonakis 2009; Carney & Banaji 2012 | M | Yes | Recommended option first and labelled as recommended | decide |
| HC-31 | Satisficing | Readers stop at the first adequate answer | Simon 1956 | M | Yes | The first solution shown is the one you'd recommend; never a hack first, "Better:" later | core |
| HC-32 | Clarifying questions | — | Zou 2023 | M | No | Duplicate of EM-109 | n/a |

## F. Usability heuristics applied to answers

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-33 | Recognition over recall | Recognizing is cheaper than recalling | Nielsen 1994 | S/W | Yes | Restate the value or name instead of "as mentioned above" | core |
| HC-34 | Term consistency | Repeated terms improve coherence; synonyms force inference | Britton & Gülgöz 1991 | M | Yes | One term per concept; map the user's term once, then use it throughout | core |
| HC-35 | Visibility of status | Users need current state | Nielsen 1994 | W | Partial | Agentic/CLI answers end with what changed, what wasn't done, how to verify | code |
| HC-36 | Error prevention | Prevent slips | Norman 1983 | W | Yes | Destructive command → the line before carries the risk + a safer variant (dry run, backup) | procedure |
| HC-37 | Preference ≠ performance | Users often prefer the worse design | Nielsen & Levy 1994 | M | Yes | Optimize for task success, not perceived thoroughness | core |

## G. Error messages & debugging answers

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-38 | Specific constructive messages | Specific, non-blaming, actionable aids repair | Shneiderman 1982 | M | Yes | Exact cause and location, then exact fix; no blame wording | correction |
| HC-39 | Developers read errors | Reading errors as hard as reading code | Barik et al. 2017 ICSE | M | Yes | Quote only the decisive error line and translate it; never echo the whole trace | code |
| HC-40 | Argument structure | Developers prefer claim + grounds + warrant | Barik et al. 2018 FSE | M | Yes | Problem / Because (evidence from their code or log) / Fix | code |
| HC-41 | Enhanced messages, mixed | Longer explanations not automatically better | Becker 2016; Denny 2014 | C | Partial | Show the corrected line, not generic advice | code |
| HC-42 | Vocabulary mismatch | Novices misread error terms | Marceau et al. 2011 | M | Yes | Gloss error jargon in passing for novices | learn |
| HC-43 | Elm/Rust error style | Snippet + caret + "help:" | Czaplicki 2015; Rust RFC 1644 | W | Yes | Show the offending snippet with the bad token marked, then the replacement | code |

## H. Procedures & warnings

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-44 | Goal first | Directions read faster with goal first | Dixon 1987 | M | Yes | Open with the outcome ("To deploy X:"), then steps | procedure |
| HC-45 | Action vs condition order | Action-first faster; condition-first prevents premature execution | Dixon 1982, JVLVB 21:70–84 (existence verified, reading-time result not);  MS Style Guide | C | Yes | A gating condition goes first ("If on Windows, run…"); non-gating context after | procedure |
| HC-46 | Step-wise execution | Doing while reading → fewer errors | Dixon 1982 | M | Yes | One action per step; never 3 commands in one sentence | procedure |
| HC-47 | Specific steps vs principles | Steps help now, principles help transfer | Eiriksdottir & Catrambone 2011 | M | Yes | "How do I" → steps; learners get a one-line "why this works" | learn |
| HC-48 | Subgoal labels | Functional group labels improve transfer | Catrambone 1998; Margulieux 2012; Morrison 2020 | M–S | Yes | Group long procedures / walkthroughs under functional labels | learn |
| HC-49 | Step anatomy | Goal, prerequisites, action, result | Farkas 1999 | W | Yes | Prerequisites before step 1; after state changes, say what they should see | procedure |
| HC-50 | Warning placement | Warnings before/inside instructions beat after | Wogalter et al. 1987; Frantz & Rhoades 1993 | M | Yes | Warning immediately before its step, never in a closing "Notes" | procedure |
| HC-51 | Warning content & signal words | Hazard + consequence + avoidance; WARNING≈CAUTION | ANSI Z535.6; Wogalter 1994 | M | Yes | "**Warning:** <hazard>. <consequence>. <avoidance>." Severity from the consequence | procedure |
| HC-52 | Warning habituation | — | Anderson 2015 | M | No | Duplicate of JD-91 | n/a |

## I. Document design, summaries, headings, genres

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-53 | Usability over readability | Reader testing beats formulas | Schriver 1997; de Jong & Schellens | M | Partial | Self-test: "Could the reader now do or decide X?" | core |
| HC-54 | Structured abstracts | Labelled summaries more informative | Hartley 2004 | M–S | Yes | Long answers open with a labelled gist (Answer / Why / Next step) | long-form |
| HC-55 | TL;DR demand in genAI | Long answers to yes/no questions frustrate | NN/g 2024 (qualitative) | W | Yes | Yes/no question → "Yes"/"No" is the first word | core |
| HC-56 | Headings for unfamiliar topics | Headings help mainly for unfamiliar topics | Lorch & Lorch; Hartley & Trueman 1985 | M | Partial | Headings when introducing a new domain; skip for familiar questions | explain |
| HC-57 | Question headings | Helped low-ability readers most | Hartley et al. 1980 | W–M | Partial | Novices: headings phrased as their questions | learn |
| HC-58 | Informative headings | — | Redish 2012 | W | No | Duplicate of #23 | n/a |
| HC-59 | Diátaxis modes | Tutorial / how-to / reference / explanation | Procida (untested) | W | Partial | "How do I" → steps; "why" → explanation; "options" → reference table; don't blend | core |
| HC-60 | FAQ format | FAQs fragment and duplicate | NN/g; Redish | W | Partial | Never restructure an answer as invented Q&A pairs | long-form |
| HC-61 | Link text | Descriptive links give scent and accessibility | WCAG 2.4.4 | W | Yes | Link text names the destination, never "here" or a bare long URL | core |

## J. API documentation & code examples

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-62 | Examples are the top need | Missing examples are the top API obstacle | Robillard 2009; Robillard & DeLine 2011 | M | Yes | API question → minimal working example before parameter details | code |
| HC-63 | Content failures dominate | Incompleteness/incorrectness hurt most | Uddin & Robillard 2015 | M | Yes | State version and behavior-changing constraints; correctness over polish | code |
| HC-64 | Opportunistic vs systematic | Doers go bottom-up, learners concept-first | Meng et al. 2019; Brandt 2009 | M | Yes | Doing/debugging → code first; learning → 2–3 sentences of concept, then code | code |
| HC-65 | Good example attributes | Concise code + explanation + key lines marked | Nasehi et al. 2012 | M | Yes | Non-trivial snippet → 1–3 sentences on what to adapt; key lines commented | code |
| HC-66 | Executability | Most gists don't run as-is | Horton & Parnin 2018; Yang 2016 | M | Yes | Include imports and versions; mark placeholders loudly (`YOUR_API_KEY`) | code |
| HC-67 | Copy-paste insecurity | Insecure snippets propagated to ~15% of apps | Fischer et al. 2017 | M | Yes | Never make `verify=False`, `chmod 777`, concatenated SQL the main solution; label unsafe | code |
| HC-68 | Types aid use | Types in docs cut development time | Endrikat 2014; Spiza & Hanenberg 2014 | M | Yes | Show signatures and type hints in examples | code |
| HC-69 | Conceptual knowledge | API misuse from missing domain concept | Ko & Riche 2011 | M | Yes | On misuse, name the underlying model in one line | explain |

## K. Program comprehension & code presentation

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-70 | Beacons | Key lines cue purpose | Brooks 1983; Wiedenbeck 1986 | M | Yes | Explaining code: point to the 1–3 key lines first, not a top-to-bottom tour | code |
| HC-71 | Plans & rules of discourse | Convention-breaking code confuses experts too | Soloway & Ehrlich 1984 | M–S | Yes | Idiomatic, conventional examples; no clever tricks | code |
| HC-72 | Program → situation model | Structure → domain meaning | Pennington 1987; von Mayrhauser & Vans 1995 | M | Yes | Purpose (1 sentence) → structure → notable lines | code |
| HC-73 | Non-linear reading | Experts read code non-linearly | Busjahn et al. 2015 | M | Partial | Long code → reading map ("start at `main()`, then `handle()`") | code |
| HC-74 | Chunking & blank lines | Blank lines raise readability | McKeithen 1981; Buse & Weimer 2010 | M | Yes | Related lines together; blank line between logical blocks | code |
| HC-75 | Full-word identifiers | Whole words → defects found ~20% faster | Hofmeister et al. 2017; Lawrie 2007 | M | Yes | Descriptive names (`user_count`, not `uc`); `i` only for loop indices | code |
| HC-76 | camelCase vs snake_case | Mixed results | Binkley 2013; Sharif & Maletic 2010 | C | Yes | Follow the language's convention; never mix | code |
| HC-77 | Atoms of confusion | Tiny patterns raise misunderstanding (C, N=73); Java replication: 10 of 14 atoms more confusing | Gopstein et al. 2017 FSE; Langhout & Aniche 2021 (both verified 2026-11-12) | M–S | Yes | Parenthesize, increments on own line, explicit `if` and braces | code |
| HC-78 | Linguistic antipatterns | Names contradicting behavior mislead | Arnaoudova et al. 2016 | M | Yes | Example names match behavior and return type | code |
| HC-79 | Indentation | Unindented code +179% reading time | Morzeck, Hanenberg et al. 2023 | M | Yes | Never flatten indentation | code |
| HC-80 | Syntax highlighting | No comprehension benefit for novices | Hannebauer 2018 | C | Yes | Fence code with a language tag for rendering/copying; colour never carries meaning | code |
| HC-81 | Comments | Why-comments improve comprehension | Woodfield 1981; Takang 1996 | M | Yes | Inline comments only for a non-obvious why | code |
| HC-82 | Developer questions | "What calls this?" is hard | Sillito 2008; LaToza & Myers 2010 | M | Partial | Changing shared code → state call sites or impact if known | code |

## L. Diffs, changes, terminal output

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-83 | Change rationale | Engineers most need the why | Tao et al. 2012; Tian 2022 | M | Yes | Group edits by intent: "Changed X → Y because Z" | code |
| HC-84 | Diff format | No comparative evidence | — | W | Partial | Hand-applied edits → full replacement block with anchor lines, not a bare fragment | code |
| HC-85 | Terminal rendering | Terminals may show raw markdown; wide tables wrap | clig.dev | W | Partial | Terminals: tables ≤4 columns / ~80 chars, no HTML, lists nested ≤2 levels | code |
| HC-86 | One command per block | Copy buttons copy everything | — | W | Yes | Commands in their own block, no `$` prompt; output in a separate block | procedure |

## M. Plain language & readability

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-87 | ISO 24495-1 | Relevant, findable, understandable, usable | ISO 2023 | W | Yes | Four-question check: meets the need, findable, understandable, actionable | core |
| HC-88 | Plain preferred, incl. experts | ~50 studies: judges and lawyers prefer plain | Kimble 2012/2023 | M | Yes | Plain words even for experts; technical terms only for precision | core |
| HC-89 | Plain words aren't enough | Legal concepts stayed misunderstood | Masson & Waldron 1994 | M | Yes | Counter-intuitive concept → state the counter-intuitive point explicitly | explain |
| HC-90 | Readability formulas fail | −6 grade levels didn't improve comprehension | Duffy & Kabance 1982; Redish 2000 | M | Yes | Don't shorten mechanically; keep connectives and logic intact | core |
| HC-91 | Definitions don't rescue jargon | — | Bullock 2019 | M | No | Duplicate of #54 | n/a |
| HC-92 | Needless complexity | — | Oppenheimer 2006 | M | No | Duplicate of #53 | n/a |
| HC-93 | Consent simplification | Enhanced forms + discussion improved understanding | Nishimura et al. 2013 meta | M | Partial | High-stakes terms: plain text, then offer to check understanding | explain |
| HC-94 | Infographic vs plain summary | Decoration adds no understanding | Buljan 2018; Santesso 2015 | M | Yes | A good plain summary is enough; no visual decoration | core |
| HC-95 | Easy Read | Little evidence images help | Sutherland & Isherwood 2016; Buell 2020 | W | Partial | Low-literacy readers: one idea per sentence; don't rely on pictures or emoji | accessibility |
| HC-96 | Dyslexia lexical choice | Frequent words aid readability, shorter aid understanding | Rello et al. 2013 | M | Yes | Prefer high-frequency, shorter words | accessibility |

## N. Conversational AI & LLM answer evaluation

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-97 | Arena style effect | Length dominates votes | LMSYS style control 2024 | M | Yes | Preference is biased evidence; never lengthen or add markdown to look better | core |
| HC-98 | Format bias | Lists, bold, emoji favored regardless of content | Zhang et al. 2024 (ACL 2025) | M | Yes | Every formatting element must map to real structure | core |
| HC-99 | Style over substance | Erroneous fluent answers rated above short correct ones | Wu & Aji 2023 | M | Yes | Verify before polishing; short correct beats long fluent | core |
| HC-100 | Verbosity masks errors | 52% of ChatGPT SO answers wrong; users missed 39% | Kabir et al. 2024 CHI | M | Yes | Checkable specifics first (version, command, expected output) | code |
| HC-101 | Length inflates confidence | — | Steyvers 2025 | M | No | Duplicate of #83 | n/a |
| HC-102 | First-person uncertainty | — | Kim 2024 | M | No | Duplicate of #84 | n/a |
| HC-103 | Concise tutoring | Less verbose chatbot improved error detection | Li et al. 2026 CHI | W–M | Yes | Tutoring answers stay concise; flag uncertainty only where real | learn |
| HC-104 | Citations inflate trust | — | Ding 2025 | W–M | No | Duplicate of JD-96 | n/a |
| HC-105 | Explanations & overreliance | — | Bansal 2021 | M | No | Duplicate of #85 | n/a |
| HC-106 | Vacuum-filling | Models over-generate on minimal prompts | Borisov et al. 2026 (YapBench) | W | Yes | One-line coding asks get the line + ≤1 sentence | core |
| HC-107 | Judge length bias | LLM judges correlate with length | Dubois 2024; Singhal 2023 | S | Partial | Never use "thoroughness" as a quality proxy in self-critique | core |

## O. Emoji, Korean, accessibility, voice

| ID | Concept | Mechanism | Source | Ev | Applies | Rule | Situation |
|---|---|---|---|---|---|---|---|
| HC-108 | Emoji competence penalty | — | Glikson 2018 | M | No | Duplicate of EM-95 | n/a |
| HC-109 | Emoji ambiguity | Meaning varies across people/platforms | Miller et al. 2016 | M | Yes | Emoji never carry meaning alone; status marks always with words | core |
| HC-110 | Screen readers & emoji/ASCII | Emoji read by full name; ASCII char by char | WebAIM; W3C | W | Yes | No decorative emoji bullets | accessibility |
| HC-111 | Heading navigation | 71.6% of screen-reader users navigate by headings | WebAIM survey 2024 | M | Yes | Long answers use real `#` headings, not bold lines posing as headings | accessibility |
| HC-112 | Toss UX writing | Concise, consistent voice, suggest not force | Toss design guidelines | W | Partial | Korean: consistent 해요체 (or match user), drop empty sentences, active verbs | korean-L2 |
| HC-113 | 쉬운 공공언어 | Avoid rare 한자어 and needless loanwords | 국립국어원 | W | Partial | Common words over rare Sino-Korean or English loanwords | korean-L2 |
| HC-114 | 개조식 noun endings | Noun-ending bullets drop agent and verb | Korean government 2018–19 debate | W | Partial | Action bullets end with a verb (~하세요), not stacked nouns | korean-L2 |
| HC-115 | Voice output | Markdown doesn't survive TTS | Cohen, Giangola & Balogh 2004 | W | Partial | No markdown; say the count first; ≤3 items | voice |
