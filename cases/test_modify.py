from common.fuction import *
import pytest
import allure
ipMethod=method()
@allure.feature("修改")
class Test_modify():
    @allure.story('删除一个节点，再去计算')
    def test_01(self):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'SUM')
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        time.sleep(2)
        top(attr[0],levelmodify[3],value_del)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal1 = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        assert reqTotal != reqTotal1


    @allure.story('删除非常规节点下所有子节点，计算时报错：需要子节点')
    @pytest.mark.parametrize('expected',['需要子节点',])
    def test_02(self,expected):
        action1(4, 1)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
        for i in range(0, 1):
            selectLevel(attr[0], levelele_2[i])
            time.sleep(3)
            input01(attr[0], level2con[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        time.sleep(2)
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'SUM')
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], levelele[0])
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'SUM')
        ipMethod.click(attr[0], menu_confirmbtn)
        top(attr[0], levelele_2[0],value_del)
        time.sleep(1)
        top(attr[0], levelele_2[1], value_del)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        alert = ipMethod.driver.switch_to.alert
        assert expected in alert.text
        alert.dismiss()




    @allure.story("更改权重值，数值，计算方法由函数更新为加权")
    @pytest.mark.parametrize('newlevelcon, newlevelsz, newlevelqz',[('测试节点11','100','0.5')])
    @pytest.mark.parametrize('newlevelcon1, newlevelsz1, newlevelqz1',[('测试节点12','200','0.1')])
    def test_03(self,newlevelcon, newlevelsz, newlevelqz,newlevelcon1, newlevelsz1, newlevelqz1):
        action(4)
        for i in range(0,4):
            selectLevel(attr[0],levelele[i])
            time.sleep(3)
            input01(attr[0],levelcon[i],levelsz[i],levelqz[i])
            ipMethod.click(attr[0],menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0],value_top)
        select_method(attr[0],calmethod_ele[2])
        selectFunc(attr[0],func_ele,'SUM')
        ipMethod.click(attr[0],menu_confirmbtn)
        ipMethod.click(attr[0],menu_calcubtn)
        time.sleep(2)
        #修改节点1内容，数值，权重
        selectLevel(attr[0], levelmodify[2])
        clear_menu()
        input01(attr[0], newlevelcon, newlevelsz, newlevelqz)
        ipMethod.click(attr[0], menu_confirmbtn)
        #修改节点2内容，数值，权重
        selectLevel(attr[0], levelmodify[3])
        clear_menu()
        input01(attr[0], newlevelcon1, newlevelsz1, newlevelqz1)
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        assert reqTotal==expected_modify[0]



    @allure.story("删除权重值，修改数值，计算方法由加权更新为加权")
    @pytest.mark.parametrize('newlevelcon, newlevelsz, newlevelqz', [('测试节点11', '100', '')])
    @pytest.mark.parametrize('newlevelcon1, newlevelsz1, newlevelqz1', [('测试节点12', '200', '')])
    def test_03(self, newlevelcon, newlevelsz, newlevelqz, newlevelcon1, newlevelsz1, newlevelqz1):
        action(4)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], levelqz[i])
            ipMethod.click(attr[0], menu_confirmbtn)
            time.sleep(3)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        # 选择节点，清空，修改节点1内容，数值，权重
        selectLevel(attr[0], levelmodify[2])
        clear_menu()
        input01(attr[0], newlevelcon, newlevelsz, newlevelqz)
        ipMethod.click(attr[0], menu_confirmbtn)
        # 选择节点，清空，修改节点2内容，数值，权重
        selectLevel(attr[0], levelmodify[3])
        clear_menu()
        input01(attr[0], newlevelcon1, newlevelsz1, newlevelqz1)
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[2])
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        reqTotal = ipMethod.getvalue(attr[0], reqTotal_ele[0], 'innerHTML')
        assert reqTotal == expected_modify[1]






    @allure.story('删除数值后能成功保存')
    def test_05(self):
        action(1)
        selectLevel(attr[0],levelmodify[4])
        input01(attr[0],levelcon[0],levelsz[0],levelqz[0])
        ipMethod.click(attr[0],menu_confirmbtn)
        ipMethod.clear(attr[0],menu_qzcount)
        ipMethod.clear(attr[0], menu_countvalue)
        ipMethod.click(attr[0], menu_confirmbtn)
        selectLevel(attr[0], value_top)
        selectLevel(attr[0], levelmodify[4])
        text=ipMethod.getvalue(attr[0],menu_qzcount,'innerHTML')
        text1 = ipMethod.getvalue(attr[0], menu_countvalue, 'innerHTML')
        assert text==''
        assert text1==''





    @allure.story("父节点下如无子节点，父节点选择非常规，则会自动创建子节点")
    def test_06(self):
        ipMethod.open()
        ipMethod.maximize()
        time.sleep(2)
        selectLevel(attr[0],value_top)
        select_method(attr[0],calmethod_ele[2])
        time.sleep(1)
        selectFunc(attr[0],func_ele,'SUM')
        ipMethod.click(attr[0],menu_confirmbtn)
        flag=True
        try:
            ipMethod.find_element(attr[0],levelmodify[1])
            return flag
        except:
            flag = False
            return  flag
        assert flag==True



    @allure.story('最全例子（包含常规，换算，脚本，加权)')
    @pytest.mark.parametrize('qjvalue11,qjvalue12,value13', [(1000,0,5)])
    @pytest.mark.parametrize('excepeted',['145.9(F)'])
    def test_07(self,qjvalue11,qjvalue12,value13,excepeted):
        action1(4, 2)
        time.sleep(2)
        top(attr[0], levelele[2], value_down)
        for i in range(0, 4):
            selectLevel(attr[0], levelele[i])
            time.sleep(3)
            input01(attr[0], levelcon[i], levelsz[i], '')
            ipMethod.click(attr[0], menu_confirmbtn)
        for i in range(0, 5):
            selectLevel(attr[0], levelele_2[i])
            time.sleep(3)
            input01(attr[0], level2con[i], levelsz2[i], levelqz2[i])
            ipMethod.click(attr[0], menu_confirmbtn)
        #设置总节点方法为函数
        selectLevel(attr[0], value_top)
        select_method(attr[0], calmethod_ele[2])
        selectFunc(attr[0], func_ele, 'SUM')
        ipMethod.click(attr[0], menu_confirmbtn)
        #设置节点1的方法为脚本
        selectLevel(attr[0], levelele[0])
        select_method(attr[0], calmethod_ele[3])
        ipMethod.sendkeys(attr[0], menu_script, script6)
        ipMethod.click(attr[0], menu_confirmbtn)
        #设置节点2的方法为加权
        selectLevel(attr[0], levelele[1])
        select_method(attr[0], calmethod_ele[1])
        ipMethod.click(attr[0], menu_confirmbtn)
        #设置节点3的方法为换算
        selectLevel(attr[0], levelele[2])
        select_method(attr[0], calmethod_ele[4])
        ipMethod.sendkeys(attr[0],coversion_input_ele+'[1]/input[1]',qjvalue11)
        ipMethod.sendkeys(attr[0], coversion_input_ele+'[1]/input[2]',qjvalue12)
        ipMethod.sendkeys(attr[0], coversion_input_ele + '[1]/input[3]',value13)
        ipMethod.click(attr[0], menu_confirmbtn)
        ipMethod.click(attr[0], menu_calcubtn)
        time.sleep(2)
        resTotal=ipMethod.getvalue(attr[0],levelele_2[5],'innerHTML')
        assert resTotal==excepeted

if __name__=="__main__":
    #pytest.main(['-s','test_modify.py','--reruns','2','--reruns-delay','3'])
    pytest.main(['-s', 'test_modify.py'])
