from common.base import *
from test_data.test_data import *
ipMethod=method()

#创建框架,右击选择下级，同级，或删除
def top(ele_attri,loc,btn):
    ipMethod.contentclick(ele_attri,loc)
    time.sleep(2)
    ipMethod.click(ele_attri, btn)




#选中节点
def selectLevel(ele_attri,ele_level):
    ipMethod.ac_click(ele_attri, ele_level)


#创建时输入数值，权重，内容
def input01(ele_attri,namevalue,countvalue,qzvalue):
    time.sleep(1)
    ipMethod.clear(ele_attri,menu_name)
    ipMethod.sendkeys(ele_attri,menu_name,namevalue)
    ipMethod.sendkeys(ele_attri, menu_countvalue, countvalue)
    ipMethod.sendkeys(ele_attri,menu_qzcount,qzvalue)
    #ipMethod.click(ele_attri,menu_confirmbtn)


#选择计算方式
def select_method(ele_attri,calele_method):
    time.sleep(1)
    js = "document.getElementsByClassName('node-menu-more')[0].style.display='block';"  # 编写JS语句
    time.sleep(1)
    ipMethod.driver.execute_script(js)
    time.sleep(2)
    #ipMethod.ac_click(ele_attri, zkbtn_ele)
    ipMethod.ac_click(ele_attri, calele_method)
    time.sleep(2)



 #选择具体函数
def selectFunc(ele_attri, funloc, name):
    ipMethod.select(ele_attri, funloc, name)




#输入脚本内容
def selectScript():
    print('脚本内容填写')


def selectCov():
    print("换算具体选择")





##修改权重值
def modifyQz(ele_attri,ele_level,qzvalue):
    time.sleep(1)
    ipMethod.ac_click(ele_attri,ele_level)
    ipMethod.clear(ele_attri,menu_qzcount)
    ipMethod.sendkeys(ele_attri, menu_qzcount, qzvalue)




##修改内容
def modifyCon(ele_attri,ele_level,con):
    time.sleep(1)
    ipMethod.ac_click(ele_attri,ele_level)
    ipMethod.clear(ele_attri,menu_name)
    ipMethod.sendkeys(ele_attri, menu_name, con)




###清空内容，数值，权重值
def clear_menu():
    ipMethod.clear(attr[0],menu_countvalue)
    ipMethod.clear(attr[0], menu_qzcount)
    ipMethod.clear(attr[0], menu_name )

#创建1层子节点
def action(j):
    time.sleep(2)
    ipMethod.open()
    ipMethod.maximize()
    time.sleep(2)
    for i in range(0,j):
        top(attr[0], value_top,value_down)
        time.sleep(3)




#创建2层子节点
def action1(m,n):
    ipMethod.open()
    ipMethod.maximize()
    time.sleep(2)
    for i in range(0, m):
        top(attr[0], value_top,value_down)
        time.sleep(1)
        # 子节点的叶子节点创建
    for k in range(0, n):
        for i in range(0,2):
            top(attr[0], levelele[k],value_down)
            time.sleep(1)






