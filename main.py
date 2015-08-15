# -*- coding: utf-8 -*-
__author__ = 'laszo'
import os
import re
import yaml
import codecs
import markdown
from jinja2 import Template

postTemplatePath = 'template/post.html'
pageTemplatePath = 'template/page.html'
indexTemplatePath = 'template/index.html'
outpath = 'output/'
contentpath = 'content/'
pagespath = 'content/pages/'
blogtitle = u'活到老，学到老'


def createPost(post):
    text = codecs.open(contentpath + post, 'r', encoding='utf8').read()
    mkdtxt, title = readConfig(text)
    content = markdown.markdown(mkdtxt)
    t = codecs.open(postTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(content=content, title=title, blogtitle=blogtitle)

    outfile = outpath + os.path.splitext(post)[0] + '.html'
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)
    return outfile, title


def create_page(page, pagelinks):
    text = codecs.open(pagespath + page, 'r', encoding='utf8').read()
    mkdtxt, title = readConfig(text)
    content = markdown.markdown(mkdtxt)
    t = codecs.open(pageTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(content=content, title=title, blogtitle=blogtitle, pagelinks=pagelinks)

    outfile = os.path.splitext(page)[0] + '.html'
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)
    return outfile, title


def readConfig(text):
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


def createIndex(postlinks, pagelinks):
    t = codecs.open(indexTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(postlinks=postlinks, pagelinks=pagelinks, title=blogtitle)

    outfile = 'index.html'
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)


def main():
    posts = os.listdir(contentpath)
    posts.reverse()
    postlinks = []
    for p in posts:
        if os.path.isfile(contentpath+p):
            url, title = createPost(p)
            postlinks.append({'title': title, 'url': url})
    pagefiles = os.listdir(pagespath)
    temp_links = []
    for p in pagefiles:
        text = codecs.open(pagespath + p, 'r', encoding='utf8').read()
        mkdtxt, title = readConfig(text)
        outfile = os.path.splitext(p)[0] + '.html'
        temp_links.append({'title': title, 'url': url})
    pagelinks = []
    for p in pagefiles:
        url, title = create_page(p, temp_links)
        pagelinks.append({'title': title, 'url': url})

    createIndex(postlinks, pagelinks)


if __name__ == '__main__':
    main()