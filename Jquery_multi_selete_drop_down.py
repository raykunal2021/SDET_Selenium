from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time

#any drop down not having select tag,like jquery/angular/react drop down

def selecrdrp(options_list,value):
    if not value[0]=='all':

        for ele in drop_down_list:
            print(ele.text)
            for i in range(len(value)):
                if ele.text==value[i]:
                    ele.click()
                    break

    else:
        try:
            for ele in options_list:
                ele.click()
        except Exception as e:
            print(e)



driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID,"justAnInputBox").click()
time.sleep(3)
drop_down_list=driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")
#value_list=['choice 1','choice 2','choice 3','choice 6 2 1']

#value_list=['choice 1']
value_list=['all']
#selecrdrp(drop_down_list,'choice 6 2 1')
selecrdrp(drop_down_list,value_list)

'''for ele in drop_down_list:
    print(ele.text)
    if ele.text=='choice 6 2 3':
        ele.click()
        break'''