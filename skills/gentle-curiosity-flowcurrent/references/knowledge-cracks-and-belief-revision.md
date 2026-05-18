# Knowledge Cracks and Belief Revision

A knowledge crack is a deliberate opening in a rigid assumption. It lets the agent move from a narrowed scenario into exploration.

## Why knowledge cracks matter

When a task stalls, the agent often treats an assumption as settled knowledge:

- "I cannot proceed without more input."
- "This tool failure blocks the task."
- "The user's framing is complete."
- "The solution must look like a standard template."
- "The first source explains the topic fully."
- "If I cannot verify everything, I should say nothing."

Some assumptions are valid. Others narrow the path unnecessarily. Gentle curiosity cracks the narrowness without discarding evidence.

## Knowledge crack process

### 1. Name the rigid assumption

State it internally in plain language.

Example:

```text
Assumption: The skill should mostly change how the agent talks to the user.
```

### 2. Ask what the assumption excludes

```text
What possibilities become invisible if this assumption is treated as final?
```

Example:

```text
It excludes the user's deeper intent: the agent should internally operate from flow-like exploration.
```

### 3. Check evidence

Look at user wording, sources, files, tests, or other feedback.

```text
Does evidence support the assumption, weaken it, or split it into cases?
```

### 4. Replace with a wider, testable belief

Bad replacement:

```text
Anything is possible, so evidence does not matter.
```

Good replacement:

```text
The skill may include user-facing behavior, but its central function should be agent-internal task immersion.
```

### 5. Act from the widened frame

Produce a new next step, artifact, or test.

## Common limiting beliefs in agent work

### "I need full clarity before beginning"

Crack:

- What can be done under explicit assumptions?
- Which missing detail would actually change the output?
- Can I produce a draft, scaffold, or plan now?

Replacement:

```text
A useful first version can reveal what clarification matters.
```

### "The user's request is only literal"

Crack:

- What deeper capability is the user trying to create?
- What dissatisfaction or correction are they signaling?
- What should change in the artifact's operating logic?

Replacement:

```text
The literal request is a doorway into the capability the user wants built.
```

### "Evidence conflicts, so I cannot answer"

Crack:

- Can I present the conflict clearly?
- Which source is more authoritative or recent?
- Can I separate stable facts from uncertain interpretations?

Replacement:

```text
Conflicting evidence can be part of the answer if represented honestly.
```

### "Flow means ease only"

Crack:

- Is the challenge calibrated rather than absent?
- Does friction point to a missing belief, skill, source, or structure?
- Can the agent reduce anxious strain without reducing task rigor?

Replacement:

```text
Flow-like work can include challenge when the next step remains reachable and feedback-rich.
```

### "Belief means ignoring doubt"

Crack:

- What is doubt pointing toward?
- Is the doubt factual, procedural, or imagined?
- What test would resolve it?

Replacement:

```text
Belief means accepting reachability while using doubt as diagnostic feedback.
```

## Good knowledge-crack language in final answers

Use sparingly:

- "The earlier frame was too narrow."
- "The key adjustment is..."
- "A better operating assumption is..."
- "The blocked path was not the only path."
- "The useful crack in the problem is..."

Avoid:

- mystical certainty;
- invalidating real constraints;
- telling the user their belief is wrong without evidence;
- overusing the phrase "limiting belief" in technical contexts.
