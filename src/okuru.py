import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_extension('/vagrant/src/LINE.crx')
options.add_argument('--user-data-dir=/home/vagrant/.config/google-chrome/Default')
driver = webdriver.Chrome('/home/vagrant/lib/chromedriver', options=options) 
driver.get('chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html')
time.sleep(4)
id_str = "@gmail.com"
password_str = ""
element = driver.find_element("xpath","/html/body/div[3]/div/div/section/div[1]/div[1]/div[1]/input")
element.clear()
element.send_keys(id_str)
element = driver.find_element("xpath","/html/body/div[3]/div/div/section/div[1]/div[1]/div[2]/input")
element.clear()
element.send_keys(password_str)

# ログインボタン
driver.find_element("xpath","/html/body/div[3]/div/div/section/div[3]/button").click()

time.sleep(4)

element = driver.find_element("xpath","/html/body/div[3]/div/div/section/h1")
if element.text == "Verify your identity":
    print("二段階認証をログインしてください。入力完了後、何らかのキーを入力してください")
    input()

customer_lists = requests.get("https://lcpc04ynec.execute-api.us-west-2.amazonaws.com/dev/get_customer_list?status=init").json()


for list in customer_lists["data"]:

    # 友だち追加ページ遷移
    driver.find_element("xpath","/html/body/div[4]/div/div[5]/div[1]/div[10]/ul/li[4]/button").click()
    time.sleep(4)

    # 友だち検索
    element = driver.find_element("xpath","/html/body/div[4]/div/div[5]/div[1]/div[6]/div[1]/div/input")
    element.send_keys(list["id"])
    time.sleep(4)
    element.send_keys(Keys.ENTER)
    time.sleep(4)

    # 友だち追加後の一覧ページでの識別用（名称は名前がずれるため一意にならない）に、URLを取得しておく。
    # path = driver.find_element("xpath","/html/body/div[4]/div/div[5]/div[1]/div[6]/div[2]/div/div[1]/img")
    user_title = driver.execute_script('return document.querySelector("#recommend_search_result_view h2")').text
    # 友だち追加ボタン押下
    element = driver.find_element("xpath","/html/body/div[4]/div/div[5]/div[1]/div[6]/div[2]/div/div[2]/button[2]")
    element.click()
    time.sleep(4)

    # メッセージ送信ページ
    driver.find_element("xpath","/html/body/div[4]/div/div[5]/div[1]/div[10]/ul/li[1]/button").click()
    time.sleep(4)

    users = driver.find_elements("xpath", '/html/body/div[4]/div/div[5]/div[1]/div[3]/div[2]/ul/li')
    for user in users:
        if user_title == user.get_attribute("title"):
            user.click()
            time.sleep(4)
            driver.execute_script('document.getElementById("_chat_room_input").innerText = "a"')
            element = driver.find_element("xpath", '/html/body/div[4]/div/div[5]/div[2]/div[1]/div[1]/div[5]/div[3]/div/div[2]/div')
            element.send_keys(Keys.ENTER)
            break
    result = requests.post("https://lcpc04ynec.execute-api.us-west-2.amazonaws.com/dev/update_customer_list", json.dumps({"customer_id": list["customer_id"]}))
driver.quit()
