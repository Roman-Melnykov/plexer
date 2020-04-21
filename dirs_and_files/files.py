from os import listdir, getcwd
import os
import re


def remove_pattern(pattern):
    import app
    """[.]*s\d[\d]*e\d[\d]* - s00e00, s01e022 etc"""
    files = get_files_in_current_directory()
    print(f'You are about to process the following files:')
    for f in files:
        print(f'{f}')
    yn = input('Continue? (y/n):')
    if yn.lower() == 'n':
        app.options_to_do()
        return
    counter = 0
    for f in files:
        f_name = os.path.basename(f)
        p = re.search(pattern, f_name)
        if p:
            print(f'f_name: {f_name}')
            new_name = os.path.dirname(f) + change_to_plex(pattern, p, f_name)
            os.rename(f, new_name)
            counter += 1
    print(f'{counter} file(s) were renamed.')


def change_to_plex(pattern, p, string):
    return re.sub(pattern, remove_letters(p.group(1)), string)


def get_files_in_current_directory():
    temp_files = listdir(getcwd())
    files = []
    for f in temp_files:
        if os.path.isfile(f):
            files.append(f)
    return files


def remove_letters(s: str):
    result = ''
    for l in s:
        if l.isnumeric():
            result += l
    return result
