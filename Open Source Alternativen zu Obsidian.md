# Open Source Alternativen zu Obsidian
Da Obsidian Closed Source ist und nur mit Abo für kommerzielle Nutzung angeboten wird, werde ich wohl kaum Obsidian in der Arbeit nutzen können. Ich benötige einen Open Source Ersatz, den ich in der Arbeit bedenkenfrei nutzen kann.

# Anforderungen
## GFM-Support
[GitHub Flavored Markdown (GFM)](https://github.github.com/gfm/) muss als Basis-Syntax verstanden und gerendert werden, weil sonst zumindest Task-Listen und Tabellen fehlen.

Dennoch bleiben selbst mit GFM-Support folgende Punkte offen:
* Support für [Quick-Links](#unterstützung-für-quick-links)
* Support für Tags in der Syntax `#`Tagname
* GFM unterstützt mittels `![Bild](bild-url.png)` nur die Einbindung von Bildern, nicht aber die dynamische Einbindung von Inhalten aus internen Links.

## Unterstützung für Quick-Links
Weder [Common Markdown](https://spec.commonmark.org/) noch das weit verbreitete [GitHub Flavored Markdown](https://github.github.com/gfm/) unterstützen die in Obsidian genutze Darstellung `[[`interner Link`]]` für interne Links. Statt dessen müssen "inline" Links dort immer in der Form `[interner Link](interner%20Link.md)` geschrieben werden. Diese Form ist unnötig redundant und eine echte Hürde bei der Nachbildung der durch Obsidian unterstützten Methodik "Zettelkasten". Die im Folgenden genannten "Quick-Links" müssen also zwingend unterstützt werden. Dabei sind folgende Varianten denkbar:

1. Die Quick-Link Notation wird durchgängig unterstützt, sowohl im Editorfenster als auch in der Preview, oder
1. Die Notation wird zur Laufzeit in inline-Links umgewandelt

## Erkennung und Darstellung von Tags
Die in Obsidian mittels `#`tag dargestellten Tags sollen in irgend einer Form sinnvoll erkannt werden. Insbesondere sollen die Tags nicht als Überschriften formatiert werden.

## Unterstützung von Backlinks (zu den o.g. Quick-Links und zu Tags)
Gemäß der "Second-Brain" Methodik kann man sich einen neu erstellten Quick-Link auch als Definition eines neuen Begriffes vorstellen, von dem man erwartet, dass dieser Begriff in Zukunft wohl noch häufiger vorkommen wird. Unter "Backlink" versteht man in diesem Zusammenhang die Möglichkeit, den neu definierten Begriff fragen zu können, in welchen Markdown-Files dieser Begriff genutzt (also Referenziert) wurde.

Backlinks sind eine wesentlicher Bestandteil, um verschiedene Dinge miteinander zu Verknüpfen und in einen Bezug bringen zu können.

## Es gibt einen Weg zu Nachbildung des Obsidian DataView-Plugins
Einen wirklichen Mehrwert im Vergleich zu bisherigen Markdown-Editoren schafft Obsidian insbesondere durch das DataView-Plugin. Es muss irgendwie möglich sein, dynamische Inhalte wie durch das DataView-Plugin dargestellt, in der Preview mit abzubilden.

# Evaluierung

## Visual Studio Code mit Markdown
* Mit der Extension **"markdown-preview-enhanced"** lassen sich andere für uns wichtige Ergänzungen machen *(Wichtig: mit Ctrl+K v erneut aktivieren!)*:
    * Die Preview kann Quick-Links darstellen! (aber leider werden Leerzeichen durch Unterstriche ersetzt, was nicht kompatibel ist zum Obsidian-Verhalten)
    * Der Parser kann erweitert werden, so dass dann auch tags sinnvoll dargestellt werden können. Dazu habe ich auch schon mit diesem [parser.js](https://shd101wyy.github.io/markdown-preview-enhanced/#/extend-parser) Snippet erste Erfahrungen gemacht (PoC ist sicherlich ausbaubar!):
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
    * Es sollen auch [Code Chunks](https://shd101wyy.github.io/markdown-preview-enhanced/#/code-chunk) möglich sein, mit denen man evtl. die Funktionen von DataView abbilden könnte
* Mit der Extension **"Markdown Linkifier"** wird die `[[`interner Link`]]` Syntax von Obsidian unterstützt  --> Aber leider nur im Markdown-Editor und nicht in der VS-Code Standard Vorschau
	* Schwächen: 
		* Backlinks werden in der Auto-Completion nicht unterstützt
		* Neue Seiten können damit nicht angelegt werden ([[Neuanlegen von Notizen über einen Quick-Link]])

### Evaluierung weiterer VSCode-Plugins
* Das Plugin **[Markdown Notes (Zettelkasten Remix)](https://marketplace.visualstudio.com/items?itemName=maxedmands.vscode-zettel-markdown-notes)** verspricht neben Quick-Links auch noch weitere Features wie z.B. das [[Neuanlegen von Notizen über einen Quick-Link]] - macht das aber ganz anders, weil eine Notiz nach dem Zettelkasten-Prinzip einen uniq Identifier besitzt (den wir aber nicht wollen, weil der Filename genug uniq ist). Über den "Pfad" als Identifier (das ist auswählbar) lassen sich aber keine neuen Notizen automatisch erstelln. Das Plugin möchte auch Tags unterstützen, habe ich aber nicht getestet. Außerdem wollen sie per Default den Suffix ".md" immer noch im Link mit aufführen, was auch zu Inkompatibllität mit Obsidian führt.

## Atom (NOK)
* https://atom.io/
* https://kofler.info/atom-als-markdownpandoc-editor/
* Wird nicht mehr weiter gepflegt, siehe https://github.blog/2022-06-08-sunsetting-atom/

## Joplin (NOK)
https://joplinapp.org/desktop/

Die Diskutieren hier, ob man "Quick Links" einführen könnte: https://discourse.joplinapp.org/t/internal-quick-linking-mindmapping/8984

### Fazit Joplin
* Joplin speichert alle Notizen ausschließlich in einer sqlite-Datenbank unterhalb `~/.config/joplin-desktop/database.sqlite` ab
* Neue Notizen erhalten eine ID mit einem Hash-Wert - ich möchte aber anstatt einem Hash-Wert den Klartext Filenamen haben, so wie ich ihn im Wiki-Link angegeben habe.
* Tags werden nicht im Dokument mit abgelegt, sondern in der Datenbank
* Leider trotz obiger Diskussion keine unmittelbare Unterstützung für Quick-Links enthalten. In meinen Recherchen habe ich aber dann nur von einem Plugin gelesen, welches in Echtzeit die `[[`linkname`]]` Syntax umwandelt in die Typische Link Syntax `(linkname)[/joplin-hash]`. Das ist für den von mir angestrebten Einsatz ohne Datenbank nicht zielführend.