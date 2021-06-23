
import requests
from datetime import datetime
api_key='99d381da942b83acf3de433e7e99b415'
location=input("Enter the city name:")
complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key+""
api_link=requests.get(complete_api_link)
#a=requests.get(complete_api_link)

api_data=api_link.json()
temp_city=((api_data['main']['temp'])-273.15)#273.15 for converting temperature into celsius
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_speed=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
f=open("E:\\CyberSecurity\\abc.txt","w")
print("******************************")
print("Weather Stats for -{} ||".format(location.upper(),date_time))
print("*************************")

print("Current temperature is:{:.2f} deg C".format(temp_city))
print("Current weather desc :",weather_desc)
print("Current Humidity     :",hmdt,'%')
f.write("Current wind speed   :"+str(wind_speed)+'kmph')
f.close()

f=open("E:\\CyberSecurity\\cybersecurity.txt","w")
f.write("*************************")
f.write("\nWeather Stats for -{} ||"+str.format(location.upper(),date_time))
f.write("\n**********************")
s="{:.2f}".format(temp_city)
f.write("\nCurrent temperature is :"+str(s)+"deg C")
f.write("\nWeather desc :"+str(weather_desc))
f.write("\nWeather Humidity :"+str(hmdt)+'%')


