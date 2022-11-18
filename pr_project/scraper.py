import requests

from bs4 import BeautifulSoup
from sys import version
from bs4 import BeautifulSoup
import requests
# from requests_html import HTMLSession
import pandas as pd
import json
main_list = []
from bs4 import SoupStrainer
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
def get_amazon_data(data):
    print(data)
    url =data
    r = requests.get(url,headers=headers)
    soup  = BeautifulSoup(r.text,'html.parser')
    try:
        name = soup.find('span',{'id':'productTitle'}).text.strip()
    except:
        name = 'Not Found'
    try:
        hendle = name.replace(',','')
        hendle = hendle.replace(' ','-')
        hendle = hendle.lower()
        hendle = hendle[:17]
    except:
        hendle = 'hendle-not-found'
    try:
        compare_at_price = soup.find('span',{'data-a-color':'secondary'}).find('span').replace('₹','').text.strip()
    except:
        compare_at_price = 'Not Found'
    try:
        final_price = soup.find('span',{'data-a-color':'price'}).find('span').replace('₹','').text.strip()
    except:
        final_price = 'Not Found' 

    try:
        short_description = soup.find('div',{'id':'feature-bullets'}).text.strip()
    except:
        short_description = 'Not Found'

    try:
        long_description = soup.find('table',{'id':'productDetails_techSpec_section_1'})
    except:
        long_description = 'Product Details not found'


    try:
        rating_count = soup.find('span',{'id':'acrCustomerReviewText'}).text.strip()
    except:
        rating_count = ' Not Found'

    try:
        rating  = soup.find('span',{'id':'acrPopover'})['title']
    except:
        rating = ' Not Found'

    try:
        img =  soup.find('div',{'id':'imgTagWrapperId'}).find('img')['src']
    except:
        img = ' Not Found'
        
    main_dir  = {
        'Title':name,
        'hendle':hendle,
        'compare_at_price':compare_at_price,
        'price':final_price,
        'short_description':short_description,
        'long_description':long_description,
        'rating_count':rating_count,
        'rating':rating,
        'img':img,
    }
    main_list.append(main_dir)

    
    # csv.to_csv('data.csv',index=False)
    print('script run successfully')
    return pd.DataFrame(main_list)




# get_amazon_data("https://www.amazon.in/Samsung-Galaxy-Storage-6000mAh-Battery/dp/B0B4F2TTTS/ref=lp_4363159031_1_1")
