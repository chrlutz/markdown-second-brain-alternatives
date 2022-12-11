# Visual Studio Code as a "Second Brain" UI

From all tools already compaired in the document [Open Source Alternatives for Obsidian (currently only in German language, sorry!)](Open%20Source%20Alternativen%20zu%20Obsidian.md), Visual Studio Code turned out to be one of the best toolings to support my workflows for building up a "Second Brain" with markdown files. Ok, according to the [Visual Studio Code License](https://code.visualstudio.com/license?lang=en) the software is not Open Source, but the license is permissive enought for me - in particular it explicitly allows usage within a "corporate network". It is also Extendible and the following "Visual Studio Code" Extensions are Open Source, so that there's even more possible in future. 

In this article I want to describe the best way I already found with Visual Studio Code.

## Visual Studio Code with Markdown

Visual Studio supports Markdown (built in) and is extendible regarding the kind of markdown and the supported dialects. There are many Extensions available for changing the behaviour of VS Code regarding markdown. VS Code also has a built in markdown preview in a "side by side" view.

## The Extension "markdown-preview-enhanced"

The extension "markdown-preview-enhanced" is an important extension which brings features important for our "Second Brain" use case (Activate the Preview with Ctrl+K v):

* The Preview is able to display "Quick-Links" in the Preview Window
* It's Parser can be extended to support the `#`Tag syntax in the preview. Just with some little prototyping in [parser.js](https://shd101wyy.github.io/markdown-preview-enhanced/#/extend-parser) I got some quite reasonable results (but can still be improved):

    ```
    module.exports = {
        onWillParseMarkdown: function(markdown) {
            return new Promise((resolve, reject)=> {
                markdown = markdown.replace(/#(\w+)/gm, ($0, $1) => `[#${$1}](tags/${$1}.md)`);
                return resolve(markdown);
            })
        },
        onDidParseMarkdown: function(html, {cheerio}) {
            return new Promise((resolve, reject)=> {
                return resolve(html)
            })
        },
        onWillTransformMarkdown: function (markdown) {
            return new Promise((resolve, reject) => {
                return resolve(markdown);
            });
        },
        onDidTransformMarkdown: function (markdown) {
            return new Promise((resolve, reject) => {
                return resolve(markdown);
            });
        }
    }
    ```
* Es allows to use [Code Chunks](https://shd101wyy.github.io/markdown-preview-enhanced/#/code-chunk) to display dynamic data within the Preview. This for example allows us to implements functions similar to the ones of the Obisidian DataView Plugin

**Weaknesses:**
* Spaces in the Link Text of a Quick-Link will be converted to underscores in the Link Destination. This is incompatible to the behaviour of Obsidian)

## The Extension "Markdown Linkifier"

(Take Care: don't mix up with "Markdown Linkify"!)

This Extension allows us to use Quick Links in the Syntax `[[`internal Link`]]` in the Editor windows (left beside the Preview Window) as well. The feature comes with autocompletion for all articles already available as files in the repository.

**Weaknesses:** 
* The Auto-Completion doesn't recognize and support new terms (for a new Quick Link, there's not automatically a new markdown file created)
* The extension can't create new Pages just by pressing the Ctrl+Click on a Quick-Link in the Editor Window.

## Mitigating the Weaknesses of the above Extensions

I think, in the long run, it would make most sense to Improve the  above Extensions somehow to get rid of the mentioned weeknesses.

As a quick and "early to use" workaround, I implemented the [wiki-link-tool.py](wiki-link-tool.py) that can be used within a markdown document using the following Syntax:

```
> ```bash {cmd=true, output="markdown"}
> ./wiki-link-tool.py --create-unresolved --backlinks-md "<filename>.md"
> ```
```

### --create-unresolved
This creates new empty markdown files for all Quick-Links in documents for which there are currently no files created. After doing so, the Auto-Completion of the "Markdown Linkifier" Extension is able to find the previously missing "Backlinks". 

### --backlinks-md
Shows backlinks to the document `<filename>.md` as markdown in the current document.