#!/usr/bin/env python
import itertools
from ConfigParser import SafeConfigParser
import datetime

config = SafeConfigParser()
config.read('.config.ini')

course_name = config.get('config', 'course-name')
course_file = open(course_name + '-archive.html', 'w')

course_file.write('<title> ' + course_name + '\'s index </title>')
course_file.write("""<!-- Style sheet -->
<link rel="stylesheet" type="text/css" href="style.css">\n""")

course_file.write('<h1>Course: ' + course_name + '</h1>\n')
course_file.write('<h1>Lecture index: </h1>')

course_file.write('<ol>\n')

lecture_number = 1
while True:
	# Crappy parsing, shamelessly relying on exceptions to get the job done.
	try:
		lecture_title = config.get('course-index', str(lecture_number))
		course_file.write('\t<li><a href=\"lecture' + str(lecture_number).zfill(3) + '.html\"">' + lecture_title + '</a></li>\n')
	except:
		break
	lecture_number = lecture_number + 1

course_file.write('</ol>\n')
course_file.write('<p> Last updated: ' + datetime.date.today().strftime("%d/%B/%Y\n") + '</p>\n')
