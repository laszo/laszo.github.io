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
blogTemplatePath = 'template/blog.html'
postoutpath = 'static/posts/'
pageoutpath = ''
contentpath = 'content/posts/'
pagespath = 'content/pages/'
indexFileName = 'index.html'
blogtitle = u'Lv Xiaoyu'


def read_config(text):
    get_header = re.compile(r'---[\s\S]*?---')
    header = get_header.findall(text)[0]
    content = text.replace(header, '', 1)
    header = header.replace('---', '')
    post_info = yaml.load(header)
    posttitle = ''
    for item in post_info:
        if item.upper() == 'title'.upper():
            posttitle = post_info[item]
    return content, posttitle


def createPost(post):
    text = codecs.open(contentpath + post, 'r', encoding='utf8').read()
    mkdtxt, posttitle = read_config(text)
    content = markdown.markdown(mkdtxt)
    t = codecs.open(postTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(content=content, posttitle=posttitle, blogtitle=blogtitle, baseurl=indexFileName)

    outfile = postoutpath + os.path.splitext(post)[0] + '.html'
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)
    return outfile, posttitle


def create_page(page, pagelinks):
    text = codecs.open(pagespath + page, 'r', encoding='utf8').read()
    mkdtxt, title = read_config(text)
    content = markdown.markdown(mkdtxt)
    t = codecs.open(pageTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(content=content, title=title, blogtitle=blogtitle, pagelinks=pagelinks)

    outfile = pageoutpath + os.path.splitext(page)[0] + '.html'
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)
    return outfile, title


def get_page_info(page):
    text = codecs.open(pagespath + page, 'r', encoding='utf8').read()
    mkdtxt, title = read_config(text)
    outfile = os.path.splitext(page)[0] + '.html'
    return outfile, title


def createBlogIndex(postlinks, pagelinks):
    t = codecs.open(blogTemplatePath, 'r', encoding='utf8').read()
    html = Template(t).render(postlinks=postlinks, pagelinks=pagelinks, title='Blog', blogtitle=blogtitle)

    outfile = indexFileName
    output_file = codecs.open(outfile, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(html)


def main():
    posts = os.listdir(contentpath)
    posts.reverse()
    postlinks = []
    for p in posts:
        if not check_file_ext(p, 'markdown'):
            continue
        if os.path.isfile(contentpath+p):
            url, title = createPost(p)
            postlinks.append({'title': title, 'url': url})
    pagefiles = os.listdir(pagespath)
    temp_links = []
    for p in pagefiles:
        if not check_file_ext(p, 'markdown'):
            continue
        text = codecs.open(pagespath + p, 'r', encoding='utf8').read()
        mkdtxt, title = read_config(text)
        outfile = os.path.splitext(p)[0] + '.html'
        temp_links.append({'title': title, 'url': url})
    pagelinks = []
    for p in pagefiles:
        if not check_file_ext(p, 'markdown'):
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

if __name__ == '__main__':
    main()
