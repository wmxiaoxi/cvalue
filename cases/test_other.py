import unittest
import allure
import pytest
from common.fuction import *
ipMethod=method()
@allure.feature("其它场景")
class Test_other():
    @allure.story('同级')
    def test_01(self):
        action(1)
        selectLevel(attr[0],value_top)
        time.sleep(1)
        top(attr[0],levelele[0],value_leveltoo)
        flag = True
        try:
            ipMethod.find_element(attr[0],levelele[1])
            return flag
        except:
            flag=False
            return flag
        assert flag==True




    @allure.story('上移')
    def test_02(self):
        action(2)
        for i in range(0, 2):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        top(attr[0],levelele[1],value_foward)
        time.sleep(2)
        selectLevel(attr[0],value_top)
        select_method(attr[0],calmethod_ele[3])
        ipMethod.contentclick(attr[0], menu_script)
        ipMethod.xfclick(attr[0], scr_insert)
        time.sleep(1)
        ele = ipMethod.driver.find_elements_by_xpath(insert_name)
        list = []
        time.sleep(1)
        for i in range(1, len(ele) + 1):
            name = ipMethod.getvalue(attr[0], insert_name + str([i]), 'innerHTML')
            list.append(name)
        assert list == [levelcon[1], levelcon[0]]




    @allure.story('下移')
    def test_03(self):
        action(2)
        for i in range(0, 2):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        top(attr[0],levelele[0],value_back)
        selectLevel(attr[0],value_top)
        select_method(attr[0],calmethod_ele[3])
        ipMethod.contentclick(attr[0], menu_script)
        ipMethod.xfclick(attr[0], scr_insert)
        time.sleep(1)
        ele = ipMethod.driver.find_elements_by_xpath(insert_name)
        list = []
        time.sleep(1)
        for i in range(1, len(ele) + 1):
            name = ipMethod.getvalue(attr[0], insert_name + str([i]), 'innerHTML')
            list.append(name)
        assert list == [levelcon[1], levelcon[0]]


    @allure.story('上级')
    def test_04(self):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        top(attr[0], levelele[0], value_par)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[3])
        ipMethod.contentclick(attr[0], menu_script)
        ipMethod.xfclick(attr[0], scr_insert)
        time.sleep(1)
        ele = ipMethod.driver.find_elements_by_xpath(insert_name)
        list = []
        time.sleep(1)
        for i in range(1, len(ele) + 1):
            name = ipMethod.getvalue(attr[0], insert_name + str([i]), 'innerHTML')
            print(name)
            list.append(name)
        assert list == ['分支主题']




    @allure.story('优先级')
    def test_05(self):
        action(1)
        selectLevel(attr[0], value_top)
        time.sleep(1)
        top(attr[0], levelele[0], value_p)
        ipMethod.ac_click(attr[0],value_p1)
        text= ipMethod.getvalue(attr[0],levelele[1],'innerHTML')
        assert text=='1'




    allure.story('进度')
    def test_06(self):
        action(1)
        selectLevel(attr[0], value_top)
        time.sleep(1)
        top(attr[0], levelele[0], value_d)
        time.sleep(1)
        ipMethod.ac_click(attr[0], value_g0)
        flag=True
        try:
            ipMethod.find_element(attr[0],'//*[@id="kity_path_40"]')
            return flag
        except:
            flag=False
            return flag
        assert flag==False



    @allure.story('撤销')
    def test_07(self):
        action(2)
        top(attr[0],value_top,value_chexiao)
        time.sleep(2)
        flag = False
        try:
            ipMethod.find_element(attr[0], levelele[1])
            return flag
        except:
            flag = True
            return flag
        assert flag == True




    @allure.story('重做')
    def test_08(self):
        action(2)
        time.sleep(1)
        top(attr[0], value_top, value_chexiao)
        top(attr[0], value_top, value_redo)
        flag = True
        try:
            ipMethod.find_element(attr[0], levelele[1])
            return flag
        except:
            flag = False
            return flag
        assert flag == True

if __name__=="__main__":
    pytest.main(['-s',"-q",'test_other.py'])

