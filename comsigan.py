from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup as bs
import time

class comsigan():
    def get():
        output_list = []
        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)
        driver.get('http://comci.net:4082/st')
        time.sleep(0.5)
        search = driver.find_element(By.ID,"sc")
        search.click()
        search.send_keys("창일중학교")
        driver.find_element(By.CSS_SELECTOR,"#학교찾기 > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=button]:nth-child(2)").click()
        time.sleep(0.3)
        driver.find_element(By.CSS_SELECTOR,"#학교명단검색 > tbody > tr:nth-child(2) > td:nth-child(2) > a").click()
        time.sleep(0.3)
        Select(driver.find_element(By.ID,"ba")).select_by_value("3-8")

        table = driver.find_element(By.CSS_SELECTOR,"#hour > table")
        th = table.get_attribute("outerHTML")
        t_soup = bs(th,'html.parser')
        lines = t_soup.find_all('td')

        output_list.append(lines[1].text+'\n')
        l1=[]
        for a in lines[3:9]:
            l1.append(a.text)
        output_list.append('  '.join(l1))
        output_list.append('\n   ')


        for b in range(int((len(lines)-9)//6)-1):
            l2=[]
            for c in range(9+6*b,9+6*b+6):
                if len(lines[c].text)==4:
                    l2.append(lines[c].text[:2]+'  |  ')
                elif len(lines[c].text)==5:
                    l2.append(lines[c].text[:3]+'  | ')
                elif len(lines[c].text)==0:
                    l2.append('     '+'    ')
                else:
                    l2.append(lines[c].text[:1]+'  |  ')
            output_list.append(''.join(l2))
            output_list.append('\n   ')
            
        return('\n'.join(output_list))
        driver.close()


