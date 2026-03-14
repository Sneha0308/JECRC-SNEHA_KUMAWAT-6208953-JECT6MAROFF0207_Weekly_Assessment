from selenium import webdriver
import time

# Open browser
driver = webdriver.Chrome()
driver.maximize_window()

websites = [
    "https://www.thesouledstore.com/",
    "https://www.nike.com/",
    "https://www.amazon.in/",
    "https://www.bbc.com/",
    "https://www.python.org/"
]

# Loop through websites
for site in websites:
    time.sleep(3)
    driver.get(site)
    print("Website:", site)
    print("Page Title:", driver.title)
    print("-----------------------------")


driver.quit()