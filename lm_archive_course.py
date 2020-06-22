#!/usr/bin/env python3

""" module to create course archive """

import configparser
import datetime
import sys

def archive_template(course_name, course_list):
    """ html template """
    title = f'<title> {course_name}\'s index </title>'
    style_sheet = '<link rel="stylesheet" type="text/css" href="style.css">'
    h1_title = f'<h1>Course: {course_name}</h1>'
    list_title = '<h1>Lecture index: </h1>'
    tuplify = (lambda i: (i, course_list[i]))
    itemify = (lambda t: \
            f'\t<li><a href=\"lecture{t[0].zfill(3)}.html\">{t[1]}</a></li>')
    course_list_s = list(map(tuplify, course_list))
    index_list = '\n'.join([
        '<ol>',
        '\n'.join(list(map(itemify, course_list_s))),
        '</ol>'
    ])
    date = datetime.date.today().strftime("%d/%B/%Y")
    date_sig = f'<p> Last updated: {date}</p>\n'

    return '\n'.join([title, style_sheet, h1_title, \
            list_title, index_list, date_sig])

def main():
    """ main function for archive """
    config = configparser.ConfigParser()
    config.read('.config.ini')
    if not config.has_section('config') \
            or 'course-name' not in config['config'] \
            or not config.has_section('course-index'):
        print('.config.ini or elements missing')
        sys.exit('missing elements')

    course_name = config['config']['course-name']
    course_list = config['course-index']
    try:
        course_file = open(f'{course_name}-archive.html', 'w')
    except OSError:
        sys.exit('Failed to create archive')
    course_file.write(archive_template(course_name, course_list))

if __name__ == '__main__':
    main()
