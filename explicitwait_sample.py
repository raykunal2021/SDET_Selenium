from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/login")
wait=WebDriverWait(driver,30)
signup_link=wait.until(ec.element_to_be_clickable((By.XPATH,'//i18n-string[text()="Sign up"]')))
print(signup_link.text)
first_name=wait.until(ec.visibility_of_element_located((By.XPATH,'//input[@name="FIRST_NAME" and @placeholder="First name"]')))
first_name.send_keys("kunal")

driver.close()