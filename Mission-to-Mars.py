#!/usr/bin/env python
# coding: utf-8


#Dependencies
from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup
import time
import requests
import pymongo




# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
#get_ipython().system('which chromedriver')




# Choose the executable path to driver 
#def init_browser():
executable_path = {'executable_path': '/Users/danieltaylor/Desktop/dstaylor37/11-Mission-To-Mars/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)



def scrape():
    Browser = init_browser()




# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[34]:


#HTML object
html = browser.html

#Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Retrieve the parent divs for all articles
news_title = soup.find('div', class_='content_title').find('a').text
news_p = soup.find('div', class_='article_teaser_body').text

#display scrapped data
print(news_title)
print(news_p)


# In[35]:


### JPL Mars Space Images - Featured Image
###Visit the url for JPL Featured Space Image 
###[here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url_featured)


# In[36]:


#html object
html_image = browser.html

#parse html with beautiful soup
soup = BeautifulSoup(html_image, 'html.parser')

#retrieve background-image url from style tag
featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

#website url
main_url = 'https://www.jpl.nasa.gov'

#combine the image and web site url
featured_image_url = main_url + featured_image_url

#show the combined image link
featured_image_url


# In[37]:


###Mars Weather
#Scrape the latest Mars weather tweet from the page
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)


# In[38]:


html_weather = browser.html

weather_soup = BeautifulSoup(html_weather, 'html.parser')

mars_weather_tweet = weather_soup.find_all('div', class_='js-tweet-text-container')

for tweet in mars_weather_tweet:
    mars_weather_tweet = tweet.find('p').text
    if tweet.text.strip().startswith('InSight sol'):
        mars_weather = tweet.text.strip()


# In[39]:


print(mars_weather_tweet)


# In[40]:


##Mars Fact
#Visit the Mars Facts webpage [here](https://space-facts.com/mars/) 
#and use Pandas to scrape the table containing facts about the planet including 
#Diameter, Mass, etc.

#Use Pandas to convert the data to a HTML table string.

url = 'https://space-facts.com/mars/'
browser.visit(url)

mars_df = pd.read_html(url)
mars_df = (mars_df[0])


mars_df.columns=['Description', 'Value']

mars_df.set_index('Description', inplace=True)

mars_df.to_html()

data = mars_df.to_dict(orient='records')

mars_df

# mars_df = mars_df.to_html(classes='mars')
# table_data = mars_df.replace('\n',' ')
# table_data


# mars_df = mars_df.to_html(classes='mars')
# table_data = mars_df.replace('\n\, ' ')
# table_data

# In[41]:


##Mars Hemispheres

hemi_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemi_url)

html_hemi = browser.html

soup = BeautifulSoup(html_hemi, 'html.parser')

items = soup.find_all('div', class_='item')

hiu = []

hemi_images_urls = 'https://astrogeology.usgs.gov'

for i in items:
    title = i.find('h3').text
    thumb_url = i.find('a', class_='itemLink product-item')['href']
    browser.visit(hemi_images_urls + thumb_url)
    thumb_image_html=browser.html
    soup = BeautifulSoup(thumb_image_html, 'html.parser')
    full_image_url = hemi_images_urls + soup.find('img', class_='wide-image')['src']
    hiu.append({'title': title, 'img_url': full_image_url})
hiu


# In[28]:


browser.quit()


# In[ ]:




