from selenium import webdriver
import Functions
from Functions import cx_Oracle
from Functions import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### Initilized Chrome and URL  ###
driver=webdriver.Chrome()
driver.implicitly_wait(5) ## Implicit Wait
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
### End ###

### Functions.SetUp()
con, cur, execution, TC1, TC2, n = Functions.SetUp()
### end

### Main ###
for columns in cur:
    username=columns[1]
    password=columns[2]
    driver.find_element_by_id("user-name").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("btn_action").click()
    element=driver.find_elements_by_css_selector('#inventory_filter_container > div') ##Explicit wait
    length=len(element)
    if length != 0:
        TC1.append("TC{}".format(n))
    else:
        TC2.append("TC{}".format(n))
    n+=1
    driver.get("https://www.saucedemo.com/")
### End ###

### Result Export ###
Functions.Results("PASSED",TC1,cur,con)
Functions.Results("FAILED",TC2,cur,con)
### End ###

driver.quit()
print("Completed!!!")

