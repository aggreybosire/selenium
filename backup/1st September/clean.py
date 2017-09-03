from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import re

driverUS = webdriver.Chrome()
urlUS = "https://understat.com/league/EPL"
driverUS.get(urlUS)
driverUS.maximize_window()

file = open('scraped.txt', 'w', encoding='utf-8')
i = 2
while i < 36:
	content = driverUS.find_element_by_id('league-players').text
	file.write(content)

	element = driverUS.find_element_by_xpath('//*[@data-page=' + str(i) + ']')
	element.click()
	i+=1

file = open("stats.csv", 'w', encoding='utf-8')
file.write("PID,Player,Team,Apps,Minutes,Goals,Assists,xG,xA,xG90,xA90\n")

for line in open("scraped.txt", encoding='utf-8'):
	#line = line.replace("\+\d.\d\d\s"," ")
	line = re.sub(r"\+\d.\d\d\s", " ", line)
	line = re.sub(r"\-\d.\d\d\s", " ", line)
	if len(line)>43:
		line = line.replace(" ", ",", 1)

		line = line.replace(" Arsenal",",Arsenal")
		line = line.replace(" Bournemouth",",Bournemouth")
		line = line.replace(" Brighton",",Brighton")
		line = line.replace(" Burnley",",Burnley")
		line = line.replace(" Chelsea",",Chelsea")
		line = line.replace(" Crystal Palace",",Crystal Palace")
		line = line.replace(" Everton",",Everton")
		line = line.replace(" Huddersfield",",Huddersfield")
		line = line.replace(" Leicester",",Leicester")
		line = line.replace(" Liverpool",",Liverpool")
		line = line.replace(" Manchester City",",Manchester City")
		line = line.replace(" Manchester United",",Manchester United")
		line = line.replace(" Newcastle United",",Newcastle United")
		line = line.replace(" Southampton",",Southampton")
		line = line.replace(" Stoke",",Stoke")
		line = line.replace(" Swansea",",Swansea")
		line = line.replace(" Tottenham",",Tottenham")
		line = line.replace(" Watford",",Watford")
		line = line.replace(" West Bromwich Albion",",West Bromwich Albion")
		line = line.replace(" West Ham",",West Ham")

		line = line.replace(" 0",",0")
		line = line.replace(" 1",",1")
		line = line.replace(" 2",",2")
		line = line.replace(" 3",",3")
		line = line.replace(" 4",",4")
		line = line.replace(" 5",",5")
		line = line.replace(" 6",",6")
		line = line.replace(" 7",",7")
		line = line.replace(" 8",",8")
		line = line.replace(" 9",",9")		

		file.write(line)

r = urllib.request.urlopen('https://fantasy.premierleague.com/drf/elements/').read()
soup = BeautifulSoup(r)

with open("playerdata.json", "w") as file:
	for line in soup:
		file.write(line)

df_us = pd.read_csv('stats.csv')
df = pd.read_json('playerdata.json')
df['Player'] = df[['first_name', 'web_name']].apply(lambda x: ' '.join(x), axis=1)
df.drop(df.columns[[0, 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 36, 40, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55]], axis=1, inplace=True)

result = pd.merge(df, df_us, on='Player')
print(result.head())
result.to_csv('testingmerge.csv')
