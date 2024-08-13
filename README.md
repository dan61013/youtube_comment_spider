# YouTube Comment Spider

用途: 爬取指定關鍵字的影片評論。

Table of contents:

- [YouTube Comment Spider](#youtube-comment-spider)
  - [使用方法](#使用方法)
  - [注意事項](#注意事項)

---

## 使用方法

1. 開啟[main.py](./main.py)
2. 修改Line 14. `SEARCH_KEY_WORD`為想要進行搜尋的關鍵字
3. F5 Run Script!

## 注意事項

- 目前只有設定透過修改關鍵字進行單一產品的評論擷取。
  - 且影片清單較少，因為在搜尋後並未加入滾動頁面的動作。
- 等待時間較長，因目前設定的sleep時間較長。
- 會擷取到影片description。
- Comment擷取到的數量過少，則修改Line 43. `range(5)`，讓`Ctrl` + `End`的動作執行更多次。
