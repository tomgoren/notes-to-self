# notes-to-self

Personal blog source for [notes.tomgoren.com](https://notes.tomgoren.com), built with Hugo.

## Human-authored content policy

All published blog content in `content/posts/` is written exclusively by a human.

Automation and machine assistance may be used for repository operations (for example: configuration, theming, tooling, refactors, or maintenance), but never to generate, rewrite, or "improve" post content.
When proposing changes, always defer to the human author for any edits to written content.

## Structure

- Site config: `hugo.toml`
- Content: `content/posts/`
- Static assets: `static/`
- Theme: `themes/hextra` (git submodule)

## Notes

- Existing post URLs are preserved under `/posts/`.
- Umami analytics is configured in `hugo.toml` via Hextra's built-in analytics settings.
