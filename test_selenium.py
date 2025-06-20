from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import mysql.connector
import tempfile
import shutil

# --- CHROME OPTIONS FOR CODESPACES ---
# Generate a temporary and unique Chrome user data directory
temp_dir = tempfile.mkdtemp()

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument(f"--user-data-dir={temp_dir}")

# Web app URL
url = "http://127.0.0.1:5000/"

# Test credentials
test_username = "testuser"
test_password = "testpass"

driver = None

try:
    print("🚀 Launching Chrome browser...")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    print("✅ Page loaded.")

    # Fill form and submit
    driver.find_element(By.NAME, "username").send_keys(test_username)
    driver.find_element(By.NAME, "password").send_keys(test_password)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    print("✅ Form submitted.")

    time.sleep(2)  # Wait for the form to process

except Exception as e:
    print(f"❌ Error during browser automation: {e}")

finally:
    if driver:
        driver.quit()
    shutil.rmtree(temp_dir)

# --- DATABASE VERIFICATION ---
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Secret5555',  # Adjust to match your Docker config
    'database': 'testdb'       # Adjust to match your schema
}

try:
    print("🔗 Connecting to MySQL database...")
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (test_username, test_password))
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    if results:
        print("✅ Test Passed: User found in database.")
    else:
        print("❌ Test Failed: User not found.")

except Exception as e:
    print(f"❌ Database error: {e}")
