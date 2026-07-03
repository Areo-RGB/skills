import subprocess
import sys


def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()


def main():
    url = input("Enter repo URL (e.g. https://github.com/org/repo.git): ").strip()
    if not url:
        print("No URL provided.")
        sys.exit(1)

    default_name = url.rstrip("/").split("/")[-1].replace(".git", "")
    name = input(f"Directory name [{default_name}]: ").strip() or default_name

    print(f"\nAdding {url} as {name}/ ...")
    run(f"git submodule add {url} {name}")

    run("git add .")
    run(f'git commit -m "Add {name} submodule"')

    push = input("Push to remote? [Y/n]: ").strip().lower()
    if push != "n":
        run("git push")
        print("Pushed.")
    else:
        print("Committed but not pushed. Run `git push` when ready.")

    print("Done.")


if __name__ == "__main__":
    main()
