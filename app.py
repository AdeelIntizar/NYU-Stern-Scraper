from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
import csv

def get_expert_profiles(url,list):
    driver.get(url)
    people = driver.find_elements(By.CSS_SELECTOR, '.table-style-notables .prose')
    time.sleep(10)

    for index, person in enumerate(people):
        try:
            name = person.find_element(By.TAG_NAME, 'strong').text
        except:
            name=""
        try:
            image = person.find_element(By.TAG_NAME, 'img').get_attribute('src')
        except:
            image=""
        try:
            email_element = person.find_elements(By.CSS_SELECTOR, 'a[href^="mailto:"]')
            email = email_element[0].text if email_element else ""
        except:
            email=""
        try:
            website_element = person.find_elements(By.TAG_NAME, 'a')
            website = website_element[0].get_attribute('href') if website_element else ""
        except:
            website=""
        try:
            description = person.find_element(By.CSS_SELECTOR, 'em').text 
        except:
            description=""

        row = [name,description, email,website, image,list]
        file_name = 'experts_data.csv'
        save_location = 'D:/'
        csv_file_path = os.path.join(save_location, file_name)
        file_exists = os.path.isfile(csv_file_path)
        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name', 'Description', 'Email', 'Website Link', 'Image','People type'])
            writer.writerow(row)
    return

if __name__=="__main__":
    driver_path ="D:\\Customer_support\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path))
    main_url="https://www.stern.nyu.edu/experience-stern/about/departments-centers-initiatives/academic-departments/economics/people/"
    people_list=['faculty','affiliated-faculty','emeriti-faculty','adjunct-faculty','visiting-scholars-0','memoriam']
    for list in people_list:
        url=main_url+list
        get_expert_profiles(url,list)
        time.sleep(10)

     