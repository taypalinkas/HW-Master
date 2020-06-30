from splinter import browser
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return browser("chrome", **execuable_path, headless=False)

def scrape():
    browser = init_browser()
    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)
    
    #news
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    results = soup.find_all('div', class_='list_text')
    news_title = results.find('div', class_='content_title').text
    news_p = results.find('div', class_='article_teaser_body').text
    mars_news = [news_title, news_p]
    
    #featured image
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    img = soup.find('a', class_='button fancybox')['data-link']
    featured_image_url = 'https://www.jpl.nasa.gov'+ img
    featured_image_url
    
    #tweets
    mars_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    tweets = soup.find_all('div', class_="css-1dbjc4n")
    tweets_lv1 = tweets[0].find('div', class_='css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
    mars_tweets = tweets_lv1.find('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').text
    mars_tweets
    
    #mars facts
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    table_facts = tables[0]
    table_facts
    
    #cerberus
    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(cerberus_url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    cerberus = soup.find('div', class_='downloads')
    cerberus_link = cerberus.find('a')['href']
    cerberus_text = soup.find('h2').text
    cerberus_text = cerberus_text.strip('Enhanced')
    cerberus = [cerberus_link, cerberus_text]
    
    #schiaparelli
    schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(schiaparelli_url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    schiaparelli = soup.find('div', class_='downloads')
    schiaparelli_link = schiaparelli.find('a')['href']
    schiaparelli_text = soup.find('h2').text
    schiaparelli_text = schiaparelli_text.strip('Enhanced')
    schiaparelli = [schiaparelli_link,schiaparelli_text]
    
    #syris major
    syrtis_major_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(syrtis_major_url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    syrtis_major = soup.find('div', class_='downloads')
    syrtis_major_link = syrtis_major.find('a')['href']
    syrtis_major_text = soup.find('h2').text
    syrtis_major_text = syrtis_major_text.strip('Enhanced')
    syrtis_major = [syrtis_major_link, syrtis_major_text]
    
    #valles marineris
    valles_marineris_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(valles_marineris_url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    valles_marineris = soup.find('div', class_='downloads')
    valles_marineris_link = valles_marineris.find('a')['href']
    valles_marineris_text = soup.find('h2').text
    valles_marineris_text = valles_marineris_text.strip('Enhanced')
    valles_marineris = [valles_marineris_link, valles_marineris_text]
    
    #mars hemispheres
    hemisphere_image_urls = [
    {"title": valles_marineris_text, "img_url": valles_marineris_link},
    {"title": cerberus_text, "img_url": cerberus_link},
    {"title": schiaparelli_text, "img_url": schiaparelli_link},
    {"title": syrtis_major_text, "img_url": syrtis_major_link},]
    hemisphere_image_urls
    
    #final output
    mars = {"News": mars_news[0],
            "Featured Image": featured_image_url,
           "Tweets": mars_tweets,
           "Facts": table_facts,
           "Cerberus": cerberus,
           "Schiaparelli": schiaparelli,
           "Syrtis Major": syrtis_major,
           "Valles Marineris": valles_marineris}
    
    browser.quit()
    return mars
        