from bs4 import BeautifulSoup

import requests

url = "https://weather.com/en-IN/weather/today/l/47eeaf5045f98224d1cff49e328705eda8e966fef416889b2604f294d5734e62"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

temp = soup.find("div",{"class":"today_nowcard-temp"}).text

time = soup.find("p",{"class":"today_nowcard-timestamp"}).text[6:]

condition = soup.find("div",class_="today_nowcard-phrase").text

high = soup.find_all("span",class_="deg-hilo-nowcard")[0].text

low = soup.find_all("span",class_="deg-hilo-nowcard")[1].text

rightnow = soup.find("div",class_="today_nowcard-sidecar component panel").find("table")

wind = rightnow.find_all("tr")[0].find("span").text

Humidity = rightnow.find_all("tr")[1].find("span").text

pressure = rightnow.find_all("tr")[3].find("span").text

visibility = rightnow.find_all("tr")[4].find("span").text

print("Time : ",time)
print("Temperature : ",temp)
print("Condition : ",condition)
print("High/Low : {}/{}".format(high,low))
print("Wind : ",wind)
print("Humidity : ",Humidity)
print("Pressure : ",pressure)
print("Visibility : ",visibility)
