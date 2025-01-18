#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from content import SITE_GROUP

def get_site_name_by_cd_and_div(siteGroupCd: str, stayDiv: str) -> str:
    for site in vars(SITE_GROUP).values():
        if site.siteGroupCd == siteGroupCd and site.stayDiv == stayDiv:
            return site.siteName
    return "Unknown Site"

def parse(result):
    data = json.loads(result.text)
    
    # 空いている日付
    available_dates = {}
    
    # 各サイトの空き状況を確認
    for site_date in data["calendarsSiteDateList"]:
        site_name = get_site_name_by_cd_and_div(site_date["siteGroupCd"], site_date["stayDiv"])
        if site_name not in available_dates:
            available_dates[site_name] = []
        
        available_dates[site_name].append({
            "calDate": site_date["calDate"],
            "remainCount": site_date["remainCount"],
            "stayDiv": site_date["stayDiv"],
            "siteGroupId": site_date["siteGroupId"],
            "siteId": site_date["siteId"]
        })
    
    return available_dates