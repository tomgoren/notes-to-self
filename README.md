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

## Development

This site pins Hugo with [mise](https://mise.jdx.dev/) in `.mise.toml`. CI installs the same mise-managed tools, so updating Hugo should only require changing `.mise.toml` and verifying the site locally.

Install the pinned tools:

```sh
mise install
```

Serve locally with the same Hugo version as CI:

```sh
mise exec -- hugo serve --environment production --disableFastRender
```

Build locally with the same Hugo version and production flags as CI:

```sh
mise exec -- hugo --gc --minify --baseURL "https://notes.tomgoren.com/"
```

If your shell has mise activated, `hugo` should already resolve to the pinned version inside this repo. `mise exec -- hugo ...` is the explicit, CI-matching form.

## Notes

- Existing post URLs are preserved under `/posts/`.
- Umami analytics is configured in `hugo.toml` via Hextra's built-in analytics settings.
