# import requests
#
# url = "https://hotels-com-free.p.rapidapi.com/srle/listing/v1/brands/hotels.com"
#
# # querystring = {"checkIn":"2021-01-27","checkOut":"2021-01-28","lat":"37.788719679657554","lon":"-122.40057774847898","locale":"en_US","rooms":"1","currency":"USD","pageNumber":"1"}
# querystring = {"checkIn":"2021-01-27","checkOut":"2021-01-28","lat":"34.0837","lon":"74.7973","locale":"en_US","rooms":"1","currency":"USD","pageNumber":"1"}
#
#
#
# # 34.0837° N, 74.7973° E
#
# headers = {
#     'x-rapidapi-key': "dfa8adb4ffmsh8f907502fefe688p17000cjsnacf1d914cbe9",
#     'x-rapidapi-host': "hotels-com-free.p.rapidapi.com"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)


# geocode

import requests

url = "https://trueway-geocoding.p.rapidapi.com/Geocode"

querystring = {"address":"Srinagar","language":"en"}

headers = {
    'x-rapidapi-key': "dfa8adb4ffmsh8f907502fefe688p17000cjsnacf1d914cbe9",
    'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
res = dict(response.json())
print(res['results'][0]['location']['lat'])
print(res['results'][0]['location']['lng'])

lat=res['results'][0]['location']['lat']
long=res['results'][0]['location']['lng']

