import time

from selenium import webdriver
from selenium.webdriver.common.by import By


complex_urls = (
    'https://www.domkor-dom.com/prodazha-kvartir-Novostroiki/kvartira-Naberezhnye-Chelny/zhk-romantiki-22-11',
    'https://www.domkor-dom.com/prodazha-kvartir-Novostroiki/kvartira-Naberezhnye-Chelny/kvartiry-novostroiki-chelny-20-14',
    'https://www.domkor-dom.com/prodazha-kvartir-Novostroiki/kvartira-Naberezhnye-Chelny/prodazha-kvartir-20-12-druzhnyi'
)

driver = webdriver.Chrome()

#def visit_houses():
#    wrap_div = driver.find_element('class name', 'wrap1050')
#    tables = wrap_div.find_elements('tag name', 'table')
#
#    for table in tables:
#        tds = table.find_elements('tag name', 'td')
#        
#        for td in tds:
#            #current_url = driver.current_url
#            a = td.find_element('tag name', 'a')
#            #div = td.find_elements('tag name', 'div')[1]
#            #img = td.find_element('tag name', 'img')
#            a.click()
#            time.sleep(1)
#            
#            driver.back()
#            time.sleep(1)

def close_popup():
        try:
            close_annoying_popup = driver.find_element(By.XPATH, "//a[@class='white-saas-generator-close-button']")
            close_annoying_popup.click()
        except:
            pass

def parse_apartment_as_html(html: str) -> list[str]:
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

def parse_residential_complex(complex_url: str) -> list[str]:
    driver.get(complex_url)
    time.sleep(2)
    close_popup()

    apartments = []
    divs = driver.find_elements(By.XPATH, "//div[contains(@id, 'kvartira')]/following-sibling::div[@class='sh']")
    for div in divs:
        apartment_html = div.get_attribute('innerHTML')
        apartments.append(parse_apartment_as_html(apartment_html))

    return apartments

def save_complexes_to_excel(columns: list[str], complexes: dict[str, list[str]]) -> None:
    from openpyxl import Workbook

    wb = Workbook()

    for name, apartments in complexes.items():
        ws = wb.create_sheet(name)
        ws.append(columns)
        for apartment in apartments:
            ws.append(apartment)

    wb.save("complexes.xlsx")

def main():
    fields = ("Квартира №", "Комнаты", "Площадь", "Цена")
    complexes = {}

    try:
        for url in complex_urls:
            apartments = parse_residential_complex(url)
            name = url.split('/')[-1]
            complexes[name] = apartments

        save_complexes_to_excel(fields, complexes)
    
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
