import unittest
import allure
import pytest
from common.fuction import *
ipMethod=method()
test_data=[(100,0,25,'25.0(C)')]
@allure.feature("导入导出")
class Test_outin():
    @allure.story('加权已计算后导出')
    def test_01(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(1)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(1)
        selectLevel(attr[0], value_top)
        input01(attr[0],'加权', '', '')
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        ipMethod.click("xpath",import_out_ele[0])
        time.sleep(5)
        ipMethod.find_element('xpath',import_in_ele[0]).send_keys(r'C:\Users\wmxia\Downloads\加权.json')
        time.sleep(1)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        reqLine = ipMethod.getvalue(attr[0], line_ele[1], 'innerHTML')
        assert reqTotal == expected_weights[0]
        assert reqLine == levelqz[0]

    @allure.story('加权未计算导出在导入')
    def test_02(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(1)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(1)
        selectLevel(attr[0], value_top)
        input01(attr[0],'加权2', '', '')
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(1)
        ipMethod.click("xpath",import_out_ele[0])
        time.sleep(5)
        ipMethod.find_element('xpath',import_in_ele[0]).send_keys(r'C:\Users\wmxia\Downloads\加权2.json')
        time.sleep(1)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        reqLine = ipMethod.getvalue(attr[0], line_ele[2], 'innerHTML')
        assert reqTotal == expected_weights[0]
        assert reqLine == levelqz[0]


    @allure.story('函数计算后导出导入')
    def test_03(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        input01(attr[0],'函数', '', '')
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'AVERAGE')
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        ipMethod.click("xpath",import_out_ele[0])
        time.sleep(6)
        ipMethod.find_element('xpath',import_in_ele[0]).send_keys(r'C:\Users\wmxia\Downloads\函数.json')
        time.sleep(2)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        assert reqTotal == expected_weights[4]



    @allure.story('换算计算后导出导入')
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13,excepted', test_data)
    def test_04(self,qjvalue11,qjvalue12,value13,excepted):
        action(1)
        time.sleep(1)
        for i in range(0, 1):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        input01(attr[0], '换算', '', '')
        select_method(attr[0], calmethod_ele[4])
        selectFunc(attr[0], coversion_ele, 'INTERVAL')
        ipMethod.sendkeys(attr[0],coversion_input_ele+'[1]/input[1]',qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele+'[1]/input[2]',qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]',value13)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        ipMethod.click("xpath", import_out_ele[0])
        time.sleep(6)
        ipMethod.find_element('xpath', import_in_ele[0]).send_keys(r'C:\Users\wmxia\Downloads\换算.json')
        time.sleep(2)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[1], 'innerHTML')
        print(reqTotal)
        assert excepted in reqTotal



    @allure.story('脚本计算后导出导入')
    def test_05(self):
        action(4)
        for i in range(0,4):
            selectLevel(attr[0],levelele[i])
            time.sleep(3)
            input01(attr[0],levelcon[i],levelsz[i],'')
            ipMethod.click(attr[0],menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0],value_top)
        input01(attr[0], '脚本', '', '')
        select_method(attr[0],calmethod_ele[3])
        ipMethod.sendkeys(attr[0],menu_script,script1)
        ipMethod.click(attr[0],menu_confirmbtn)
        ipMethod.click(attr[0],menu_calcubtn)
        time.sleep(2)
        ipMethod.click("xpath", import_out_ele[0])
        time.sleep(6)
        ipMethod.find_element('xpath', import_in_ele[0]).send_keys(r'C:\Users\wmxia\Downloads\脚本.json')
        time.sleep(2)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        print(reqTotal)
        assert expected_script[0] in reqTotal

if __name__=="__main__":
    pytest.main(['-q','test_outimportin.py'])

