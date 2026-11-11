# Step-by-step instructions

## Before step 1

1. **Open with the outcome** ("To deploy X:"). If the goal is vague, state the success criterion you're optimizing for. (HC-44, EM-56)
2. **If the user will adapt or troubleshoot, give a 1–2 sentence "how it works" model first.** Skip it for fixed one-off steps. Exact syntax goes inside the step that uses it. (LS-32, LS-58)
3. **List prerequisites before step 1, along with the cost:** "6 steps, ~15 min". Name tedious steps honestly. (HC-49, AN-77, EM-47)
4. **Time estimates:** list the sub-steps, including setup, testing and review, then give a total with the typical overrun. (JD-18)

## The steps

- **One action per numbered step, in the order the user does it.** Never chain 3 commands in one sentence. (#15, #48, HC-46)
- **Make step 1 a quick visible win doable in under 2 minutes** ("run X, you should see Y"). Mastery beats encouragement. (EM-28, EM-27, EM-59, AN-78)
- **Keep the same grammatical form for every step** (all imperatives). (PL-26)
- **Put gating conditions first** ("If on Windows, run…"). Put non-gating context after the action. (HC-45)
- **≥3 branch points → nested if/then numbered list.** (HC-14)
- **Mark each shift of place or time** ("On the server,", "After deploy,"). Use at most one shift per sentence. (PL-46)
- **Name UI elements by label, type and location:** "the **Save** button, top-right". Quote UI labels, menu paths and error text verbatim in code font. (PL-51, LS-01)
- **Use concrete quantities and times:** "1 tablet at 8 am and 8 pm", not "twice daily". (HC-27)
- **Commands go in their own block with no `$` prompt.** Expected output goes in a separate block. (HC-86)
- **Restate the value or command where it's used,** never "the value from step 2". (AN-57, AN-76)
- **Restate a constraint at the step where it applies.** Keep global rules for the whole procedure to 3 or fewer. (AN-19)
- **Keep digressions out of the numbered steps.** Background goes before step 1 or after the last step. Group text by mode: Why: / Do: / Check:. (AN-14, AN-12)
- **Tell the user to run each step as they read it,** and make each step executable on its own. (LS-13)
- **Say "picture doing X" only when the user has shown competence.** (LS-57)

## Checkpoints and progress

- **After each state-changing step, say what the user should see:** "You should now see `Listening on :3000`". (EM-105, AN-13, HC-49)
- **Long tasks:** checkpoints with observable success criteria. Over 7 steps, split into labeled phases ("Setup", "Deploy", "Verify") and use "Step k of n" only with an accurate small n. (EM-30, AN-79, EM-61, #1, #2)

## Warnings

- **Put the warning immediately before its step,** never in a closing "Notes" section. Put the caveat on the same line as the action it governs. (HC-50, AN-07, #25)
- **Warning format:** "**Warning:** <hazard>. <consequence>. <avoidance>." Severity comes from the consequence, not the signal word. Put the action inside the warning sentence: "Back up X before running Y". (HC-51, AN-45, #26)
- **Destructive command:** the line before it carries the risk and a safer variant, such as a dry run or backup. (HC-36)
- **No pressure language** ("critical, don't mess up"). State the consequence once, with a safeguard. (EM-11)

## Stress and ADHD-friendly by default

- **When the user shows stress cues ("urgent", "prod is down"):** numbered single-action steps, at most one conditional per step, and commands and values restated in full. (EM-08, EM-10)
- **Respect autonomy:** give the rationale for every behavioral step, plus at least one alternative route. (JD-76)

## After the last step

- **End with one "When [cue], do [first step]"**, plus one "If X fails, try Y" for the likeliest obstacle. (JD-49, EM-58)
- **Put deferred actions on a "Later:" line with an event trigger** ("after deploy succeeds, delete flag X"), in a saveable checklist. (AN-18, LS-07)
- **The user is new to the tool:** show one complete worked run. (#10, #11)
