import pytest
from common.fuction import *
import allure
ipMethod=method()
@allure.feature('计算方法为脚本')
class Test_script():
    # @allure.story('中心节点计算方法脚本,正常计算')
    # def test_01(self):
    #     action(4)
    #     for i in range(0,4):
    #         selectLevel(attr[0],levelele[i])
    #         time.sleep(3)
    #         input01(attr[0],levelcon[i],levelsz[i],'')
    #         ipMethod.click(attr[0],menu_confirmbtn)
    #         time.sleep(3)
    #     selectLevel(attr[0],value_top)
    #     select_method(attr[0],calmethod_ele[3])
    #     ipMethod.sendkeys(attr[0],menu_script,script1)
    #     ipMethod.click(attr[0],menu_confirmbtn)
    #     ipMethod.click(attr[0],menu_calcubtn)
    #     time.sleep(2)
    #     reqTotal=ipMethod.getvalue(attr[0],reqTotal_ele[0],'innerHTML')
    #     assert reqTotal == expected_script[0]
    #
    #
    # @allure.story('脚本中节点名称不存在，计算报错')
    # def test_02(self):
    #     action(4)
    #     for i in range(0,4):
    #         selectLevel(attr[0],levelele[i])
    #         time.sleep(3)
    #         input01(attr[0],levelcon[i],levelsz[i],'')
    #         ipMethod.click(attr[0],menu_confirmbtn)
    #         time.sleep(3)
    #     selectLevel(attr[0],value_top)
    #     select_method(attr[0],calmethod_ele[3])
    #     ipMethod.sendkeys(attr[0],menu_script,script2)
    #     ipMethod.click(attr[0],menu_confirmbtn)
    #     ipMethod.click(attr[0],menu_calcubtn)
    #     time.sleep(2)
    #     alert=ipMethod.driver.switch_to.alert
    #     assert expected_script[1] in alert.text
    #     alert.dismiss()
    #
    #
    #
    #
    #
    # @allure.story('脚本中节点名称为空，计算报错')
    # def test_03(self):
    #     action(4)
    #     for i in range(0,4):
    #         selectLevel(attr[0],levelele[i])
    #         time.sleep(3)
    #         input01(attr[0],levelcon[i],levelsz[i],'')
    #         ipMethod.click(attr[0],menu_confirmbtn)
    #         time.sleep(3)
    #     selectLevel(attr[0],value_top)
    #     select_method(attr[0],calmethod_ele[3])
    #     ipMethod.sendkeys(attr[0],menu_script,script3)
    #     ipMethod.click(attr[0],menu_confirmbtn)
    #     ipMethod.click(attr[0],menu_calcubtn)
    #     time.sleep(2)
    #     alert=ipMethod.driver.switch_to.alert
    #     assert expected_script[1] in alert.text
    #     alert.dismiss()
    #
    #
    #
    #
    # @allure.story('脚本里存在小数和负数')
    # def test_04(self):
    #     action(4)
    #     for i in range(0,4):
    #         selectLevel(attr[0],levelele[i])
    #         time.sleep(3)
    #         input01(attr[0],levelcon[i],levelsz[i],'')
    #         ipMethod.click(attr[0],menu_confirmbtn)
    #         time.sleep(3)
    #     selectLevel(attr[0],value_top)
    #     select_method(attr[0],calmethod_ele[3])
    #     ipMethod.sendkeys(attr[0],menu_script,script4)
    #     ipMethod.click(attr[0],menu_confirmbtn)
    #     ipMethod.click(attr[0],menu_calcubtn)
    #     time.sleep(2)
    #     reqTotal=ipMethod.getvalue(attr[0],reqTotal_ele[0],'innerHTML')
    #     assert reqTotal == expected_script[3]



    @allure.story('脚本错误')
    def test_05(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[3])
        ipMethod.sendkeys(attr[0], menu_script, script5)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert = ipMethod.driver.switch_to.alert
        assert expected_script[4] in alert.text
        alert.dismiss()



    @allure.story('脚本中右击插入列表中显示名称正确,且点击列表中名称成功显示在脚本输入框内')
    def test_06(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[3])
        ipMethod.contentclick(attr[0], menu_script)
        ipMethod.xfclick(attr[0],scr_insert)
        time.sleep(1)
        ele=ipMethod.driver.find_elements_by_xpath(insert_name)
        list=[]
        time.sleep(1)
        for i in range(1,len(ele)+1):
            name=ipMethod.getvalue(attr[0],insert_name+str([i]),'innerHTML')
            print(name)
            list.append(name)
        assert list==[levelcon[0],levelcon[1],levelcon[2],levelcon[3]]
        ipMethod.click(attr[0],insert_name+str([1]))
        name1=ipMethod.getvalue(attr[0],menu_script,'value')
        assert  name1==list[0]


    #@pytest.mark.skip(reason='bug还没修复好')
    @allure.story('脚本中右击插入列表中无数据显示时显示')
    def test_07(self):
        ipMethod.open()
        ipMethod.maximize()
        time.sleep(2)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[3])
        ipMethod.contentclick(attr[0], menu_script)
        ipMethod.xfclick(attr[0], scr_insert)
        time.sleep(1)
        flag=True
        try:
            ipMethod.driver.find_elements_by_xpath(insert_name)
            time.sleep(1)
            return flag
        except:
            flag=False
            return flag

        assert flag==False




if __name__=="__main__":
    pytest.main(['-s',"-q",'test_script.py'])
