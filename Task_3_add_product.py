from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

username = "standard_user"
password = "secret_sauce"
firstname = "Bartek"
lastname = "Stachowski"
zipcode = "53321"

driver = webdriver.Chrome(executable_path='D:\Programming\Selenium\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
driver.maximize_window() 

username_textbox = driver.find_element_by_xpath('//*[@id="user-name"]') 
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_xpath('//*[@id="password"]') 
password_textbox.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@id="login-button"]')
login_btn.click()

add_btn = driver.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-backpack"]')
add_btn.click()

shoping_card_btn = driver.find_elements_by_xpath('//*[@id="shopping_cart_container"]')[0]
shoping_card_btn.click()

checkout_btn = driver.find_element_by_xpath('//*[@id="checkout"]').click()

firstname_textbox = driver.find_element_by_xpath('//*[@id="first-name"]').send_keys(firstname) 
lastname_textbox = driver.find_element_by_xpath('//*[@id="last-name"]').send_keys(lastname)
zipcode_textbox = driver.find_element_by_xpath('//*[@id="postal-code"]').send_keys(zipcode)

continue_btn = driver.find_element_by_xpath('//*[@id="continue"]').click()

finish_btn = driver.find_element_by_name('finish').click()

if driver.find_element_by_class_name('complete-text').text:
    print("Your order has been dispatched, and will arrive just as fast as the pony can get there!")

sleep(1)
driver.close()