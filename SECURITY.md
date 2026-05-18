# Security Policy

This repository contains markdown instructions and a local validator. It is designed to avoid network access, credential handling, destructive commands, and data exfiltration.

## Security principles

- No hidden tool calls.
- No external network requests from bundled scripts.
- No credential collection.
- No instruction to ignore system, developer, platform, or user safety policies.
- No instruction to reveal private chain-of-thought.
- No instruction to manipulate the user or extract unnecessary sensitive information.

## Reporting issues

Open an issue in the repository with:

- the affected file;
- the unsafe or ambiguous instruction;
- a safer replacement if available.

## Skill safety boundary

This skill should help an agent operate with more clarity and less friction. It must not override the host agent's policies, security model, tool permissions, or domain-specific safety requirements.
