#extra challenge with SF Open Data

from urllib2 import urlopen
from json import load

api_endpoint = "https://data.sfgov.org/resource/hsxb-ci7b.json"

api_result = urlopen(api_endpoint)

json_result = load(api_result)


rent_dict = {}

for index, item in enumerate(json_result, 0):   #enumerate is automatically assigns the items in the list with an index
	rent_dict