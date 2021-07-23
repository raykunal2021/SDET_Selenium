import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

def test_drag():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://qavbox.github.io/demo/dragndrop/")
    driver.maximize_window()
    driver.implicitly_wait(3)

    source_ele=driver.find_element(By.ID,'draggable')
    target_ele=driver.find_element(By.ID,'droppable')
    act_chains=ActionChains(driver)

    #act_chains.click_and_hold(source_ele).move_to_element(target_ele).release().perform()
    act_chains.drag_and_drop(source_ele,target_ele).release().perform()
    time.sleep(5)
    driver.save_screenshot('C:/Users/kunal/PycharmProjects/SDET_Selenium/pytest_project/drag_drop1.png')

    driver.close()









