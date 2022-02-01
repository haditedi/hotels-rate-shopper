from selenium import webdriver

from functions import get_input, get_hotel_m_rate

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

arrival_date, num_days = get_input()

driver = webdriver.Chrome(options=options)
get_hotel_m_rate(arrival_date, num_days, driver)
   
driver.close()



