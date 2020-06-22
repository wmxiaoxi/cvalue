# # 新建一个文件test_fixt.py
# # coding:utf-8
# import sys
# import pytest
#
# import allure
# # minversion=pytest.mark.skip(reason='not test')
# # @minversion
# # @pytest.mark.parametrize('a,b',[('hello','hello word'),pytest.param('tian','tiantian',marks=pytest.mark.xfail),])
# # def test_02(a,b):
# #     assert a in b
# #@pytest.mark.run(order=1)
# # @pytest.mark.repeat(2)
# # def test_03():
# #     a="yoyo"
# #     b="yoyo"
# #     assert a==b
# #@pytest.mark.run(order=2)
# # @pytest.mark.repeat(2)
# # def test_04():
# #     a=5
# #     b=6
# #     assert a!=b
# #
# #
# #
# # if __name__=="__main__":
# #     pytest.main(['-s','test_obj.py'])
#
#
#
#
# # import pytest
# # # 测试登录数据
# # test_login_data = [("admin", "111111"),  ("admin", "")]
# #
# # @pytest.fixture(scope='module')
# # def login(request):
# #     '''普通登录函数'''
# #     user=request.param['user']
# #     psw=request.param['psw']
# #     print("登录账户：%s"%user)
# #     print("登录密码：%s"%psw)
# #     if psw:
# #         return True
# #     else:
# #         return False
# #
# # @pytest.mark.parametrize("login", test_login_data)
# # def test_login(login):
# #     '''登录用例'''
# #     a=login
# #     assert a,  "失败原因：密码为空"
# #
# # if __name__ == "__main__":
# #     pytest.main(["-s", "test_obj.py"])
#
#
#
# # import pytest
# # test_user=['admin1','admin2']
# # test_psw=['111111','22222']
# # @pytest.fixture(scope='module')
# # def input_user(request):
# #      user=request.param
# #      print("登陆账户:%s"%user)
# #      return user
# # @pytest.fixture(scope='module')
# # def input_psw(request):
# #     psw=request.param
# #     print("登陆密码:%s"%psw)
# #     return psw
# # @pytest.mark.parametrize("input_user",test_user,indirect=True)
# # @pytest.mark.parametrize("input_psw",test_user,indirect=True)
# # def test_login(input_user,input_psw):
# #     a=input_user
# #     b=input_psw
# #     print("测试数据a->%s,b->%s"%(a,b))
# # if __name__ =="__main__":
# #     pytest.main(['-s','test_obj.py'])
#
#
# import pytest
# @allure.story('测试模块')
# @pytest.fixture()
# def user():
#     print("获取用户名")
#     a='yoyo'
#     return a
#
# @pytest.fixture()
# def psw(user):
#     a=user
#     print("获取密码")
#     b='12345'
#     return (a,b)
#
# @pytest.mark.chrome
# def test_01(psw):
#     u=psw[0]
#     p=psw[1]
#     print("测试账号：%s,密码：%s"%(u,p))
#     assert u=='yoyo1'
#
# @pytest.mark.chrome
# @pytest.mark.repeat(1)
# #@pytest.mark.xfail
# def test_02(psw):
#     u=psw[0]
#     p=psw[1]
#     print("测试账号：%s,密码：%s"%(u,p))
#     assert u=='yoyo1'
# if __name__=="__main__":
#     pytest.main(['-m=chrome','--reruns','2','--reruns-delay','2','--html=report.html'])












