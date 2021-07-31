from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

myname = 'Hansen'
myemail = 'ignhansen28@gmail.com'
myphone = '081296766540'
mymessage = 'inet saya lag'
mycomplain = 'saya pelanggan dengan id 1100000115340 minta tolong internet saya direfresh, terima kasih'


driver = webdriver.Chrome()
driver.get("https://www.biznethome.net/")

chatboxbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/div[17]')))
chatboxbtn.click()

sleep(5)

iframe = driver.find_element_by_xpath('//*[@id="siqiframe"]')
driver.switch_to.frame(iframe)

name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="visname"]')))
name.send_keys(myname)

email = driver.find_element_by_xpath('//*[@id="visemail"]')
email.send_keys(myemail)

phone_number = driver.find_element_by_xpath('//*[@id="visphone"]')
phone_number.send_keys(myphone)

choosedepartment = driver.find_element_by_xpath('//*[@id="sqico-drpdwn"]')
choosedepartment.click()

sleep(3)

choose = driver.find_element_by_xpath('//*[@id="dropcontent"]/li[2]')
choose.click()

message = driver.find_element_by_xpath('//*[@id="msgarea"]')
message.send_keys(mycomplain)

send_chat = driver.find_element_by_xpath('//*[@id="sqico-send"]')
send_chat.click()


