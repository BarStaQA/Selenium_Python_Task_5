from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

driver = webdriver.Chrome(executable_path='D:\Programming\Selenium_Python_Task_5\chromedriver.exe')
driver.get('https://parabank.parasoft.com/parabank/register.htm')

firstname_textbox = driver.find_element_by_name('customer.firstName').send_keys("Bartek")
lastname_textbox = driver.find_element_by_name('customer.lastName').send_keys("Stachowski")
adress_textbox = driver.find_element_by_name('customer.address.street').send_keys("test 54/1")
city_textbox = driver.find_element_by_name('customer.address.city').send_keys("Wroclaw")
state_textbox = driver.find_element_by_name('customer.address.state').send_keys("Dolnoslaskie")
zip_code_textbox = driver.find_element_by_name('customer.address.zipCode').send_keys("53321")
phone_textbox = driver.find_element_by_name('customer.phoneNumber').send_keys("111222333")
ssn_textbox = driver.find_element_by_name('customer.ssn').send_keys("123456789")
username_textbox = driver.find_element_by_name('customer.username').send_keys("Selenium2")
password_textbox = driver.find_element_by_name('customer.password').send_keys("123456789")
confirm_textbox = driver.find_element_by_name('repeatedPassword').send_keys("123456789")

register_btn = driver.find_element_by_class_name('button').click()
sleep(2)

check = driver.find_element_by_tag_name('h1')
assert check.text == "ParaSoft Demo Website"
print("Account correctly set up")

sleep(1)
driver.close()
