
class my_autotest:
    def __init__(self, url):
        from selenium import webdriver
        import os
        import time

        # 启动tomcat
        # os.system(r'D:\testtools\apache-tomcat-9.0.45\apache-tomcat-9.0.45\bin\startup.bat')
        # time.sleep(30)
        # 定义初始化时geturl
        driver = webdriver.Chrome()
        self.driver = driver
        self.driver.get(url)
        self.driver.maximize_window()




    def loggin(self,xpath1,name,xpath2,pwd,loggin_button):
        import  time
        self.find_element('xpath',xpath1)
        self.element.clear()
        self.sendkeys(name)
        self.find_element('xpath',xpath2)
        self.element.clear()
        self.sendkeys(pwd)
        self.find_element('xpath',loggin_button)
        self.click()
        time.sleep(2)


    def find_element(self, findmethod1, findvalue1):
        from selenium import webdriver
        import time
        time.sleep(1)
        self.element=self.driver.find_element(findmethod1, findvalue1)

    def sendkeys(self,values):
        self.element.clear()
        self.element.send_keys(values)

    def click(self):
        self.element.click()

    def text(self):
        self.element.text()

    def get_text(self,name):
        self.element.get_attribute(name)

    def mytest_assert(self, runresult, exceptresult):
        if runresult == exceptresult:
            print('期望结果：', exceptresult)
            print('运行结果：', runresult, '>>>>比对一致，测试通过')
        elif runresult != exceptresult:
            print('期望结果：', exceptresult)
            print('运行结果：', runresult, '>>>>比对不一致，测试失败')
    def refrushpage(self):
        self.driver.refresh()
    def back(self):
        self.driver.back()
    def switch_to_alert_accept(self):
        self.driver.switch_to.alert.accept()

    def quit(self):
        self.driver.quit()
        import os
        # os.system(r'D:\testtools\apache-tomcat-9.0.45\apache-tomcat-9.0.45\bin\shutdown.bat')




