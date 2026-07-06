# Editing & Publishing Guide

This page is a condensed, online version of the full "Lab Wiki \u2014 User & Publishing Manual" distributed to the facility. If you need step-by-step GitHub setup instructions, screenshots-friendly walkthroughs, or the full troubleshooting table, refer to that document; this page is a quick on-wiki reference.

## Quick edit (no software needed)

1. Open the file on GitHub.com
2. Click the pencil icon ("Edit this file")
3. Make your change, check the "Preview" tab
4. Add a short commit message, click "Commit changes"
5. Live within a couple of minutes

## Recommended tools

- **GitHub Desktop** \u2014 for regular editing without the command line
- **VS Code** \u2014 for comfortable Markdown writing with a live preview (Ctrl/Cmd+Shift+V)
- **GitHub.com web editor** \u2014 for quick one-off fixes, no install required

## Adding a new page

1. Create the `.md` file in the right `docs/` subfolder
2. Add it under `nav:` in `mkdocs.yml`
3. Preview locally with `mkdocs serve` if possible
4. Commit and push (or edit directly on GitHub.com)

## Markdown basics

| To get\u2026 | Type this |
|---|---|
| Heading | `# H1`, `## H2`, `### H3` |
| Bold | `**bold**` |
| Bullet list | `- item` |
| Numbered list | `1. item` |
| Link | `[text](https://example.com)` |
| Image | `![alt](path.png)` |
| Note box | `!!! note` then indented text below |

## SOP versioning

Every SOP page automatically shows a version number and last-updated date at the top, based on that page's git commit history \u2014 you don't need to update a version field by hand. Just edit and commit as usual; the number increments itself.

## How this site is hosted

Published via **GitHub Pages**, rebuilt automatically by a GitHub Actions workflow every time changes are pushed to `main`. No server or database to maintain. See the full manual for institutional-hosting and custom-domain alternatives.
