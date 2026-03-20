# Open Amazon
#
# Verify page title and current URL
#
# Locate the category dropdown (next to search bar)
#
# Select "Books" using Select class
#
# Enter "Harry Potter" in search and press Enter
#
# Use explicit wait to wait until results are visible
#
# Get all product titles using find_elements
#
# Print first 5 product names
#
# Click on the first product
from itertools import product

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in')
driver.maximize_window()

wait_obj = WebDriverWait(driver, 6)

print(driver.title)
print(driver.current_url)



submit = wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="a-button-inner"]')))
submit.click()

# btn = driver.find_element(By.XPATH, '//select[@id ="searchDropdownBox"]')
# btn.click()


dropdown = wait_obj.until(EC.presence_of_element_located((By.ID, "searchDropdownBox")))
sleep(3)
select = Select(dropdown)
select.select_by_visible_text("Books")
sleep(3)

search= wait_obj.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="twotabsearchtextbox"]')))
search.send_keys("Harry Potter", Keys.ENTER)
sleep(3)

product_name = wait_obj.until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-component-type="s-search-results"]/descendant::h2')))
print("\nFirst 5 Products:")
for i in product_name[:5]:
    print(i.text)

product_name[0].click()

driver.quit()
