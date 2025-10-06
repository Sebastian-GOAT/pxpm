from commands.lib.getconfig import get_config
from pathlib import Path
import shutil
import json

def uninstall(names: list[str], flags: list[str]):

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

    any_removed = False

    # Remove requested packages from dependencies
    for name in names:
        if name in config_packages:

            # Update moduleconfig.json and modules/
            del config_packages[name]

            package_path = modules_path / name
            if package_path.is_dir():
                try:
                    shutil.rmtree(package_path)
                except:
                    print(f'Couldn\'t remove package \'{name}\'')
                    continue

            any_removed = True

            print(f'Removed package \'{name}\' from modules/')

    if any_removed:
        try:
            with open('moduleconfig.json', 'w') as f:
                json.dump(config, f, indent=4)
        except:
            print(f'Failed to write updated moduleconfig.json')

    print('All specified modules uninstalled.')