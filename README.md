# Skills

A collection repo for managing multiple skill repositories via [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

## Current Submodules

| Name | Repository |
|------|------------|
| flutter | [flutter/skills](https://github.com/flutter/skills) |
| vercel-labs | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| anthropics | [anthropics/skills](https://github.com/anthropics/skills) |

## Skills Directory

### [Flutter](https://github.com/flutter/skills)

| Skill | Link |
|-------|------|
| flutter-add-integration-test | [view](https://github.com/flutter/skills/tree/main/skills/flutter-add-integration-test) |
| flutter-add-widget-preview | [view](https://github.com/flutter/skills/tree/main/skills/flutter-add-widget-preview) |
| flutter-add-widget-test | [view](https://github.com/flutter/skills/tree/main/skills/flutter-add-widget-test) |
| flutter-apply-architecture-best-practices | [view](https://github.com/flutter/skills/tree/main/skills/flutter-apply-architecture-best-practices) |
| flutter-build-responsive-layout | [view](https://github.com/flutter/skills/tree/main/skills/flutter-build-responsive-layout) |
| flutter-fix-layout-issues | [view](https://github.com/flutter/skills/tree/main/skills/flutter-fix-layout-issues) |
| flutter-implement-json-serialization | [view](https://github.com/flutter/skills/tree/main/skills/flutter-implement-json-serialization) |
| flutter-setup-declarative-routing | [view](https://github.com/flutter/skills/tree/main/skills/flutter-setup-declarative-routing) |
| flutter-setup-localization | [view](https://github.com/flutter/skills/tree/main/skills/flutter-setup-localization) |
| flutter-use-http-package | [view](https://github.com/flutter/skills/tree/main/skills/flutter-use-http-package) |

### [Vercel-Labs](https://github.com/vercel-labs/agent-skills)

| Skill | Link |
|-------|------|
| composition-patterns | [view](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns) |
| deploy-to-vercel | [view](https://github.com/vercel-labs/agent-skills/tree/main/skills/deploy-to-vercel) |
| react-best-practices | [view](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| react-native-skills | [view](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-native-skills) |
| react-view-transitions | [view](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-view-transitions) |
| vercel-cli-with-tokens | [view](https://github.com/vercel-labs/agent-skills/tree/main/skills/vercel-cli-with-tokens) |
| vercel-optimize | [view](https://github.com/vercel-labs/agent-skills/tree/main/skills/vercel-optimize) |
| web-design-guidelines | [view](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) |
| writing-guidelines | [view](https://github.com/vercel-labs/agent-skills/tree/main/skills/writing-guidelines) |

### [Anthropics](https://github.com/anthropics/skills)

| Skill | Link |
|-------|------|
| algorithmic-art | [view](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) |
| brand-guidelines | [view](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) |
| canvas-design | [view](https://github.com/anthropics/skills/tree/main/skills/canvas-design) |
| claude-api | [view](https://github.com/anthropics/skills/tree/main/skills/claude-api) |
| doc-coauthoring | [view](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) |
| docx | [view](https://github.com/anthropics/skills/tree/main/skills/docx) |
| frontend-design | [view](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| internal-comms | [view](https://github.com/anthropics/skills/tree/main/skills/internal-comms) |
| mcp-builder | [view](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) |
| pdf | [view](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| pptx | [view](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| skill-creator | [view](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |
| slack-gif-creator | [view](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator) |
| theme-factory | [view](https://github.com/anthropics/skills/tree/main/skills/theme-factory) |
| web-artifacts-builder | [view](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) |
| webapp-testing | [view](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) |
| xlsx | [view](https://github.com/anthropics/skills/tree/main/skills/xlsx) |

### [Remotion-Dev](https://github.com/remotion-dev/skills)

| Skill | Link |
|-------|------|
| remotion | [view](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |

## Usage

### Clone with all submodules

```bash
git clone --recursive https://github.com/Areo-RGB/skills.git
```

### Add a new skill repo

```bash
python add_repo.py
```

Or manually:

```bash
git submodule add https://github.com/org/repo.git org-name
git commit -m "Add org-name submodule"
git push
```

### Update all submodules

```bash
git submodule update --remote --merge
git commit -am "Update submodules"
git push
```
