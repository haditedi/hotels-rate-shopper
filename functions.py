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
            print(arrival, elem.text)
            y_axis.append(elem.text)   
        except:
            print("not available")
            y_axis.append(None)
        finally:
            x_axis.append(arrival)
            arrival+=timedelta(days=1)
    print(x_axis, y_axis)
        
        
def get_test(arrival, num_days, driver):
    x_axis = []
    y_axis = []
    for i in range(1,num_days+1):
        time.sleep(3)
        departure = arrival + timedelta(days=1)
       
        # url = f"https://www.booking.com/hotel/gb/the-kings-arms-hampton-court.en-gb.html?aid=356983;label=gog235jc-1DCAMoUEIHaGFtcHRvbkgJWANoUIgBAZgBCbgBF8gBDNgBA-gBAfgBAogCAagCA7gC9rrujwbAAgHSAiQ4YmFhOWQ2My1jYjRlLTRmYjktOTc1Mi1jMGE2YTFlNzg2NzHYAgTgAgE;sid=0a4bcaf9f993c503a84f679acc58c6d0;all_sr_blocks=3434808_183674060_2_1_0;checkin={arrival};checkout={departure};dest_id=-2598072;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=5;highlighted_blocks=3434808_183674060_2_1_0;hpos=5;matching_block_id=3434808_183674060_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=3434808_183674060_2_1_0__12000;srepoch=1643879815;srpvid=af4041432a920248;type=total;ucfs=1&#hotelTmpl"  
        url=f"{hotel_m_url};label=gog235jc-1DCAMoUEIHaGFtcHRvbkgJWANoUIgBAZgBCbgBF8gBDNgBA-gBAfgBAogCAagCA7gC9rrujwbAAgHSAiQ4YmFhOWQ2My1jYjRlLTRmYjktOTc1Mi1jMGE2YTFlNzg2NzHYAgTgAgE;sid=0a4bcaf9f993c503a84f679acc58c6d0;all_sr_blocks=11258_218417501_0_1_0;checkin={arrival};checkout={departure};dest_id=-2598072;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=3;highlighted_blocks=11258_218417501_0_1_0;hpos=3;matching_block_id=11258_218417501_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=11258_218417501_0_1_0__19000;srepoch=1643879817;srpvid=af4041432a920248;type=total;ucfs=1&#hotelTmpl"
        driver.get(url)

        try:
            elem=driver.find_element(By.XPATH, '//*[@id="room_type_id_11258"]/span')
            print(elem.text)
            elem=driver.find_element(By.XPATH, '//*[@id="hprt-table"]/tbody/tr[1]/td[3]/div/div/div[1]/div[2]/div/span')
            print(arrival, elem.text)
            
            x_axis.append(arrival)
            y_axis.append(elem.text)
          
        except:
            print(arrival,"not available")
            x_axis.append(arrival)
            y_axis.append(None)
            # //*[@id="hprt-table"]/tbody/tr[1]/td[3]/div/div/div[1]/div[2]/div/span
            # //*[@id="hprt-table"]/tbody/tr[1]/td[3]/div/div/div[1]/div[2]/div/span
            #//*[@id="room_type_id_11258"]/span
            
        finally:
            arrival+=timedelta(days=1)
    print(x_axis, y_axis)

