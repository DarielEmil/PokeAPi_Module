from requests import  HTTPError, get
from operator import attrgetter

__URL = "https://pokeapi.co/api/v2/berry"

#TODO: Poke APi module 

def checkStatus():
    try:
        response = get(__URL)
        return response.status_code
    except HTTPError as e:
        return e

