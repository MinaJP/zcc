import requests
from decouple import config


def get_tickets(url, perpage=25, auth=(config('EMAIL'), config('PASSWORD'))):
    req = requests.get(
        url, auth=auth)
    if req.status_code == 403:
        return False, "authentication error"
    elif req.status_code == 404:
        return False, "not found error"
    elif req.status_code == 200:
        return True, req.json()
    else:
        return False, "an error occur during accessing the api"
