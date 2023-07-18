from requests import  HTTPError, get
from json import loads, dumps

__URL = "https://pokeapi.co/api/v2/berry"

#TODO: Berries module

def getBerries(name:str):
    try:
        response = get(f"{__URL}/{name}") 
        if response.status_code == 200:
            basicInfo = response.json()
            basicTxt = "Berry Name:{}, \nSize: {}".format(*list(map(basicInfo.get, ('name','size'))))
            return basicTxt
    except HTTPError as e:
        return e


