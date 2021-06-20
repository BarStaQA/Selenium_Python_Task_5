from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

username = "standard_user"
password = "secret_sauce"
firstname = "Bartek"
lastname = "Stachowski"
zipcode = "53321"

driver = webdriver.Chrome(executable_path='D:\Programming\Selenium_Python_Task_5\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
driver.maximize_window() 

username_textbox = driver.find_element_by_name('user-name') 
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('password') 
password_textbox.send_keys(password)

login_btn = driver.find_element_by_name('login-button').click()

add_btn = driver.find_element_by_name('add-to-cart-sauce-labs-backpack')
add_btn.click()

shoping_card_btn = driver.find_elements_by_class_name('shopping_cart_link')[0]
shoping_card_btn.click()

checkout_btn = driver.find_element_by_name('checkout').click()

firstname_textbox = driver.find_element_by_name('firstName').send_keys(firstname) 
lastname_textbox = driver.find_element_by_name('lastName').send_keys(lastname)
zipcode_textbox = driver.find_element_by_name('postalCode').send_keys(zipcode)

continue_btn = driver.find_element_by_name('continue').click()

finish_btn = driver.find_element_by_name('finish').click()

element = driver.find_element_by_class_name('complete-text')
assert element.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
print("Product correctly ordered")

sleep(1)
driver.close()