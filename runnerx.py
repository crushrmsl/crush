from HTMLTestRunner import HTMLTestRunner  #导入 # HTMLTestRunner用来生成HTML格式的测试报告
from crmTestSuite2.public.crmlogin import CRM_loggin
from crmTestSuite2.public.crmdatabase import CRM_database
from selenium.webdriver.support.select import Select
from crmTestSuite2.public import sendmail as SENDMAIL
from crmTestSuite2.public import createdata as CR
import unittest
import time
import os


class CRM_addEmployee(unittest.TestCase,CRM_loggin):    #工作列表——添加员工
    '''该测试针对crm系统的添加员工模块测试，对比页面添加内容与数据库新增的内容，验证页面添加员工的的合理性与完整性'''
    def test_select_department(self): #测试部门下拉框选项与数据库是否一致
        self.loggin('admin','123456')
        self.change_frame1('frame', 1)  # 跳转到工作列表frame
        self.driver.find_element_by_xpath('//*[@id="imgmenu4"]/table/tbody/tr/td[2]').click()  # 点击管理员按钮
        self.driver.find_element_by_xpath('//*[@id="submenu4"]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/span/a').click()  # 点击添加员工按钮
        self.change_frame1('frame', 2)  # 跳转到中部frame
        menu_table = self.driver.find_element("xpath", '/html/body/form/table[1]/tbody/tr[6]/td[2]/select')
        department_numbers = len(menu_table.find_elements_by_tag_name('option'))  # 获取option标签的数量
        db = CRM_database()
        dbres_num = db.excute('select count(department_name) from department_info', 2)
        print(department_numbers)
        print(dbres_num[0][0])
        if department_numbers==dbres_num[0][0]:
            print('部门选项与数据库数量一致！测试通过')
        else:
            print('部门选项与数据库数量不一致！测试失败')
    def test_select_role(self): #测试角色下拉框选项与数据库是否一致
        self.loggin('admin','123456')
        self.change_frame1('frame', 1)  # 跳转到工作列表frame
        self.driver.find_element_by_xpath('//*[@id="imgmenu4"]/table/tbody/tr/td[2]').click()  # 点击管理员按钮
        self.driver.find_element_by_xpath(
            '//*[@id="submenu4"]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/span/a').click()  # 点击添加员工按钮
        self.change_frame1('frame', 2)  # 跳转到中部frame
        time.sleep(1)
        menu_table = self.driver.find_element("xpath", '/html/body/form/table[1]/tbody/tr[6]/td[4]/select')
        department_numbers = len(menu_table.find_elements_by_tag_name('option'))  # 获取option标签的数量
        db = CRM_database()
        dbres_num = db.excute('select count(role_name) from user_role', 2)
        if department_numbers==dbres_num[0][0]:
            print('角色选项与数据库数量一致！测试通过')
        else:
            print('角色选项与数据库数量不一致！测试失败')

    def addEmployee_mudle(self,line_num):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>testbegin')
        self.loggin('admin','123456')
        self.change_frame1('frame',1)#跳转到工作列表frame
        self.driver.find_element_by_xpath('//*[@id="imgmenu4"]/table/tbody/tr/td[2]').click()  #点击管理员按钮
        self.driver.find_element_by_xpath('//*[@id="submenu4"]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/span/a').click()  # 点击添加员工按钮
        self.change_frame1('frame',2) # 跳转到中部frame
        time.sleep(1)
        with open(r'crmTestSuite2/Data/adddata.txt', 'r', encoding='utf-8') as file_data:
            lines_0 = file_data.readlines()
            lines=lines_0[line_num].split(',')
            print(lines)
        if lines[0]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[0]!='name':  #必填项name
                send_name=lines[0]
            else:
                send_name = CR.name()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td[2]/input').send_keys(send_name)

        if lines[1]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[1]!='age': #必填项age
                send_age=lines[1]
            else:
                send_age = CR.age()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[3]/td[2]/input').send_keys(send_age)

        if lines[2]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[2]!='gender':
                send_gender=lines[2]
            else:
                send_gender = CR.gender()
            Select(self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[4]/td[2]/select')).select_by_visible_text(send_gender)
        if lines[3]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[3]!='edu':
                send_edu=lines[3]
            else:
                send_edu = CR.edu()
            Select(self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[5]/td[2]/select')).select_by_visible_text(send_edu)
        if lines[4]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[4]!='department':
                send_depart=lines[4]
            else:
                send_depart= CR.department()
            Select(self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[6]/td[2]/select')).select_by_visible_text(send_depart)
        if lines[5]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[5]!='landline':
                send_landline=lines[5]
            else:
                send_landline = CR.landline()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[7]/td[2]/input').send_keys(send_landline)
        if lines[6]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[6]!='bandcard':
                send_bandcard=lines[6]
            else:
                send_bandcard = CR.bank_card_number()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[8]/td[2]/input').send_keys(send_bandcard)
        if lines[7]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[7]!='idcard':
                send_idcard=lines[7]
            else:
                send_idcard = CR.id()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[9]/td[2]/input[1]').send_keys(send_idcard)
        if lines[8]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[8]!='addman':  #必填项添加人
                send_addman=lines[8]
            else:
                send_addman = CR.addMan()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[10]/td[2]/input').send_keys(send_addman)
        if lines[9]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[9]!='user_num':  #必填项账号
                send_user_num=lines[9]
            else:
                send_user_num = CR.user_num()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td[4]/input').send_keys(send_user_num)
        if lines[10]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[10]!='pwd':  #必填项密码
                send_pwd=lines[10]
            else:
                send_pwd ='123456'
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[3]/td[4]/input').send_keys(send_pwd)
        if lines[11]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[11]!='nation':
                send_nation=lines[11]
            else:
                send_nation = CR.nation()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[4]/td[4]/input').send_keys(send_nation)
        if lines[12]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[12]!='marriage':
                send_marriage=lines[12]
            else:
                send_marriage = CR.marriage()
            Select(self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[5]/td[4]/select')).select_by_visible_text(send_marriage)
        if lines[13]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[13]!='role':
                send_role=lines[13]
            else:
                send_role = CR.role()
            Select(self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[6]/td[4]/select')).select_by_visible_text(send_role)
        if lines[14]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[14]!='faveriate':
                send_faveriate=lines[14]
            else:
                send_faveriate = CR.faveriate()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[7]/td[4]/input').send_keys(send_faveriate)
        if lines[15]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[15]!='tel':
                send_tel=lines[15]
            else:
                send_tel = CR.tel()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[8]/td[4]/input').send_keys(send_tel)
        if lines[16]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[16]!='address':
                send_address=lines[16]
            else:
                send_address = CR.dress()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[9]/td[4]/input').send_keys(send_address)
        if lines[17]!='IGNORE':   #数据驱动，IGNORE跳过,指定值则调用函数随机生成，否则使用数据值
            if lines[17]!='email':
                send_email=lines[17]
            else:
                send_email = CR.email()
            self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[10]/td[4]/input').send_keys(send_email)
        now = time.strftime("%Y-%m-%d-%H-%M-%S")
        screenshot_path=r'D:\Python\pythonproject\crmTestSuite2\report'+'crm_addemployee'+now+'.png'
        self.driver.get_screenshot_as_file(screenshot_path)
        '''点击提交按钮'''
        self.driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/input').click()
        webtext=self.driver.switch_to.alert.text
        print(webtext)
        print(lines[19])
        if lines[19].rstrip('\n') in webtext:
            print('>>>>>>>>>>测试标题：',lines[18],'测试通过！')
        else:
            print('>>>>>>>>>>测试标题：', lines[18], '测试失败')

    def test_addEmployee(self):
        with open(r'crmTestSuite2/Data/adddata.txt', 'r', encoding='utf-8') as file_data:
            lines_0 = file_data.readlines()
            for line_num in range(len(lines_0)):
                self.addEmployee_mudle(line_num)




if __name__ == '__main__':
        sendlist=[]
        # 测试套件，构建测试集
        dis= unittest.defaultTestLoader.discover(r'/crmTestSuite2', pattern='runnerx.py')

        # 我们要新建一个用于保存我们测试结果的文件，html
        now = time.strftime("%Y-%m-%d-%H-%M-%S")
        # 定义文件的名字
        filename = r'D:\Python\pythonproject\crmTestSuite2\report' + now + "_result.html"
        file = open(filename, "wb")
        # 执行我们的报告写入
        runner = HTMLTestRunner(stream=file, title="crm添加员工测试报告", description="用例执行情况:")
        # stream：是指定测试报告文件
        # title：指定报告的标题
        # description:指定报告的副标题
        # 执行我们测试用例
        runner.run(dis)
        time.sleep(1)
        # 关闭文件
        file.close()
        mail=SENDMAIL.send_mail()  #建立邮件连接
        for i in os.listdir(r'/crmTestSuite2/report') :   # 遍历Report文件夹，将文件名保存在列表
            a=i.lstrip('crm_addemployee')
            b=a.rstrip('.png')
            if b >=now:
                shotspath= r'D:\Python\pythonproject\crmTestSuite2\report'+i  #筛选大于程序开始时间的文件及截图
                sendlist.append(shotspath)
        print(sendlist)
        mail.addFile(sendlist)  #添加邮件
        mail.final_send()   #建立附件















