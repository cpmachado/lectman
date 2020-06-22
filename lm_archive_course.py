#!/usr/bin/env python3

""" module to create course archive """

import configparser
import datetime

def archive_template(course_name, course_list):
    """ html template """
    TITLE = f'<title> {course_name}\'s index </title>'
    STYLESHEET = '<link rel="stylesheet" type="text/css" href="style.css">'
    H1TITLE = f'<h1>Course: {course_name}</h1>'
    LIST_TITLE = '<h1>Lecture index: </h1>'
    tuplify = (lambda i: (i, course_list[i]))
    itemify = (lambda t: \
            f'\t<li><a href=\"lecture{t[0].zfill(3)}.html\">{t[1]}</a></li>')
    course_list_s = list(map(tuplify, course_list))
    INDEX_LIST = '\n'.join([
        '<ol>',
        '\n'.join(list(map(itemify, course_list_s))),
        '</ol>'
    ])
    DATE = datetime.date.today().strftime("%d/%B/%Y");
    DATE_SIG = f'<p> Last updated: {DATE}</p>\n'

    return '\n'.join([TITLE, STYLESHEET, H1TITLE, \
            LIST_TITLE, INDEX_LIST, DATE_SIG])

def main():
    """ main function for archive """
    config = configparser.ConfigParser()
    config.read('.config.ini')
    course_name = config['config']['course-name']
    course_list = config['course-index']
    course_file = open(f'{course_name}-archive.html', 'w')
    course_file.write(archive_template(course_name, course_list))

if __name__ == '__main__':
    main()
