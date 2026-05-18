# Example: Coding Flow

## User request

"Fix the login bug. It keeps failing after OAuth redirect."

## FlowCurrent setup

```text
Objective: Identify and fix login failure after OAuth redirect.
Curiosity object: Where does expected auth state diverge from actual state?
Accepted reachability: The bug can be narrowed through logs, route handling, state storage, and token exchange checks.
First feedback source: Search auth redirect handler and failing tests/logs.
```

## Operating loop

1. Inspect route and callback code.
2. Compare expected state parameter with stored state.
3. Check token exchange error handling.
4. Run tests or static checks.
5. Patch the smallest failing path.
6. Validate and summarize.

## Knowledge cracks

- "OAuth provider is broken" → first verify local state and callback handling.
- "Need a rewrite" → first locate the divergence.
- "No tests means no feedback" → use logs, static analysis, and a minimal reproduction.

## Final response shape

```text
I found the failure in [component]. The callback expected [X], but [Y] occurred after redirect. I changed [patch]. Validation: [test/check]. Remaining risk: [risk if any].
```
