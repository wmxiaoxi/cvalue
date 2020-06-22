import unittest
import allure
import pytest
from common.fuction import *
ipMethod=method()

test_data=[(100,0,25,'25.0(C)'),(10,0,25,'25.0(C)'),(20,'9.99','-0.46','-0.46(C)'),('10.01',0,25,'25.0(C)')]
test_data1=[(20,10,'0.46','输入值不在区间范围内'),('9.99',-1,'0.46','输入值不在区间范围内')]
test_data2=[('',9,'0.46','不能为空'),('10','','0.46','不能为空'),('10','0','','不能为空'),('10a','0','0.46','格式错误'),('10','1a','0.46','格式错误'),('10','1','0.46a','格式错误'),('','','','不能为空'),('','','0.45','不能为空'),('1','20','0.45','大到小填写'),('10.0001','1.1111','0.46666','格式错误')]
test_data4=[('100','9','0.45','重复','20','0','0.46')]
test_data5=[('100','11','0.45','0.46(C)','10','0','0.46')]
test_data6=[('100','11','0.45','不在区间范围内','9','0','0.46')]
test_data7=[('100','0','0.45','不能为空','','','')]
test_data8=['设置5个区间']
test_data9=[('100','0','25','一个子节点')]
test_data10=[(10,0,0,'0.0(C)')]
test_data11=[("0","-1",0,'不在区间范围内')]
'''
@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷
CRITICAL = 'critical'　严重缺陷
NORMAL = 'normal'　　  一般缺陷
MINOR = 'minor'　　    次要缺陷
TRIVIAL = 'trivial'　　轻微缺陷　
'''
@allure.feature('计算方法为换算')
class Test_conversion():
    @allure.story('一个区间值,正常在区间范围内包含边界值，正常计算')
    @allure.severity("critical")
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted',test_data)
    def test_01(self,qjvalue11,qjvalue12,value13,excepted):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0],coversion_input_ele+'[1]/input[1]',qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele+'[1]/input[2]',qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]',value13)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[1], 'innerHTML')
        print(reqTotal)
        assert excepted in reqTotal

    @allure.story('值是区间边界值，不在区间内,计算报错')
    @allure.severity("critical")
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted', test_data1)
    def test_01(self, qjvalue11, qjvalue12, value13, excepted):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[1]', qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[2]', qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]', value13)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        alert=ipMethod.driver.switch_to.alert
        assert excepted in alert.text
        alert.dismiss()


    @allure.story('区间及值输入不合法,计算报错包含了由小到大输入')
    @allure.severity("normal")
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted', test_data2)
    def test_02(self, qjvalue11, qjvalue12, value13, excepted):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[1]', qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[2]', qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]', value13)
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(3)
        alert=ipMethod.driver.switch_to.alert
        assert excepted in alert.text
        alert.dismiss()



    @allure.story("区间值有重复")
    @allure.severity("minor")
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted,qjvalue21,qjvalue22,value23', test_data4)
    def test_02(self, qjvalue11, qjvalue12, value13, excepted,qjvalue21,qjvalue22,value23):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[1]', qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[2]', qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]', value13)
        ipMethod.click(attr[0],add_btn_ele)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[1]', qjvalue21)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[2]', qjvalue22)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[3]', value23)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        alert = ipMethod.driver.switch_to.alert
        assert excepted in alert.text
        alert.dismiss()




    @allure.story("多个区间，区间有截断,在区间内")
    @allure.severity("critical")
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted,qjvalue21,qjvalue22,value23', test_data5)
    def test_03(self, qjvalue11, qjvalue12, value13, excepted, qjvalue21, qjvalue22, value23):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[1]', qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[2]', qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]', value13)
        ipMethod.click(attr[0],add_btn_ele)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[1]', qjvalue21)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[2]', qjvalue22)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[3]', value23)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[1], 'innerHTML')
        print(reqTotal)
        assert excepted in reqTotal



    @allure.story("多个区间，区间有截断,不在区间内")
    @allure.severity("critical")
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted,qjvalue21,qjvalue22,value23', test_data6)
    def test_04(self, qjvalue11, qjvalue12, value13, excepted, qjvalue21, qjvalue22, value23):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[1]', qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[2]', qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]', value13)
        ipMethod.click(attr[0],add_btn_ele)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[1]', qjvalue21)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[2]', qjvalue22)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[3]', value23)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(3)
        alert = ipMethod.driver.switch_to.alert
        assert excepted in alert.text
        alert.dismiss()




    @allure.story("多个区间，一个区间为空")
    @allure.severity("minor")
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted,qjvalue21,qjvalue22,value23', test_data7)
    def test_04(self, qjvalue11, qjvalue12, value13, excepted, qjvalue21, qjvalue22, value23):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[1]', qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[2]', qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]', value13)
        ipMethod.click(attr[0], add_btn_ele)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[1]', qjvalue21)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[2]', qjvalue22)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[2]/input[3]', value23)
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(3)
        alert = ipMethod.driver.switch_to.alert
        assert excepted in alert.text
        alert.dismiss()



    @allure.story('区间增加了5个后，点击新增报错')
    @allure.severity("minor")
    @pytest.mark.parametrize("expected",test_data8)
    def test_05(self,expected):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        for j in range(0,5):
            ipMethod.click(attr[0], add_btn_ele)
            time.sleep(3)
        alert=ipMethod.driver.switch_to.alert
        assert expected in alert.text





    @allure.story("区间值增加后删除，测试删除按钮")
    @allure.severity("minor")
    def test_05(self):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        for j in range(0,1):
            ipMethod.click(attr[0], add_btn_ele)
        ipMethod.click(attr[0], reduce_btn_ele)
        time.sleep(3)
        li=ipMethod.driver.find_elements_by_xpath('//*[@id="node-menu"]/div[3]/div[3]/div[2]/ul/li')
        assert len(li)==1


    @allure.story('换算父节点下有多个子节点，计算报错')
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted', test_data9)
    def test_06(self,qjvalue11,qjvalue12,value13,excepted):
        action(2)
        for i in range(0, 2):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[1]', qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[2]', qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]', value13)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert=ipMethod.driver.switch_to.alert
        assert excepted in alert.text
        alert.dismiss()




    @allure.story('区间及区间值为0可以正常保存1')
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted', test_data10)
    def test_07(self,qjvalue11,qjvalue12,value13,excepted):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[1]', qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[2]', qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]', value13)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[1], 'innerHTML')
        print(reqTotal)
        assert excepted in reqTotal



    @allure.story('区间及区间值为0可以正常保存2')
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted', test_data11)
    def test_08(self, qjvalue11, qjvalue12, value13, excepted):
        action(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[1]', qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[2]', qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]', value13)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0],menu_calcubtn)
        time.sleep(1)
        alert=ipMethod.driver.switch_to.alert
        assert excepted in alert.text


    if __name__=="__main__":
        pytest.main(['-s','test_conversion.py'])
