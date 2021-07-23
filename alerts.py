from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#Click on the "Alert" button to generate the Simple Alert
driver.find_element_by_xpath("//button[normalize-space()='Click Me']").click()
#Switch the control to the Alert window
obj=driver.switch_to.alert
time.sleep(5)
#Retrieve the message on the Alert window
message=obj.text
print("Alert shows following message: "+ message)
time.sleep(5)
#use the accept() method to accept the alert
obj.accept()
#get the text returned when OK Button is clicked.
txt=driver.find_element_by_css_selector("#demo")
print(" Clicked on the OK Button in the Alert Window : ",txt.text)

# Section 2
# Re-generate the Confirmation Alert
button = driver.find_element_by_xpath("//button[normalize-space()='Click Me']")
button.click()

time.sleep(2)

#Switch the control to the Alert window
obj1 = driver.switch_to.alert

# Dismiss the Alert using
obj1.dismiss()

#get the text returned when Cancel Button is clicked.
txt1=driver.find_element_by_css_selector("#demo")
print(" Clicked on the Cancle Button in the Alert Window : ",txt1.text)

driver.switch_to.default_content()#use it to come back to default page

time.sleep(2)


driver.close()