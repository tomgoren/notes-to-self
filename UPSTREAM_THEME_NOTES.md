# Upstream theme note: head extension hook

## Context

This site uses `hugo-theme-m10c` as a git submodule in `themes/hugo-theme-m10c`.

We needed to add Umami analytics to the `<head>` element of every page.

## Limitation in upstream theme

In upstream `hugo-theme-m10c/layouts/_default/baseof.html`, the `<head>` is defined inline and there is no extension hook partial (for example, no `head-extra.html` include).

Because of that, adding one script currently requires a full site-level override copy at:

- `layouts/_default/baseof.html`

This creates avoidable duplication and makes future upstream syncs noisier.

## Proposed upstream improvement

Add a head hook partial in upstream base template, e.g. near the end of `<head>`:

```go-html-template
{{ partial "head-extra.html" . }}
```

Optionally include a no-op default partial in the theme:

- `layouts/partials/head-extra.html`

With this hook, downstream sites can inject analytics/snippets without duplicating `baseof.html`.

## PR framing

- Keep behavior unchanged by default.
- Add only the hook and optional empty/default partial.
- Explain this improves extensibility for analytics, consent scripts, verification tags, and similar one-line additions.
