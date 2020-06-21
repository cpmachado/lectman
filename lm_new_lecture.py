#!/usr/bin/env python3

""" module to create course lecture """

import configparser
import sys
import datetime

config = configparser.ConfigParser()
config.read('.config.ini')

lecture_number = int(config['config']['lecture-number']) + 1
config.set('config', 'lecture-number', str(lecture_number))

lecture_file_name = 'lecture' + str(lecture_number).zfill(3) + '.html'
lecture_file = open(lecture_file_name, 'w')

lecture_file.write("""<!-- Style sheet -->
<link rel="stylesheet" type="text/css" href="style.css">\n""")

lecture_file.write('<!-- Date -->\n')
lecture_file.write(datetime.date.today().strftime("%d/%B/%Y\n"))
lecture_file.write('<hr/>')

lecture_title = ' '.join(sys.argv[1:])
lecture_file.write('<title>' + lecture_title + '</title>')

config.set('course-index', str(lecture_number), lecture_title)

with open('.config.ini', 'w') as config_file:
    config.write(config_file)
