#!/usr/bin/env python3

""" module to create course lecture """

import configparser
import sys
import datetime


def lecture_template(lecture_title):
    """ define lecture html template """
    style_sheet = '<link rel="stylesheet" type="text/css" href="style.css">'
    title = '<title> {lecture_title} </title>'
    date = datetime.date.today().strftime("%d/%B/%Y\n")
    return '\n'.join([
            style_sheet,
            title,
            date,
            '<hr/>'
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
    lecture_file.write(lecture_template(lecture_title))
    config.set('course-index', str(lecture_number), lecture_title)
    with open('.config.ini', 'w') as config_file:
        config.write(config_file)



if __name__ == '__main__':
    main()
