'''
A quick api to visualize data grabs from wqpy
'''

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from wqpy import get_wqp_results, SITE_URL, RESULTS_URL, SUMMARY_DATA_URL
import uvicorn
import json

app = FastAPI()

@app.get('/')
def show_features():
    results = query_wqp(
        url=RESULTS_URL,
        sampleMedia='Water',
        characteristicType='Physical',
        siteType='Well',
        countyname='taos',
        dataProfile='narrowResult',
        providers=['STORET', 'NWIS', 'STEWARDS'])
    #print(results.keys())
    return results

@app.get('/wells/site-data')
def get_well_site_data():
    results = query_wqp(
        url=RESULTS_URL,
        sampleMedia='Water',
        characteristicType='Physical',
        siteType='Well',
        countyname='taos',
        dataProfile='summaryMonitoringLocation',
        providers=['STORET', 'NWIS', 'STEWARDS'],
        )
    return JSONResponse(content=results)

if __name__ == '__main__':
    uvicorn.run('main:app', host = '127.0.0.1', port = 80, reload = True)