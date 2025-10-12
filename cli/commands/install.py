from pathlib import Path
import json
from commands.lib.getconfig import get_config

# REMOVE, THIS IS JUST FOR TESTING
def get_package(name: str) -> dict:
    """Return package data as an object"""
    return {
        'name': name,
        'version': 'latest',
        'code': f'# Code for package {name}\nprint("Hello from {name}")'
    }

def install(names: list[str], flags: list[str]):

    names = list(set(names))

    # Get moduleconfig.json
    config = get_config()
    if not config:
        print('Error: failed to access moduleconfig.json')
        return

    # Get the packages from moduleconfig.json
    config_packages = config.get('dependencies', {})

    # Ensure modules/ exists
    modules_path = Path('modules')
    modules_path.mkdir(exist_ok=True)

    # Add new requested packages to dependencies if missing
    for name in names:
        if name not in config_packages:

            # Get the package
            pkg_obj = get_package(name)
            if not pkg_obj:
                print(f'Error: failed to get the package \'{name}\'')
                continue

            # Update moduleconfig.json and modules/
            config_packages[name] = pkg_obj['version']

            package_path = modules_path / name
            package_path.mkdir(exist_ok=True)
            (package_path / '__init__.py').write_text(pkg_obj['code'])

            print(f'Added package \'{name}\' to modules/')

    try:
        with open('moduleconfig.json', 'w') as f:
            json.dump(config, f, indent=4)
        print('moduleconfig.json updated.')
    except:
        print(f'Failed to write updated moduleconfig.json')

    print('All modules installed and are in sync with moduleconfig.json')