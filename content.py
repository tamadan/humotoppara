import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Site:
    siteGroupCd: str
    stayDiv: str
    siteName: str

class SiteGroup:
    def __init__(self, campDay: Site, campStay: Site, cottageKashiwa: Site, suizanso: Site, kenashisan: Site, kanayamaCabin: Site, korokke: Site):
        self.campDay = campDay
        self.campStay = campStay
        self.cottageKashiwa = cottageKashiwa
        self.suizanso = suizanso
        self.kenashisan = kenashisan
        self.kanayamaCabin = kanayamaCabin
        self.korokke = korokke

SITE_GROUP = SiteGroup(
    campDay=Site(
        siteGroupCd="01",
        stayDiv="DAY",
        siteName="キャンプ日帰り"
    ),
    campStay=Site(
        siteGroupCd="01",
        stayDiv="STAY",
        siteName="キャンプ宿泊"
    ),
    cottageKashiwa=Site(
        siteGroupCd="02",
        stayDiv="STAY",
        siteName="コテージ柏"
    ),
    suizanso=Site(
        siteGroupCd="03",
        stayDiv="STAY",
        siteName="翠山荘"
    ),
    kenashisan=Site(
        siteGroupCd="04",
        stayDiv="STAY",
        siteName="毛無山荘"
    ),
    kanayamaCabin=Site(
        siteGroupCd="05",
        stayDiv="STAY",
        siteName="金山キャビン"
    ),
    korokke=Site(
        siteGroupCd="07",
        stayDiv="STAY",
        siteName="コロッケ"
    )
)

searchURL = "https://reserve.fumotoppara.net/api/shared/reserve/calendars"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
    "Cookie": "i18n_redirected=ja; auth.strategy=local",
    "If-None-Match": 'W/"255a0-gsrz7QvAQDcS5biEJtQb5QsFIvc"',
    "Referer": "https://reserve.fumotoppara.net/reserved/reserved-calendar-list",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "X-Api-Key": "51ff85fe-ca21-4a42-f8cc-cf5f34b964e5"
}

reserveURL = "https://reserve.fumotoppara.net/reserved/reserved-date-selection"

loginEmail = os.getenv("LOGIN_EMAIL")
loginPassword = os.getenv("LOGIN_PASSWORD")
