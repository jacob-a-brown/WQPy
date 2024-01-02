from enum import Enum
from typing import Union
import requests
import json
from lookup_tables import state_letters_to_state_code, nm_county_name_to_county_code

SITE_URL = 'https://www.waterqualitydata.us/data/Station/search?'
RESULTS_URL = 'https://www.waterqualitydata.us/data/Result/search?'
SUMMARY_DATA_URL = 'https://www.waterqualitydata.us/data/summary/monitoringLocation/search?'

# ------------------
# BEGIN TYPE HINTING
# ------------------

#bBox = List[Union[int, float]]

# ------------------
# END TYPE HINTING
# ------------------


def create_query_list(s: Union[list, str]) -> list:
    '''
    Returns lists of query elements

    Parameters:
    s (list or str): string or list of strings

    Returns:
    list: list of query elements 
    '''
    if type(s) is str:
        query_list = [s]
    else:
        query_list = [str(element) for element in s]
    return query_list

def query_wqp(url: str,
              bBox = None,
              lat = None,
              lon = None,
              within = None,
              countrycode = None,
              stateletters = None,
              countyname = None,
              siteType = None,
              organization = None,
              siteid = None,
              huc = None,
              sampleMedia = None,
              characteristicType = None,
              characteristicName = None,
              pCode = None,
              activityId = None,
              startDateLo = None,
              startDateHi = None,
              mimeType = 'csv',
              zipped = "no",
              providers = None,
              sorted = None,
              dataProfile = None,
              pagesize = None):
 
    query_params = {}

    if bBox:
        query_params['bBox'] = bBox

    if lat:
        query_params['lat'] = create_query_list(lat)

    if lon:
        query_params['long'] = create_query_list(lon)

    if within:
        query_params['within'] = create_query_list(within)

    if countrycode:
        query_params['countrycode'] = create_query_list(countrycode)

    if stateletters:
        stateletters = create_query_list(stateletters)
        stateletters = [letters.upper() for letters in stateletters]
        statecodes = [state_letters_to_state_code[sl] for sl in stateletters]
        query_params["statecode"] = statecodes

    if countyname:
        countynames = create_query_list(countyname)
        countynames = [name.lower() for name in countynames]
        countynames = [nm_county_name_to_code[name] for name in countynames]
        query_params['countycode'] = countynames

    if siteType:
        query_params['siteType'] = create_query_list(siteType)

    if organization:
        query_params['organization'] = organization

    if siteid:
        query_params['siteid'] = siteid

    if huc:
        query_params['huc'] = huc

    if sampleMedia:
        query_params['sampleMedia'] = create_query_list(sampleMedia)

    if characteristicType:
        query_params['characteristicType'] = create_query_list(characteristicType)

    if characteristicName:
        query_params['characteristicName'] = characteristicName

    if pCode:
        query_params['pCode'] = pCode

    if activityId:
        query_params['activityId'] = activityId

    if startDateLo:
        query_params['startDateLo'] = startDateLo

    if startDateHi:
        query_params['startDateHi'] = startDateHi

    if dataProfile:
        query_params['dataProfile'] = dataProfile

    if providers:
        query_params['providers'] = create_query_list(providers)

    request_url = f'{url}mimeType={mimeType}&zip={zipped}'

    if pagesize:
        request_url = f'{request_url}&pagesize={pagesize}'

    headers = {'Content-Type': 'application/json'}
    

    print(request_url)
    print(json.dumps(query_params))

    response = requests.post(url = request_url,
                             data = json.dumps(query_params),
                             headers = headers)

    print(response)
    return response.content

if __name__ == '__main__':
    test = get_wqp_results(url = SUMMARY_DATA_URL,
                           stateletters = 'NM',
                           countyname = 'taos',
                           dataProfile = 'summaryMonitoringLocation')
