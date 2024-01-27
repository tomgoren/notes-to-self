+++
title = 'Developing Rust in Neovim'
date = 2019-10-18
+++

## Overview
Here is a short set of instructions on how to get started with Rust in Neovim.

This guide assumes [Neovim](https://neovim.io/) is already installed and that we are using [vim-plug](https://github.com/junegunn/vim-plug) to manage its plugins.

## Install
We need Rust.

```
curl https://sh.rustup.rs -sSf | sh
```

* [Source](https://www.rust-lang.org/tools/install)


## Install extras
We need `rls` for the LanguageClient plugin to check our code in real time.

```
rustup component add rls rust-analysis rust-src
```

> The RLS provides a server that runs in the background, providing IDEs, editors, and other tools with information about Rust programs. It supports functionality such as 'goto definition', symbol search, reformatting, and code completion, and enables renaming and refactorings.

* [Source](https://github.com/rust-lang/rls)


## Install and configure IDE
Add the following to `~/.config/nvim/init.vim` (or equivalent):

```
Plug 'autozimu/LanguageClient-neovim', {
    \ 'branch': 'next',
    \ 'do': 'bash install.sh',
    \ }

let g:LanguageClient_serverCommands = {
    \ 'rust': ['~/.cargo/bin/rustup', 'run', 'stable', 'rls'],
    \ }
```
* [Source](https://github.com/autozimu/LanguageClient-neovim)
