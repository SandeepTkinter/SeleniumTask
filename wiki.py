import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def wikisearch(movie,browser):
    browser=browser
    browser.get('http://www.google.com')
    search = browser.find_element(By.NAME,'q')
    search.send_keys("wikipedia " +movie +" film")
    search.send_keys(Keys.RETURN) # hit return after you enter search text
    result = browser.find_element(By.TAG_NAME,'h3')
    result.click()
    time.sleep(5)
    wiki = browser.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table/tbody')

    listed= ''
    country2=''

    for val in wiki:
        listed = listed+str(val.text)

    listed=listed.split("\n")

    for val in listed:
        if 'Country' in val:
            val=val.split(" ")
            val=val[1]
            country2=country2+(val)
            break

    releaseDate = listed[listed.index('Release date')+1]

    return[releaseDate, country2]






