# Skills

A collection repo for managing multiple skill repositories via [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

## Current Submodules

| Name | Repository |
|------|------------|
| flutter | [flutter/skills](https://github.com/flutter/skills) |
| vercel-labs | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |

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
