from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

#  Open website
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

sleep(5)

# Username field (
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
print(username.text)
print('name')

# Password field
password = driver.find_element(By.CSS_SELECTOR, "input#password")
print(password.text)
print('*******')

#  Login button
login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print(login_btn.text)
print('submit')

sleep(3)

#  Footer link
footer_link = driver.find_element(By.CSS_SELECTOR, "div#page-footer a")
print(footer_link.text)
print('successfully ')

driver.quit()