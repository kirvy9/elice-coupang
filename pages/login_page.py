from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
import time



class LoginPage: 
  
  #user password and account info input function
  #coopang login page open
  #account input 찾기 -> xpath: //~~
  #password input ~~

  URL = "https://login.coupang.com/login/login.pang?"
  USER = ""
  PASSWORD = ""

  def __init__(self, driver: WebDriver):
     self.driver = driver  

  def open(self):
     self.driver.get(self.URL)

  def input_password_and_email(self, wait):
     user_box = wait.until(EC.presence_of_element_located((By.ID, 'login-email-input')))
     user_box.send_keys(self.USER)

        # 비밀번호 입력 필드 대기 후 입력
     password_box = wait.until(EC.presence_of_element_located((By.ID, 'login-password-input')))
     password_box.send_keys(self.PASSWORD)

  def click_login_button(self, wait):
     wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'login__button--submit')]"))).click()

  #user password and account info input function
  #coopang login page open
  #account input 찾기 -> xpath: //~~
  #password input ~~

  #def open():
    
  #def input_password_and_email():

  #def click_login_button():  