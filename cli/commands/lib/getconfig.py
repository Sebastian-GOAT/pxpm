import json

def get_config() -> dict | None:

    try:
        with open('moduleconfig.json', 'r') as f:
            config = json.load(f)

        return config
    except:
        return