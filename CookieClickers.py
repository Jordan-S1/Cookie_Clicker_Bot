from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"
products_price_p = "productPrice"
product_prefix = "product"

# AMERICAN USERS WILL NEED TO COMMENT OUT LINES 22-25

# Wait for the "Consent" button to appear and click it
consent_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fc-button-label"))
    )
consent_button.click()

# Select a language before stating the game
language_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'English')]"))
    )
language_button.click()

# MAKE SURE TO SCROLL DOWN MANUALLY A BIT TO MAKE THE PRODUCTS VISIBLE 
# OR ELSE IT WILL STOP WORKING AFTER SOME COOKIES ARE CLICKED

# Wait for the cookie to load
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, cookie_id)))
cookie = driver.find_element(By.ID, cookie_id)


# Click the cookie to get cookies
while True:
    cookie.click()
    cookies_ct = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_ct = int(cookies_ct.replace(",", ""))

    # Check if we can buy a product
    for i in range(4):
        product_price = driver.find_element(By.ID, products_price_p + str(i)).text.replace(",", "")
        
        if not product_price.isdigit():
            continue

        product_price = int(product_price)
        # If we can buy the product, buy it
        if product_price <= cookies_ct:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break