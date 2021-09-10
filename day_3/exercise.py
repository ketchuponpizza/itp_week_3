# import requests

# response = requests.get("https://rickandmortyapi.com/api/character")

# # print response
# print(response.text)


# import json
# from io import StringIO
# str_io_obj = StringIO()
# #Use JSON Dump to make StringIO
# json.dump(["India", "Australia", "Brazil"], str_io_obj)
# print('StringIO Object value: ' + str(str_io_obj.getvalue()))
# my_json = {
#     "name" : "Kalyan",
#     "age" : 25,
#     "city" : 'Delhi'
# }
# print(json.dumps(my_json, indent=4))

# import requests
# import json

# using the requests package, we can make API calls to retrieve JSON
# and storing it into a variable here called "response"
# response = requests.get("https://rickandmortyapi.com/api/character")

# verify the response status as 200
# print(response)

# verify the raw string data of the response
# print(response.text)

# load as a python json object and store into a variable called "clean_data"
# clean_data = json.loads(response.text)

# print(clean_data)

# go through the results,

# for each row in an excel spreadsheet
# grab the name, species, gender, location name

import requests
import openpyxl
import json

response = requests.get("https://rickandmortyapi.com/api/character")
clean_data = json.loads(response.text)

print(clean_data)

for x in clean_data:
    print(x)
    if x == "results":
        for i in clean_data["results"]:
            print(i['name'])
            print(i['species'])
            print(i['gender'])
            print(i['location'])

# print(i['name'] + ' : ' + i['species'])
