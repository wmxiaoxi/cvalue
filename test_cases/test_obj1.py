import unittest
from common.fuction import *
ipMethod=method()
import allure


@allure.epic('计算方法为函数，求和')
@allure.feature("测试模块")
class Test_evaute():

#中心节点计算方法是函数求和,正常计算
    @allure.story("用户故事：1")
    @allure.title("用例的标题")
    @allure.severity("critical")
    def test_01(self):
        '''case description:作者：上海-悠悠 qq交流群：874033608
        1.点文章分类导航标签 -跳转编辑页面
        2.编辑页面输入，分类名称，如:上海-悠悠-可以输入
        3.点保存按钮保存成功
        '''
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





















