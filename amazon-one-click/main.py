from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = '/Users/thomas/drivers/chrome-mac-arm64/Google Chrome for Testing.app'  # Update this path to your chromedriver location
driver = webdriver.Chrome()

login_email = ""
login_password = ""
item_asin = "B07614PPV8"  # ASIN for the item to be purchased

driver.get("https://www.amazon.com.au/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com.au%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=auflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

# Enter email
try:
    email_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='ap_email_login']"))
    )
    email_input.send_keys(login_email)
    email_input.send_keys(Keys.RETURN)
    print("Email entered successfully.")
except Exception as e:
    print("Error entering email:", e)

# Enter password
try:
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='ap_password']"))
    )
    password_input.send_keys(login_password)
    password_input.send_keys(Keys.RETURN)
    print("Password entered successfully.")
except Exception as e:
    print("Error entering password:", e)

driver.get("https://www.amazon.com.au/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance?ASIN=" +  item_asin + "&quantity=1&submit.buy-now=Submit&account-linking=yes&dropdown-selection=add-new&dropdown-selection-ubb=add-new&tag=&offeringID=")

# Wait for the title to be exactly "Place Your Order", refreshing if not
max_retries = 1000000
for attempt in range(max_retries):
    try:
        place_order_btn = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='bottomSubmitOrderButtonId']/span/input"))
        )
        place_order_btn.click()
        print("Clicked 'Place your order' button successfully.")
        break
    except Exception:
        print(f"Title not matched, refreshing... (attempt {attempt + 1})")
        driver.refresh()
else:
    print("Failed to reach the 'Place Your Order' page after several attempts.")

print("Order placed successfully.")

driver.quit()