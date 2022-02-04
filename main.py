from selenium import webdriver

from functions import get_input, get_hotel_m_rate, get_hotel_h_rate
from charting import plot_chart


#SETUP CHROME DRIVER
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#CONTENT
arrival_date, num_days = get_input()
driver = webdriver.Chrome(options=options)
# x_axis, y_axis = get_hotel_m_rate(arrival_date, num_days, driver)

h_x_axis, h_y_axis = get_hotel_h_rate(arrival_date, num_days, driver)
driver.close()

plot_chart(h_x_axis, h_y_axis)





