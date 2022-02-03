from datetime import date, timedelta
import time

from selenium.webdriver.common.by import By

#SETUP ENVIRONMENT
from dotenv import load_dotenv
import os
load_dotenv()
hotel_m_url = os.environ.get("HOTEL_M_URL")


#CONTENT
def get_input():
    enter_date = date.fromisoformat(input("Enter date (YYYY-MM-DD) :"))
    day_length = int(input("how many days? :"))
    return enter_date, day_length

def get_hotel_m_rate(arrival, num_days, driver):
    print("Hotel M")
    print("Date       Rate")

    x_axis = []
    y_axis = []
    for i in range(1,num_days+1):
        time.sleep(3)
        departure = arrival + timedelta(days=1)     
        url = f"{hotel_m_url}&adult=2&arrive={arrival}&chain=22402&child=0&config=SLH_HOTEL&configcode=SLH_HOTEL&currency=GBP&depart={departure}&hotel=35006&level=hotel&locale=en-US&rooms=1&src=24C"  
        driver.get(url)
        
        try: 
            elem=driver.find_element(By.XPATH, '//*[@id="auto-child-card-CLA0"]/div/div/div[2]/div[1]/div/div[1]/span')
            if elem.text == "Per Night":
                elem=driver.find_element(By.XPATH, '//*[@id="auto-child-card-CLA0"]/div/div/div[2]/div[1]/div/ins/span[2]')
            room_rate = int(elem.text[1:])
            print(arrival, elem.text)
            y_axis.append(room_rate)   
        except:
            print(arrival, "not available")
            y_axis.append(None)
        finally:
            x_axis.append(arrival)
            arrival+=timedelta(days=1)
    return x_axis, y_axis
        
        

