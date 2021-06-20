from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

firstname = "Bartek"
lastname = "Stachowski"
adress = "test 54/1"
city = "Wroclaw"
state = "Dolnoslaskie"
zip_code = "53321"
phone = "111222333"
ssn = "123456789"
username = "Selenium2"
password = "123456789"

driver = webdriver.Chrome(executable_path='D:\Programming\Selenium_Python_Task_5\chromedriver.exe')
driver.get('https://parabank.parasoft.com/parabank/register.htm')

firstname_textbox = driver.find_element_by_xpath('//*[@id="customer.firstName"]').send_keys(firstname)
lastname_textbox = driver.find_element_by_xpath('//*[@id="customer.lastName"]').send_keys(lastname)
adress_textbox = driver.find_element_by_xpath('//*[@id="customer.address.street"]').send_keys(adress)
city_textbox = driver.find_element_by_xpath('//*[@id="customer.address.city"]').send_keys(city)
state_textbox = driver.find_element_by_xpath('//input[@id="customer.address.state"]').send_keys(state)
zip_code_textbox = driver.find_element_by_xpath('//*[@id="customer.address.zipCode"]').send_keys(zip_code)
phone_textbox = driver.find_element_by_xpath('//*[@id="customer.phoneNumber"]').send_keys(phone)
ssn_textbox = driver.find_element_by_xpath('//*[@id="customer.ssn"]').send_keys(ssn)
username_textbox = driver.find_element_by_xpath('//*[@id="customer.username"]').send_keys(username)
password_textbox = driver.find_element_by_xpath('//*[@id="customer.password"]').send_keys(password)
confirm_textbox = driver.find_element_by_xpath('//*[@id="repeatedPassword"]').send_keys(password)

register_btn = driver.find_element_by_xpath('//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input').click()
sleep(2)

if driver.find_elements_by_css_selector('#rightPanel > p'):
    print("Your account was created successfully")

sleep(1)
driver.close()
