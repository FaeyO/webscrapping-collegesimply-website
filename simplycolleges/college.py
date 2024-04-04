from selenium import webdriver
#import undetected_chromedriver as uc
import time
import csv
#driver = uc.Chrome()

driver = webdriver.Chrome()

# Create a list to store the data
data_list = []

for x in range(1,3):
    driver.get(f"https://www.collegesimply.com/colleges/rank/colleges/lowest-graduation-rate/?page={x}")
    time.sleep(5)

    schools = driver.find_elements("xpath","//tr[@itemprop='itemListElement']")
    
    for school in schools:
        name = school.find_element("xpath", ".//h6[@class='card-title mb-1']/a").text
        location = school.find_element("xpath", ".//p[@class='card-text small text-muted']").text
        graduation_rate = school.find_element("xpath", ".//td[@class='text-right pr-0 font-weight-bold']").text
        link = school.find_element("xpath", ".//h6[@class='card-title mb-1']/a").get_attribute("href")

        driver.get(link)
        enrollment = driver.find_element("xpath", "(//div[@class='h2 mb-4'])[1]").text

        # Append the data to the list
        data_list.append([name, location, graduation_rate, link, enrollment])
        print(name,location,graduation_rate,link,enrollment)

        driver.back()

driver.quit()    
        #driver.forward()

# Write the data to a CSV file
with open("colleges_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Location", "Graduation Rate", "Link", "Enrollment"])
    writer.writerows(data_list)

   