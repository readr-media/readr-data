# readme
### 名詞定義
* hk = 被刪除的帳號中，有發過反送中推文的，共有 105 個帳號

### 資料清單
* 01_dele_accounts_group：940 個被刪除帳號清單，hk 帳號在 group 欄位標註為 hk （組別標示方式：READr 團隊將 2019 年 2 月——香港政府推出《逃犯條例》修正後——有發文的貼文篩出，人工辨識內容是否跟反送中運動有關）
* 02_hk_post：hk 帳號所有推文，檔案另放在：[02_hk_post.csv - Google 雲端硬碟](https://drive.google.com/file/d/17UC8t5b7Ivnh6Iby2PpUGYWYWLlCZHax/view?usp=sharing)
* 03_at_hk_list：曾經與 hk 互動過的帳號清單
* 04_node_list：hk 帳號互動網絡帳號資料，gephi 繪圖用，node資料，group 欄位 1=hk帳號，2=其他被刪除帳號，3=其他帳號
* 05_edge_count：hk 帳號互動網絡關係資料，gephi 繪圖用，edges 資料
* 06_nodes_timeline：05 帳號資料加上時間變化，gephi 繪圖用，node資料
* 07_edges_timeline：06 關係資料加上時間變化，gephi 繪圖用，node資料
* 08 機器學習結果
* 09_tweets_language：推特推文語言代碼中文翻譯對照（in 不在官方 support language 中，依照內文翻譯是印尼文；und 不知道是什麼… 歸到 NA）
* 10_users_train1.csv 用來進行機器學習的 training data
* 11_users_train2.csv 用來作為機器學習的驗證資料


註：資料 01、02、03 為 Twitter 公佈原始資料，只是依照需求切分小檔，並另外標註組別
#twitter
