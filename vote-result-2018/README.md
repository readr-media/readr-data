2018年中華民國地方公職人員選舉結果與村里資料彙整
=============

## 檔案名稱與用途
資料格式皆為 .json 檔

### 縣市層級資料
檔名為下列格式
	
	vote_info_by_province.json
	{縣市編號}.json (例：63000.json 為台北市投票結果)

### 鄉鎮市區層級資料
檔名為下列格式

	vote_info_by_area.json
	{縣市編號}{鄉鎮市區編號}.json (例：63000010.json 為台北市松山區投票結果)

### 村里層級資料
檔名為下列格式

	vote_info_by_location.json
	{縣市編號}{鄉鎮市區編號}_detail.json (例：63000010_detail.json 為台北市松山區各里投票結果)

### 村里對照表
	village_code_mapping.json
此表用於以 {縣市編號} {鄉鎮市區編號} {村里編號} 的形式索引村里名稱

## 資料格式
- 欄位說明
	- TC : 縣市長投票結果
	- T1, T2, T3 : 議員投票結果
	- F1, ... , F9, FA : 公投投票結果
	- age : 該地區年齡分佈，第一區間為 15-20 歲人數，以五歲為區間遞增，最後一欄為 100+ 歲人數
	- education : 該地區教育程度，分別為 "國小畢以下", "國中畢", "高中畢", "專畢", "大畢", "碩畢", "博畢" 的人數
	- sex : 該地區性別人數，分別為"男性", "女性"
	- middle_num : 該地區收入中位數

- 大選投票結果欄位說明 (TC, T1, T2, T3)
	- candTksInfo : 以 array 儲存候選人得票資料 (縣市層級只有政黨得票資料)
		- tks : 得票數
		- tksRate : 得票率 (得票數/總有效票)
		- party : 候選人所屬政黨
		- name : 候選人姓名
		- candNo : 候選人號次
		- birthday : 候選人生日
		- candVictor : 當選註記，對應意義請參照中選會資料
	- totalVotables : 總可投票人數
	- voteRate : 投票率
	- areaCode : 選區編號

- 公投結果欄位說明
	- agreeTks : 同意票數
    - disagreeTks : 不同意票數
    - totalVotables : 總可投票人數
    - voteRate : 投票率

## 資料來源
- 投票資料 https://github.com/kiang/2018.cec.gov.tw
- 村里人口、教育、年齡統計數據 https://data.moi.gov.tw/MoiOD/Data/DataDetail.aspx?oid=4E7FFDCC-17EC-4E5C-9DD7-780C2890AF6B
- 村里收入統計數據 https://ws.fia.gov.tw/001/upload/ias/isa105/105%E5%B9%B4%E5%BA%A6%E7%B6%9C%E5%90%88%E6%89%80%E5%BE%97%E7%A8%85%E7%94%B3%E5%A0%B1%E5%88%9D%E6%AD%A5%E6%A0%B8%E5%AE%9A%E7%B5%B1%E8%A8%88%E5%B0%88%E5%86%8A.html