from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(2)
print(driver.title)
assert "ProtoCommerce" in driver.title
print(driver.current_url)
assert "https://rahulshettyacademy.com/angularpractice/" in driver.current_url

driver.find_element_by_xpath('//a[@class="nav-link" and text()="Shop"]').click()
products=driver.find_elements_by_xpath('//div[@class="card h-100"]')
#//div[@class="card h-100"]/div/h4/a  ---name of the products
#//div[@class="card h-100"]/div/button ----footer section add button use only the remaining part of the xpath
for product in products:
    productName=product.find_element_by_xpath("div/h4/a").text
    if productName=='Blackberry':
        #add product to cart
        product.find_element_by_xpath('div/button').click()
        time.sleep(2)

driver.find_element_by_xpath('//a[@class="nav-link btn btn-primary"]').click()
driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
driver.find_element_by_id('country').send_keys('ind')
wait=WebDriverWait(driver,10)
wait.until(ec.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element_by_link_text('India').click()
driver.find_element_by_xpath('//div[@class="checkbox checkbox-primary"]').click()
driver.find_element_by_xpath('//input[@class="btn btn-success btn-lg" and @value="Purchase"]').click()

successText=driver.find_element_by_class_name('alert-success').text
print(successText)

assert "Success! Thank you!" in successText
driver.get_screenshot_as_file("screen.png")





driver.close()