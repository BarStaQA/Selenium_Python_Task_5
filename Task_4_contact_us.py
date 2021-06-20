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

#contact_us_btn = driver.find_element_by_xpath('//*[@id="contact-us"]/div/div[1]')
#contact_us_btn.click()

first_name_textbox = driver.find_element_by_css_selector('#contact_form > input:nth-child(1)') 
first_name_textbox.send_keys(firstname)

last_name_textbox = driver.find_element_by_xpath('//*[@id="contact_form"]/input[2]')
last_name_textbox.send_keys(lastname)

email_textbox = driver.find_element_by_xpath('//*[@id="contact_form"]/input[3]')
email_textbox.send_keys(email)

comment_textbox = driver.find_element_by_xpath('//*[@id="contact_form"]/textarea')
comment_textbox.send_keys(comment)

submit_btn = driver.find_element_by_xpath('//*[@id="form_buttons"]/input[2]')
submit_btn.click()

if driver.find_elements_by_css_selector('#contact_reply'):
    print("The message has been sent successfully.")

sleep(5)
driver.close()
