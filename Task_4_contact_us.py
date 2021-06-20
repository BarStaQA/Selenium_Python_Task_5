from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

firstname = "Bartek"
lastname = "Stachowski"
email = "test@gmail.com"
comment = "Hello"

driver = webdriver.Chrome(executable_path='D:\Programming\Selenium_Python_Task_5\chromedriver.exe')
driver.get('http://webdriveruniversity.com/Contact-Us/contactus.html')

first_name_textbox = driver.find_element_by_name('first_name') 
first_name_textbox.send_keys(firstname)

last_name_textbox = driver.find_element_by_name('last_name')
last_name_textbox.send_keys(lastname)

email_textbox = driver.find_element_by_name('email')
email_textbox.send_keys(email)

comment_textbox = driver.find_element_by_name('message')
comment_textbox.send_keys(comment)

submit_btn = driver.find_element_by_xpath('//*[@id="form_buttons"]/input[2]').click()

check = driver.find_element_by_tag_name('h1')
assert check.text == "Thank You for your Message!"
print("Message successfully sent.")

sleep(5)
driver.close()
