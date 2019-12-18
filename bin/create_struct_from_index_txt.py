#!/usr/bin/python3
import os
import re
import unidecode

INDEX = []


def get_path(*fname):
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', *fname)


def slug(text):
    text = text.replace('\t', '')
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)


def read_struct_txt():
    with open(get_path('index.txt'), 'r') as fp:
        content = fp.read()
    return [(slug(l), len(l.split('\t'))) for l in content.split('\n')]


def create_file(parent, title):
    if not title or not parent:
        return
    INDEX.append(os.path.join(*parent[1:], title))
    path = get_path(*parent)
    if not os.path.exists(path):
        os.makedirs(path)
        open(os.path.join(path, '.gitkeep'), 'a').close()
    open(os.path.join(path, '%s.rst' % title), 'a').close()


def create_struct(lines, index, parent=[]):
    title, level = lines[index]
    if len(lines) == index + 1:
        create_file(parent, title)
        return
    next_level = lines[index + 1][1]
    if next_level == level:
        create_file(parent, title)
    elif next_level < level:
        create_file(parent, title)
        for i in range(level - next_level):
            parent.pop()
    elif next_level > level:
        parent.append(title)
    create_struct(lines, index + 1, parent)


lines = read_struct_txt()
create_struct(lines, 0)
with open(get_path('index.rst'), 'w') as fp:
    fp.write('.. toctree::\n')
    for line in INDEX:
        fp.write('   %s\n' % line)
