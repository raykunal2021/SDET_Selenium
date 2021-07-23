from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

#working with the radio buttons

radiobutton1=driver.find_element(By.XPATH,'//label[text()="Male"]').is_selected()
print(radiobutton1)

driver.find_element(By.XPATH,'//label[text()="Male"]').click()

radiobutton1=driver.find_element(By.XPATH,'//label[text()="Male"]').is_selected()
print(radiobutton1)

#working with checkboxes

sundaybox=driver.find_element(By.XPATH,'//label[normalize-space()="Sunday"]').click()
#verify1=driver.find_element(By.XPATH,'//label[normalize-space()="Sunday"]').is_selected()
#print(verify1)
saturdaybox=driver.find_element(By.XPATH,'//label[normalize-space()="Saturday"]').click()


