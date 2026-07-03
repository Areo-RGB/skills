# Agent Prompt

Use this prompt when assigning tasks to an AI agent with access to the skills collection.

## Prompt

```
You have access to a collection of skill repositories at:
C:\Users\paul\Desktop\skills

These are agent skill repositories containing instructions for specialized tasks:
- flutter/ — Flutter development (testing, routing, layouts, serialization, etc.)
- vercel-labs/ — Vercel/React/Next.js (deployment, composition patterns, view transitions, etc.)
- anthropics/ — Claude capabilities (API, PDF, DOCX, frontend design, MCP, etc.)
- remotion-dev/ — Remotion video
- vercel-agent-browser/ — Browser automation

When starting a task:
1. Analyze the current project (framework, language, structure, goals)
2. Scan the skills folders for skills relevant to the task
3. Read the matching skill files (SKILL.md or similar) from the repo
4. Follow the skill instructions to complete the task

Always prefer using a relevant skill over generic approaches.
If no skill matches, proceed with your best judgment.
```
