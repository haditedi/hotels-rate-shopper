from datetime import date

from selenium.webdriver.common.by import By

def get_input():
    enter_date = date.fromisoformat(input("Enter date (YYYY-MM-DD) :"))
    
    print(type(enter_date))
    day_length = int(input("how many days? :"))
    # begin_date = date.fromisoformat(enter_date)
    # end_date = begin_date + timedelta(days=day_length)
    return enter_date, day_length

def get_hotel_m_rate(arrival, departure, driver):
   
    url = f"https://be.synxis.com/?_ga=2.209538075.842375199.1642673487-1871191479.1642673487&adult=2&arrive={arrival}&chain=22402&child=0&config=SLH_HOTEL&configcode=SLH_HOTEL&currency=GBP&depart={departure}&hotel=35006&level=hotel&locale=en-US&rooms=1&src=24C"  
   
    driver.get(url)
    try: 
        elem=driver.find_element(By.XPATH, '//*[@id="auto-child-card-CLA0"]/div/div/div[2]/div[1]/div/div[1]/span')
        if elem.text == "Per Night":
            elem=driver.find_element(By.XPATH, '//*[@id="auto-child-card-CLA0"]/div/div/div[2]/div[1]/div/ins/span[2]')
        print(elem.text)
    except:
        print("not available")
    