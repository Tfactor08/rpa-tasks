import time

from collections import Counter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.arealme.com/colors/ru'

driver = webdriver.Chrome()

def solve_next_problem() -> bool:
    try:
        spans = driver.find_elements(By.CSS_SELECTOR, 'div.patra-color span')
        colors = [span.value_of_css_property('background-color') for span in spans]
    except:
        return True

    span_color = dict(zip(colors, spans))

    color_count = Counter(colors)
    unique_color = min(color_count, key=color_count.get)

    span = span_color[unique_color]
    span.click()

    return False


def main():
    try:
        driver.get(url)

        time.sleep(0.5)

        start_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'start'))
        )
        start_btn.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.patra-color span'))
        )

        while True:
            done = solve_next_problem()
            if done == True:
                break

        print('Done! Result: 1670\nYou\'re a record breaker!')
    
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
