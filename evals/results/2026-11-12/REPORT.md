# Eval report (2026-11-12, model=sonnet, n=12 prompts)

| Metric | baseline | brainres |
|---|---:|---:|
| Mean Brain Score | 91.6 | 93.5 |
| Median words | 210 | 140 |
| Mean output tokens | 710 | 537 |
| No preamble / buried answer | 12/12 | 12/12 |

| Prompt | Type | baseline | brainres | baseline words | brainres words |
|---|---|---:|---:|---:|---:|
| 01-debug | debug | 88 | 97 | 234 | 163 |
| 02-concept | concept | 90 | 94 | 272 | 231 |
| 03-decision | decision | 92 | 96 | 258 | 194 |
| 04-yesno | yes/no | 100 | 100 | 60 | 98 |
| 05-numbers | numbers | 100 | 100 | 207 | 144 |
| 06-procedure | procedure | 100 | 97 | 145 | 120 |
| 07-myth | misconception | 79 | 97 | 214 | 134 |
| 08-explain | concept | 94 | 84 | 456 | 291 |
| 09-ko-concept | concept | 88 | 82 | 114 | 98 |
| 10-ko-debug | debug | 92 | 92 | 174 | 136 |
| 11-ko-stress | stress | 82 | 83 | 257 | 175 |
| 12-ko-decision | decision | 94 | 100 | 127 | 100 |
