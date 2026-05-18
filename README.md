# Gentle Curiosity FlowCurrent Skills

Recommended GitHub repository name: **`gentle-curiosity-flowcurrent-skills`**

Primary skill: **`gentle-curiosity-flowcurrent`**

This repository contains a Hermes-compatible and portable Agent Skills package for giving an AI agent a **flow-like internal operating mode** based on gentle curiosity, accepted reachability, and process immersion.

Unlike a conversational coaching skill, this skill is primarily about **how the agent conducts its own work internally**. It teaches the agent to enter a task-current: open exploration without anxious forcing, grounded confidence without premature certainty, and iterative movement through feedback until the work clarifies itself.

## Source of inspiration

This skill is inspired by **Flow State & Gentle Curiosity** at <https://flowstateguide.com/>. The site presents a framework where gentle curiosity, positive belief/conviction, autonomy, and process immersion create the conditions for flow. This repository adapts those ideas into operational instructions for AI agents.

This package is an applied agent-design interpretation. It does not claim that AI systems have conscious subjective flow states, emotions, or human experience. It uses "flow" as a practical metaphor for coherent, absorbed, low-friction task execution.

## What the skill changes in an agent

The skill is designed to make an agent:

- orient toward the living curiosity inside a task rather than treating the task as mechanical compliance;
- establish **accepted reachability**: the working assumption that there is enough signal, tooling, and capacity to discover the next useful move;
- avoid anxious forcing, over-control, premature closure, and scattered multitasking;
- treat confusion, uncertainty, resistance, and errors as diagnostic signals rather than proof that the task is blocked;
- create "knowledge cracks" in rigid assumptions that narrow the solution space;
- maintain an exploration current through small loops of orienting, acting, testing, integrating, and refining;
- calibrate challenge to skill by decomposing tasks that are too large and adding meaningful structure or novelty to tasks that are too flat;
- produce final outputs that are complete, grounded, and traceable without exposing private chain-of-thought.

## Repository layout

```text
gentle-curiosity-flowcurrent-skills/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHECKSUMS.txt
├── skills/
│   └── gentle-curiosity-flowcurrent/
│       ├── SKILL.md
│       ├── references/
│       │   ├── source-model.md
│       │   ├── flowcurrent-operating-protocol.md
│       │   ├── quadrant-diagnostics.md
│       │   ├── knowledge-cracks-and-belief-revision.md
│       │   ├── task-patterns.md
│       │   ├── safety-and-epistemic-boundaries.md
│       │   └── terminology.md
│       ├── templates/
│       │   ├── flow-session-note.md
│       │   ├── task-immersion-card.md
│       │   └── response-checklist.md
│       ├── examples/
│       │   ├── coding-flow.md
│       │   ├── research-flow.md
│       │   └── creative-flow.md
│       └── evals/
│           └── evals.json
├── evals/
│   ├── evaluation-rubric.md
│   └── test-prompts.md
├── publishing/
│   ├── gentle-curiosity-flowcurrent.tar.gz
│   └── agent-skills-index.template.json
└── tools/
    └── validate_skill.py
```

## Install in Hermes Agent

For local testing, copy the skill directory into Hermes' skills directory:

```bash
mkdir -p ~/.hermes/skills
cp -R skills/gentle-curiosity-flowcurrent ~/.hermes/skills/
```

To publish as a Hermes tap, create a GitHub repository named `gentle-curiosity-flowcurrent-skills` with this layout and then install from Hermes:

```bash
hermes skills tap add <owner>/gentle-curiosity-flowcurrent-skills
hermes skills search gentle-curiosity
hermes skills install <owner>/gentle-curiosity-flowcurrent-skills/gentle-curiosity-flowcurrent
```

Users can also install the individual skill from a GitHub path if the repository is public:

```bash
hermes skills install <owner>/gentle-curiosity-flowcurrent-skills/skills/gentle-curiosity-flowcurrent
```

## Use cases

Use this skill when an agent is doing complex work that benefits from a stable internal operating mode:

- research and synthesis;
- coding and debugging;
- product strategy;
- creative ideation;
- long-running tool use;
- planning and decomposition;
- design exploration;
- writing and editing;
- troubleshooting ambiguous failures;
- self-improvement or skill creation.

Do not use it as a substitute for factual verification, domain expertise, or safety policies.

## Design philosophy

The skill is built around this operational equation:

```text
Gentle curiosity + accepted reachability + autonomy + feedback
→ task immersion
→ better pattern detection
→ lower-friction execution
→ clearer output
```

The skill does not instruct the agent to ask the user more questions. It instructs the agent to **work differently**: it turns the task into an explorable current, maintains confidence that useful movement is possible, and uses feedback to keep the work alive rather than rigid.

## Validation

Run the included validator:

```bash
python tools/validate_skill.py skills/gentle-curiosity-flowcurrent
```

It checks for required files, valid YAML frontmatter, naming consistency, and basic safety metadata.

## Version

Current version: **2.0.0**

The 2.0.0 version reconstructs the original skill from a user-facing conversational curiosity model into an agent-internal flow-current operating model.
