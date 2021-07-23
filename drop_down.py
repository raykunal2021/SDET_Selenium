from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  #need it for drop down,use Select class

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

#select one drop down option
#find out/capture how to many options present in the drop down
#count all options

element=driver.find_element(By.XPATH,'//select[@id="RESULT_RadioButton-9" and @class="drop_down"]')
dropdown=Select(element)

#select by visible text  run options one by one
#dropdown.select_by_visible_text("Afternoon")

#select by index
#dropdown.select_by_index(3)

#select by value
dropdown.select_by_value("Radio-0")

#count number of options
print(len(dropdown.options))

#capture all the options and print them in the output

all_options=dropdown.options
for i in all_options:
    print(i.text)

