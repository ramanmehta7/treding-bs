# pip install -U selenium
# https://www.geeksforgeeks.org/how-to-install-selenium-in-python/

# python -m pip install mysql-connector-python
import requests
# import mysql.connector
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

URL = "https://www.youtube.com/feed/trending"
driver = webdriver.Firefox()
driver.get(URL)

video_title = []
video_url = []
description = []
view_count = []

tag_list = driver.find_elements_by_tag_name(
    'ytd-expanded-shelf-contents-renderer')
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

print(len(video_url))

view_count_list = []
subscribers_count_list = []
channel_name_list = []
# for url in video_url:
for i in range(len(video_url)):
    url = video_url[i]
    if(i == 5):
        break
    driver.get(url)
    # video_page_info_tag = driver.find_element_by_tag_name(
    #     'ytd-video-view-count-renderer')
    # video_views_count = video_page_info_tag.find_element_by_tag_name(
    #     'span').text
    # video_views_count = driver.find_element_by_css_selector(
    #     ".view-count .style-scope .ytd-video-view-count-renderer").text
    wait = WebDriverWait(driver, 30)
    title2 = wait.until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, 'h1.ytd-video-primary-info-renderer yt-formatted-string')))
    print("Title : " + title2.text)

    video_views_count = wait.until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, '#count > ytd-video-view-count-renderer > span.view-count.style-scope.ytd-video-view-count-renderer')))

    video_likes_count = wait.until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, '#top-level-buttons-computed > a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer > yt-formatted-string')))

    video_dislikes_count = wait.until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, '#top-level-buttons-computed > a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer > yt-formatted-string')))

    print("dislikes Count :" + video_dislikes_count.text)

    channel_data = driver.find_elements_by_css_selector(
        'ytd-video-secondary-info-renderer ytd-video-owner-renderer yt-formatted-string ')
    
    channel_name_list.append(channel_data[0].text)
    subscribers_count_list.append(channel_data[1].text)
    view_count_list.append(video_views_count.text)

print(channel_name_list)
print(subscribers_count_list)
print(view_count_list)

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="trending"
# )

# cursor = db.cursor()

# cursor.execute("CREATE TABLE videos (title VARCHAR(1024), description VARCHAR(4096), url VARCHAR(256), views VARCHAR(16))")
# for i in range(len(video_title)):
#     sql = 'INSERT INTO videos VALUES ("' + video_title[i] + '", "' + description[i] + '",  "' + video_url[i] + '",  "' + view_count[i] + '")'
#     print(sql)
#     cursor.execute(sql)
#     db.commit()

# print(cursor.rowcount, " was inserted.")
