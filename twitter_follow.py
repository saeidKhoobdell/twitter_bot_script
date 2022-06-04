from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def cookies_catcher():
  driver = webdriver.Chrome()
  driver.get('https://twitter.com/i/flow/login')
  sleep(10)
  username_input_path = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
  username=driver.find_element(By.XPATH ,username_input_path)
  username.clear()
  username.send_keys('username')
  next_btn = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
  next_btn.click()
  sleep(5)
  secure_input_path ='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
  secure_input =driver.find_element(By.XPATH,secure_input_path)
  secure_input.send_keys('username')
  next2_btn_path='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div'
  next2_btn = driver.find_element(By.XPATH,next2_btn_path)
  next2_btn.click()
  sleep(2)
  password_input_path ='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
  password =driver.find_element(By.XPATH,password_input_path)

  password.send_keys('password')
  sleep(2)
  login_btn_path ='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
  login = driver.find_element(By.XPATH,login_btn_path)
  login.click()
  sleep(10)
  # part2
  search_input_path='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'
  search_user = driver.find_element(By.XPATH,search_input_path)

  search_user.send_keys('sara')
  search_user.send_keys(Keys.RETURN)
  sleep(10)
  view_all_path ='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[6]/div/div/a/div/span'
  view_all = driver.find_element(By.XPATH, view_all_path)
  view_all.click()
  sleep(10)
  for i in range(1,200):
   follow_btn_path='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[{}]/div/div/div/div/div[2]/div[1]/div[2]/div/div/span/span'.format(i)
   follow = driver.find_element(By.XPATH, follow_btn_path)
   follow.click()
   sleep(5)
  sleep(50)
  driver.close()

def follow():

  driver = webdriver.Chrome()
  driver.get('https://twitter.com/home')
  sleep(10)
  header_path='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/a/div[4]/div'
  header=driver.find_element(By.XPATH,header_path)
  header.click()
  sleep(20)
  driver.close()
