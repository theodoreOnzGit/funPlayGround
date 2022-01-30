#https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

# first i installed beautifulsoup using pip
# pip install beautifulsoup4
# https://www.geeksforgeeks.org/beautifulsoup-installation-python/
# had a bug at line 28, urllib request could not be loaded

# i thought urllib needed to be pip installed, but nope, it's a standard library apperntly
# https://stackoverflow.com/questions/47730259/installing-urllib-in-python3-6/49085923

# never fully debugged, just playing around... 


import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
line_count = 1 #variable to track what line you are on
for one_a_tag in soup.findAll('a'):  #'a' tags are for links
    if line_count >= 36: #code for text files starts at line 36
        link = one_a_tag['href']
        download_url = 'http://web.mta.info/developers/'+ link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
        time.sleep(1) #pause the code for a sec
    #add 1 for next line
    line_count +=1
