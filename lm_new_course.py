#!/usr/bin/env python3

""" module to create course """

import configparser
import os
import re
import sys


def get_index():
    """ copy default style """
    xdg_path = os.environ['XDG_DATA_HOME']
    paths = [
        f'{xdg_path}/lecture-manager/index.ini',
        '/usr/local/share/lecture-manager/index.ini',
        '~/.lecture-manager/index.ini'
    ]
    try:
        index = next(x for x in paths if os.path.exists(os.path.expanduser(x)))
    except StopIteration:
        index = paths[0]
    return index

def copy_style(course_name):
    """ copy default style """
    xdg_path = os.environ['XDG_DATA_HOME']
    paths = [
        f'{xdg_path}/lecture-manager/style.css',
        '/usr/local/share/lecture-manager/style.css',
        '~/.lecture-manager/style.css'
    ]
    try:
        style = next(x for x in paths if os.path.exists(os.path.expanduser(x)))
    except StopIteration:
        sys.exit('lectman not configured')
    os.system(f'cp {style} ./{course_name}/')

def main():
    """ main function for new course """
    if len(sys.argv) == 2:
        course_name = sys.argv[1]
    else:
        course_name = input('Course name: ')
    # strip spaces
    course_name = re.sub('\s+', '_', course_name)
    if os.path.exists(course_name):
        sys.exit("Folder occupied")
    # Create course directory
    os.mkdir(course_name)
    copy_style(course_name)

    config_file_name = f'{course_name}/.config.ini'
    config = configparser.ConfigParser()
    config.read(config_file_name)
    config.add_section('config')
    config.set('config', 'course-name', course_name)
    config.set('config', 'lecture-number', '0')
    config.add_section('course-index')

    with open(config_file_name, 'w') as config_file:
        config.write(config_file)

    # global index
    config_file_name = get_index()
    config = configparser.ConfigParser()
    config.read(config_file_name)
    if not config.has_section('courses'):
        config.add_section('courses')
    config.set('courses', course_name, f'{os.getcwd()}/{course_name}')
    with open(config_file_name, 'w') as config_file:
        config.write(config_file)

if __name__ == '__main__':
    main()
