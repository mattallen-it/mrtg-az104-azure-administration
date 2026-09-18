# Evidence and completion standard

## Status vocabulary

- **Planned:** instructions exist; work has not been performed.
- **In progress:** work has started; validation is incomplete.
- **Validated:** the stated lab scope has documented expected behavior, relevant failure/denial and retest where applicable, and cleanup. List untested extensions explicitly; a design-only core task does not qualify.
- **Design-only:** studied or modeled, not executed; retain the practical gap.
- **Needs repeat:** evidence or understanding is insufficient.

## Minimum evidence for a completed lab

1. MRTG requirement and starting state.
2. A justified configuration decision.
3. Expected versus observed result, including a denial/failure where applicable.
4. Sanitized evidence with a sentence explaining what each item proves.
5. Troubleshooting and retest when a fault is introduced.
6. Cleanup verification or an explicit retained-resource/cost record.
7. Limitations and a plain-language explanation without the walkthrough.

Screenshots are supporting evidence. A configuration screenshot alone does not prove successful access, alert delivery, or restoration. Record measured outcomes only: no invented savings, uptime, recovery times, or production impact.

## Evidence placement

Plan screenshot checkpoints before executing: important configuration, observed success, relevant fault/retest, and cleanup. Capture configuration and results before removing resources. Put each image beside the step it supports with a caption explaining what it proves; avoid a duplicate gallery. Keep expected/observed results and test-identity aliases in the lab’s validation table. Record timestamps only when they help interpret a test, incident, or cost.

Keep evidence next to the relevant lab. Prefer a few readable, purposeful screenshots to a capture of every click. Remove credentials, tokens, private keys, personal identifiers, billing details, and unrelated browser information. Review command output and exported configuration as well as images.

## Publication checklist

- [ ] Results distinguish performed work from proposed work.
- [ ] Every image has meaningful alt text and an explanatory caption.
- [ ] Links resolve and paths match actual filenames.
- [ ] The lab status and central progress tracker agree.
- [ ] Cleanup and remaining charges are documented.
- [ ] Screenshots and files have been reviewed for sensitive information.
