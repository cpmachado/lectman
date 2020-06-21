#!/usr/bin/env python3

""" module to create course """

import os
from sys import argv
import configparser

if len(argv) == 2:
    course_name = argv[1]
else:
    course_name = input('Course name: ')

# Create course directory
os.mkdir(course_name)

# Copy stylesheet
os.system('cp '+ '~/.lecture-manager/style.css ' + course_name + '/style.css')

config_file_name = course_name + '/.config.ini'

config = configparser.ConfigParser()
config.read(config_file_name)

config.add_section('config')
config.set('config', 'course-name', course_name)
config.set('config', 'lecture-number', '0')

config.add_section('course-index')

with open(config_file_name, 'w') as config_file:
    config.write(config_file)
