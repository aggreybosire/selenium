from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()
url = "https://understat.com/league/EPL"
driver.get(url)
driver.maximize_window()

file = open('test.txt', 'w', encoding='utf-8')
i = 2
while i < 36:
	content = driver.find_element_by_id('league-players').text
	file.write(content)

	element = driver.find_element_by_xpath('//*[@data-page=' + str(i) + ']')
	element.click()
	i+=1

file = open("cleaned.txt", 'w', encoding='utf-8')

for line in open("test.txt", encoding='utf-8'):
	if len(line)>43:
		file.write(line)

