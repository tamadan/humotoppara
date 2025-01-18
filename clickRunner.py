# -*- coding: utf-8 -*-
# browser_auto_foods.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime 
import content
import time

def days_difference_from_first_of_month(dateStr):
    # dateStrを日付オブジェクトに変換
    target_date = datetime.strptime(dateStr, '%Y-%m-%d')
    # 現在時刻の月初を取得
    now = datetime.now()
    first_of_current_month = datetime(now.year, now.month, 1)
    # 日数の差を計算
    difference = (target_date - first_of_current_month).days
    return difference

def secureCampSite(targetSite, dateStr):
    days_diff = days_difference_from_first_of_month(dateStr)

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--lang=ja")   
    # ChromeDriverを使用してWebDriverのインスタンスを作成
    chrome = webdriver.Chrome(options=options)

    # 予約サイトを開く
    chrome.get(content.reserveURL)
    try:
        # 注意事項のモーダルを閉じる
        closeButton = WebDriverWait(chrome, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.el-dialog__close.el-icon.el-icon-close'))
        )
        closeButton.click()
        # ログイン
        loginSection = WebDriverWait(chrome, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'login-area'))
        )

        # input要素を探して値を入力
        inputs = loginSection.find_elements(By.TAG_NAME, 'input')
        inputs[0].send_keys(content.loginEmail)
        inputs[1].send_keys(content.loginPassword)

        # ログインボタンを探してクリック
        loginButton = loginSection.find_element(By.CSS_SELECTOR, 'button.el-button.el-button--primary')
        loginButton.click()

        # ログイン処理待ち
        time.sleep(5)

        # カレンダーのテーブルを探して取得
        calendarTable = WebDriverWait(chrome, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'calendar-table'))
        )
        # サイト名を探して取得
        target_tr = next(
            (tr for tr in calendarTable.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
             if tr.find_element(By.TAG_NAME, 'th').find_element(By.TAG_NAME, 'p').text == targetSite.siteName),
            None
        )
        if target_tr:
            # 日付を探して取得
            targetDay = target_tr.find_elements(By.TAG_NAME, 'td')[days_diff]
            targetDay.click()
            return True
        else:
            print("指定されたサイトが見つかりませんでした")
            return False
    except Exception as e:
        print("要素が見つかりませんでした:", e)
        return False
