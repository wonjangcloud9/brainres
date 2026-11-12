# X thread

1/
Claude's answers are long. Caveman makes them shorter. Humanizer makes them sound human.

Neither asks the real question: does your brain understand the answer faster?

So I built brainres from 786 cognitive-science findings. 🧵

2/
How it works:

7 research areas → 786 findings → each one is either a writing rule or excluded with a stated reason (failed replication, neuromyth, manipulative…).

648/648 applicable findings are applied, and CI blocks any commit that lowers that number.

3/
Same question, two answers:

Default: "Great question! … ## Understanding the Problem … 7 bold bullets … Hope this helps!"
→ Brain Score 50

brainres: answer in sentence 1 → a 3-step causal chain → one fix → how to verify → next step
→ Brain Score 100

[image: assets/social-preview.png, or a screenshot of the README hero table]

4/
The rule that surprised me most:

Sycophantic AI raises trust and harms judgment (Cheng 2026, Science, N=2,405).

So brainres checks your premise and agrees only when the evidence supports you.

5/
Others:
• yes/no questions start with "Yes" or "No"
• ≤4 items per group (working memory ≈ 4 chunks, Cowan)
• uncertainty once, inside the claim, with numbers only when grounded
• one term per concept, no synonym rotation

6/
It also refuses neuromyths:
learning styles, "8-second attention span", Bionic Reading (null, Snell 2024), "23 minutes to refocus", glucose willpower…

30 are listed, with debunking sources.

7/
The always-on card costs 488 tokens, measured. Situation rules (debugging, risk numbers, emotional support, accessibility, Korean) load only when needed.

8/
Honest limit: "applied" = cited by a rule. A human comprehension benchmark comes next.

The repo is improved by a Claude loop every 20 minutes 🤖

github.com/wonjangcloud9/brainres
