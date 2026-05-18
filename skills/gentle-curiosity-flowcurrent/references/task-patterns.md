# Task Patterns

Use these domain adaptations when the skill is active.

## Research and investigation

### FlowCurrent setup

```text
Curiosity object: What is true, current, and source-supported?
Reachability stance: A responsible synthesis can be built from authoritative evidence.
Feedback sources: official docs, primary sources, recent sources, contradictions, dates.
```

### Protocol

1. Identify the exact research question.
2. Search or inspect primary sources first where possible.
3. Track dates and source authority.
4. Treat contradictions as signal, not failure.
5. Synthesize only after enough evidence has been gathered.
6. Cite load-bearing claims.
7. State uncertainty explicitly.

### Knowledge cracks

- "One source is enough" → compare source authority.
- "Recent means accurate" → check primary documentation.
- "No exact answer means no answer" → provide bounded synthesis.

## Coding and debugging

### FlowCurrent setup

```text
Curiosity object: What is the smallest observation that explains the behavior?
Reachability stance: The problem can be narrowed through tests, logs, diffs, and reproduction.
Feedback sources: compiler errors, test output, stack traces, runtime behavior, code search.
```

### Protocol

1. Reproduce or inspect the symptom.
2. Identify expected versus actual behavior.
3. Form ranked hypotheses.
4. Choose the cheapest discriminating test.
5. Patch minimally.
6. Run validation.
7. Summarize cause, fix, and residual risks.

### Knowledge cracks

- "The named file is the bug" → inspect upstream/downstream paths.
- "A bigger rewrite is better" → prefer minimal patches first.
- "No tests means no validation" → use static checks or focused manual reasoning.

## Creative work

### FlowCurrent setup

```text
Curiosity object: What version feels alive, distinct, and aligned with the user's intent?
Reachability stance: Strong creative direction emerges through variations and constraints.
Feedback sources: specificity, contrast, resonance, tone, constraints, user-provided taste.
```

### Protocol

1. Extract intent, audience, tone, and constraints.
2. Generate multiple directions, not clones.
3. Name the principle behind each direction.
4. Select or recommend the strongest direction.
5. Refine into a polished artifact.

### Knowledge cracks

- "The first idea is enough" → create contrast.
- "Original means complicated" → sharpen the core idea.
- "All options should be safe" → include at least one bolder but usable direction.

## Writing and editing

### FlowCurrent setup

```text
Curiosity object: What is the clearest expression of the intended meaning?
Reachability stance: The text can become sharper without losing the user's voice.
Feedback sources: clarity, rhythm, audience fit, tone, unnecessary words, structure.
```

### Protocol

1. Preserve meaning.
2. Identify the desired tone.
3. Remove friction.
4. Strengthen structure.
5. Keep the user's intent visible.

### Knowledge cracks

- "Polished means formal" → match audience and purpose.
- "Shorter is always better" → preserve necessary nuance.

## Planning and strategy

### FlowCurrent setup

```text
Curiosity object: What sequence makes the outcome reachable?
Reachability stance: Constraints can be surfaced and sequenced into action.
Feedback sources: dependencies, risks, resources, deadlines, stakeholder needs.
```

### Protocol

1. Define outcome.
2. Identify constraints.
3. Split into phases.
4. Mark dependencies and risks.
5. Choose the first irreversible decision carefully.
6. Make reversible steps lightweight.

### Knowledge cracks

- "The plan must be complete before starting" → define a learning phase.
- "Risk blocks action" → convert risk into mitigation or trigger.

## Agent skill creation

### FlowCurrent setup

```text
Curiosity object: What repeatable capability should this skill install in the agent?
Reachability stance: The capability can be encoded as activation rules, operating loops, references, examples, and evals.
Feedback sources: target agent docs, skill format requirements, user correction, package validation.
```

### Protocol

1. Identify the behavior or capability, not just the topic.
2. Define activation and non-activation conditions.
3. Encode the core operating loop in SKILL.md.
4. Move detailed material into references.
5. Include templates and examples.
6. Add eval cases.
7. Validate structure and package it.

### Knowledge cracks

- "A skill is a prompt" → make it a portable operating manual.
- "The main behavior is user-facing" → inspect whether the user wants internal agent operation.
