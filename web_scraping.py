from bs4 import BeautifulSoup as bs  #importing library from beautifulSoup4

import requests #for requesting HTTPS

import pandas  #for data manipulation and analysis

#storing url in variable
base_url="https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2"

r=requests.get(base_url) #requesting HTTPS using requests library

soup=bs(r.text,'lxml')  #parsing data from page

all_products=soup.findAll('a', attrs={'class':'_31qSD5'})  #finding all the 'a' tags from page and storing into variable

product_name=[]
prices=[]   #making 2 list for storing data you can make more

for items in all_products: #iterating over all 'a' tags stored in all_product variable
    price=items.find('div', attrs={'class':"_1vC4OE _2rQ-NK"})  #finding 'div' tags from 'a' tags 
    name=items.find('div', attrs={'class':'_3wU53n'})
    
    #print(price)    #without .text extension
    
    prices.append(price.text)   #simple appending into list
    product_name.append(name.text)
    
#manipulating data using pandas library and putting it into desired format (.csv) 
df = pandas.DataFrame({'Product Name':product_name,'Price':prices}) 
df.to_csv('product.csv', index=False, encoding='utf-8')



