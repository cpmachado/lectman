#!/usr/bin/env python3

""" module to create course lecture """

import configparser
import sys
import datetime


def lecture_template(lecture_title, tags):
    """ define lecture html template """
    title = f'<title> {lecture_title} </title>'
    style_sheet = '<link rel="stylesheet" type="text/css" href="style.css">'
    meta_charset = '<meta charset="utf-8">'
    meta_tags_list = list(map((lambda i: (i, tags[i])), tags))
    meta_tags = list(map((lambda tup: f'<meta {tup[0]}="{tup[1]}">'),
                         meta_tags_list))
    date = datetime.date.today().strftime("%d/%B/%Y\n")
    h1_title = f'<h1> {lecture_title} </h1>'
    return '\n'.join([
        title,
        style_sheet,
        meta_charset,
        '\n'.join(meta_tags),
        date,
        '<hr/>',
        h1_title
    ])


def main():
    """ main function for new lecture """
    if len(sys.argv) < 2:
        lecture_title = input('Lecture name: ')
    else:
        lecture_title = ' '.join(sys.argv[1:])

    config = configparser.ConfigParser()
    config.read('.config.ini')
    lecture_number = int(config['config']['lecture-number']) + 1
    config.set('config', 'lecture-number', str(lecture_number))

    lecture_file_name = f'lecture{str(lecture_number).zfill(3)}.html'
    lecture_file = open(lecture_file_name, 'w')
    if config.has_section('tags'):
        tags = config['tags']
    else:
        tags = []
    lecture_file.write(lecture_template(lecture_title, tags))
    config.set('course-index', str(lecture_number), lecture_title)
    with open('.config.ini', 'w') as config_file:
        config.write(config_file)



if __name__ == '__main__':
    main()
