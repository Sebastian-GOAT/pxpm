from pathlib import Path

def init():

    config_path = Path('moduleconfig.json')

    # Check if moduleconfig.json exists
    if config_path.is_file():
        print('Error: pxpm already initialized')
        return
    
    # Create & write moduleconfig.json

    script_path = Path(__file__).resolve().parent
    baseconfig_path = script_path / 'lib' / 'baseconfig.json'

    try:
        ## Get base config
        with open(baseconfig_path, 'r') as f:
            config = f.read()

        ## Write moduleconfig.json
        with open(config_path, 'w') as f:
            f.write(config)
    except:
        print('Error: couldn\'t initialize project')