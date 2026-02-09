# notes-to-self

Personal blog source for [notes.tomgoren.com](https://notes.tomgoren.com), built with Hugo.

## Structure

- Site config: `hugo.toml`
- Content: `content/posts/`
- Static assets: `static/`
- Theme: `themes/hugo-theme-m10c` (git submodule)
- Site-level template overrides: `layouts/`

## Theme override note

This repo currently overrides `layouts/_default/baseof.html` to inject Umami analytics into `<head>`.

Reason: upstream `hugo-theme-m10c` defines `<head>` inline in its base template and does not expose a head extension partial/hook. For a fuller note and proposed upstream fix, see `UPSTREAM_THEME_NOTES.md`.
