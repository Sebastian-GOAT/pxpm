from commands.lib.getconfig import get_config
from commands.lib.getpackage import get_package
from pathlib import Path
import json

def update(names: list[str]):

    if not names:
        print('Usage: "pxpm update <...packages | *>"')
        return

    names = list(set(names))

    modules_path = Path('modules')
    modules_path.mkdir(exist_ok=True)

    config = get_config()
    config_packages: dict = config['dependencies']

    to_update = [pkg for pkg in names if pkg in config_packages.keys()]

    for pkg in to_update:
        package = get_package(pkg)

        # Add to modules/
        if not package:
            print(f'Error: failed to get the package \'{pkg}\'.')
            continue

        config_packages[pkg] = package['version']

        package_path = modules_path / pkg
        package_path.mkdir(exist_ok=True)
        (package_path / '__init__.py').write_text(package['code'])

        print(f'Updated package \'{pkg}\' to the latest version.')

    try:
        with open('moduleconfig.json', 'w') as f:
            json.dump(config, f, indent=4)
        print('moduleconfig.json updated.')
    except:
        print(f'Failed to write updated moduleconfig.json')

    print('All modules updated.')