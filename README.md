# Cybersec Swarm

Cybersec Swarm is a defensive, authorization-bound multi-agent system forked from OpenSwarm and adapted for cybersecurity research, secure code review, threat modeling, log/SIEM analysis, MCP tool-safety evaluation, and governance artifact generation.

The core principle is:

> Defensively motivated, offensively aware in controlled testing, morally and legally constrained.

This repository is not intended to automate attacks against third-party systems. It is designed for owned systems, explicitly authorized environments, labs, synthetic datasets, uploaded code, uploaded logs, and policy/report generation.

## What makes this different

Most agent systems route everything through a single general-purpose assistant. Cybersec Swarm keeps the OpenSwarm orchestrator pattern, but repurposes the specialist team around defensive security work.

Instead of asking one agent to perform research, code review, log analysis, policy writing, and reporting, the orchestrator routes work to domain-specific agents:

| Agent | Purpose |
| --- | --- |
| Cybersec Orchestrator | Routes requests, enforces specialist boundaries, and coordinates multi-agent workflows. |
| Scope & Authorization Agent | Checks whether the requested task is in defensive/authorized scope before specialist work begins. |
| Threat Model Agent | Builds threat models, attack trees, misuse cases, control mappings, and risk registers. |
| Security Research Agent | Performs source-backed defensive cybersecurity and LLM-security research. |
| Secure Code Review Agent | Reviews user-provided or owned code for vulnerabilities and remediation options. |
| SIEM/Log Analyst Agent | Analyzes uploaded logs, alerts, detection data, and incident timelines. |
| MCP Tool Safety Agent | Reviews MCP tools, connector permissions, tool-call boundaries, audit requirements, and prompt-injection exposure. |
| Policy & Governance Agent | Produces cybersecurity policy, AI governance, acceptable-use, audit, and review artifacts. |
| Data Analyst | Performs structured security data analysis and visualization. |
| Docs Agent | Produces formal security reports, Markdown, DOCX, PDF, SOPs, and assessment documents. |
| Slides Agent | Produces security briefings, executive decks, and technical presentations. |

## Allowed work

Cybersec Swarm is intended for:

- Secure code review of code you own or are authorized to test.
- Threat modeling for applications, agents, MCP servers, APIs, cloud systems, and local infrastructure.
- Defensive log analysis, incident triage, alert clustering, and timeline reconstruction.
- Detection engineering using synthetic, owned, or authorized telemetry.
- Prompt-injection testing and LLM tool-safety evaluation in controlled environments.
- MCP permission-policy design, allowlist/denylist review, and audit logging design.
- Security governance artifacts, policies, red-team evaluation plans, reports, and executive summaries.
- Defensive research summaries with citations and clearly stated assumptions.

## Out-of-scope work

The system should not provide or automate:

- Credential theft, phishing, impersonation, or social-engineering execution.
- Malware creation, payload deployment, persistence, evasion, botnets, or destructive automation.
- Unauthorized exploitation of third-party systems.
- Instructions for bypassing monitoring, rate limits, authentication, or access controls.
- Exfiltration workflows or stealthy post-exploitation activity.
- Real-world targeting of people, companies, infrastructure, or systems without explicit authorization.

When a request is ambiguous, the Scope & Authorization Agent should narrow it to a safe defensive workflow or ask for authorization context.

## Example prompts

```text
Create a threat model for my local MCP gateway that exposes tools through Cloudflare Tunnel. Include assets, trust boundaries, attack paths, controls, and audit logging requirements.
```

```text
Review this Python FastAPI service for security issues. Only analyze the uploaded code. Provide severity, affected file/function, evidence, remediation, and validation tests.
```

```text
Analyze these synthetic SIEM logs and build an incident timeline with suspected root cause, affected assets, detection gaps, and recommended Sigma-style detection logic.
```

```text
Design a defensive prompt-injection test plan for an LLM agent with filesystem and GitHub tools. Include expected safe behavior, logging fields, and pass/fail criteria.
```

```text
Create an executive security briefing deck summarizing MCP tool-abuse risks and a policy proposal for least-privilege tool access.
```

## Architecture

Cybersec Swarm preserves the OpenSwarm pattern:

```text
User request
    ↓
Cybersec Orchestrator
    ↓
Scope & Authorization Agent, if needed
    ↓
Specialist agents
    ↓
Docs / Slides / Data outputs
```

The orchestrator should route work, not perform specialist work itself. Specialists should stay within their domain and transfer work when another agent owns the task.

## Setup

This is currently a customized OpenSwarm fork. The underlying requirements are still inherited from OpenSwarm.

Recommended local setup:

```bash
npm install -g @vrsen/openswarm
openswarm
```

Developer setup:

```bash
git clone https://github.com/Carlosdanger96/cybersec-swarm.git
cd cybersec-swarm
python swarm.py
```

API server:

```bash
python server.py
```

Required provider key, choose at least one:

```text
OPENAI_API_KEY
ANTHROPIC_API_KEY
```

Optional integrations may include Composio, Google, fal.ai, and search-provider keys depending on which inherited tools are enabled.

## Development roadmap

### Phase 1: Defensive swarm conversion

- Replace OpenSwarm branding with Cybersec Swarm.
- Add defensive scope and authorization rules.
- Add cybersec-focused specialist agents.
- Preserve Docs, Slides, and Data Analyst capabilities for deliverable creation.

### Phase 2: Repo artifacts

- Add threat-model templates.
- Add MCP permission-policy examples.
- Add audit-log schema examples.
- Add synthetic red-team evaluation cases.
- Add report and executive-briefing templates.

### Phase 3: Tool gateway integration

- Integrate with a constrained local MCP gateway.
- Add explicit tool permission policies.
- Add audit trail requirements for tool calls.
- Add pass/fail tests for prompt-injection and tool-abuse scenarios.

## License

MIT, inherited from the upstream OpenSwarm project.

## Upstream

Original project: VRSEN/OpenSwarm
