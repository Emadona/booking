from selenium import webdriver
from driver import MyBot
from bs4 import BeautifulSoup


url = 'https://www.booking.com/searchresults.en.html?'
class Booking:
    def __init__(self):
        # self.url = url
        self.driver = MyBot().driver
    
    def scraper(self,city='', adults='', children='', checkin_year='',checkin_month='',checkin_day='',checkout_year='',checkout_month='',checkout_day='',selected_currency='USD'):
        self.url= url+'ss={0}&group_adults={1}&group_children={2}&checkin_year={3}&checkin_month={4}&checkin_monthday={5}&checkout_year={6}&checkout_month={7}&checkout_monthday={8}&selected_currency={9}'.format(city, adults, children, checkin_year,checkin_month,checkin_day,checkout_year,checkout_month,checkout_day,selected_currency)
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        containers = soup.find_all('div' , {"data-testid":"property-card"})
        if len(containers) >0:
            all_data = []
            for container in containers:
                try:
                    title = container.find('div',{'data-testid':"title"}).text
                except:
                    title = ''
                try:
                    address = container.find('span',{'data-testid':"address"}).text
                except:
                    address = ''
                try:
                    review = container.find('div',{'class':"_9c5f726ff bd528f9ea6"}).text
                except:
                    review = ''
                try:
                    type1 = container.find('span',{'class':"_c5d12bf22"}).text
                except:
                    type1 = ''
                try:
                    description = container.find('div',{'class':"_2075f7b46"}).text
                except:
                    description = ''
                try:
                    price = container.find('span',{'class':"fde444d7ef _e885fdc12"}).text
                except:
                    price = ''
                data = {
                    'title' : title,
                    'aadress': address,
                    'review' : review,
                    'type' : type1,
                    'description' : description,
                    'price' : price
                }
                
                all_data.append(data)
            return all_data
        else:
            return {'message' : 'please try again'}
