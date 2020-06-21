#!/usr/bin/env python3

""" module to create course archive """

import configparser
import datetime

config = configparser.ConfigParser()
config.read('.config.ini')

course_name = config.get('config', 'course-name')
course_file = open(course_name + '-archive.html', 'w')

course_file.write('<title> ' + course_name + '\'s index </title>')
course_file.write("""<!-- Style sheet -->
<link rel="stylesheet" type="text/css" href="style.css">\n""")

course_file.write('<h1>Course: ' + course_name + '</h1>\n')
course_file.write('<h1>Lecture index: </h1>')

course_file.write('<ol>\n')

for lecture_number in config['course-index']:
    lecture_title = config['course-index'][lecture_number]
    course_file.write('\t<li><a href=\"lecture')
    course_file.write(str(lecture_number).zfill(3))
    course_file.write('.html\"">' + lecture_title + '</a></li>\n')

course_file.write('</ol>\n')
course_file.write('<p> Last updated: ' + datetime.date.today().strftime("%d/%B/%Y\n") + '</p>\n')
