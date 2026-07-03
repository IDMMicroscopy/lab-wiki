# Lab Wiki

SOPs, equipment guides, training materials, and policies for the facility — written as Markdown, versioned in this repo, and published as a searchable website using [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/).

## Structure

```
docs/
  index.md          # home page
  sops/              # standard operating procedures
  equipment/         # instrument pages
  training/          # onboarding & competency material
  policies/          # facility policies
mkdocs.yml           # site config + navigation
```

Every page is a plain `.md` file. Add a new page by creating the file, then adding it under `nav:` in `mkdocs.yml`.

## Local setup (to preview before publishing)

1. Install Python 3.9+ if you don't have it.
2. From this folder, install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Start the local preview server:
   ```
   mkdocs serve
   ```
4. Open `http://127.0.0.1:8000` in your browser — it live-reloads as you edit files.

## Publishing (GitHub Pages)

This repo includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that automatically builds and publishes the site to GitHub Pages every time you push to `main`.

**One-time setup after pushing this repo to GitHub:**

1. Push this folder to a new GitHub repository (public or internal, depending on your institution's GitHub setup).
2. In the repo, go to **Settings → Pages**, and set the source to the `gh-pages` branch (this branch is created automatically the first time the workflow runs).
3. Edit `site_url` in `mkdocs.yml` to match your published URL, e.g. `https://your-org.github.io/lab-wiki/`.
4. Anyone with the link can then read the wiki — no login needed, since it's a static site.

If your institution restricts GitHub Pages or you need it behind institutional login, the same `site/` folder that `mkdocs build` produces can instead be hosted on any internal web server (Apache/Nginx) or your existing university web hosting.

## Adding content — day to day

1. Create or edit a `.md` file in the right subfolder (e.g. `docs/sops/confocal-startup.md`).
2. If it's a new page, add a line for it under the matching section in `mkdocs.yml`'s `nav:`.
3. Commit and push. The site rebuilds automatically within a minute or two.

A blank SOP template is provided at `docs/sops/example-sop.md` — copy it as a starting point for new SOPs.

## Who can edit

Anyone with write access to the GitHub repo can edit pages directly on GitHub.com (no local setup needed — click the pencil icon on any file) or via a pull request, which is useful if you want changes reviewed before they go live.
