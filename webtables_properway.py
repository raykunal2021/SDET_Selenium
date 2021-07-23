from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://qavbox.github.io/demo/webtable/")
driver.implicitly_wait(3)
driver.maximize_window()
#to set browser loadtime after which timeout exception will throw
#driver.set_page_load_timeout(50)
print(driver.title)
assert 'webtable' in driver.title
print(driver.current_url)

#select the table
table=driver.find_element(By.ID,'table01')

#identify the header part using table as it is a element

'''headers=driver.find_elements_by_tag_name('th')
for i in headers:
    print(i.text)'''

#identify the all cells

body=driver.find_element_by_tag_name('tbody')
rows=body.find_elements_by_tag_name('tr')
cells=body.find_elements_by_tag_name('td')
print(len(rows))
#suppose you need to search and click something in table,iterate through entire table

for i in range(len(rows)):
    columns=rows[i].find_elements_by_tag_name('td')
    for j in range(len(columns)):
        if columns[j].text=="QC ALM":
            columns[0].click()

time.sleep(5)




#if you know the certain tr and td you need to find interview question
print(driver.find_element(By.XPATH,"//table[@id='table01']/tbody/tr[2]/td[4]").text)

'''for i in cells: #to find out the cell value
    print(i.text)'''



driver.close()
