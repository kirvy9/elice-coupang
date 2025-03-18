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

    #@pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
class TestMainPage2:
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

            main_page = MainPage(driver)
            main_page.click_by_LINK_TEXT('마이쿠팡')
 
            wait.until(EC.url_contains("mc.coupang.com"))
            assert "mc.coupang.com" in driver.current_url

        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지(로그인)-마이쿠팡-실패-노서치')
            assert False
        
        except TimeoutException as e:
            driver.save_screenshot('메인페이지(로그인)-마이쿠팡-실패-타임에러.jpg')
            assert False

