from requests import  HTTPError, get
from collections import OrderedDict

__URL = "https://pokeapi.co/api/v2/"

#TODO: Berries module

#NOTE: Function to return some basic berry info

def getBerries(name:str):
    try:
        response = get(f"{__URL}/berry/{name}") 
        if response.status_code == 200:
            basicJson = response.json()
            basicInfo = {key:basicJson[key] for key in basicJson.keys() & {'name', 'size', 'growth_time', 'soil_dryness'}}
            return basicInfo
    except HTTPError as e:
        return e

#NOTE: Function to see berries Flavor (return berries flavor name)

def viewBerryFlavor(nm:int):
    try:
        if not nm in list(range(1,5)) :
            raise Exception ('Not found berry flavor')
        else:
            response = get(f"{__URL}/berry-flavor/{nm}")
            if response.status_code == 200:
                brryJson = response.json()
                brryName = [x.get('berry')['name'] for x in brryJson['berries']]
                return sorted(brryName) 
    except HTTPError as e:
        return e


