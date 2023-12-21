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
                    statecode = None,
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
                    dataProfile = None):
 
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

    if statecode:
        statecodes = parse_string_or_list(statecode)
        statecodes = [state_letters_to_statecode[sl] for sl in statecodes]
        query_params["statecode"] = statecodes

    if siteType:
        query_params['siteType'] = siteType

    if organization:
        query_params['organization'] = organization

    if siteid:
        query_params['siteid'] = siteid

    if huc:
        query_params['huc'] = huc

    if sampleMedia:
        query_params['sampleMedia'] = sampleMedia

    if characteristicType:
        query_params['characteristicType'] = characteristicType

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

    headers = {'Content-Type': 'application/json'}
    request_url = f'{url}mimeType={mimeType}'

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