import requests

def get_package(name: str) -> dict | None:

    try:
        url = f'/api/package/{name}'
        res = requests.get(url) # REPLACE WITH ACTUAL API URL

        if res.status_code != 200:
            return
        
        return res.json()
    except:
        return