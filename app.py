from dirs_and_files import directories, files
from colorama import Fore
import os


def options_to_do():
    print(f'\nYou are currently in {Fore.GREEN} {os.getcwd()} {Fore.RESET} directory.\n\t'
          f'What do you like to do?\n'
          f'1. Switch working directory\n'
          f'2. Work with files here\n'
          f'3. Exit')
    option = int(input('Enter your option: '))

    if option == 1:
        directories.dir_options()
        return
    if option == 2:
        files.remove_pattern('(s\\d[\\d]*\\.?e\\d[\\d]*)')
    if option == 3:
        print('See ya!')
        exit(0)
    else:
        options_to_do()


if __name__ == '__main__':
    options_to_do()
