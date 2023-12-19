'''
This script is to explore how to access data from WQP programatically

There is not an API with endpoints that can be accessed. One needs to contstruct
a url from query parameters, then access the data with a get request

The goal with this exercise is to get the data as a JSON and then process it.
To process it I'll create a plot. I do not, however, want to store there data 
locally. Exporting the data will be a future function when we actually use this
information to build out beaver.
'''

'''
Notes

# mimeType is the type of data that will be returned
'''
from fastapi import FastAPI
import requests

BASE_URL = 'metadata: https://www.waterqualitydata.us/data/Station/search?'


query_params = []

url = 'https://www.waterqualitydata.us/data/Station/search?countycode=US%3A40%3A109&characteristicName=Atrazine&mimeType=geojson'
r = requests.get(url)
print(r.status_code)
print(r.json())

