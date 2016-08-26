#!/usr/bin/env python

from ConfigParser import SafeConfigParser
from sys import argv
import datetime

config = SafeConfigParser()
config.read('.config.ini')

lecture_number = int(config.get('config','lecture-number')) + 1
config.set('config', 'lecture-number', str(lecture_number))

lecture_file_name = 'lecture' + str(lecture_number).zfill(3) + '.html'
lecture_file = open(lecture_file_name, 'w')

lecture_file.write("""<!-- Style sheet -->
<link rel="stylesheet" type="text/css" href="style.css">\n""")

lecture_file.write('<!-- Date -->\n')
lecture_file.write(datetime.date.today().strftime("%d/%B/%Y\n"))
lecture_file.write('<hr/>')

lecture_title = ' '.join(argv[1:])
lecture_file.write('<title>' + lecture_title + '</title>')

config.set('course-index', str(lecture_number), lecture_title)

with open('.config.ini', 'w') as config_file:
	config.write(config_file)
