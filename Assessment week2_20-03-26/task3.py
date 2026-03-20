# Open Google
#
# Enter "Selenium Python"
#
# Use explicit wait for suggestions
#
# Capture all suggestions using find_elements
#
# Print them
#
# Click one suggestion


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=opts)
driver.get('https://www.google.com/')
driver.maximize_window()

wait_obj = WebDriverWait(driver, 6)

search= wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//textarea[@name="q"]')))
search.send_keys("Selenium Python", Keys.ENTER)
sleep(3)

suggestions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul[role='listbox'] li")))

print("Suggestions:")
valid_suggestions = []

for i, suggestion in enumerate(suggestions):
    text = suggestion.text
    if text:
        valid_suggestions.append(suggestion)
        print(f"{len(valid_suggestions)}. {text}")

if valid_suggestions:
    valid_suggestions[0].click()

driver.quit()
sleep(5)