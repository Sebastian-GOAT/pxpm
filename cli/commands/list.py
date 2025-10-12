from commands.lib.getconfig import get_config

def show_list(names: list[str]):

    if not names:
        print('Usage: "pxpm list <...packages | *>"')
        return
    
    names = list(set(names))

    config = get_config()

    if not config:
        print('Failed to list the dependencies.')

    config_packages: dict = config['dependencies']

    packages = config_packages.keys() if '*' in names else [pkg for pkg in names if pkg in config_packages.keys()]

    if not packages:
        print('No listed packages found.')
        return

    print('Packages:\n')
    for pkg in packages:
        print(f'- {pkg}@{config_packages[pkg]}')