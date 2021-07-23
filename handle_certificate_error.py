from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager


#chrome 1st way of handling certificate error
'''options=Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)'''

#chrome 2nd way of handling certificate error

'''desired_capabilities=DesiredCapabilities().CHROME.copy()
desired_capabilities['acceptInsecureCerts']=True
driver=webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=desired_capabilities)
driver.implicitly_wait(10)'''

#chrome 3rd way of handling certificate error

'''options=Options()
options.set_capability('acceptInsecureCerts',True)
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(10)'''

#firefox 1st way of handling of certificate error

'''profile=webdriver.FirefoxProfile()
profile.accept_untrusted_certs=True
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=profile)
driver.implicitly_wait(10)'''

#firefox 2nd way of handling of certificate error

desired_capabilities=DesiredCapabilities.FIREFOX.copy()
desired_capabilities['acceptInsecureCerts']=True
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(),desired_capabilities=desired_capabilities)
driver.implicitly_wait(10)
driver.get("https://expired.badssl.com/")
driver.maximize_window()


print(driver.find_element(By.TAG_NAME,"h1").text)