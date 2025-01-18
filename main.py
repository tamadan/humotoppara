#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import content
import parseResponseJson
import clickRunner
import time

def getCampStock(targetSite, targetDates):
    while True:
        response = requests.get(content.searchURL, headers=content.headers)
        if response.status_code == 200:
            siteInfoList = parseResponseJson.parse(response)
            targetSiteInfo = [
                site for site in siteInfoList[targetSite.siteName]
                if site["calDate"] in targetDates and site["remainCount"] > 0
            ]
            if len(targetSiteInfo) > 0:
                success = clickRunner.secureCampSite(targetSite, targetSiteInfo[0]["calDate"])
                if success:
                    print(f"予約枠を確保しました {targetSiteInfo[0]['calDate']} 20分後有効")
                    # 予約に必要な情報を記入する時間を20分確保
                    time.sleep(20 * 60)
                    break
                else:
                    print("予約枠の要素が見つかりませんでした")
                    break
            else:
                print("空きなし 1分後に再検索")
                time.sleep(60)
        else:
            print(f"Failed with status code: {response.status_code}")
            break

getCampStock(content.SITE_GROUP.suizanso, ["2025-01-20", "2025-01-24", "2025-01-26"])
