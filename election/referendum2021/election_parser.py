#!/usr/bin/python3

import json
from requests.api import request
from google.cloud import storage
import gzip
import json
import requests

with open("zone-code.json", "r") as area_file:
    area_code = area_file.read()
area_data = json.loads(area_code)
output_file = open('referendum2021_result.csv', "w")
output_file.write("timestamp, 編號, 縣市, 鄉鎮市區, 省市別, 縣市別, 鄉鎮市區, 投開票所編號, 同意票數, 同意比率, 不同意票數, 不同意比率, 通過註記, 有效票數, 無效票數, 投票數, 已領未投票數, 發出票數, 用餘票數, 投票權人數, 投票率, 應送達鄉鎮市區數, 已送達鄉鎮市區數, 應送投開票所數, 已送投開票所數, 有效同意票數對投票權人數百分比, 開票進度百分比, 開票狀況及時下載檔案")

cases = ['F1', 'F2', 'F3', 'F4']
f = open('RFrunning.json')
data = json.load(f)
dashboard = {}
dashboard["ST"] = data["ST"]
dest = 'json/tv-schedule.json'
bucket_name = ''

def upload_data(bucket_name: str, data: bytes, content_type: str, destination_blob_name: str):
    '''Uploads a file to the bucket.'''
    # bucket_name = 'your-bucket-name'
    # data = 'storage-object-content'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    # blob.content_encoding = 'gzip'
    blob.upload_from_string(
        # data=gzip.compress(data=data, compresslevel=9),
        data=bytes(data.encode('utf-8')),
        content_type=content_type, client=storage_client)
    blob.content_language = 'zh'
    blob.cache_control = 'max-age=300,public'
    blob.patch()

for case in cases:
    if case in data:
        dashboard[case] = {}
        for zone in data[case]:
            if zone["prvCode"] == "00" and zone["cityCode"] == "000" and zone["deptCode"] == "000":
                print(zone["agreeTks"], zone["agreeRate"], zone["disagreeTks"], zone["disagreeRate"], zone["prgRate"])
                dashboard[case]["agreeTks"] = zone["agreeTks"]
                dashboard[case]["agreeRate"] = zone["agreeRate"]
                dashboard[case]["disagreeTks"] = zone["disagreeTks"]
                dashboard[case]["disagreeRate"] = zone["disagreeRate"]
                dashboard[case]["prgRate"] = zone["prgRate"]
            if zone["deptCode"] != "000":
                city_code = zone["prvCode"] + "-" + zone["cityCode"] + "-000"
                combined_code = zone["prvCode"] + "-" + zone["cityCode"] + "-" + zone["deptCode"]
                voting = []
                voting.append(dashboard["ST"])
                voting.append(case)
                voting.append(area_data[city_code])
                voting.append(area_data[combined_code])
                for k in zone:
                    voting.append(str(zone[k]))
                output_file.write(",".join(voting) + "\n")
#upload_data(bucket_name=bucket_name, data=json.dumps(dashboard, indent=4, ensure_ascii=False), content_type='application/json; charset=utf-8', destination_blob_name=dest)
print(json.dumps(dashboard))
