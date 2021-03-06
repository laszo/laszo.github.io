#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'laszo'
import codecs
import os
import re

import markdown
import yaml
from jinja2 import Template

postTemplatePath = 'template/post.html'
pageTemplatePath = 'template/page.html'
blogTemplatePath = 'template/blog.html'
postoutpath = 'static/posts/'
pageoutpath = ''
contentpath = 'content/posts/'
pagespath = 'content/pages/'
indexFileName = 'index.html'
blogtitle = u'Lv Xiaoyu `Site'


def read_config(text):
    anchors = get_anchors(text)
    get_header = re.compile(r'---[\s\S]*?---')
    header = get_header.findall(text)[0]
    content = text.replace(header, '', 1)
    header = header.replace('---', '')
    post_info = yaml.load(header)
    posttitle = ''
    # anchors = list()
    for item in post_info:
        if item.upper() == 'title'.upper():
            posttitle = post_info[item]
        # if item.upper().startswith('anchor'.upper()):
        #     line = post_info[item]
        #     words = line.split(',')
        #     if len(words) == 2:
        #         anchors.append((words[0], words[1]))
    return content, posttitle, anchors


def get_anchors(text):
    anchors = list()
    pat = re.compile(r"<h\d\sid='(?P<href>\w+)'>(?P<title>.*)</h\d>")
    res = pat.findall(text)
    if res:
        for mat in res:
            anchors.append(mat)
    return anchors


def createPost(post):
    text = codecs.open(contentpath + post, 'r', encoding='utf8').read()
    mkdtxt, posttitle, anchors = read_config(text)
    content = markdown.markdown(mkdtxt, \
                                extensions=['markdown.extensions.footnotes', 'markdown.extensions.codehilite'])
    t = codecs.open(postTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(content=content, title=posttitle, \
                              blogtitle=blogtitle, baseurl=indexFileName, anchors=anchors)

    outfile = postoutpath + os.path.splitext(post)[0] + '.html'
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)
    return outfile, posttitle


def create_page(page, pagelinks):
    text = codecs.open(pagespath + page, 'r', encoding='utf8').read()
    mkdtxt, title, anchors = read_config(text)
    content = markdown.markdown(mkdtxt, extensions=['markdown.extensions.footnotes'])
    t = codecs.open(pageTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(content=content, title=title, blogtitle=blogtitle, pagelinks=pagelinks)

    outfile = pageoutpath + os.path.splitext(page)[0] + '.html'
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)
    return outfile, title


def get_page_info(page):
    text = codecs.open(pagespath + page, 'r', encoding='utf8').read()
    mkdtxt, title, anchors = read_config(text)
    outfile = os.path.splitext(page)[0] + '.html'
    return outfile, title


def createBlogIndex(postlinks, pagelinks):
    t = codecs.open(blogTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(postlinks=postlinks, pagelinks=pagelinks, title='Blog', blogtitle=blogtitle)

    outfile = indexFileName
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)


_file_ext = 'markdownmd'


def main():
    posts = os.listdir(contentpath)
    posts.reverse()
    postlinks = []
    for p in posts:
        if not check_file_ext(p, _file_ext):
            continue
        if os.path.isfile(contentpath + p):
            url, title = createPost(p)
            postlinks.append({'title': title, 'url': url})
    pagefiles = os.listdir(pagespath)
    temp_links = []
    for p in pagefiles:
        if not check_file_ext(p, _file_ext):
            continue
        text = codecs.open(pagespath + p, 'r', encoding='utf8').read()
        mkdtxt, title, anchors = read_config(text)
        outfile = os.path.splitext(p)[0] + '.html'
        temp_links.append({'title': title, 'url': url})
    pagelinks = []
    for p in pagefiles:
        if not check_file_ext(p, _file_ext):
            continue
        url, title = get_page_info(p)
        pagelinks.append({'title': title, 'url': url})
    pagelinks.append({'title': 'Blog', 'url': indexFileName})
    pagelinks = sorted(pagelinks, key=lambda link: link['title'])
    for p in pagefiles:
        create_page(p, pagelinks)

    createBlogIndex(postlinks, pagelinks)


def check_file_ext(fname, ext):
    tlist = fname.split('.')
    if len(tlist) >= 1:
        if tlist[-1] == ext:
            return True
    return False


def get_files():
    for dirpath, dirnames, filenames in os.walk('content'):
        for fn in filenames:
            yield os.path.join(dirpath, fn)


def change_name():
    for a, b, c in os.walk('content\\posts'):
        for d in c:
            d1 = d.replace('markdownmd', 'md')
            f = os.path.join(a, d)
            f1 = os.path.join(a, d1)
            print(f)
            print(f1)
            os.rename(f, f1)


if __name__ == '__main__':
    # main()
    change_name()
