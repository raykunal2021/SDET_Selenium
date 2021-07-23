from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver import ActionChains

options=webdriver.ChromeOptions()
options.headless=True
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get("https://www.reddit.com/")

#driver.get_screenshot_as_file('reddit1.png')

#full page screenshot runs only on headless mode
S=lambda X:driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S("Width"),S("Height"))
driver.find_element_by_tag_name('body').screenshot('redditfull.png')
driver.close()
