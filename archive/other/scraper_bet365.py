# import requests
# from bs4 import BeautifulSoup
# import csv

# request = requests.get("https://www.bet365.com/#/AC/B17/C20890481/D1/E90598494/F2/")
# soup = BeautifulSoup(request.content, "html.parser")
# print(soup)
# divs = soup.body.find("div", attrs={"class": "wc-WebConsoleModule_SiteContainer "})
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# DRIVER_PATH = "../sports_better/chromedriver"

# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.get("https://www.google.com/")
# print(driver.page_source)
# driver.quit()

import time
from selenium import webdriver


driver = webdriver.Chrome('../sports_better/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
driver.quit()