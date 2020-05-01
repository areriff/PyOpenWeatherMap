import requests

url = "https://restcountries-v1.p.rapidapi.com/all"

headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "f15e5a0541msh7614a614c264efcp18a791jsn45f26fc2419d"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)