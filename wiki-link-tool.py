#!/bin/python3
###################################################################################
# MIT License
# 
# Copyright (c) 2022 Christoph Lutz
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###################################################################################
'''
   Simple Tool for wiki-links in markdown-documents with the syntax "[[wiki link]]".
'''
import argparse
import sys
import re
import os
import pathlib

WIKI_LINK_RE=re.compile(r"\[\[([^\]#]+)(#[^\]]*)?\]\]")

def getWikiLinks(filename):
    links=set()
    with open(filename, "r") as md:
        for line in md.read().split("\n"):
            for m in WIKI_LINK_RE.finditer(line):
                links.add(m.group(1))
    return links

def getLinkList(files):
    links = dict()
    for filename in files:
        for link in getWikiLinks(filename):
            linklist = links.get(link) or []
            linklist.append(filename)
            links[link] = linklist
        myself=filename.replace(".md", "")
        links[myself] = links.get(myself) or []
    return links

def show_link_list(links):
    for link, linklist in sorted(links.items()):
            print("{} --> {}".format(link, ", ".join(linklist)))

def create_unresolved(links):
    for link, linklist in sorted(links.items()):
        mdfile = "{}.md".format(link)
        if not os.path.exists(mdfile):
            print("Creating file {}".format(filename_to_md_link(mdfile)))
            pathlib.Path(mdfile).touch()

def filename_to_md_link(filename):
        return "[{}]({})".format(filename.replace(".md", ""), filename.replace(" ", "%20"))

def backlinks_md(links, forFiles):
    for filename in forFiles:
        print("\n**Backlinks for {}**\n".format(filename_to_md_link(filename)))
        linklist = links.get(filename.replace(".md", "")) or []
        for linked_from in sorted(linklist):
            print("* {}".format(filename_to_md_link(linked_from)))

def is_unmodified(filename):
    return os.stat(filename).st_size == 0

def remove_unmodified_unlinked_files(links):
    for link, linklist in sorted(links.items()):
        filename="{}.md".format(link)
        if len(linklist) == 0:
            if is_unmodified(filename):
                print("Removing Unlinked and Unmodified '{}'".format(filename))
                os.remove(filename)
                del links[link]

def main():
    parser = argparse.ArgumentParser( prog = 'wiki-link-tool.py', description = __doc__)
    parser.add_argument('filename', nargs="*", help='markdown file for which an action is required (e.g. --backlinks-md)')
    parser.add_argument('--show-link-list', action="store_true", help='dump the link list created internally')
    parser.add_argument('--create-unresolved', action="store_true", help='create empty markdown files for all unresolved links')
    parser.add_argument('--backlinks-md', action="store_true", help='List backlinks for provided filename(s) in markdown style')
    parser.add_argument('--remove-unlinked', action="store_true", help='Removes all unlinked and unmodified markdown files (which might have been renamend)')
    args = parser.parse_args()

    mdfiles = list()
    for filename in os.listdir():
        if filename.endswith(".md"):
            mdfiles.append(filename)
        
    links = getLinkList(mdfiles)
    if args.show_link_list:
        show_link_list(links)

    if args.create_unresolved:
        create_unresolved(links)

    if args.remove_unlinked:
        remove_unmodified_unlinked_files(links)

    if args.backlinks_md:
        backlinks_md(links, args.filename or [])

        
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR: {}".format(e))
        sys.exit(1)
