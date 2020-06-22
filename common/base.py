from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from common.logger import *
import pytest
# logger=Logger(logger="method").getlog()
# exc_info = 1
class method():

    # option=webdriver.ChromeOptions()
    # option.add_argument('--headless')
    # option.add_argument("start-maximized")
    # self.driver = webdriver.Chrome(options=option)
    driver=webdriver.Chrome()
    #driver=webdriver.Ie()
    # driver=webdriver.Firefox()


    def open(self):
        # logger.info('打开浏览器...')
        self.url = "http://192.168.17.214/#/"
        self.driver.get(self.url)
        self.driver.refresh()

    #定位元素
    def find_element(self,ele_attri,loc):
        try:
            #WebDriverWait(self.driver,6).until(ec.visibility_of_element_located(ele_attri,loc))
            WebDriverWait(self.driver, 6).until(lambda x: x.find_element(ele_attri,loc))
            return self.driver.find_element(ele_attri,loc)
            # logger.info('未找到元素%s',loc)
        except Exception as e:
            raise e




    def clear(self,ele_attri,loc):
        self.find_element(ele_attri,loc).clear()




    def sendkeys(self,ele_attri,loc,value):
        #self.clear(ele_attri,loc)
        self.find_element(ele_attri,loc).send_keys(value)

    def click(self,ele_attri,loc):
        self.find_element(ele_attri,loc).click()


    def  getvalue(self,ele_attri,loc,attribute):
        return self.find_element(ele_attri,loc).get_attribute(attribute)



    def contentclick(self,ele_attri,loc):
        elecomm=self.find_element(ele_attri,loc);
        ActionChains(self.driver).context_click(elecomm).perform()


    def drag(self,ele_attri,loc):
        elecomm=self.find_element(ele_attri,loc);
        ActionChains(self.driver).drag_and_drop(elecomm).perform()

    def xfclick(self,ele_attri,loc):
        elecomm=self.find_element(ele_attri,loc);
        ActionChains(self.driver).move_to_element(elecomm).perform()


    def maximize(self):
        self.driver.maximize_window()



    def ac_click(self,ele_attri,loc):
        self.elecomm=self.find_element(ele_attri,loc)
        ActionChains(self.driver).click(self.elecomm).perform()



    def quit(self):
        self.driver.quit()



    def close(self):
        self.driver.close()


    def image(self):##as_base64用到html报告中  as_file保存到文件中
        self.nowtime=time.strftime('%Y-%m-%d %H%M%S')
        self.driver.get_screenshot_as_file('%s.jpg'%self.nowtime)



    def select(self,ele_attri,loc,name):
        select=self.find_element(ele_attri,loc)
        Select(select).select_by_value(name)


