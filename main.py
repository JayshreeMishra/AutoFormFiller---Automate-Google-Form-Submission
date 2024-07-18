from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--incognito")

driver_path = r"C:\Users\your_file_path\msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)

driver.get("https://docs.google.com/forms/google_form_link")



# Full Name
full_name_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @jsname='YPqjbf']"))
)
full_name_element.send_keys("your_name")

#Contact Number
contact_number_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@jsname='YPqjbf' and @aria-labelledby='i5']"))
)
contact_number_element.send_keys("your_contact_number")

#Email ID
email_id_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@jsname='YPqjbf' and @aria-labelledby='i9']"))
)
email_id_element.send_keys("your_email@gmail.com")

# Full Address
full_address_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//textarea[@jsname='YPqjbf' and @aria-labelledby='i13']"))
)
full_address_element.send_keys("your_address")

# Pin Code
pin_code_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@jsname='YPqjbf' and @aria-labelledby='i17']"))
)
pin_code_element.send_keys("your_pin_code")

# Date of Birth
date_of_birth_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='date' and @jsname='YPqjbf']"))
)
date_of_birth_element.send_keys("your_dob")

# Gender
gender_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @jsname='YPqjbf' and @aria-labelledby='i26']"))
)
gender_element.send_keys("your_gender")

# Other Sections
other_sections_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @jsname='YPqjbf' and @aria-labelledby='i30']"))
)
other_sections_element.send_keys("other_sections_info")

time.sleep(30)

# Submit the form
submit_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")))
submit_button.click()

time.sleep(20)

#Close the browser
driver.quit()



