from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
import time

# enter your id/pass
usernameStr = ''
passwordStr = ''

# timeout = 3

# headless - without opening browser 
options = Options()
options.headless = True

# initiallizing driver Firfox Browser
browser = webdriver.Firefox(
    options=options, executable_path=r'E:\New Project\Scrapsrm by Python\geckodriver.exe')
# browser = webdriver.Chrome()

browser.implicitly_wait(30)

browser.get(('https://iac.srmist.edu.in/connect/Access'))

time.sleep(2)

username = browser.find_element_by_id('LoginUserPassword_auth_username')
username.clear()
password = browser.find_element_by_id('LoginUserPassword_auth_password')
username.clear()
username.send_keys(usernameStr)
password.send_keys(passwordStr)

browser.find_element_by_id("UserCheck_Login_Button").click()
time.sleep(2)

# take screenshot after completion
# screenshot = browser.save_screenshot('snap3.png')

browser.quit()
