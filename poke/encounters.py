from requests import HTTPError, get

#TODO: Encounters module

__URL = 'https://pokeapi.co/api/v2/encounter-method/'

#NOTE: Function to see which the player might can encounter pokemon

def encountMethods(n:int)->list|HTTPError: #HACK: list(Encounter pokemon) 
    try:
        response = get(__URL,params={'limit':n})
        if response.status_code == 200:
            encountLst:list[str]=[response.json()['results'][en].get('name') for en in range(0,n)]
            return sorted(encountLst) 
    except HTTPError as e:
        return e
    raise Exception
