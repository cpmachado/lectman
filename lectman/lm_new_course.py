#!/usr/bin/env python3

""" module to create course """

import configparser
import os
import re
import shutil
import sys

def get_data_folder():
    """ get data folder """
    if 'XDG_DATA_HOME' in os.environ:
        xdg_path = os.environ['XDG_DATA_HOME']
    else:
        xdg_path = '/'.join([os.environ['HOME'], '.local/share'])

    paths = [
        f'{xdg_path}/lecture-manager',
        '~/.lecture-manager',
        '/usr/local/share/lecture-manager'
    ]
    paths = list(map(os.path.expanduser, paths))
    try:
        data = next(x for x in paths if os.path.exists(x))
    except StopIteration:
        return None
    return data

def get_index():
    """ get index """
    data = get_data_folder()
    if data is None:
        return None
    return f'{data}/index.ini'

def get_style():
    """ get style """
    data = get_data_folder()
    style = f'{data}/style.css'
    if not os.path.exists(style):
        return None
    return style

def main():
    """ main function for new course """
    index = get_index()
    if index is None:
        sys.exit('lectman isn\'t configured')
    style = get_style()
    if style is None:
        sys.exit('lectman installation missing style.css')

    if len(sys.argv) == 2:
        course_name = sys.argv[1]
    else:
        course_name = input('Course name: ')

    course_name = re.sub(r'\s+', '_', course_name)
    if os.path.exists(course_name):
        sys.exit("Folder occupied")

    os.mkdir(course_name)
    shutil.copyfile(style, f'{course_name}/style.css')

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
    config_file_name = index
    config = configparser.ConfigParser()
    config.read(config_file_name)
    if not config.has_section('courses'):
        config.add_section('courses')
    config.set('courses', course_name, f'{os.getcwd()}/{course_name}')
    with open(config_file_name, 'w') as config_file:
        config.write(config_file)

if __name__ == '__main__':
    main()
