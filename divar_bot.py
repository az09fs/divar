from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import requests

#login
search = input('what you want?\n')
city = input(f'which city? (type in english):\n')
phone_number = input('please enter your phone number: +98')
message = input('what you want to ask?\n')
page = input('how many divar pages you want to ask the price?\n')
page = int(page)+1
driver = webdriver.Chrome()
driver.get('https://www.divar.ir/')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/nav/div[2]/div[2]/i').click()
driver.find_element_by_xpath('//*[@id="app"]/div[1]/nav/div[2]/div[2]/div[2]/a[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div/div/div/div/div[1]/input').send_keys(phone_number)
time.sleep(1)
code = input('please enter the code that site sent you: ------:\n')
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div[2]/div[1]/div/div/div/input').send_keys(code)
# login end

# finding cases that their chat is enable
l1=[]
l2=[]
l3=[]
for i in range (1,page):
    i = str(i)
    r = requests.get(f'https://divar.ir/s/'+city+'?q='+search+'&page='+i)
    link = re.findall(r'(/v/.*?)\"',r.text)

    for j in range(0,len(link)):
        l1.append('http://divar.ir'+link[j])

for k in range(0,len(l1)):
    driver.get(f'{l1[k]}')
    try:
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div[2]/button[2]').click()
        assert driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div[2]/p').text == "توافقی"
        try:
            driver.find_element_by_xpath('/html/body/div[6]/div/article/footer/button').click()
        except:
            pass
        l2.append(l1[k])
    except:
        pass    
        
for l in range(0,len(l2)):
    q = l2[l].split('/')
    q1 = q[0]+'//'+'chat'+'.'+q[2]+'/'+'conversation'+'/'+q[-1]
    l3.append(q1)

# finding end

# price asking
for m in range(0,len(l3)):
    driver.get(f'{l3[m]}')
    time.sleep(10)
    try:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[3]/div/div[3]/div[2]/div/textarea').send_keys(message)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[3]/div/div[3]/div[2]/div/img').click()
        time.sleep(2)
    except:
        pass