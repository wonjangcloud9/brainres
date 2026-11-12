# Eval report (2026-11-12-opus-split, model=opus, 12 prompts × 1 sample(s))

| Metric | baseline | brainres |
|---|---:|---:|
| Mean Brain Score | 92.8 | 96.6 |
| Median words | 220 | 140 |
| Mean output tokens | 1000 | 945 |
| No preamble / buried answer | 12/12 | 12/12 |

| Prompt | Type | baseline score | brainres score | baseline words | brainres words |
|---|---|---:|---:|---:|---:|
| 01-debug | debug | 94 | 100 | 273 | 194 |
| 02-concept | concept | 94 | 96 | 373 | 239 |
| 03-decision | decision | 86 | 100 | 256 | 159 |
| 04-yesno | yes/no | 100 | 100 | 121 | 77 |
| 05-numbers | numbers | 100 | 100 | 244 | 142 |
| 06-procedure | procedure | 92 | 100 | 124 | 101 |
| 07-myth | misconception | 94 | 93 | 196 | 127 |
| 08-explain | concept | 100 | 88 | 470 | 301 |
| 09-ko-concept | concept | 86 | 94 | 141 | 120 |
| 10-ko-debug | debug | 88 | 94 | 188 | 139 |
| 11-ko-stress | stress | 94 | 100 | 317 | 155 |
| 12-ko-decision | decision | 86 | 94 | 113 | 77 |
