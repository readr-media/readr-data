# README
* covid19_comfirmed_case_taiwan 臺灣武漢肺炎確診病例資料說明
	* 資料來源：衛生福利部疾管署
	* patient_id 病例案號
	* report_reason 通報原因
		* filtered at airport 機場採檢
		* hospitalized 就醫
		* identified as a contact 和確診者有接觸
		* home isolation 居家隔離，14 天內禁止外出，也不可搭乘大眾運輸工具，衛生主管機關每天兩次追蹤健康情況
		* home quarantine 居家檢疫，14 天內禁止外出，也不可搭乘大眾運輸工具，里長或里幹事每天兩次追蹤健康情況
		* group quarantine 集中檢疫，於集中檢疫所檢疫 14 天，通常出現在包機或群聚事件
		* stringent self-health management 加強自主健康管理，自主管理者每天量體溫並通報，有症狀就要回報，若有違反檢疫規定就會重罰
	* case_type 個案類型
		* imported case 境外移入
		* indigenous case 本土感染
	* imported_country：個案在哪個國家感染
	* contact_with：個案與誰接觸
	* group 案例群組：指標個案導致的群聚感染，以及隸屬同一個旅行團的個案，會被囊括在同一個群組裡
	* symptoms 症狀
	* show_symptoms 發病日期
	* reported_date 通報日期
	* tourism_history 有無旅遊史
	* medical_history 有無慢性病史
	* confirmed_date 確診日期
	* released_date 解除隔離日期
	* deceased_date 死亡日期
	* departure_date 出國日期
	* arrival_date 回國日期
	* deceased_date 死亡日期
	* State 狀態 （疾管署回應，為了保護隱私，不再公布3/10之後解除隔離之個案）
		* released 解除隔離
		* isolated 隔離中
		* deceased 死亡
	* VOC 該病例為英國變種新冠病毒（英國變異株 VOC 202012/01）
	* mock_case_number 統計用模擬案號：自 2021-05-15 起，疾管署不再公布詳細個案疫調，改授權地方政府公布。但為計算指標群聚案數量（group），故會先編號，待地方政府公布詳細疫調資訊後配合修改。意即，若 mock_case_number 欄位內容為 y，表示政府未公布該個案的資料；若 mock_case_number 欄位內容為空白，則該個案的案號跟內容是政府公佈過或 READr 詢問過主管機關的
	* city_of_residence 個案居住地：個案所在縣市，但僅有被地方政府公佈足跡的個案會有此資料。若要查詢縣市病例數，請以資料 indigenous_case_county.csv 為主
 
* risk_categories_for_countries_regions
	* 資料來源：衛生福利部疾管署（自 2021-04-28 開始更新）
	* 感染風險國家名單：疾管署公布，自 2020-06-22 起若從中、低感染風險國家入境，並符合特殊條件者，可以縮短居家檢疫的時間。條件為：
		* 停留台灣時間少於 3 個月
		* 出發地為中低感染風險地區
		* 登機前 14 天沒有其他國家的旅遊史
		* 自低風險國家出發者，5 天居家檢疫後，可自費採檢，陰性則改自主健康管理
		* 自中低風險國家出發者，7 天居家檢疫後，可自費採檢，陰性則改自主健康管理 
	* risk_level 感染風險等級
		* low：低風險國家地區
		* medium：高風險國家地區
	* update_time 異動日期（若從名單上移除，會直接刪除資料，請至 file_change 查詢異動）

* country_epid_level_taiwan 臺灣旅遊疫情建議分級地區
	* 資料來源：衛生福利部疾管署（兩週更新一次）
	*  level 臺灣旅遊疫情建議分級
		* 1：第一級，注意（watch），提醒民眾需遵守當地的一般預防措施
		* 2：第一級，警示（Alert），提醒民眾對當地採取加強防護
		* 3：第三級，警告（Warning），民眾應避免所有非必要旅遊，從 3 月 16 日起，若執意去已公布第三級地區旅遊，回台確診武漢肺炎者，不得領取隔離補償，需自費相關防疫費用，且會被公布姓名
	* coordinate 座標是 infogram.com 的地圖系統
* indigenous_case_county
	* 各縣市確診數量資料    
	* 資料來源：https://nidss.cdc.gov.tw/nndss/DiseaseMap?id=19CoV
* risk_level_county
	* 各縣市疫情警戒等級
License: CC0 (https://creativecommons.org/publicdomain/zero/1.0/legalcode)
