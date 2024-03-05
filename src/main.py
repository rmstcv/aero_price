import time
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.keys import Keys
from _vars import AERO_PATH, CITY_DEST, DATE_DEPART
from _vars import class_CITY_DEPART, class_DATE_DEPART_FROM, class_SERCH_BTN, class_PRICE

if sys.version_info < (3, 11):
  print("Требуется Python версии 3.11 или новее")

svc = webdriver.ChromeService(executable_path = binary_path)

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service = svc, options = options)
driver.get(AERO_PATH)
time.sleep(10)

city_destination = driver.find_element(By.ID, class_CITY_DEPART)
city_destination.send_keys(CITY_DEST)
time.sleep(3)

date_depart_from = driver.find_element(By.ID, class_DATE_DEPART_FROM)
date_depart_from.clear()
time.sleep(3)

for i in range(10):
  date_depart_from.send_keys(Keys.BACKSPACE)
  time.sleep(1)
time.sleep(3)

date_depart_from.send_keys(DATE_DEPART)
time.sleep(2)

date_depart_from.send_keys(Keys.ENTER)
date_depart_from.send_keys(Keys.ENTER)

date_depart_to = driver.find_element(By.ID, class_DATE_DEPART_FROM)
date_depart_to.clear()
date_depart_to.send_keys(Keys.ENTER)
time.sleep(5)

search_btn = driver.find_element(By.CLASS_NAME, class_SERCH_BTN)
search_btn.click()
time.sleep(5)

price_min = driver.find_elements(By.CLASS_NAME, class_PRICE)

for price in price_min:
  print(price.text)

time.sleep(2)
driver.quit()