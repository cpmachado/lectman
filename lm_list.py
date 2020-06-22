#!/usr/bin/env python3

""" module to list global index """

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
        sys.exit('There are no courses')
    return index

def main():
    """ main function for list """
    if len(sys.argv) > 1:
        sys.exit("This command takes no arguments")

    index = get_index()
    config = configparser.ConfigParser()
    config.read(index)
    if config.has_section('courses'):
        courses = config['courses']
        for i in courses:
            print(f'{i} - {courses[i]}')
    else:
        print("There are no courses")


if __name__ == '__main__':
    main()

