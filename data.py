# pip install -U selenium
# https://www.geeksforgeeks.org/how-to-install-selenium-in-python/
# python -m pip install mysql-connector-python 
import requests
import mysql.connector 
# from bs4 import BeautifulSoup
# r = requests.get(URL)
# 'pip install html5lib --user' - Specifying the HTML parser we want to use
# data = BeautifulSoup(r.content, 'html5lib')
# print(data.prettify())
# title = data.find_all('yt-formatted-string')
# for i in range(len(title)):
#     print(title[i])
# print(title)

# n = data.find_all('div', {'class':['style-scope', 'ytd-video-renderer']})
# print(n)
from selenium import webdriver

URL = "https://www.youtube.com/feed/trending"
driver = webdriver.Firefox()
driver.get(URL)

video_title = []
video_url = []
description = []
view_count = []

tag_list = driver.find_elements_by_tag_name('ytd-expanded-shelf-contents-renderer')
for tag in tag_list:
    title_anchor_tag = tag.find_elements_by_id('video-title')
    description_tag = tag.find_elements_by_id('description-text')
    view_count_div_tag = tag.find_elements_by_id('metadata-line')

    for anchor_tag in title_anchor_tag:
        video_title.append(anchor_tag.text)
        video_url.append(anchor_tag.get_attribute('href'))

    for desc in description_tag:
        description.append(desc.text)

    for views_count_tag in view_count_div_tag:
        view_count_span_tag = views_count_tag.find_element_by_tag_name('span')
        view_count_string = view_count_span_tag.text
        view_count_number = view_count_string[0:len(view_count_string) - 6]
        view_count.append(view_count_number)

# view_count = []
# for url in video_url:
#     driver.get(url)
    # video_page_info_tag = driver.find_element_by_tag_name('ytd-video-view-count-renderer')
    # video_views_count = video_page_info_tag.find_element_by_tag_name('span').text
    # video_views_count = driver.find_element_by_css_selector(".view-count .style-scope .ytd-video-view-count-renderer").text
    # view_count_number = video_views_count[0:len(video_views_count) - 6]
    # view_count.append(view_count_number)
    # print(view_count)

    # a1 = driver.find_elements_by_id('owner-sub-count')
    # if (len(a1) == 2):
    #     print(a1[1].text)
    # for i in a1:
    #     a2 = i.find_element_by_tag_name('a').text
    #     print(a2)
        # for i in like_count:
        #     print(i)

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="trending"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE videos (title VARCHAR(1024), description VARCHAR(4096), url VARCHAR(256), views VARCHAR(16))")
for i in range(len(video_title)):
    sql = 'INSERT INTO videos VALUES ("' + video_title[i] + '", "' + description[i] + '",  "' + video_url[i] + '",  "' + view_count[i] + '")'
    print(sql)
    cursor.execute(sql)
    db.commit()

print(cursor.rowcount, " was inserted.") 