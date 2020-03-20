# README
* covid19_comfirmed_case_taiwan 臺灣武漢肺炎確診病例資料說明
	* 資料來源：衛生福利部疾管署
	* patient_id 病例案號
	* report_reason 通報原因
		* filtered at airport 機場採檢
		* hospitalized 就醫
		* identified as a contact 和確診者有接觸
	* infection_reason 感染原因
	* case_type 個案類型
		* imported case 境外移入
		* indigenous case 本土感染
	* group 案例群組：指標個案導致的群聚感染，以及隸屬同一個旅行團的個案，會被囊括在同一個群組裡
	* symptom 有無症狀
	* tourism_history 有無旅遊史
	* medical_history 有無慢性病史
	* confirmed_date 確診日期
	* released_date 解除隔離日期
	* deceased_date 死亡日期
	* State 狀態
		* released 解除隔離
		* isolated 隔離中
		* deceased 死亡

* country_epid_level_taiwan 臺灣旅遊疫情建議分級地區
	* 資料來源：衛生福利部疾管署
	*  level 臺灣旅遊疫情建議分級
		* 1：第一級，注意（watch），提醒民眾需遵守當地的一般預防措施，從此地回台灣需要自主健康管理 14 天
		* 2：第一級，警示（Alert），提醒民眾對當地採取加強防護，從此地回台灣需要自主健康管理 14 天
		* 3：第三級，警告（Warning），民眾應避免所有非必要旅遊，從此地回台灣需要居家檢疫 14 天。且從 3 月 16 日起，若執意去已公布第三級地區旅遊，回台確診武漢肺炎者，不得領取隔離補償，需自費相關防疫費用，且會被公布姓名
	* coordinate 座標是 infogram.com 的地圖系統

License: CC0 (https://creativecommons.org/publicdomain/zero/1.0/legalcode)