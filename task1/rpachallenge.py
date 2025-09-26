from selenium import webdriver
from selenium.webdriver.common.by import By

from extract_input import extract_fields, extract_records


url = "https://www.rpachallenge.com"
rounds = 10

def main():
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        fields = extract_fields()
        records = extract_records(fields)
        
        start_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]")
        submit_btn = driver.find_element(By.XPATH, "//input[@value='Submit']")

        start_btn.click()

        for i in range(rounds):
            record = records[i]
            for field in fields:
                query = "//label[contains(text(), '%s')]/../input" % field
                curr_input = driver.find_element(By.XPATH, query)
                curr_input.send_keys(record[field])
            submit_btn.click()

        driver.save_screenshot("result.png")
    
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
