# coding=utf-8
from selenium import webdriver
import time
import requests
from aip import AipOcr
import os

def readfile(config_dir):
    for root,dirs,files in os.walk():
        for iter_files in files:
            return iter_files



class loginTest():
    def __init__(self):
        self.url = 'https://192.168.6.248/#/'
        self.driver = webdriver.Firefox()

    def initial(self):
        """ 初始化连接 """
        APP_ID = '16611607'
        API_KEY = 'wAIXfXOUS8ztLa4FrK3rZex1'
        SECRET_KEY = '3b8nvjSGUZq0LPC18VVAizKYRBbny6Mq'
        return AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(self, filePath):
        """ 读取图片 """
        with open(filePath, 'rb') as f:
            return f.read()

    def log_in(self,name):
        self.driver.get(self.url)
        time.sleep(3)
        # //*[@id="codes"]
        # self.driver.save_screenshot("0.jpg")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/div/div/input').send_keys(name)
        # 输入密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/div/div/input').send_keys("Jiangmin123456")
        # 登录成功的标志，默认true
        flag = True
        while flag:
            image = self.driver.find_element_by_class_name('auth_code')
            print(image)
            file_path = 'a.png'
            image.screenshot(file_path)

            client = self.initial()
            image = self.get_file_content(file_path)
            res = client.basicGeneral(image)
            print(res)

            # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[3]/div/div/input').send_keys(
            #     res['words_result'][0]['words'])
            button= self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[3]/div/div/input')
            button.clear()
            button.send_keys(res['words_result'][0]['words'])
            # 点击登陆  //*[@id="app"]/div/div[3]/form/div[5]/div/button
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[5]/div/button').click()
            time.sleep(2)
            # 输出登陆之后的cookies
            print(self.driver.get_cookies())
            time.sleep(2)

            # cookie_dict = self.driver.get_cookie('httpOnly')
            # # log_success = cookie_dict.get('secure')
            # print("cookie_dict:",cookie_dict)
            cur_url=self.driver.current_url
            print("cur_sul:",cur_url)
            if cur_url!=self.url:
                flag = False

    def add_user(self,name):
        self.driver.get('https://192.168.6.248/#/users')
        # self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[3]').click()
        #//*[@id="pane-first"]/section/div[1]/form/div[1]/div/div/input
        #//*[@id="pane-first"]/section/div[1]/form/div[1]/div/div/input
        #//*[@id="pane-first"]/section/div[1]/form/div[2]/div/div/input
        self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/section/div[1]/form/div[1]/div/div/input').send_keys(name)
        self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/section/div[1]/form/div[2]/div/div/input').send_keys(
            "Jiangmin123456")
        self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/section/div[1]/form/div[3]/div/div/input').send_keys(
            "Jiangmin123456")
        #姓名
        self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/section/div[1]/form/div[4]/div/div/input').send_keys(
            "xiaxia")
        #部门
        self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/section/div[1]/form/div[5]/div/div/input').send_keys(
            "xiaxia")
        #电话
        self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/section/div[1]/form/div[6]/div/div/input').send_keys(
            15031568956)
        #阀值
        fazhi = self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/section/div[1]/form/div[7]/div/div/div/input')
        fazhi.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
        #角色
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/section/div[1]/form/div[8]/div/div/label[1]/span[1]/input').click()
        #添加
        self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/section/div[1]/form/div[9]/div/button/span').click()

    def input_file(self,config_dir):
        self.driver.get('https://192.168.6.248/#/import_file')
        #前往导入页 //*[@id="homebody"]/div/div[2]/div/div[2]/p
        # input=self.driver.find_elements_by_xpath('//*[@id="homebody"]/div/div[2]/div/div[2]/p')
        # input.click()
        #//*[@id="check_file"]
        for root, dirs, files in os.walk(config_dir):
            for iter_files in files:
                path = root + '\\' + iter_files
                self.driver.find_element_by_name('filename').send_keys(path)
        #下一步
        # next=self.driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[1]/div/div[2]/div[2]/form/div[6]/div/button[2]')
        # next.click()


if __name__ == '__main__':
    text_login = loginTest()
    text_login.log_in("admin")
    text_login.add_user("xixia2")
    # text_login.input_file(r'E:\app_downloads')

