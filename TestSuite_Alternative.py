from selenium import webdriver
import cx_Oracle
import time
import os

### Set Path to instant Oracle client ###
os.environ['PATH']='C:\\app\Admin\\product\\12.1.0\\dbhome_1\\instantclient'
### End ###

### Initilized Chrome and URL  ###
driver=webdriver.Chrome()
driver.implicitly_wait(5) ## Implicit Wait
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
### End ###

### Establish connection to database ###
con=cx_Oracle.connect("xxxxx","xxxxxxx","xxxxxxx")
cur=con.cursor()
### End ###

### Function: SetUp query,variables and lists ###
query_select="select * From inputdata"
cur.execute(query_select)
n=1
TC1=[]
TC2=[]
### End ###

### Main ###
for columns in cur:
    username=columns[1]
    password=columns[2]
    driver.find_element_by_id("user-name").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("btn_action").click()
    element=driver.find_elements_by_css_selector('#inventory_filter_container > div') ## Explicit Wait
    length=len(element)
    if length != 0:
        TC1.append("TC{}".format(n))
    else:
        TC2.append("TC{}".format(n))
    n+=1
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
### End ###

### Function: Results ###
def Results(status,list):
    for i in list:
        cur.execute("update inputdata set result='{}' where id='{}'".format(status,i))
    con.commit()
### End ###

### Result Export ###
Results("PASSED",TC1)
Results("FAILED",TC2)
### End ###

driver.quit()
print("Completed!!!")

