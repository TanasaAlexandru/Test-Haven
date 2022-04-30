
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By



os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://politrip.com")
driver.maximize_window()
my_element=driver.find_element(By.ID,'cookiescript_accept')
my_element.click()
driver.implicitly_wait(5)



element_sing_up= driver.find_element(By.ID,'qa_header-signup').click()
first_name_sing=driver.find_element(By.ID,'first-name').send_keys('Tanasa')
name_sing=driver.find_element(By.ID,'last-name').send_keys('Alex')
sing_email= driver.find_element(By.ID,'email').send_keys('testare.HavenS@gmail.com')
pas1_sing=driver.find_element(By.ID,'sign-up-password-input').send_keys('Andrei9!')
pas2_sing=driver.find_element(By.ID,'sign-up-confirm-password-input').send_keys('Andrei9!')
driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
time.sleep(3)
sing_click=driver.find_element(By.XPATH,'//*[@id=" qa_loader-button"]/span').click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, window.scrollY + 150)")
time.sleep(3)
content_clicK=driver.find_element(By.ID,'qa_signup-participant').click()





my_secound_element=driver.find_element(By.ID,'qa_header-login')
my_secound_element.click()
my_element_login = driver.find_element(By.ID,'login-email-input').send_keys('testare.HavenS@gmail.com')
my_element_pass=driver.find_element(By.ID,'login-password-input').send_keys('Andrei9!')
log_in_button=driver.find_element(By.XPATH,'//*[@id=" qa_loader-button"]/span').click()
mes_button=driver.find_element(By.XPATH,'//*[@id="qa_header-chat"]/span[2]').click()
