
import requests
import json
import time
############
import math
import sys

def calcPoint(degHead, points):
    maxPoints=32
    if points not in(8,16,32):
        sys.exit("not a good question")
    degHead=(degHead+(360/points/2))/(360/maxPoints)
    j =int(int( int(degHead  % 8)%8/(maxPoints/points))*maxPoints/points)
    degHead = int(degHead / 8) % 4
    cardinal = ['North', 'East', 'South', 'West']
    pointDesc = ['W', 'W by x', 'W-z', 'Z by w', 'Z', 'Z by x', 'X-z', 'X by w']#vars not compass points
    W = cardinal[degHead]
    X = cardinal[(degHead + 1) % 4]
    w=W.lower()
    x=X.lower()
    if (W == cardinal[0] or W == cardinal[2]) :
        Z =W + x
    else:
        Z =X + w
    z=Z.lower()
    return pointDesc[j].replace('W', W).replace('X', X).replace('w', w).replace('x', x).replace('Z', Z).replace('z', z)

def getShortName(name): 
    return name.replace('North', 'N').replace('East', 'E').replace('South', 'S').replace('West', 'W').replace('north', 'N').replace('east', 'E').replace('south', 'S').replace('west', 'W').replace('by', 'b').replace(' ', '').replace('-', '')

def input_number(msg, err_msg=None):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            sys.exit("not a number")

#while True:
#    headingCalib=input_number("input a number: ")
#    print (headingCalib, end=' ')
#    name = calcPoint(headingCalib,32) #degrees heading, points of compass 8,16 or 32)
#    print (name, end=' ')
#    shortName = getShortName(name)
#    print (shortName)
############

api_key = "28905967d3974d14e0097a9184c95460"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
# city_name = input("Enter city name : ")
#city_name = "taiping"
#country_code = "MY"
#complete_url = base_url + "&q=" + city_name + "," + country_code + "&appid=" + api_key
# by id Kuala Ketil ID
city_id = "1735498"
complete_url = base_url + "&id=" + city_id + "&appid=" + api_key
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json()
#print("==============")
#print(x)
#print("==============")

if x["cod"] != "404": 
    y = x["main"]
    name = x["name"]
    curr_temp = y["temp"] - 273.15 #convert to celcius from kelvin
    feels_like = y["feels_like"] - 273.15
    temp_min = y["temp_min"]
    temp_max = y["temp_max"]
    curr_pressure = y["pressure"]
    curr_humidity = y["humidity"]
    
    z = x["weather"] 
    weather_description = z[0]["description"]
    weather_type = z[0]["main"]

    w = x["wind"]
    wind_speed = w["speed"]
    wind_degree = w["deg"]

    sys = x["sys"]
    sunrise = sys["sunrise"]
    sunrise_local = time.strftime('%I:%M %p', time.localtime(sunrise))
    sunset = sys["sunset"]
    sunset_local = time.strftime('%I:%M %p', time.localtime(sunset))
    today_date = time.strftime('%d %B %Y', time.localtime(sunset))

    print("     *=================================*")
    print("     | " + str(name) + " weather condition |")
    print("     *=================================*")
    
    print("- Temperature = "   + "%.2f" % curr_temp + "°C (feels like " + "%.2f" % feels_like + "°C)")
    print("- Atmo pressure = " + str(curr_pressure)        + "hpa")
    print("- Humidity = "      + str(curr_humidity)        + " %")
    print("- Description = "   + str(weather_description).capitalize())
    print("- Wind speed = " + str(wind_speed) + " m/s")
    name = calcPoint(wind_degree, 16)  #degrees heading, points of compass 8,16 or 32)
    short_name = getShortName(name)
    print("- Wind direction = " + str(wind_degree) + "° " + name + " (" + short_name + ")")
    print("- Today is " + today_date)
    print("- Sunrise = " + sunrise_local)
    print("- Sunset = " +  sunset_local)
    

else: 
    print(" City Not Found ") 
