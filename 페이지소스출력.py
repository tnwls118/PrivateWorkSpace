from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pandas as pd


# chrome 경로 설정
chrome_path = r"C:\Users\82109\Desktop\frontspace\privateworkspace\chromedriver.exe"

# 홈페이지 url 설정
url = "https://happycommunity.happyconnect.co.kr/CO000.do"
happyconnect = webdriver.Chrome(executable_path=chrome_path)
happyconnect.get(url)
happyconnect.maximize_window()

# 대기 시간 설정 (최대 10초)
wait = WebDriverWait(happyconnect, 10)

# Login 시도
user_id = "hc_csj"
user_pw = "2023tid^^"
login_id = happyconnect.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[2]/form/div[1]/dl[1]/dd/input")
login_id.send_keys(user_id)
login_pw = happyconnect.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[2]/form/div[1]/dl[2]/dd/input")
login_pw.send_keys(user_pw)

login_button = happyconnect.find_element(By.XPATH,
                                         "/html/body/div[1]/div/div[2]/form/div[1]/button")
login_button.click()

time.sleep(3)

data = []

try:
    start_time_task1 = time.time()
    print("페이지 소스 추출 작업 시작")
    page_source = happyconnect.page_source
    end_time_task1 = time.time()
    elapsed_time_task1 = end_time_task1 - start_time_task1
    print("페이지 소스 추출 작업 종료")
    print(f"소요시간:{elapsed_time_task1}초")
    data.append(page_source)

    start_time_task2 = time.time()
    print("엑셀 저장 작업 시작")
    excel_path = r"C:\Users\82109\Desktop\새 Microsoft Excel 워크시트.xlsx"
    excel = pd.DataFrame(data, columns=["content"])
    excel.to_excel(excel_path, index=True)
    end_time_task2 = time.time()
    elapsed_time_task2 = end_time_task2 - start_time_task1
    print("엑셀 저장 작업 종료")
    print(f"소요 시간: {elapsed_time_task2}초")
except Exception as e:
    print(f"에러내용:{e}")
finally:
    happyconnect.quit()
