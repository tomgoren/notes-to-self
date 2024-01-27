+++
title = 'How this blog is hosted'
date = 2020-01-19
+++

## Overview

This is a meta post about how to host a blog with [Pelican](https://blog.getpelican.com/), the static site generator, and [Firebase Hosting](https://firebase.google.com/docs/hosting/), Google's easy-peasy platform.

## Why?

* Static pages are fast and uncomplicated
* Creating static pages with Markdown templates is more straightforward than writing HTML
* With a static site generator we can manage content with version control
* No database required
* Pelican is good at turning Markdown into HTML pages; it is written in Python, and it provides the following out of the box:
    * Themes
    * Syntax highlighting for code samples
    * Support for RSS feeds
    * etc.
* With Firebase we don't have to think about:
    * Servers
    * Object storage
    * Permissions
    * CDN
    * SSL
    * etc.

## How?

### Initial setup

* Follow the [Pelican quickstart](https://docs.getpelican.com/en/stable/quickstart.html)
* Follow the instructions [here](https://firebase.google.com/docs/hosting/) to get Firebase Hosting set up
* Pick a [theme](https://github.com/getpelican/pelican-themes)

#### Project layout

* I opted for the following directory structure:
```
.
├── blog
│  ├── __pycache__
│  ├── content
│  ├── output
│  ├── pelican-elegant -> ../../pelican-elegant
│  └── pelicanconf.py
├── firebase.json
├── LICENSE
└── requirements.txt
```
* The symlink to the theme directory (`pelican-elegant`) is cloned separately
    * This is to avoid some of the pains associated with [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

#### Firebase configuration

* Create a `firebase.json` file, something like:
```
{
  "hosting": {
    "public": "./blog/output",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ]
  }
}
```

#### Production

* Once you are happy with your new site, run `firebase deploy`
* Point DNS to the new website

### Day-to-day

* Create content (`vim ./content/this_post.md`)
* Generate static content (`pelican content`)
* Test locally (`pelican --listen`)
* Commit (`git add -A && git commit -am "Add a post about important content" && git push`)
* Deploy (`firebase deploy`)

## Notes

Some of the complexities and prerequisites not detailed here:

* Setting up a local Python development environment
* Creating a Google Cloud Platform account and hooking it up with Firebase
* Buying a domain and configuring DNS

### Source

This source of this project can be found [here](https://github.com/tomgoren/notes-to-self)
