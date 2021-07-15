class CRM_loggin:
    def loggin(self,username,pwd):
        ##CRM系系统打开url及登录
        from selenium import webdriver
        import time
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.driver = driver
        self.driver.get('http://localhost:8080/crm/')
        self.driver.find_element_by_name('userNum').send_keys(username)
        self.driver.find_element_by_name('userPw').send_keys(pwd)
        self.driver.find_element_by_id('in1').click()


    def change_frame1(self,framename,num):
        #跳转到指定frame
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name(framename)[num])


