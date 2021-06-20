from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

username = "locked_out_user"
password = "secret_sauce"

driver = webdriver.Chrome(executable_path='D:\Programming\Selenium_Python_Task_5\chromedriver.exe')
driver.get('https://www.saucedemo.com/')

username_textbox = driver.find_element_by_xpath('//*[@id="user-name"]') 
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_xpath('//*[@id="password"]') 
password_textbox.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@id="login-button"]')
login_btn.click()

print(driver.find_element_by_xpath('//*[@id="login_button_container"]/div/form/div[3]/h3').text)
print("Locked out user successful check")

sleep(2)
driver.close()