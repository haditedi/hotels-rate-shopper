from selenium import webdriver

from functions import get_input, get_hotel_m_rate, get_hotel_h_rate
from charting import plot_chart

import concurrent.futures


#SETUP CHROME DRIVER
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#CONTENT
arrival_date, num_days = get_input()
driver1 = webdriver.Chrome(options=options)
driver2 = webdriver.Chrome(options=options)

#FETHCING RATES IN PARALLEL BY LAUNCHING TWO BROWSER
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_m = executor.submit(get_hotel_m_rate, arrival_date, num_days, driver1)
    future_h = executor.submit(get_hotel_h_rate, arrival_date, num_days, driver2)
    (m_x_axis, m_y_axis) = future_m.result()
    (h_x_axis, h_y_axis) = future_h.result()

driver1.close()
driver2.close()

plot_chart(h_x_axis, h_y_axis, m_y_axis)





