#how many links present in a webpage
#Capture links
#click on the link

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#driver.get("https://www.freshworks.com/")
driver.maximize_window()

links=driver.find_elements(By.TAG_NAME,'a')
print("number of links present in page",len(links)) #print how many links present in the page

#print all the link present in the page
for i in links:
    print(i.text)
#click on a link using linktext/partial linktext
wait=WebDriverWait(driver,20)
link1=wait.until(ec.element_to_be_clickable((By.LINK_TEXT,'Software Testing Tutorials'))).click()
#driver.find_element_by_link_text("Software Testing Tutorials").click()
print(driver.current_url)
try:


    #link2=wait.until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Tools Training'))).click()
#driver.find_element_by_partial_link_text("Tools Training").click()
    link2=WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Tools Training')))
    link2.click()
    print(driver.current_url)
finally:
    driver.close()

