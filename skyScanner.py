import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/MY/MYR/en-GB/"

querystring = {"query":"London"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "f15e5a0541msh7614a614c264efcp18a791jsn45f26fc2419d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)