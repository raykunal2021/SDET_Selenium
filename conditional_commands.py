'''is_displayed()
is_enabled()
is_selected()'''

from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//a[@id='hrefUserIcon']//*[local-name()='svg']").click()
time.sleep(5)

ele=driver.find_element_by_xpath('//input[@name="username" and @type="text"]')
print(ele.is_displayed())#returns true or false based on element status
print(ele.is_enabled())#returns true/false

driver.get("https://www.singaporeair.com/en_UK/in/home#/book/bookflight")
time.sleep(5)
print(driver.title)
print(driver.current_url)
radiobtn1=driver.find_element_by_xpath('//label[@class="form__label" and text()="Book flights"]')
radiobtn2=driver.find_element_by_xpath('//label[@for="redeemFlights" and text()="Redeem flights"]')
print(radiobtn1.is_selected())#returns true or false
print(radiobtn2.is_selected())

#driver.close()
driver.quit()