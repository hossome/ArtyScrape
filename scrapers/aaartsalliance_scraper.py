from selenium import webdriver
from selenium.webdriver.common.by import By


class Site1Scraper:

    # Start Selenium WebDriver
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.data = []

    def scrape(self):
        # Load the webpage (replace with the actual URL)
        self.driver.get("https://www.aaartsalliance.org/opportunities/")

        # Find all opportunity elements
        opportunities = self.driver.find_elements(By.CLASS_NAME, "opportunity")

        x = 1
        # Iterate through each opportunity and extract details
        for opp in opportunities:
            title = opp.find_element(By.TAG_NAME, "h2").text
            organization = opp.find_element(By.CLASS_NAME, "tiny-title").text.split("\n")[0]
            call_type = opp.find_elements(By.CLASS_NAME, "col-md-3")[0].text
            deadline = opp.find_elements(By.CLASS_NAME, "col-md-3")[1].text
            link = opp.find_element(By.TAG_NAME, "a").get_attribute("href")
            if call_type == "CALL FOR SUBMISSIONS":
                self.data.append([title, organization, call_type, deadline, link])
            '''
            
                print(f"Title: {title}")
                print(f"Organization: {organization}")
                print(f"Call Type: {call_type}")
                print(f"Deadline: {deadline}")
                print(f"Link: {link}")
                print("=" * 50)
                x = x + 1
        print(x)'''
        return self.data

    def close(self):
        # Close the browser
        self.driver.quit()
