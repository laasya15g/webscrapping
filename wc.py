#scape information from website
import requests #use to get webpage libraries for now html
from bs4 import BeautifulSoup #lib will be responsibe to pass html code

oyo_url= "https://www.oyorooms.com/hotels-in-bangalore/"
    
req= requests.get(oyo_url) #to get the accessed content
content= req.content

#need to pass content to form soup object class bs4 package
soup= BeautifulSoup(content,"html.parser") #The parser module provides an interface to Python's internal parser and byte-code compiler
all_hotels = soup.find_all('div',{"class":"hotelCardListing"})
#each listing card info
for h in all_hotels :
    hotel_name = h.find("h3",{"class":"listingHotelDescription__hotelName"}).text
    hotel_address = h.find("span",{"itemprop":"streetAddress"}).text
     #try and throw block in python try expected block
    try:
        hotel_rating = h.find("span",{"class":"hotelRating__ratingSummary"}).text
    except AttributeError:
        pass
    hotel_cost = h.find("span",{"class":"listingPrice__finalPrice"}).text
   
    print(hotel_name,hotel_address,hotel_cost,hotel_rating)
