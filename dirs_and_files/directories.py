import os
import os.path
from colorama import Fore


def dir_options():
    import app
    temp_dirs = os.listdir(os.getcwd())
    dirs = []
    for d in temp_dirs:
        if os.path.isdir(d):
            dirs.append(d)
    print(f'You are currently in {Fore.GREEN} {os.getcwd()} {Fore.RESET} directory.\n\tWhere do you like to go:\n1. Up'
          f'\n2. Stay here and go back to options'
          f'\n3. Enter an absolute path manually')
    for d in range(0, len(dirs)):
        print(f'{d+4}. {dirs[d]}')

    option = int(input("Your option:"))
    if option == 1:
        os.chdir('../')
    elif option == 2:
        app.options_to_do()
        return
    elif option == 3:
        manual_dir = input('Enter an absolute path:')
        try:
            os.chdir(manual_dir)
        except:
            print(f'{Fore.RED}Wrong absolute path.{Fore.RESET}')
            dir_options()
    for i in range(4, len(dirs)+4):
        if option == i:
            os.chdir(dirs[i-4])
    dir_options()

