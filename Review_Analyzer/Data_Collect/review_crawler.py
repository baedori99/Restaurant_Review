from typing import List, Literal

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


class Review_Crawler:
    """네이버 리뷰 크롤링 하는 클래스
    """
    def __init__(self):
        self.driver = None

    def open_url(self, url):
        """크롬 창을 열고 url에 접속하는 함수

        Args:
            url (str): 네이버 리뷰 링크
        """
        # 크롬창 열기
        options = Options()
        self.driver = webdriver.Chrome(options = options)

        # 창모드 전체화면으로 크기 늘리기
        self.driver.maximize_window()

        # 로딩시간: 페이지 로딩
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))

        # 네이버 리뷰 주소 접속하기
        self.driver.get(url)

        # 로딩시간: 페이지 로딩
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
        
    def count_reviews(self):
        """더보기 버튼을 통해 구하고자 하는 리뷰 갯수의 총 갯수를 구하는 함수"""
        for _ in range(19):
            self.driver.find_element(By.CLASS_NAME, 'fvwqf').click()
            time.sleep(1.5)
        rows = self.driver.find_elements(By.CLASS_NAME, 'owAeM')

        # rows의 개수를 세어 for문을 돌린다.
        cnt = len(rows)
        print("총 리뷰 개수:", cnt)
        
        return rows, cnt
    
    def crawling_reviews(self, rows, cnt):
        """리뷰 데이터를 추출하는 함수"""
        # 데이터 받을 빈 딕셔너리
        review_data = {"UserID":[],"Review_Text":[],"Date":[], "NumberOfVisit":[]}
        
        # 리뷰 추출하기
        log_count = 0
        print("START", end = " >>> ")
        for i in range(cnt):
            # 리뷰 내용 더보기 버튼이 없는 리뷰들 예외구문
            try:
                rows[i].find_element(By.CLASS_NAME, 'Ky28p').click()
            except:
                pass
            user_id = rows[i].find_element(By.CLASS_NAME, 'qgLL3')
            review_text = rows[i].find_element(By.CLASS_NAME, 'zPfVt')
            number_visits = rows[i].find_elements(By.CLASS_NAME, 'CKUdu')[1]
            visit_date = rows[i].find_elements(By.CLASS_NAME, 'CKUdu')[0].find_elements(By.CLASS_NAME, 'place_blind')[1]
            
            review_data['UserID'].append(user_id.text)
            review_data['Review_Text'].append(review_text.text)
            review_data['Date'].append(visit_date.text)
            review_data['NumberOfVisit'].append(number_visits.text)
            
            # 로그 만들기
            log_count += 1
            if log_count > 0 and log_count % 20 == 0:
                print(log_count, end= " >>> ")
        print("End")
    
        return review_data
    
    
    def get_review(self, url):
        """메인 출력 함수"""
        # 크롬 창 열기
        print(f"크롬 창을 열고 있습니다.", end=" ")
        self.open_url(url)
        print()
        
        title = self.driver.find_element(By.CLASS_NAME, 'GHAhO').text

        # 총 리뷰 개수 구하기
        print("'{0}'의 리뷰를 가지고 오는 중입니다.".format(title))
        rows, cnt = self.count_reviews()
        
        # 딕셔너리 만들기
        review_data = self.crawling_reviews(rows,cnt)
        
        # 데이터프레임 만들기
        print("데이터프레임으로 변환 중입니다.",end=" ")
        df_reviews = pd.DataFrame(review_data)
        print("... 완료!")
        
        # .csv파일로 저장
        df_reviews.to_csv("./test.csv", index=False, encoding="utf-8")
        
        self.driver.quit()
        
        return df_reviews
    
crawler = Review_Crawler()
url = "https://pcmap.place.naver.com/restaurant/13166754/review/visitor"
crawler.get_review(url)