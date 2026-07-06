"""
Auto-versioning for SOP pages.

For every page under docs/sops/ (excluding the section index page), this hook
inspects the file's git history and injects a small version banner at the top
of the rendered page — no manual editing required. The version number is
derived from how many commits have touched that file:

    v1.<number of commits that changed this file>

and is paired with the date of the most recent commit to that file.

If the file has no git history yet (e.g. a brand-new page that hasn't been
committed), a "draft" banner is shown instead so authors know it isn't
version-tracked yet.

Requires the CI checkout to use `fetch-depth: 0` (full history) — a shallow
clone will only show the most recent commit and undercount revisions.
"""

import os
import subprocess


def _git_history(file_path, repo_root):
    try:
        result = subprocess.run(
            ["git", "log", "--follow", "--format=%h|%ad", "--date=short", "--", file_path],
            capture_output=True,
            text=True,
            cwd=repo_root,
            timeout=10,
        )
    except Exception:
        return None

    if result.returncode != 0:
        return None

    lines = [line for line in result.stdout.strip().splitlines() if line]
    if not lines:
        return None

    commit_count = len(lines)
    latest_date = lines[0].split("|")[1]
    return commit_count, latest_date


def on_page_markdown(markdown, page, config, files, **kwargs):
    src_relpath = page.file.src_path.replace("\\", "/")
    parts = src_relpath.split("/")

    # Only stamp actual SOP documents, not the section index page.
    if len(parts) < 2 or parts[0] != "sops" or parts[-1] == "index.md":
        return markdown

    repo_root = os.path.dirname(os.path.abspath(config["config_file_path"]))
    src_abspath = page.file.abs_src_path

    history = _git_history(src_abspath, repo_root)

    if history:
        commit_count, latest_date = history
        version = f"v1.{commit_count}"
        plural = "" if commit_count == 1 else "s"
        banner = (
            f'!!! info "Document version"\n'
            f"    **{version}** &nbsp;\u2014&nbsp; Last updated **{latest_date}** "
            f"&nbsp;({commit_count} revision{plural} on file)\n\n"
        )
    else:
        banner = (
            '!!! info "Document version"\n'
            "    **Draft** \u2014 not yet committed to version control. "
            "A version number and date will appear automatically once this page is committed.\n\n"
        )

    return banner + markdown
