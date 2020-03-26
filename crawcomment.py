from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time 
import json

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=QJzSJhM9blI")
time.sleep(2)  # give the page some time to load

# --------------- FETCH TITLE ---------------
# get the video's title
title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
print(title)

# --------------- LOAD ALL COMMENTS ---------------
# defining the numbers here so we can reference and easily change them
SCROLL_PAUSE_TIME = 2
CYCLES = 100

# we know there's always exactly one HTML element, so let's access it
html = driver.find_element_by_tag_name('html')
# first time needs to not jump to the very end in order to start
html.send_keys(Keys.PAGE_DOWN)  # doing it twice for good measure
html.send_keys(Keys.PAGE_DOWN)  # one time sometimes wasn't enough
# adding extra time for initial comments to load
# if they fail (because too little time allowed), the whole script breaks
time.sleep(SCROLL_PAUSE_TIME * 3)
# and now for loading the hidden comments by scrolling down and up
for i in range(CYCLES):
    html.send_keys(Keys.END)
    time.sleep(SCROLL_PAUSE_TIME)
    # might not be necessary; try out without it.
    # html.send_keys(Keys.PAGE_UP)
    # time.sleep(SCROLL_PAUSE_TIME)

# --------------- GETTING THE COMMENT TEXTS ---------------
comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
# pprint(comment_elems)  # for double-checking
all_comments = [elem.text for elem in comment_elems]

# --------------- WRITING TO OUTPUT FILE ---------------
with open('yt_comments.json', 'w') as f:
    json.dump(all_comments, f)



# driver.find_element_by_name("q").send_keys("corona" + Keys.RETURN)

# time.sleep(5)
# soup = BeautifulSoup(driver.page_source, 'lxml')
# raw = soup.findAll('div', attrs={'class': 'r'})
# urls=[]
# for res in raw:
#     urls.append(res.find("a",href = True).get("href"))

# print(urls)

# for klik in urls:
#     driver.get(klik)

