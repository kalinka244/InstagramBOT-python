import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the web browser
driver = webdriver.Chrome()

# Go to the Instagram login page
url = "https://www.instagram.com/accounts/login/"
driver.get(url)

# Wait for the cookie popup and click "Decline All" if present
try:
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button._a9--._a9_1"))
    )
    cookie_button.click()
except:
    print("The cookie popup or button was not found.")

# Define username and password
username = "xxx"
password = "xxx"

# Wait for the username field
try:
    username_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_element.clear()
    username_element.send_keys(username)
except:
    print("The username field was not found.")

# Find the password field and fill it out
password_element = driver.find_element(By.NAME, "password")
password_element.clear()
password_element.send_keys(password)

# Simulate pressing the Enter key to submit the login form
password_element.send_keys(Keys.RETURN)

# Wait for 5 seconds before switching to the desired profile URLs
time.sleep(5)

# List of URLs to follow
profile_urls = [
    "https://www.instagram.com/shakira/",
    "https://www.instagram.com/shakira/",
    "https://www.instagram.com/shakira/",
    # Add more URLs here
]

# Iterate through the URLs and perform the follow action
for url in profile_urls:
    driver.get(url)
    
    # Wait for the 'Follow' element and click it
    try:
        follow_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="_aacl _aaco _aacw _aad6 _aade" and text()="Follow"]'))
        )
        follow_button.click()
        print(f"Followed the profile at {url}.")
    except:
        print(f"The 'Follow' element was not found on {url}.")

# Keep the script running without closing the browser
input("Press Enter to exit the script and manually close the browser...")

# Manually close the web browser after pressing Enter
driver.quit()
