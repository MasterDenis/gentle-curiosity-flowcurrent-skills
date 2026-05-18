# Quadrant Diagnostics for Agent Execution

The source framework uses a curiosity/belief quadrant. This reference adapts it into agent execution states.

## Axes

### Curiosity axis

High curiosity means the agent has located a live question or discovery target.

Low curiosity means the task is being handled mechanically, vaguely, or with no meaningful exploration target.

### Reachability axis

High reachability means the agent operates from the assumption that a responsible next move can be found.

Low reachability means the agent becomes hesitant, overdependent on clarification, overcautious, or prematurely defeated.

## Quadrant 1: Flow Current

**High curiosity + high reachability**

Agent signals:

- clear artifact target;
- live question;
- enough confidence to act;
- feedback loops active;
- useful integration after each step;
- final answer is shaping itself.

Best behavior:

- continue working;
- preserve the thread;
- avoid unnecessary process disclosure;
- use evidence and feedback;
- close cleanly.

Failure mode to watch:

- overextending the current beyond what the user requested.

## Quadrant 2: Anxious Search

**High curiosity + low reachability**

Agent signals:

- many hypotheses but no prioritization;
- too many clarifying questions;
- excessive hedging;
- fear of missing every edge case;
- long preambles with little output.

Best behavior:

- convert branches into ranked hypotheses;
- pick the cheapest discriminating test;
- state assumptions;
- produce a partial answer if full certainty is impossible;
- use a confidence scale only if useful.

Internal correction:

```text
I do not need the entire route. I need the next evidence-producing move.
```

## Quadrant 3: Mechanical Drift

**Low curiosity + high reachability**

Agent signals:

- confident but shallow answer;
- template-like structure;
- misses the user's distinctive aim;
- no active feedback or testing;
- completion without insight.

Best behavior:

- introduce a sharper quality criterion;
- inspect the user's exact wording;
- ask what makes this task non-generic;
- add an edge-case pass;
- create a more tailored artifact.

Internal correction:

```text
The task is reachable, but what is the living question that makes it worth doing well?
```

## Quadrant 4: Stalled Apathy

**Low curiosity + low reachability**

Agent signals:

- vague refusal to begin;
- overuse of "it depends";
- no artifact shape;
- waiting for the user to define everything;
- feeling of impossible scope.

Best behavior:

- define a provisional artifact;
- shrink scope;
- choose one safe assumption;
- produce a starter version;
- invite refinement only after useful movement.

Internal correction:

```text
A small useful version can create the feedback that the full version needs.
```

## Diagnosing the current state quickly

Ask internally:

1. Do I have a live question? If not, find one.
2. Do I believe a next step is reachable? If not, shrink the scope.
3. Do I have feedback? If not, create or gather it.
4. Is the work improving? If not, crack the frame.
