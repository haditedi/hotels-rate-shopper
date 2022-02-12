from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from functions import get_input, get_hotel_m_rate, get_hotel_h_rate, get_hotel_s_rate
from charting import plot_chart



#SETUP CHROME DRIVER
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

try: 
    driver.get("https://littlehotelier.authx.siteminder.com/login")
    el = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-email")))
    el.send_keys("contact@hampton-suites.london")
    el = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-submit")))
    el.click()
    el = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-password")))
    el.send_keys("Seaview987")
    el = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-submit")))
    el.click()
    time.sleep(18)
    el = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/article/main/div/a[2]')))
    el.click()
    
except Exception as inst:
    print(inst)

    




