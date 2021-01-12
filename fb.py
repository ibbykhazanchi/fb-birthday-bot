class fb_birthday:

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def getBirthdays(self):
        
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        import time
        from selenium.webdriver.common.keys import Keys

        #options set up
        options = Options()
        options.add_argument("--disable-infobars")
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        options.add_argument("--headless")

        #open fb
        driver = webdriver.Chrome(options= options)
        driver.get("http://facebook.com")
        driver.maximize_window()

        #login
        login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
        login.send_keys("{}".format(self.username))
        password = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/input')
        password.send_keys("{}".format(self.password))
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

        #open birthdays
        search = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/label/input')
        search.click()
        search = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/label/input')
        search.send_keys("birthdays")
        search.send_keys(Keys.RETURN)

        #get the bdays
        time.sleep(15)
        bdays = driver.find_elements_by_xpath('//h3[contains(@class, "gmql0nx0") and contains(@class, "l94mrbxd") and contains(@class, "p1ri9a11") and contains(@class, "lzcic4wl") and contains(@class, "d2edcug0") and contains(@class, "hpfvmrgz")]')
        bdays2 = [elem for elem in bdays if elem.text != ""]
        result =[]
        for bday in bdays2:
            result.append(bday.text)
        return result

        

        
