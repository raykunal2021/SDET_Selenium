from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()
driver.implicitly_wait(3)

#find particular tr td
print(driver.find_element_by_xpath('//table[@id="customers"]/tbody/tr[6]/td[2]').text)

#iterate through the table to find

body=driver.find_element_by_tag_name('tbody')
rows=driver.find_elements_by_tag_name('tr')
columns=driver.find_elements_by_tag_name('td')

for i in range(len(rows)):
    col=rows[i].find_elements_by_tag_name('td')
    for j in range(len(col)):
        if col[j].text=="Italy":
            print("the country name "+col[j].text+" is found")
            break



driver.close()