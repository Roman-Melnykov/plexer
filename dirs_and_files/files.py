from os import listdir, getcwd
import os
import re
from colorama import Fore


def remove_pattern(pattern):
    import app
    """(s\\d[\\d]*\\.?e\\d[\\d]*) - s00.e00, s01e022 etc"""
    files = get_files_in_current_directory()
    files_to_process = get_files_that_contain(files, pattern)

    print(f'\nYou are about to process the following files:')
    for f in files_to_process:
        print(f'>> {Fore.GREEN}{f}{Fore.RESET}')
    yn = input('Continue? (y/n):')
    if yn.lower() != 'y':
        app.options_to_do()

    counter = 0
    new_names = []
    for f in files_to_process:
        f_name = os.path.basename(f)
        p = re.search(pattern, f_name)
        new_name = change_to_plex(pattern, p, f_name, os.path.dirname(f))
        os.rename(f, new_name)
        counter += 1
        new_names.append(new_name)
    print(f'\n{counter} file(s) were renamed:')
    for f in new_names:
        print(f'>> {Fore.GREEN}{f}{Fore.RESET}')


def get_files_that_contain(files: list, pattern: str):
    files_to_process = []
    for f in files:
        f_name = os.path.basename(f)
        p = re.search(pattern, f_name)
        if p:
            files_to_process.append(f)
    return files_to_process


def change_to_plex(pattern, p, file_name, dir_path):
    return dir_path + re.sub(pattern, remove_letters(p.group(1)), file_name)


def get_files_in_current_directory():
    temp_files = listdir(getcwd())
    files = []
    for f in temp_files:
        if os.path.isfile(f):
            files.append(f)
    return files


def remove_letters(s: str):
    result = ''
    for let in s:
        if let.isnumeric() or let == '.':
            result += let
    return result
