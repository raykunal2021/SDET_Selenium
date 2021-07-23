from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver import ActionChains

options=webdriver.ChromeOptions()
options.headless=False
options.add_argument('--incognito')
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
