import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def imdbsearch(movie, browser):
    browser = browser
    # browser.get('http://www.google.com')
    # search = browser.find_element(By.NAME,'q')
    # search.send_keys("imdb " +movie)
    # search.send_keys(Keys.RETURN) # hit return after you enter search text
    # result = browser.find_element(By.TAG_NAME,'h3')
    # result.click()
    # time.sleep(20)
    # release = browser.find_element(By.XPATH,'//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[10]/div[2]/ul')
    # details = ''
    browser.get('https://www.imdb.com')
    time.sleep(5)
    searchbox = browser.find_element(By.ID, "suggestion-search")
    searchbox.click()
    searchbox.send_keys(movie)
    searchbox.send_keys(Keys.ENTER)
    current=browser.current_url
    browser.get(str(current))

    imdb = browser.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul')
    # sleep(10)
    release=''
    for child in imdb.find_elements(By.TAG_NAME, "a"):
        if child.text == movie:
            child.click()
            time.sleep(10)
            release = browser.find_element(By.XPATH,'//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[10]/div[2]/ul')
            print(release)
            break
    details=''

    for child in release.find_elements(By.TAG_NAME,"a"):
        temp = str(child.text)+"^"
        details = details+temp

    details = details.split('^')
    release=details[1].replace(',',"")
    release=release.split(" ")
    releaseText = release[1]+" "+release[0]+" "+release[2]

    release = releaseText
    country = details[3]

    return [release,country]
