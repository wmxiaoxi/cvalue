import unittest
from common.fuction import *
ipMethod=method()
import allure
import pytest


@allure.epic('计算方法为函数，求和')
@allure.feature("测试模块")
class Test_evaute():

    @allure.story("用户故事：1")
    @allure.title("用例的标题")
    @allure.severity("critical")
    #@pytest.mark.repeat(2)
    #@pytest.mark.flaky(reruns=2, reruns_delay=4)
#中心节点计算方法是函数求和,正常计算
    def test_01(self):
        action(4)
        for i in range(0,4):
            selectLevel(attr[0],levelele[i])
            time.sleep(3)
            input01(attr[0],levelcon[i],levelsz[i],'')
            ipMethod.click(attr[0],menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0],value_top)
        select_method(attr[0],calmethod_ele[2])
        selectFunc(attr[0],func_ele,'SUM')
        ipMethod.click(attr[0],menu_confirmbtn)
        ipMethod.click(attr[0],menu_calcubtn)
        time.sleep(2)
        reqTotal=ipMethod.getvalue(attr[0],reqTotal_ele[0],'innerHTML')
        assert reqTotal == expected_func[0]

#中心节点计算方法是函数求平均值,正常计算
    def test_02(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'AVERAGE')
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal=ipMethod.getvalue(attr[0],reqTotal_ele[0],'innerHTML')
        assert reqTotal == expected_func[1]


#中心节点计算方法是函数求最小值,正常计算

    def test_03(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'MIN')
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal=ipMethod.getvalue(attr[0],reqTotal_ele[0],'innerHTML')
        assert reqTotal == expected_func[2]


#中心节点计算方法是函数求最大值,正常计算

    def test_04(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'MAX')
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal=ipMethod.getvalue(attr[0],reqTotal_ele[0],'innerHTML')
        assert reqTotal == expected_func[3]



#中心节点计算方法是函数求最大值,(数值存在小数)，正常计算

    def test_05(self):
        action(4)
        for i in range(0, 2):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], levelele[2])
        input01(attr[0], levelcon[2], levelsz[8], '')
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[10], '')
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'MAX')
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal=ipMethod.getvalue(attr[0],reqTotal_ele[0],'innerHTML')
        assert reqTotal == expected_func[4]


