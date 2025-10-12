from pathlib import Path
import os

def config():

    config_path = Path.home() / 'AppData' / 'Roaming' / 'pxpm' / 'config.json'

    if not config_path.is_file():
        print(f'Configuration file not found. Make sure it exists at {str(config_path)}')
        return
    
    os.startfile(config_path)