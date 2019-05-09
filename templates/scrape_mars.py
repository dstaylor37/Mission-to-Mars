#!/usr/bin/env python
# coding: utf-8

#Dependencies
from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup
import time
import requests
import pymongo

# # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
# get_ipython().system('which chromedriver')


# # Choose the executable path to driver 
def init_browser():
        executable_path = {'executable_path': '/Users/danieltaylor/Desktop/dstaylor37/11-Mission-To-Mars/chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)

mars_info = {}

def scrape_mars_news():
        try:

                browser = init_browser()
                # URL of page to be scrape
                News_url = 'https://mars.nasa.gov/news/'
                browser.visit(url)
                html = browser.html
                soap = BeautifulSoup(html, 'html.parser')
                news_title = soup.find('div', class_='content_title').find('a').text
                news_p = soup.find('div', class_='article_teaser_body').text
        
                mars_info['news_title'] = news_title
                mars_info['news_paragraph'] = news_p

                return mars_info
        finally:
                browser.quit()

def scrape_mars_image():

        try:
                Browser = init_browser()

                image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
                browser.visit(image_url_featured)
                #HTML object
                html = browser.html

                #Parse HTML with Beautiful Soup
                soup = BeautifulSoup(html_image, 'html.parser')

                #retrieve background-image url from style tag
                featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

               #website url
                main_url = 'https://www.jpl.nasa.gov'

                #combine the image and web site url
                featured_image_url = main_url + featured_image_url

                #show the combined image link
                featured_image_url 

                mars_info['featured_image_url'] = featured_image_url 

                return mars_info
        finally:
                Browser.quit()

def scrape_mars_weather():

        try:

                Browser = init_browser()

                ###Mars Weather
                #Scrape the latest Mars weather tweet from the page
                weather_url = 'https://twitter.com/marswxreport?lang=en'
                browser.visit(weather_url)

                html_weather = browser.html

                weather_soup = BeautifulSoup(html_weather, 'html.parser')

                mars_weather_tweet = weather_soup.find_all('div', class_='js-tweet-text-container')

                for tweet in mars_weather_tweet:
                        mars_weather_tweet = tweet.find('p').text
                if tweet.text.strip().startswith('InSight sol'):
                        mars_weather = tweet.text.strip()

                        mars_info['weather_tweet'] = weather_tweet

                return mars_info
        finally:
                broswer.quit()

#mars facts
def scrape_mars_facts():

        url = 'https://space-facts.com/mars/'
        browser.visit(url)

        mars_df = pd.read_html(url)
        mars_df = (mars_df[0])

        mars_df.columns=['Description', 'Value']

        mars_df.set_index('Description', inplace=True)

        mars_df.to_html()

        data = mars_df.to_dict(orient='records')

        mars_df

def scrape_mars_hemispheres():

##Mars Hemispheres
        try:
                broswer = init_browser()

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
                        mars_info['hiu'] = hiu

                return mars_info
        finally:

                browser.quit()