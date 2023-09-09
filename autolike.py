import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the function for the login process and liking posts
def like_posts_with_account(username, password, profile_urls):
    # Start the web browser
    driver = webdriver.Chrome()
    
    try:
        # Go to the Instagram login page
        driver.get("https://www.instagram.com/accounts/login/")

        # Wait for the cookie popup and click "Decline All" if present
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button._a9--._a9_1"))
            )
            cookie_button.click()
        except:
            print("The cookie popup or button was not found.")

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

        # Iterate through the URLs and perform the liking
        for url in profile_urls:
            driver.get(url)

            # Wait for the 'Like' element and click it
            try:
                like_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[@class="xp7jhwk"]'))
                )
                like_button.click()
                print(f"Post at {url} has been liked.")
            except:
                print(f"The 'Like' button was not found on {url}.")

    finally:
        # Close the web browser after liking
        driver.quit()

# List of URLs to like
profile_urls = [
    "link",
    "link",
    "link"
    # Add more URLs here
]

# List of account data
account_data = [
    {"username": "xxx", "password": "xxx"},

    # Add more account data here
]

# Use a ThreadPoolExecutor to perform likes for different accounts concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    for account in account_data:
        executor.submit(like_posts_with_account, account["username"], account["password"], profile_urls)
        print(f"Likes have been initiated for account {account['username']}.")

# Keep the script running
input("Press Enter to exit the script...")

# All browser instances should be closed automatically
