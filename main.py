# Load selenium components

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import date, timedelta

from functions import get_input, get_hotel_m_rate


arrival_date, num_days = get_input()

driver = webdriver.Chrome()

for i in range(1,num_days+1):
    time.sleep(5)
    departure = arrival_date + timedelta(days=i)
    get_hotel_m_rate(arrival_date, departure,driver)
   
driver.close()

