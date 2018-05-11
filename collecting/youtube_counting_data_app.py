import time
from datetime import datetime
import random
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from selenium import webdriver
import sqlite3
import json
import sys, os, inspect
from pathlib import Path

# sql_transaction = []
browser=webdriver.Chrome("/home/young/chromedriverfolder/chromedriver")
# 2 address
# address_list=["https://www.youtube.com/watch?v=qj9-9c6DJCs","https://www.youtube.com/watch?v=ippg-fn61_4"]
# 3 address
# address_list=["https://www.youtube.com/watch?v=qj9-9c6DJCs","https://www.youtube.com/watch?v=ippg-fn61_4","https://www.youtube.com/watch?v=nZ1cV-PcBPc"]
# full address
# address_list=["https://www.youtube.com/watch?v=qj9-9c6DJCs","https://www.youtube.com/watch?v=ippg-fn61_4","https://www.youtube.com/watch?v=nZ1cV-PcBPc","https://www.youtube.com/watch?v=stGPHxtQLZw","https://www.youtube.com/watch?v=6KpibWZr0ME&t","https://www.youtube.com/watch?v=zpEq3gBpBs4","https://www.youtube.com/watch?v=qDXEs5YBfTk"]
address_list=["https://www.youtube.com/watch?v=KshpDBbpmQA",
"https://www.youtube.com/watch?v=X3aLv6N5pCE&t",
"https://www.youtube.com/watch?v=bH7b8TZLNSk&t",
"https://www.youtube.com/watch?v=74yf7f3FNDU",
"https://www.youtube.com/watch?v=KKbhrvWy2JQ&t",
"https://www.youtube.com/watch?v=L6aZA4Jz57Y",
"https://www.youtube.com/watch?v=js4w9MN8Da4&t",
"https://www.youtube.com/watch?v=-B0kzKkcuX4&t",
"https://www.youtube.com/watch?v=Cwc8gLiZ3Sk",
"https://www.youtube.com/watch?v=ic7nJ42GA3A"]

data_dictionary={}

title_list=[]
view_list=[]
like_list=[]
dislike_list=[]
comment_list=[]

for one_address in address_list:
    browser.get(one_address)
    time.sleep(3)
    extracted_title=browser.find_element_by_css_selector("#container > h1 > yt-formatted-string")
    time.sleep(0.4)
    extracted_number_of_view=browser.find_element_by_css_selector("#count > yt-view-count-renderer > span.view-count.style-scope.yt-view-count-renderer")
    time.sleep(0.4)
    extracted_number_of_like=browser.find_element_by_css_selector("#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a #text")
    time.sleep(0.4)
    extracted_number_of_dislike=browser.find_element_by_css_selector("#top-level-buttons > ytd-toggle-button-renderer:nth-child(2) > a > #text")
    time.sleep(0.4)
    extracted_number_of_comment=browser.find_element_by_css_selector("#count > yt-formatted-string")
    time.sleep(0.4)

    title_list.append(extracted_title.text)
    view_list.append(extracted_number_of_view.text)
    # print("extracted_number_of_like.__dir__()",extracted_number_of_like.__dir__())
    #  ['_parent', '_id', '_w3c', '__module__', '__doc__', '__init__', '__repr__', 'tag_name', 'text', 'click', 'submit', 'clear', 'get_property', 'get_attribute', 'is_selected', 'is_enabled', 'find_element_by_id', 'find_elements_by_id', 'find_element_by_name', 'find_elements_by_name', 'find_element_by_link_text', 'find_elements_by_link_text', 'find_element_by_partial_link_text', 'find_elements_by_partial_link_text', 'find_element_by_tag_name', 'find_elements_by_tag_name', 'find_element_by_xpath', 'find_elements_by_xpath', 'find_element_by_class_name', 'find_elements_by_class_name', 'find_element_by_css_selector', 'find_elements_by_css_selector', 'send_keys', 'is_displayed', 'location_once_scrolled_into_view', 'size', 'value_of_css_property', 'location', 'rect', 'screenshot_as_base64', 'screenshot_as_png', 'screenshot', 'parent', 'id', '__eq__', '__ne__', '_execute', 'find_element', 'find_elements', '__hash__', '_upload', '__dict__', '__weakref__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

    like_list.append(extracted_number_of_like.get_attribute("aria-label"))
    dislike_list.append(extracted_number_of_dislike.get_attribute("aria-label"))
    comment_list.append(extracted_number_of_comment.text)


number_of_site=len(address_list)
title_temp_list=[]
for i in range(number_of_site):
    title_temp_list.append(str(title_list[i])+"@@@")
title_concatenated_in_string="".join(title_temp_list)[:-3]

view_temp_list=[]
for i in range(number_of_site):
    view_temp_list.append(str(view_list[i])+"@@@")
view_concatenated_in_string="".join(view_temp_list).replace("조회수 ","").replace("회","").replace(",","")[:-3]

like_temp_list=[]
for i in range(number_of_site):
    like_temp_list.append(str(like_list[i])+"@@@")
like_concatenated_in_string="".join(like_temp_list).replace("좋아요 ","").replace("개","").replace(",","")[:-3]

dislike_temp_list=[]
for i in range(number_of_site):
    dislike_temp_list.append(str(dislike_list[i])+"@@@")
dislike_concatenated_in_string="".join(dislike_temp_list).replace("싫어요 ","").replace("개","").replace(",","")[:-3]

comment_temp_list=[]
for i in range(number_of_site):
    comment_temp_list.append(str(comment_list[i])+"@@@")
comment_concatenated_in_string="".join(comment_temp_list).replace("댓글 ","").replace("개","").replace(",","")[:-3]

current_working_directory_in_string=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def sql_insert_has_parent(date,title,view_count,like,dislike,comment):
    try:
        
        sql = """INSERT INTO youtube_data (date, title, view_count, like, dislike, comment) VALUES ("{}","{}","{}","{}","{}","{}");""".format(date, title, view_count, like, dislike, comment)
        # print("sql",sql)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion',str(e))
    
def transaction_bldr(sql):
    connection = sqlite3.connect('youtube_data.db')
    c = connection.cursor()
    c.execute('BEGIN TRANSACTION')
    c.execute(sql)
    connection.commit()

if not os.path.isfile(current_working_directory_in_string+"/youtube_data.db"):
    connection = sqlite3.connect('youtube_data.db')
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS youtube_data(date TEXT, title TEXT, view_count TEXT, like TEXT, dislike TEXT, comment TEXT)")
    connection.commit()
    date=str(datetime.now())
    sql_insert_has_parent(date,title_concatenated_in_string,view_concatenated_in_string,like_concatenated_in_string,dislike_concatenated_in_string,comment_concatenated_in_string)
else:
    date=str(datetime.now())
    sql_insert_has_parent(date,title_concatenated_in_string,view_concatenated_in_string,like_concatenated_in_string,dislike_concatenated_in_string,comment_concatenated_in_string)


import sqlite3
import pandas as pd

cnx = sqlite3.connect('youtube_data.db')
df = pd.read_sql_query("SELECT * FROM youtube_data", cnx)
df.to_csv("youtube_data.csv", encoding='utf-8', index=False)

import pandas as pd

import csv
 
entire_data_list_from_csv=[]
with open('youtube_data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        entire_data_list_from_csv.append(row)

entire_kind_of_data_list=[]

number_of_column=len(entire_data_list_from_csv[0])

number_of_row_tries=df.shape[0]
number_of_element_of_data=4
address_list=["https://www.youtube.com/watch?v=KshpDBbpmQA",
"https://www.youtube.com/watch?v=X3aLv6N5pCE&t",
"https://www.youtube.com/watch?v=bH7b8TZLNSk&t",
"https://www.youtube.com/watch?v=74yf7f3FNDU",
"https://www.youtube.com/watch?v=KKbhrvWy2JQ&t",
"https://www.youtube.com/watch?v=L6aZA4Jz57Y",
"https://www.youtube.com/watch?v=js4w9MN8Da4&t",
"https://www.youtube.com/watch?v=-B0kzKkcuX4&t",
"https://www.youtube.com/watch?v=Cwc8gLiZ3Sk",
"https://www.youtube.com/watch?v=ic7nJ42GA3A"]
number_of_site=len(address_list)

for i in range(number_of_column):
    entire_kind_of_data_list.append(list(np.array(entire_data_list_from_csv)[:,i][1:].T))


entire_date_data_list=[]
entire_title_data_list=[]
entire_view_data_list=[]
entire_like_data_list=[]
entire_dislike_data_list=[]
entire_comment_data_list=[]

for i in range(number_of_column):
    if i==0:
        entire_date_data_list=entire_kind_of_data_list[i]
    if i==1:
        entire_title_data_list=entire_kind_of_data_list[i]
    if i==2:
        entire_view_data_list=entire_kind_of_data_list[i]
    if i==3:
        entire_like_data_list=entire_kind_of_data_list[i]
    if i==4:
        entire_dislike_data_list=entire_kind_of_data_list[i]
    if i==5:
        entire_comment_data_list=entire_kind_of_data_list[i]

entire_date_data_list_without_at=[]
for i in range(number_of_row_tries):
    entire_date_data_list_without_at.append(str(entire_date_data_list[i]))
entire_title_data_list_without_at=[]
for i in range(number_of_row_tries):
    entire_title_data_list_without_at.append(str(entire_title_data_list[i]).split("@@@"))
entire_view_data_list_without_at=[]
for i in range(number_of_row_tries):
    entire_view_data_list_without_at.append(str(entire_view_data_list[i]).split("@@@"))
entire_like_data_list_without_at=[]
for i in range(number_of_row_tries):
    entire_like_data_list_without_at.append(str(entire_like_data_list[i]).split("@@@"))
entire_dislike_data_list_without_at=[]
for i in range(number_of_row_tries):
    entire_dislike_data_list_without_at.append(str(entire_dislike_data_list[i]).split("@@@"))
entire_comment_data_list_without_at=[]
for i in range(number_of_row_tries):
    entire_comment_data_list_without_at.append(str(entire_comment_data_list[i]).split("@@@"))                    


grouped_by_each_site_title_data_list=[]
for i in range(number_of_site):
    grouped_by_each_site_title_data_list.append(np.array(entire_title_data_list_without_at)[:,i].T)

grouped_by_each_site_view_data_list=[]
for i in range(number_of_site):
    grouped_by_each_site_view_data_list.append(np.array(entire_view_data_list_without_at)[:,i].T)

grouped_by_each_site_like_data_list=[]
for i in range(number_of_site):
    grouped_by_each_site_like_data_list.append(np.array(entire_like_data_list_without_at)[:,i].T)    

grouped_by_each_site_dislike_data_list=[]
for i in range(number_of_site):
    grouped_by_each_site_dislike_data_list.append(np.array(entire_dislike_data_list_without_at)[:,i].T)    

grouped_by_each_site_comment_data_list=[]
for i in range(number_of_site):
    grouped_by_each_site_comment_data_list.append(np.array(entire_comment_data_list_without_at)[:,i].T)    


empty_figure=plt.figure()

subplot_list=[]
for i in range(number_of_site):
    subplot_list.append(empty_figure.add_subplot(number_of_site,1,i+1))

for i in range(number_of_site):
    subplot_list[i].plot(entire_date_data_list_without_at, grouped_by_each_site_view_data_list[i], label="view_count")
    subplot_list[i].plot(entire_date_data_list_without_at, grouped_by_each_site_like_data_list[i], label="view_count")
    subplot_list[i].plot(entire_date_data_list_without_at, grouped_by_each_site_dislike_data_list[i], label="view_count")
    subplot_list[i].plot(entire_date_data_list_without_at, grouped_by_each_site_comment_data_list[i], label="view_count")
plt.show()

for i in range(number_of_site+1):
    plt.plot(entire_date_data_list_without_at, grouped_by_each_site_view_data_list[i], label="view_count")
    plt.plot(entire_date_data_list_without_at, grouped_by_each_site_like_data_list[i], label="view_count")
    plt.plot(entire_date_data_list_without_at, grouped_by_each_site_dislike_data_list[i], label="view_count")
    plt.plot(entire_date_data_list_without_at, grouped_by_each_site_comment_data_list[i], label="view_count")
    plt.show()


# * You prepare youtube video links which you want to analyze.
# * This test, for example, performed with 10 youtube video links.
# * This app collects youtube video data(collecting data time, title, view count, like count, dislike count, comment count).
# * This app draws distribution of data on plane.
# * The order of line is comment count, dislike count, like count, view count.
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/entire_in_one_show.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1-1.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1-2.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1-3.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1-4.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1-5.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1-6.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1-7.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1-8.png"><xmp>
# </xmp><img src="https://raw.githubusercontent.com/youngmtool/myapp/master/collecting/pic/Figure_1-9.png"><xmp>
