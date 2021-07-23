from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()




#how to find how many text boxes present in the page
inputboxes=(driver.find_elements(By.CLASS_NAME,'text_field'))
print(len(inputboxes))

#how to get the status
status=driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print("displayed or not",status)
status1=driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print("enabled or not",status1)


#how to provide values into text boxes
driver.find_element(By.ID,'RESULT_TextField-1').send_keys("kunal")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("ray")
driver.find_element_by_id('RESULT_TextField-3').send_keys(123456789)
driver.find_element_by_id('RESULT_TextField-4').send_keys('india')
