# Verification round 1 (2026-11-12)

This round re-checked the citations that the catalogs flagged as unverified, plus the 5 studies that the README and always-on card lean on most.
Method: web search for the primary record (journal, DOI, proceedings, or arXiv), reading the full text where one was reachable.

| ID | Citation | Result | Grade change |
|---|---|---|---|
| JD-102 | Cheng et al. 2026, *Science* 391:eaec8352 | **Verified.** 3 preregistered experiments (N=2,405); 11 models affirmed users' actions 49% more often than humans; users preferred and trusted the sycophantic AI | S (unchanged) |
| JD-96 | Ding et al. 2025, AAAI 39:23787–95 | **Verified.** Trust rose with citations, even random ones, and fell when participants checked them | M (unchanged) |
| EM-91 | Ibrahim, Hafner & Rocher 2026, *Nature* | **Verified.** 5 models, >400k responses; warm-tuned models made 10–30 pts more errors and ~40% more agreement with false beliefs; cold-tuned models kept accuracy | M (unchanged) |
| #84 | Kim et al. 2024, FAccT | **Verified.** Preregistered, N=404; first-person hedges lowered agreement and raised accuracy; impersonal hedges were weaker and not significant | M (unchanged) |
| #83 | Steyvers et al. 2025, *Nat Mach Intell* | **Verified.** Longer explanations raised confidence without raising accuracy; confidence-matched explanations narrowed the gap. Caveat: GPT-3.5 / PaLM2 on MMLU-style questions | M (unchanged) |
| EM-110 | Ashktorab et al. 2019, CHI | **Verified from full text.** N=203; "providing options and explanations were generally favored", even when the repair failed; preferences for Repeat were noisier | **W → M** |
| HC-77 | Gopstein et al. 2017 FSE; Langhout & Aniche 2021 | **Verified.** C study, N=73; the Java replication found 10 of 14 atoms more confusing | M–S (unchanged) |
| PL-14 | Hales, Williams & Rector 2017 | **Corrected.** This is an *APS Observer* opinion piece, not an experiment; the earlier "n=98" was not supported. The acronym corpus finding (Barnett & Doubleday 2020, eLife) stands | **W–M → W** |
| HC-13 | Wright & Reid 1973, *J Appl Psych* 57:160–166 | The paper exists; the result is known only through secondary sources | M (unchanged, flagged) |
| HC-45 | Dixon 1982, *JVLVB* 21:70–84 | The paper exists; the action-first reading-time result was not located | C (unchanged, flagged) |
| EM-112 | Korean speech-level UX study | Still not peer-reviewed; no peer-reviewed chatbot 존댓말/반말 experiment found | W (unchanged) |

**Effect on rules:** none had to be removed. PL-14's rule ("define acronyms the user hasn't used") is still supported by #54 (jargon penalty) and #40 (curse of knowledge), so it rests on those now. Its own citation counts as weak.

Sources: [Cheng 2026](https://www.ebsco.com/articles/psychology/b97e12e3-f8f7-57bb-b906-7956732ee30e/sycophantic-ai-decreases-prosocial-intentions-and-promotes-dependence) · [Ding 2025](https://ojs.aaai.org/index.php/AAAI/article/view/34550) · [Ibrahim 2026](https://www.ox.ac.uk/news/2026-04-29-friendly-ai-chatbots-make-more-mistakes-and-tell-people-what-they-want-to-hear) · [Kim 2024](https://www.arxiv.org/abs/2405.00623) · [Steyvers 2025](https://arxiv.org/html/2401.13835v2) · [Ashktorab 2019](https://dblp.org/rec/html/conf/chi/AshktorabJLW19) · [Gopstein 2017](https://pure.psu.edu/en/publications/understanding-misunderstandings-in-source-code/) · [Langhout & Aniche 2021](https://ar5iv.labs.arxiv.org/html/2103.05424) · [Hales 2017](https://www.purdue.edu/newsroom/releases/2017/Q1/fyi-abbreviations-exclude-readers-in-scientific-communication,-experts-say.html) · [Barnett & Doubleday 2020](https://elifesciences.org/articles/60080.pdf) · [Dixon 1982](https://scilit.com/publications/3c1c0efd41bec7bd5abe055cfa1d690b)
