from sys import argv
from commands.print_help import print_help
from commands.init import init
from commands.install import install
from commands.uninstall import uninstall
from commands.config import config
from commands.list import show_list
from commands.exists import exists
from commands.update import update

def main():
    
    if len(argv) == 1:
        print_help()
        return
    
    command = argv[1]
    rest = argv[2:]
    names = [arg for arg in rest if not (arg.startswith('--') or arg.startswith('-'))]
    flags = [arg for arg in rest if arg.startswith('--') or arg.startswith('-')]

    if command == 'init':
        init()
        return

    if command == 'install' or command == 'i':
        install(names, flags)
        return
    
    if command == 'uninstall' or command == 'uni':
        uninstall(names, flags)
        return

    if command == 'config':
        return
    
    # Lists specified packages (* for all)
    if command == 'list':
        return
    
    # Checks if specified packages are installed (* for all)
    if command == 'exists':
        return
    
    # Updates specified packages (* for all)
    if command == 'update':
        return



if __name__ == '__main__':
    main()