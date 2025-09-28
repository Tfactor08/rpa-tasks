import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#url = 'https://www.domkor-dom.com/prodazha-kvartir-Novostroiki/kvartira-Naberezhnye-Chelny/'

url = 'https://www.domkor-dom.com/prodazha-kvartir-Novostroiki/kvartira-Naberezhnye-Chelny/zhk-romantiki-22-11'
rounds = 10

def visit_houses():
    wrap_div = driver.find_element('class name', 'wrap1050')
    tables = wrap_div.find_elements('tag name', 'table')

    for table in tables:
        tds = table.find_elements('tag name', 'td')
        
        for td in tds:
            #current_url = driver.current_url
            a = td.find_element('tag name', 'a')
            #div = td.find_elements('tag name', 'div')[1]
            #img = td.find_element('tag name', 'img')
            a.click()
            time.sleep(1)
            
            driver.back()
            time.sleep(1)


def close_popup():
        try:
            annoying_popup = driver.find_element(By.XPATH, "//a[@class='white-saas-generator-close-button']")
            annoying_popup.click()
        except:
            pass

def parse_appartment_as_html(html: str) -> list[str]:
    import re

    pattern_common = r'<br>\s*([^<\s\n][^<\n]*?)\s*(?=<br>|$)'
    results_common = re.findall(pattern_common, html)

    pattern_price  = r'<font[^>]*>(.*?)</font>'
    results_pirce = re.findall(pattern_price, html)

    pattern_no = r'№\s*(\d+)'
    results_no = re.findall(pattern_no, html)

    rooms = re.sub(r'\D', '', results_common[0])
    no = results_no[0]
    price = results_pirce[1]
    area = results_common[2]

    data = [no, rooms, area, price]

    return data

def main():
    appartments = []

    try:
        driver = webdriver.Chrome()
        driver.get(url)

        time.sleep(2)

        close_popup()

        divs = driver.find_elements(By.XPATH, "//div[contains(@id, 'kvartira')]/following-sibling::div[@class='sh']")
        for appartment in divs:
            appartment_html = appartment.get_attribute('innerHTML')
            appartments.append(parse_appartment_as_html(appartment_html))
    
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
