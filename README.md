# 📄 AutoFormFiller - Automate Google Form Submission

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Download and Install WebDriver](#download-and-install-webdriver)
  - [Setup WebDriver](#setup-webdriver)
  - [Clone the Repo](#clone-the-repo)
  - [Customize the Script](#customize-the-script)
  - [Run the Script](#run-the-script)
- [Limitations](#limitations)

## Description
AutoFormFiller is a Python script that uses Selenium WebDriver to automate the process of filling out and submitting a Google Form. This can be useful for automating repetitive data entry tasks, such as filling out a form on a regular basis.

## Features
- Automates filling out Google Forms
- Supports multiple pages Google Forms
- Can be customized with specific data inputs
- Uses Selenium WebDriver for browser automation
- Supports Google Forms that collect email addresses

## Prerequisites
- Python 3.x
- Selenium library (install using `pip install selenium`)
- Microsoft Edge WebDriver

## Getting Started

### Download and Install WebDriver
1. For Edge, click on the three dots at the top right corner of the browser.
2. Then click on "Help" and finally "About Microsoft Edge."
3. You should see the version number in the middle of the tab that opens up!
4. Download the WebDriver that matches your Edge version.
5. Extract the zip file to the folder where you cloned the repo.

### Setup WebDriver
1. Download the Microsoft Edge WebDriver from [this link](https://msedgedriver.azureedge.net/126.0.2592.102/edgedriver_win64.zip).
2. Extract the downloaded file and note the path to `msedgedriver.exe`.

### Clone the Repo
```sh
git clone https://github.com/JayshreeMishra/AutoFormFiller---Automate-Google-Form-Submission.git
cd AutoFormFiller---Automate-Google-Form-Submission
```

### Customize the Script
#### Finding the Elements in the Webpage
1. Open up your targeted website normally and press `Ctrl+Shift+C`. This should open up a tab on the right and will show you the HTML code for whichever element (the section you want to fill info in, e.g., full name) you hover on.
2. Select the element you would like, right-click on it, and then choose `Copy -> Copy XPath`.

#### Interacting with the Elements
Use the copied XPath to interact with the elements in your script. For example:
```python
# Full Name
full_name_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @jsname='YPqjbf']"))
)
full_name_element.send_keys("your_name")
```

Edit `main.py` to customize the form fields with your data.

### Run the Script
To run the script, execute the Python file:
```sh
python main.py
```

## Limitations
- The script relies on XPath locators, which may need to be adjusted if the structure of the Google Form changes.
- Time delays (`time.sleep`) are used to handle loading times, which may need to be adjusted based on your internet connection speed.

---


Feel free to adjust the paths and form field details as per your requirements. This script is for the Microsoft Edge browser; if you are using a different browser, use the WebDriver specific to that browser and make the necessary changes in the code.

```
