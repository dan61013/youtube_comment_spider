# -*- coding: utf-8 -*-
"""
Author: Dan Cai
Date: 2024-08-08
Description: Crawl YouTube comments.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

SEARCH_KEY_WORD = "iphone 15 Pro"

def main():
    """Run YouTube Comment Spider
    """

    driver = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")
    driver.get(f"https://www.youtube.com/results?search_query={SEARCH_KEY_WORD}")
    driver.maximize_window()
    time.sleep(15)

    # 取得所有影片連結(不重複)

    link_list = []
    # 找出所有tag<a>的網址
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute("href")
        # 抓取一部影片就好，因為會爬到一部影片的多個章節點(連結)
        if href and "watch" in href and href.count("=") == 1:
            link_list.append(href)
    clean_link_list = list(set(link_list))  # 去除重複爬取影片網址
    print(f"爬取網址清單: \n{clean_link_list}")

    comment_list = []
    # 對link_list進行迴圈
    for i in clean_link_list:
        driver.get(i)  # 移動到該影片網址
        # 滾動頁面 -> 執行5次
        for _ in range(5):
            body = driver.find_element_by_tag_name("body")
            body.send_keys(Keys.END)  # 輸入Ctrl + End(移動到頁面底端)
            time.sleep(10)
        # 取得文字元素List
        text_list = driver.find_elements(By.TAG_NAME, 'yt-attributed-string')
        # 如果comment.text is True，就加入到comment_list
        for j in text_list:
            comment_text = j.text
            if comment_text:
                comment_list.append(j.text)
        time.sleep(5)
    driver.quit()

    # Output csv file
    df = pd.Series(comment_list)
    df.to_csv("./output/spider.csv", encoding="utf-8-sig")

if __name__ == "__main__":
    main()
