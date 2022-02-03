from selenium import webdriver

from functions import get_input, get_hotel_m_rate, get_test

import matplotlib.pyplot as plt
import numpy as np


#SETUP CHROME DRIVER
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


#CONTENT
arrival_date, num_days = get_input()
driver = webdriver.Chrome(options=options)
get_hotel_m_rate(arrival_date, num_days, driver)

#x_axis, y_axis = get_test(arrival_date,num_days, driver)
#print(plt.style.available)
# plt.style.use('seaborn')
# x_axis = ['22-03-01', '22-03-03', '22-03-04', '22-03-06', '22-03-07']

# series1 = np.array([200, None, 240, 200, 190]).astype(np.double)
# s1mask = np.isfinite(series1)
# series2 = np.array([220, 270, 240, 300, 320]).astype(np.double)
# s2mask = np.isfinite(series2)

# plt.plot(x_axis[s1mask], series1[s1mask], linestyle='-', marker='o')
# plt.plot(x_axis[s2mask], series2[s2mask], linestyle='-', marker='o')



#print(x_axis, y_axis)   
# plt.plot(x_axis, y_axis, marker=".", ms=15, label="HOTEL M")
# plt.plot(x_axis, hotelb_y_axis, marker=".", ms=15, label="HOTEL A")

# plt.xlabel("DATE")
# plt.ylabel("RATE (£)")
# plt.tight_layout()
# plt.legend()
# plt.show()
#driver.close()



