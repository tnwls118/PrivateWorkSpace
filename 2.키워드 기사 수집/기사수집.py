import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome 경로 설정
chrome_path = r"C:\Users\82109\Desktop\frontspace\privateworkspace\chromedriver.exe"
google_driver = webdriver.Chrome(executable_path=chrome_path)

# google 열기
google_driver.get("https://www.google.com/?&hl=ko")
google_driver.maximize_window()

# google 기사 추출 작업
i = 1
try:
    while True:
        print("추출 기사 키워드 입력(프로그램 종료 시 exit 입력) : ")
        # Google 검색창의 이름은 "q"입니다.
        search_box = google_driver.find_element(By.NAME, "q")
        search_box.clear()
        user_input = input()
        if user_input.lower() == "exit":
            break
        search_box.send_keys(user_input)
        search_box.submit()
        print("검색을 시작합니다.")

        # 검색 결과가 나타날 때까지 대기
        time.sleep(5)

        # 검색 결과를 DataFrame에 저장
        articles = []
        search_results = google_driver.find_elements(By.CSS_SELECTOR, "div.g")
        for result in search_results:
            title = result.find_element(By.CSS_SELECTOR, "h3").text
            link = result.find_element(
                By.CSS_SELECTOR, "a").get_attribute("href")
            articles.append({"Title": title, "Link": link})

        df = pd.DataFrame(articles)
        df.to_excel("articles" + str(i) + ".xlsx", index=False)
        print(f"기사가 articles{i}.xlsx 파일에 저장되었습니다.")
        i += 1

except Exception as e:
    print(f"에러내용: {e}")

finally:
    print("프로그램을 종료합니다.")
    google_driver.quit()
