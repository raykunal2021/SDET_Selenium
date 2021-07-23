from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://advantageonlineshopping.com/#/")

wait = WebDriverWait(driver,10)
wait.until(ec.title_contains('Advantage'))
print(driver.title)
email_id=wait.until(ec.presence_of_element_located((By.XPATH, '//span[@class="roboto-medium ng-binding" and text()="dvantage"]')))

driver.close()
