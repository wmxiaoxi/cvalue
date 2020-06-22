import unittest
import allure
from common.fuction import *
ipMethod=method()
import pytest
@allure.feature('加权')
class Test_weights():


    @allure.story('中心节点计算方法是加权,子节点权重和为1（权重为正整数），正常计算')
    def test_01(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(1)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(1)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        reqLine = ipMethod.getvalue(attr[0], line_ele[0], 'innerHTML')
        assert reqTotal == expected_weights[0]
        assert reqLine== levelqz[0]





    @allure.story('#中心节点计算方法是加权，子节点权重和为<1,报错提示')
    def test_02(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[3], levelqz[10])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert=ipMethod.driver.switch_to.alert
        print(alert.text)
        assert expected_message[0] in alert.text
        alert.dismiss()





    @allure.story(' #中心节点计算方法是加权，子节点权重和为>1,报错提示')
    def test_03(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(1)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[3], levelqz[0])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(2)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert=ipMethod.driver.switch_to.alert
        print(alert.text)
        assert expected_message[0] in alert.text
        alert.dismiss()




    @allure.story('#中心节点计算方法是加权，子节点权重和为=1（权重存在小数）')
    def test_04(self):
        action(4)
        for i in range(0, 2):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], levelele[2])
        input01(attr[0], levelcon[2], levelsz[2], levelqz[5])
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[3], levelqz[6])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        assert reqTotal == expected_weights[0]





    @allure.story('#中心节点计算方法为加权，子节点的权重值超出位数（为五位小数），报错提示')
    def test_06(self):
        action(4)
        time.sleep(1)
        selectLevel(attr[0], levelele[0])
        time.sleep(3)
        input01(attr[0], levelcon[0], levelsz[0], levelqz[9])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(3)
        alert=ipMethod.driver.switch_to.alert
        assert expected_message[1] in alert.text
        alert.dismiss()




    @allure.story('#中心节点计算方法为加权，子节点的权重值为空，权重和为1应正常计算')
    def test_07(self):
        action(4)
        for i in range(0, 2):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], levelele[2])
        input01(attr[0], levelcon[2], levelsz[2], levelqz[0])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[3], levelqz[4])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(2)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        assert reqTotal == expected_weights[1]



    @allure.story('#中心节点计算方法为加权，子节点的权重值为0，权重和为1应正常计算')
    def test_08(self):
        action(4)
        for i in range(0, 2):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], levelele[2])
        input01(attr[0], levelcon[2], levelsz[2], levelqz[0])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[3], levelqz[8])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(2)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        assert reqTotal == expected_weights[1]



    @allure.story('#中心节点计算方法为加权，子节点的权重值包含字母，应报错提示')
    def test_09(self):
        action(4)
        for i in range(0, 2):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], levelele[2])
        input01(attr[0], levelcon[2], levelsz[2], levelqz[11])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(3)
        alert=ipMethod.driver.switch_to.alert
        assert expected_message[1] in alert.text
        alert.dismiss()


    @allure.story(' #中心节点计算方法为加权，权重和为1，叶子节点数值为空，应报错提示')
    def test_10(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[4], levelqz[3])
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert=ipMethod.driver.switch_to.alert
        assert expected_message[2] in alert.text
        alert.dismiss()





    @allure.story('#中心节点计算方法为加权，权重和为1，叶子节点数值为负数（支持负数）')
    def test_11(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[6], levelqz[3])
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0],value_top)
        select_method(attr[0],calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        resTotal=ipMethod.getvalue(attr[0],reqTotal_ele[0],'innerHTML')
        assert resTotal==expected_weights[5]





    @allure.story('#中心节点计算方法为加权，权重和为1，叶子节点数值为小数（超出2位小数），应报错提示')
    def test_12(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[7], levelqz[3])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(2)
        alert=ipMethod.driver.switch_to.alert
        assert expected_message[3] in alert.text
        alert.dismiss()



    @allure.story('# 中心节点计算方法为加权，权重和为1，叶子节点数值存在字母，应报错提示')
    def test_13(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[9], levelqz[3])
        ipMethod.click(attr[0], menu_confirmbtn)
        time.sleep(2)
        alert = ipMethod.driver.switch_to.alert
        assert expected_message[3] in alert.text
        alert.dismiss()


    @allure.story('#中心节点计算方法为加权，权重和为1，叶子节点数值为小数（正常小数）应正常计算')
    def test_14(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[8], levelqz[3])
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        assert reqTotal == expected_weights[2]



    @allure.story('#中心节点计算方法为加权，权重和为1，叶子节点数值为0,应正常计算')
    def test_15(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[3], levelsz[5], levelqz[3])
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        assert reqTotal == expected_weights[3]


    @allure.story('#中心节点计算方法为加权，内容为空,计算时应报错(空字符未写)')
    def test_16(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[4], levelsz[5], levelqz[3])
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert=ipMethod.driver.switch_to.alert
        assert expected_message[4] in alert.text
        alert.dismiss()

    @allure.story('中心节点计算方法为加权，内容为重复,计算时应报错（内容带空格暂不写）')
    def test_17(self):
        action(4)
        for i in range(0, 3):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], levelele[3])
        input01(attr[0], levelcon[0], levelsz[3], levelqz[3])
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert=ipMethod.driver.switch_to.alert
        assert expected_message[5] in alert.text
        alert.dismiss()


if __name__=="__main__":
    pytest.main(['-s',"-q",'test_weightsevaute.py'])