from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.freshworks.com/")
driver.maximize_window()
wait=WebDriverWait(driver,20)
ele=wait.until(ec.presence_of_element_located((By.XPATH,'//img[@class="logo logo-fworks "]')))
ele3=wait.until(ec.text_to_be_present_in_element((By.XPATH,'//h1[text()="Best-in-class customer and employee engagement"]'),'Best-in-class'))
ele1=wait.until(ec.element_to_be_clickable((By.XPATH,'//div[@class="button button--solid in-page-scroll" and text()="Get started"]')))
ele2=driver.find_element_by_xpath('//h2[text()="Refreshing business software that your teams will love"]')
print(ele2.text)
driver.close()