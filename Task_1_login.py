from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

username = "standard_user"
password = "secret_sauce"

driver = webdriver.Chrome(executable_path='D:\Programming\Selenium_Python_Task_5\chromedriver.exe')
driver.get('https://www.saucedemo.com/')

username_textbox = driver.find_element_by_name('user-name') 
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('password') 
password_textbox.send_keys(password)

login_btn = driver.find_element_by_name('login-button')
login_btn.click()

element = driver.find_element_by_class_name('inventory_item_name')
assert element.text == "Sauce Labs Backpack"

print("Logged in successfully")

sleep(2)
driver.close()
