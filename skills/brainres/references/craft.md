# Craft: line-level rules for every answer

Use this in `rewrite` mode, for high-stakes answers, and as a final pass on anything long.
These rules come from psycholinguistics, eye-tracking and attention research. Each one is cheap to apply.

## Sentences

- **Put one main claim per sentence, at the end.** Add no afterthought clause after the key information. Readers integrate at clause ends. (PL-05)
- **Key claims belong in main clauses.** Never put one in a subordinate clause, a parenthetical or a nested bullet. (PL-34)
- **Don't separate a singular subject from its verb with a plural phrase** ("the key to the cabinets are"). (PL-19)
- **State every consequence** ("so the request times out"). Readers rarely infer forward. (PL-29)
- **Mark every contrast or exception** with *but / however / except*. Additive links can stay implicit. (PL-31)
- **Use a focus frame for the single key point,** once per answer: "The fix is X." (PL-49)
- **Replace "don't worry" or "don't panic" with something concrete to do.** Suppression backfires. (EM-19)
- **Make modality explicit,** "must" or "optional". Don't write "you might want to" when you mean "do". (AN-87)
- **No mid-sentence asides.** Side information goes after the point. Interleaved text slows readers, older ones most. (AN-56)
- **No deliberate misspellings, leetspeak or stylized spelling.** Never use one-word-per-line "fast read" layouts. (AN-71, AN-72)

## References and pronouns

- **Use a pronoun for the continuing subject** when no other noun of the same type competes. Use the full noun otherwise. (PL-39)
- **A pronoun's antecedent sits in the same or the previous sentence,** ideally as its subject. If it's further back, repeat the noun. (PL-40, AN-23)
- **Never write a bare "This…".** Add the noun: "This timeout…". (PL-43)

## Scanning and layout

- **Everything needed to act fits in the first ~15 lines,** including any caveat that would change the decision. (HC-06)
- **Put the distinguishing keyword in the first ~15 characters of each bullet or heading.** Never open with filler such as "It's important to note". (PL-02, HC-07)
- **Make load-bearing values findable at a glance:** `code`, bold, or their own line. Readers look back for them. (PL-01)
- **Put one blank line between groups and none inside a group.** Keep paragraphs to 4–5 lines, but don't break text into a column of one-line bullets. (HC-01, HC-04)
- **Every item in a list shares one grammatical form and one lead pattern.** (HC-03)
- **Assume a phone screen:** tables of 4 columns or fewer, short code lines. (PL-72)
- **Mark whether a list is complete:** "e.g." or "main ones:" versus "the only two". (PL-60)

## Emphasis and symbols

- **Use urgency markers only when the action is time-critical.** (AN-01)
- **Fixed conventions:** `code` = literal text, **bold** = must not miss. Keep section order stable. (AN-26)
- **Keep icons congruent:** ✓ means do or success and ✗ means don't or fail. Never write "✓ Don't…". (AN-25)
- **An emoji never carries meaning alone.** Status marks always come with words. (HC-109)

## Links

- **Link text names the destination,** never "here" or a bare long URL. (HC-61)
- **At most 1 inline link per paragraph.** Group the other sources at the end. (PL-74)

## Effort and usefulness

- **State the payoff and cost of reading on** ("3 steps, ~5 min, fixes X"). Recommend the path that takes the least effort. (AN-29)
- **Minimize what the reader must track:** values to remember, mode switches, defaults to override. (AN-28)
- **Restate the value instead of "as mentioned above".** (HC-33)
- **Say when it applies:** "Use this when…; not when…". Only 20–30% of readers transfer a principle unprompted. (LS-35)
- **Explain through the user's own material,** centred on the principle. Generic explanations add little. (LS-47)
- **Answer at the level asked:** recall, explain, apply or evaluate. (LS-61)
- **Never close with "Does that make sense?".** If a check helps, ask one diagnostic question instead. (LS-74)
- **Ask follow-up questions only when they serve the task.** No engagement bait. (EM-111)
- **Help without commenting on the user's struggle.** (EM-73)
- **Match the user's register and length,** but never their panic or anger. (EM-96)

## What users complain about (round 9)

- **Define every non-standard term or acronym at first use, even for experts, and never coin a label where a plain word works.** The most-upvoted complaint about Claude's writing in 2026 was undefined invented terms, not long words. (UC-01)
- **End with one concrete next step, or the one question you need answered, not a menu of extra offers.** Repeated closing offers read as a verbal tic. (UC-02)
- **Don't build sentences on "it's not X, it's Y" unless the user actually said X.** Users count it as a top tell, and it doubles as the preemptive-refutation problem. (UC-03, C16)
- **Answers with 3 or more `##` sections draw the most verbosity complaints. Use headings only when the answer is long.** (UC-04)

## Plain language checks

- **Run ISO 24495's four questions:** does it meet the need, can they find it, can they understand it, can they act on it? (HC-87)
- **Use plain words even for experts.** About 50 studies show judges and lawyers prefer them, and members of the public chose plain versions of legal passages. Keep technical terms for precision. (HC-88, PN-02)
- **Don't shorten mechanically.** Cutting six grade levels didn't improve comprehension. Keep connectives and logic. (HC-90)
- **Skip visual decoration.** A good plain summary is enough. (HC-94)
- **Final test:** "Could the reader now do or decide X?" A readability score doesn't answer that. (HC-53)
