from enum import Enum
from typing import Union
import requests
import json

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

state_letters_to_statecode = {
    'AL': 'US:01',
    'AK': 'US:02',
    'AZ': 'US:03',
    'AR': 'US:04',
    'CA': 'US:05',
    'CO': 'US:08',
    'CT': 'US:09',
    'DE': 'US:10',
    'DC': 'US:11',
    'FL': 'US:12',
    'GA': 'US:13',
    'HW': 'US:15',
    'ID': 'US:16',
    'IL': 'US:17',
    'IN': 'US:18',
    'IA': 'US:19',
    'KS': 'US:20',
    'KY': 'US:21',
    'LA': 'US:22',
    'ME': 'US:23',
    'MD': 'US:24',
    'MA': 'US:25',
    'MI': 'US:26',
    'MN': 'US:27',
    'MS': 'US:28',
    'MO': 'US:29',
    'MT': 'US:30',
    'NE': 'US:31',
    'NV': 'US:32',
    'NH': 'US:33',
    'NJ': 'US:34',
    'NM': 'US:35',
    'NY': 'US:36',
    'NC': 'US:37',
    'ND': 'US:38',
    'OH': 'US:39',
    'OK': 'US:40',
    'OR': 'US:41',
    'PA': 'US:42',
    'RI': 'US:44',
    'SC': 'US:45',
    'SD': 'US:46',
    'TN': 'US:47',
    'TX': 'US:48',
    'UT': 'US:49',
    'VT': 'US:50',
    'VA': 'US:51',
    'WA': 'US:53',
    'WV': 'US:54',
    'WI': 'US:55',
    'WY': 'US:56'
}

county_name_to_code = {
    'bernalillo': 'US:35:001',
    'catron': 'US:35:003',
    'chaves': 'US:35:005',
    'cibola': 'US:35:006',
    'colfax': 'US:35:007',
    'curry': 'US:35:009',
    'debaca': 'US:35:011',
    'dona ana': 'US:35:013',
    'eddy': 'US:35:015',
    'grant': 'US:35:017',
    'guadalupe': 'US:35:019',
    'harding': 'US:35:021',
    'hidalgo': 'US:35:023',
    'lea': 'US:35:025',
    'lincoln': 'US:35:027',
    'los alamos': 'US:35:028',
    'luna': 'US:35:029',
    'mckinley': 'US:35:031',
    'mora': 'US:35:033',
    'otero': 'US:35:035',
    'quay': 'US:35:037',
    'rio arriba': 'US:35:039',
    'roosevelt': 'US:35:041',
    'sandoval': 'US:35:043',
    'san juan': 'US:35:045',
    'san miguel': 'US:35:047',
    'santa fe': 'US:35:049',
    'sierra': 'US:35:051',
    'socorro': 'US:35:053',
    'taos': 'US:35:055',
    'torrance': 'US:35:057',
    'union': 'US:35:059',
    'valencia': 'US:35:061'
}

def parse_string_or_list(s: Union[list, str]) -> list:
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

def get_wqp_results(url: str,
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
                    mimeType = 'geojson',
                    zip = None,
                    providers = None,
                    sorted = None,
                    dataProfile = None,
                    pagesize = None):
 
    query_params = {}

    if bBox:
        query_params['bBox'] = bBox

    if lat:
        query_params['lat'] = parse_string_or_list(lat)

    if lon:
        query_params['long'] = parse_string_or_list(lon)

    if within:
        query_params['within'] = parse_string_or_list(within)

    if countrycode:
        query_params['countrycode'] = parse_string_or_list(countrycode)

    if stateletters:
        stateletters = parse_string_or_list(stateletters)
        stateletters = [letters.upper() for letters in stateletters]
        statecodes = [state_letters_to_statecode[sl] for sl in stateletters]
        query_params["statecode"] = statecodes

    if countyname:
        countynames = parse_string_or_list(countyname)
        countynames = [name.lower() for name in countynames]
        countynames = [county_name_to_code[name] for name in countynames]
        query_params['countycode'] = countynames

    if siteType:
        query_params['siteType'] = parse_string_or_list(siteType)

    if organization:
        query_params['organization'] = organization

    if siteid:
        query_params['siteid'] = siteid

    if huc:
        query_params['huc'] = huc

    if sampleMedia:
        query_params['sampleMedia'] = parse_string_or_list(sampleMedia)

    if characteristicType:
        query_params['characteristicType'] = parse_string_or_list(characteristicType)

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
        query_params['providers'] = parse_string_or_list(providers)

    request_url = f'{url}mimeType={mimeType}'

    if pagesize:
        request_url = f'{request_url}&pagesize={pagesize}'

    headers = {'Content-Type': 'application/json'}
    

    print(request_url)
    print(json.dumps(query_params))

    response = requests.post(url = request_url,
                             data = json.dumps(query_params),
                             headers = headers)
    print(response.status_code)
    return response.json()

if __name__ == '__main__':
    test = get_wqp_results(url = SUMMARY_DATA_URL,
                           statecode = 'NM',
                           dataProfile = 'summaryMonitoringLocation')
    print(test)


