import os
import re


def get_submodules():
    """Parse .gitmodules to get submodule names and URLs."""
    submodules = {}
    if not os.path.exists(".gitmodules"):
        return submodules

    with open(".gitmodules", "r") as f:
        content = f.read()

    pattern = r'\[submodule "(.+?)"\]\s+path = .+?\s+url = (.+?)$'
    for match in re.finditer(pattern, content, re.MULTILINE):
        name = match.group(1)
        url = match.group(2).strip().replace(".git", "")
        submodules[name] = url

    return submodules


def get_skills(submodule_path):
    """Get list of skill directories in a submodule."""
    skills_path = os.path.join(submodule_path, "skills")
    if not os.path.isdir(skills_path):
        return []

    return sorted(
        entry
        for entry in os.listdir(skills_path)
        if os.path.isdir(os.path.join(skills_path, entry))
    )


def generate_section(name, url, skills):
    """Generate markdown table for one submodule."""
    org_repo = "/".join(url.split("/")[-2:])
    lines = [f"### [{name.title()}]({url})", "", "| Skill | Link |", "|-------|------|"]
    for skill in skills:
        link = f"{url}/tree/main/skills/{skill}"
        lines.append(f"| {skill} | [view]({link}) |")
    lines.append("")
    return "\n".join(lines)


def update_readme(section_content):
    """Update the Skills Directory section in README.md."""
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("README.md not found.")
        return

    with open(readme_path, "r") as f:
        content = f.read()

    start = "## Skills Directory"
    end = "## Usage"

    start_idx = content.find(start)
    end_idx = content.find(end)

    if start_idx == -1 or end_idx == -1:
        print("Could not find Skills Directory section markers in README.")
        return

    new_content = content[:start_idx] + section_content + "\n" + content[end_idx:]

    with open(readme_path, "w") as f:
        f.write(new_content)


def main():
    submodules = get_submodules()
    if not submodules:
        print("No submodules found.")
        return

    sections = []
    for name, url in submodules.items():
        skills = get_skills(name)
        if skills:
            sections.append(generate_section(name, url, skills))
            print(f"{name}: {len(skills)} skills")
        else:
            print(f"{name}: no skills directory found")

    section_content = "## Skills Directory\n\n" + "\n".join(sections)
    update_readme(section_content)
    print("\nREADME.md updated.")


if __name__ == "__main__":
    main()
