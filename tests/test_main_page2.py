# tests/test_main_page2.py
import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver # noqa
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests.pages.login_page import LoginPage

from urllib import parse


class TestMainPage2:
    #@pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_open_main_page(self, driver: WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()

            time.sleep(2)

            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("https://login.coupang.com")) #URL 검증
            assert "login" in driver.current_url #검증 

            login_page.input_password_and_email(wait)
            login_page.click_login_button(wait)

            wait.until(EC.url_contains("https://coupang.com")) #URL 검증

            time.sleep(10)

            element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, 'mc.coupang.com')]"))).click()
            main_page = MainPage(driver)
            #main_page.click_by_LINK_TEXT('마이쿠팡')

            #time.sleep(5)

            wait.until(EC.url_contains("mc.coupang.com"))
            assert "mc.coupang.com" in driver.current_url

        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지(로그인)-마이쿠팡-실패-노서치')
            assert False
        
        except TimeoutException as e:
            driver.save_screenshot('메인페이지(로그인)-마이쿠팡-실패-타임에러.jpg')
            assert False

    #상품 검색 
    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_search_items(self, driver: WebDriver):
   
        try:
            login_page = LoginPage(driver)
            login_page.open()

            time.sleep(2)

            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("https://login.coupang.com")) #URL 검증
            assert "login" in driver.current_url #검증 

            login_page.input_password_and_email(wait)
            login_page.click_login_button(wait)

            wait.until(EC.url_contains("https://coupang.com")) #URL 검증

            time.sleep(10)

            ITEMS_XPATH = "//form//ul/li"

            time.sleep(2)

            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증 
        
            time.sleep(2) #2초 왜? 봇인거 안들키기 위해서 
        
            main_page = MainPage(driver)
            main_page.search_items('노트북')

            ws(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ITEMS_XPATH))
            )

            items = driver.find_elements(By.XPATH, ITEMS_XPATH)
            item_name = parse.quote('노트북')

            assert len(items) > 0
            assert item_name in driver.current_url
            
            driver.save_screenshot('메인페이지-검색-성공.jpg')
        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지-검색-실패-노서치.jpg')
            assert False

        except TimeoutException as e:
            driver.save_screenshot('메인페이지-검색-실패-타임에러.jpg')
            assert False
    