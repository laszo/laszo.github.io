# -*- coding: utf-8 -*-
__author__ = 'laszo'
import os
import re
import yaml
import codecs
import markdown
from jinja2 import Template

postTemplatePath = 'template/post.html'
indexTemplatePath = 'template/index.html'
outpath = 'output/'
contentpath = 'content/'
blogtitle = u'学到老，活到老'


def createPost(post):
    text = codecs.open(contentpath + post, 'r', encoding='utf8').read()
    mkdtxt, title = readPostConfig(text)
    content = markdown.markdown(mkdtxt)
    t = codecs.open(postTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(content=content, title=title, blogtitle=blogtitle)

    outfile = outpath + os.path.splitext(post)[0] + '.html'
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)
    return outfile, title


def readPostConfig(text):
    get_header = re.compile(r'---[\s\S]*?---')
    header = get_header.findall(text)[0]
    content = text.replace(header, '', 1)
    header = header.replace('---', '')
    post_info = yaml.load(header)
    title = ''
    for item in post_info:
        if item.upper() == 'title'.upper():
            title = post_info[item]
    return content, title


def createIndex(links):
    t = codecs.open(indexTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(links=links, title=blogtitle)

    outfile = 'index.html'
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)


def main():
    posts = os.listdir(contentpath)
    posts.reverse()
    links = []
    for p in posts:
        url, title = createPost(p)
        links.append({'title':title, 'url':url})
    createIndex(links)


if __name__ == '__main__':
    main()