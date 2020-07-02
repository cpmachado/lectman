#!/usr/bin/env python3

""" module to list global index """

import configparser
import os
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

def main():
    """ main function for list """
    if len(sys.argv) > 1:
        sys.exit('This command takes no arguments')

    index = get_index()
    if index is None:
        sys.exit('There isn\'t a global index')
    config = configparser.ConfigParser()
    config.read(index)
    if config.has_section('courses'):
        courses = config['courses']
        for i in courses:
            print(f'{i}\t{courses[i]}')
    else:
        print('There are no courses')


if __name__ == '__main__':
    main()
