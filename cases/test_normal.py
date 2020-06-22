import pytest
from common.fuction import *
import allure
ipMethod=method()
@allure.feature("计算方法为常规")
class Test_normal():
    @allure.story('总节点为常规节点,计算应报错')
    def test_01(self):
        action(4)
        for i in range(0,4):
            selectLevel(attr[0],levelele[i])
            time.sleep(3)
            input01(attr[0],levelcon[i],levelsz[i],'')
            ipMethod.click(attr[0],menu_confirmbtn)
            time.sleep(3)
        ipMethod.click(attr[0],menu_calcubtn)
        time.sleep(2)
        alert=ipMethod.driver.switch_to.alert
        assert '不能为常规方法' in alert.text
        alert.dismiss()





    @allure.story('中间父节点为常规,则计算报错')
    def test_02(self):
        action1(4, 1)
        for i in range(0,4):
            selectLevel(attr[0],levelele[i])
            time.sleep(3)
            input01(attr[0],levelcon[i],levelsz[i],'')
            ipMethod.click(attr[0], menu_confirmbtn)
        for i in range(0,1):
            selectLevel(attr[0], levelele_2[i])
            time.sleep(3)
            input01(attr[0], level2con[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'SUM')
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert=ipMethod.driver.switch_to.alert
        assert '不能为常规节点' in alert.text
        alert.dismiss()

if __name__=="__main__":
    pytest.main(['-s','test_normal.py'])
