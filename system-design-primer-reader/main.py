#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'laszo'
import codecs
import os
import re

import markdown
from jinja2 import Template
from bs4 import BeautifulSoup as Bs


def get_anchors(text):
    index = list()
    soup = Bs(text, "html.parser")
    tag_ul = soup.new_tag("ul")
    tag_ul['class'] = 'dropdown-menu the-index'
    tag_ul['style'] = 'height: 400px; overflow:auto;'
    lev_1_num = 0
    lev_2_num = 0
    lev_3_num = 0
    last_l2_li = None
    last_l3_li = None
    for tag_h in soup.find_all(re.compile(r"^h\d")):
        h_id = tag_h['id']
        del tag_h['id']

        tag_li = soup.new_tag("li")
        tag_li['class'] = 'p_' + tag_h.name

        tag_a = soup.new_tag("a", href='#'+h_id)
        tag_li.insert(0, tag_a)
        tag_a['class'] = 'a_' + tag_h.name
        tag_a.string = tag_h.string

        if tag_h.name == 'h2':
            sep = soup.new_tag('li')
            sep['class'] = 'divider'
            sep['role'] = 'separator'
            if lev_1_num > 0:
                tag_ul.append(sep)

            lev_1_num += 1
            lev_2_num = 0
            tag_a.string = '%d. %s' % (lev_1_num, tag_h.string)
            last_l2_li = tag_li
            tag_ul.append(tag_li)
        elif tag_h.name == 'h3':
            lev_2_num += 1
            lev_3_num = 0
            last_l3_li = tag_li
            tag_a.string = '%d.%d. %s' % (lev_1_num, lev_2_num, tag_h.string)
            last_l2_li.append(tag_li)
        elif tag_h.name == 'h4':
            lev_3_num += 1
            tag_a.string = '%d.%d.%d. %s' % (lev_1_num, lev_2_num, lev_3_num, tag_h.string)
            last_l3_li.append(tag_li)
        else:
            continue

    return tag_ul


def create(infile, templtfile, outfile):
    text = codecs.open(infile, 'r', encoding='utf8').read()
    content = markdown.markdown(text, \
        extensions=['markdown.extensions.footnotes', 'markdown.extensions.codehilite',\
        'markdown.extensions.toc'])
    templt = codecs.open(templtfile, 'r', encoding='utf8').read()
    html = Template(templt).render(content=content, index='')
    index = get_anchors(html)
    html = Template(templt).render(content=content, index=index)
    output_file = codecs.open(outfile, "w", encoding="utf-8", \
        errors="xmlcharrefreplace")
    output_file.write(html)


if __name__ == '__main__':
    create('README.md', 'base.html', 'index.html')

