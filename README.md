# markdown-second-brain-alternatives

This repository contains a collection of thoughts and scripts helping me to create my own set of markdown files that I can use like a "second brain" under a none restrictive lincensing model.

## What's a second brain and why (not) building it with markdown?

I am not a scientist, but I really like the approach of the closed source tool [obsidian.md](https://obsidian.md/) to work with markdown files implementing an own kind of [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten) for my own knowledge-management purposes. This approach puts it's **main focus on connecting things together in a very easy manner** and Obsidian proves that connecting things together could be a really easy game.

And that even I didn't like markdown very much for a long time. In the past, I used Markdown just for some documentation tasks within my own GitHub Projects, and maybe I didn't like it that much because just one simple restriction that seems to be a fundamental part of the [CommonMark-Specification](https://spec.commonmark.org/):

It's **cumbersome Syntax for expressing internal (inline) Links**. According to the CommonMark-Specification, an inline link always consists of two (mandatory) parts `[link text](link destination)` and this syntax forces you to write nearly redundant code if you just want to insert a repository/wiki internal link. For example for referring to an markdown page called "A Second Brain" in the same folder of my repository, I would have to write `[A Second Brain](A%20Second%20Brain.md)` which doesn't look very intuitive and forces me to write the title twice. This is not "quick"!

In the approach of a "Second Brain", I want to wite my notes as quick and with less overhead as possible. I want to connect different things (terms) together in a very easy way and with great support from the editor-tool, so that there is an autocompletion feature that automatically completes all references to terms that were already defined in the past. **Why is autocompletion so important?** It not just speeds up your writing time, but also ensures that the term is written correctly, so that we can match together all references to the same term later on. This way we can let our "Second Brain" continiously grow. We can collect thinks like daily worknotes, people, ideas, tasks, experiences, issues, ... together to one big building in which the things are connected and there are multiple paths to get knowlege back at a later time.

For this purpose, we don't just need References to a term, but **we also need backreferences** so that we can take a term and ask it "what did refer to you?". But backreferences are expensive as they force us to scan the complete set of our markdown files before we we know "who's referring what".

(How) can this be done with markdown?

  1. I would say that markdown is one of the simplest forms of writing structured notes. It's not overloaded with formatting features and corresponding metadata. Markdown has a very small footprint, so that **scanning the complete set of our markdown files is done very efficiently**. This allows us to implement backreferences easily.
  1. The above mentioned "inline links of CommonMark" are not suitable for quick linking things toghether, but other Wiki-Markdown-like languages use a so called "Wiki-Link" or (as I call them) **"Quick-Links" in the syntax `[[`link text`]]`**. This syntax is less redundant and quite more inteligent, as it is able to automatically create a correct link destination (e.g. by just adding a `.md` suffix to the link text according to the context). But just again for the record: **This syntax can't be read by some of the most important current markdown tools!** There is a kind of tradeoff between compatibility and "easy linking" and in the context of a "second brain" we regard "easy lining" as more important.
  1. Choose a **good editor with a great User Interface for markdown support**

In **conclusion** I would say that pure Markdown according the CommonMark-Specification is not really suitable for building up a "Second Brain", but if we expand markdown to an own dialect and find a User Interface that supports this dialect, markdown could be a really great thing for our "Second Brain".

And this is what this repository is about. **A collection of evaluation results, ideas and prototypes with the goal to implement the workflows for efficiently building a "Second Brain" with none closed source tools.**

## Evaluation of alternative Markdown Editors
Please continue to read in [Open Source Alternatives for Obsidian (currently only in German language, sorry!)](Open%20Source%20Alternativen%20zu%20Obsidian.md)


# How could you help?
If you think that there's something wrong in this collection of articles, or you know some new aspects not yet considered, please open an GitHub-Issue in this repository.

# License
Everything in this folder is under [MIT License](LICENSE).