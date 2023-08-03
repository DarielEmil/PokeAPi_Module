from requests import  HTTPError, get

__URL = "https://pokeapi.co/api/v2/"

#TODO: Berries module

#NOTE: Function to see basic berry info

def getBerries(name:str)-> dict | HTTPError: #HACK: return dict(some basic berry info)
    try:
        response = get(f"{__URL}/berry/{name}") 
        if response.status_code == 200:
            basicJson = response.json()
            basicInfo:dict[str,str|int] = {key:basicJson[key] for key in basicJson.keys() & {'name', 'size', 'growth_time', 'soil_dryness'}}
            return basicInfo
    except HTTPError as e:
        return e
    raise Exception ("Error")

#NOTE: Function to see berries Flavor 

def viewBerryFlavor(nm:int)-> list | HTTPError: #HACK: return list(berries flavor name)
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
    raise Exception ("Error")

#NOTE: Function  
