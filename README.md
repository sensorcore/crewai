# SensorCore Analytics Crew

AI-powered product analytics crew that connects to your [SensorCore](https://sensorcore.dev) project and delivers a comprehensive analysis report — health status, growth opportunities, and bug investigation — all in one run.

## What It Does

This crew deploys **3 specialized AI agents** that analyze your product data through SensorCore's 21 ML-powered tools via MCP:

| Agent | What It Does |
|---|---|
| **Health Monitor** | Detects errors, anomalies, regressions, and forecasts trends using Isolation Forest, Prophet, and PELT algorithms |
| **Growth Analyst** | Maps user flows, finds conversion bottlenecks, discovers behavioral predictors, and compares segments |
| **Bug Detective** | Investigates error patterns with Decision Trees, replays user journeys, and confirms findings with statistical tests |

The crew runs sequentially: Health → Growth → Bugs → Executive Summary, and saves a final `report.md` with prioritized findings and action items.

## SensorCore MCP Tools Used

All 21 tools run server-side on SensorCore — no local compute needed:

- **Discovery**: `get_project_stats`, `get_event_names`, `get_metadata_keys`
- **Data Access**: `get_logs`, `get_users`, `get_user_journey`, `get_dropoff_users`
- **ML Analytics**: `get_smart_alerts`, `get_error_clusters`, `get_anomalies`, `get_forecast`, `get_statistical_test`, `get_bug_detective`, `get_cohort_analysis`, `get_association_rules`, `get_user_flow`, `get_change_points`, `get_segment_comparison`, `run_behavioral_analysis`
- **Remote Config**: `get_remote_config`, `set_remote_config_flag`

## Quick Start

### Prerequisites

- Python 3.10+
- A [SensorCore](https://sensorcore.dev) account and project with data
- An OpenAI API key (or other LLM provider)

### Installation

```bash
# Clone the repository
git clone https://github.com/sensorcore/crewai.git
cd crewai

# Install dependencies
pip install -e .

# Set up environment
cp .env.example .env
# Edit .env with your API keys
```

### Configuration

Add your API keys to `.env`:

```env
SENSORCORE_API_KEY=sc_YOUR_PROJECT_API_KEY
OPENAI_API_KEY=sk-YOUR_OPENAI_KEY
```

Get your SensorCore API key from the [SensorCore Dashboard](https://sensorcore.dev) → Project Settings.

### Run

```bash
crewai run
```

The crew will analyze your project and save the results to `report.md`.

## Example Output

```markdown
# Product Analytics Report

## TL;DR
Error rate increased 23% after v2.1 release (Feb 15), primarily affecting
iOS 17.4 users. Conversion funnel shows 45% drop-off at paywall step.
Top growth opportunity: users who complete tutorial convert at 3.2x higher rate.

## Health Status: ⚠️ WARNING
- Error clusters: 3 active (payment_timeout most critical, 42 users affected)
- Anomaly detected: 2 users with abnormal navigation patterns
- Trend: Daily active events forecasted to grow 8% next week

## Growth Opportunities
1. Tutorial completion → 3.2x conversion lift (currently only 34% complete it)
2. Settings engagement → users who visit settings have 2.1x retention
3. DE segment outperforms US by 18% in retention (p=0.02)

## Critical Bugs
1. payment_timeout — 85% on iOS 17.4 + app_version=2.1.0 (p<0.001)
2. screen_render_crash — only on iPhone 12, iOS 17.x

## Action Plan
1. 🔴 Fix payment_timeout on iOS 17.4 (42 users affected, revenue impact)
2. 🟡 Add tutorial completion prompt after onboarding
3. 🟢 Investigate DE market for expansion opportunity
```

## How It Works

```
┌────────────────────────────────────────────────────────┐
│                    CrewAI Runtime                       │
│                                                        │
│  Health Monitor ──→ Growth Analyst ──→ Bug Detective   │
│       │                   │                  │         │
│       └───────────────────┴──────────────────┘         │
│                           │                            │
│                    Executive Summary                   │
│                     → report.md                        │
└────────────────────────┬───────────────────────────────┘
                         │ MCP Protocol
                         ▼
              ┌─────────────────────┐
              │  SensorCore Server  │
              │  21 ML-powered tools │
              │  Prophet, PELT,      │
              │  Isolation Forest,   │
              │  Decision Trees...   │
              └─────────────────────┘
```

## Customization

### Change the LLM

Set any [CrewAI-supported LLM](https://docs.crewai.com/concepts/llms) via environment variable:

```env
OPENAI_MODEL_NAME=gpt-4o-mini
```

### Modify Agents or Tasks

Edit the YAML configs:

- `src/sensorcore_crew/config/agents.yaml` — agent roles, goals, backstories
- `src/sensorcore_crew/config/tasks.yaml` — task descriptions and expected outputs

### Use a Different MCP Endpoint

For local development or self-hosted SensorCore:

```env
SENSORCORE_MCP_URL=http://localhost:3000/api/mcp/sse
```

## About SensorCore

[SensorCore](https://sensorcore.dev) is an AI-powered analytics and logging platform for mobile, web, and backend applications. It provides:

- **SDKs** for iOS (Swift) and JavaScript/TypeScript
- **21 MCP tools** for AI-agent analytics (12 ML algorithms)
- **Remote Config** for feature flags without app updates
- **Dashboard** for log viewing, user management, and project settings

→ [sensorcore.dev](https://sensorcore.dev) — create a free account to get your API key.

## Links

- [SensorCore Website](https://sensorcore.dev)
- [SensorCore Skills (AI Agent Docs)](https://github.com/sensorcore/skills)
- [SensorCore iOS SDK](https://github.com/sensorcore/ios)
- [SensorCore JS SDK](https://github.com/sensorcore/js)
- [CrewAI Documentation](https://docs.crewai.com)

## License

MIT
