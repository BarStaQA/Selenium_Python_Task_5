from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

username = "standard_user"
password = "secret_sauce"

driver = webdriver.Chrome(executable_path='D:\Programming\Selenium\chromedriver.exe')
driver.get('https://www.saucedemo.com/')

username_textbox = driver.find_element_by_xpath('//*[@id="user-name"]') 
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_xpath('//*[@id="password"]') 
password_textbox.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@id="login-button"]')
login_btn.click()

print(driver.find_element_by_class_name('inventory_item_name').text)
print("Logged in successfully")

sleep(2)
driver.close()
