


#数值属性布局里属性定位
menu_name = '//*[@id="node-menu"]/ul/li[1]/input'
menu_countvalue = "//*[@id='node-menu']/ul/li[2]/input"
menu_qzcount = "//*[@id='node-menu']/ul/li[3]/input"
menu_confirmbtn = '//*[@id="confirm-btn"]'
menu_calcubtn='//*[@id="compute"]'
zk_ele='//*[@id="node-menu"]/div[2]/span'
calmethod_ele=['//*[@id="normal"]','//*[@id="weights"]','//*[@id="function"]','//*[@id="script"]','//*[@id="conversion"]']
func_ele='//*[@id="function-type"]'
coversion_ele='//*[@id="conversion-type"]'
coversion_input_ele='//*[@id="node-menu"]/div[3]/div[3]/div[2]/ul/li'
add_btn_ele='//*[@id="add-interval"]'
reduce_btn_ele='//*[@id="reduce-interval"]'
select_name=['SUM','AVERAGE','MAX','MIN','INTERVAL']
#脚本输入框
menu_script="//*[@id='script-contain']"
attr=['xpath','css selector','id','name','class']
#根节点的元素定位
value_top="//*[@id='kity_text_22']"
#下级按钮元素 定位
value_down="/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[2]/span[1]"
#删除按钮元素 定位
value_del="/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[5]/span[1]"
#同级 按钮元素 定位
value_leveltoo="/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[3]/span[1]"
#前移按钮
value_foward='/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/span[1]'
#后移按钮
value_back='/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[4]/span[1]'
#上级
value_par='/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/div[6]/span[1]'
#撤销
value_chexiao='/html/body/div[1]/div[3]/div[2]/div[1]/div[4]/div[1]/span[1]'
#重做
value_redo='/html/body/div[1]/div[3]/div[2]/div[1]/div[4]/div[2]/span[1]'
#优先级
value_p='/html/body/div[1]/div[3]/div[2]/div[1]/div[4]/div[3]/span[1]'
#进度
value_d='/html/body/div[1]/div[3]/div[2]/div[1]/div[4]/div[4]/span[1]'
#P1级
value_p1='/html/body/div[1]/div[3]/div[2]/div[2]/div[3]/div[1]/span[1]'
#G0
value_g0='/html/body/div[1]/div[3]/div[2]/div[3]/div[3]/div[1]/span[1]'
import_out_ele=['/html/body/h1/a[2]']
import_in_ele=['//*[@id="fileInput"]']

#脚本插入按钮
scr_insert='//*[@id="script-menu"]/li'
insert_name='//*[@id="script-children-list"]/li'
##################################################test_weightsevaute.py     test_funceva.py       test_outimportin.py######################################
#节点1/节点2，节点3，节点4，
levelele=["//*[@id='kity_text_34']","//*[@id='kity_text_43']","//*[@id='kity_text_52']","//*[@id='kity_text_61']"]
levelele_2=['//*[@id="kity_text_70"]','//*[@id="kity_text_79"]','//*[@id="kity_text_88"]','//*[@id="kity_text_97"]','//*[@id="kity_text_106"]','//*[@id="kity_text_150"]']

reqTotal_ele=["//*[@id='kity_text_85']",'//*[@id="kity_text_46"]']
line_ele=['//*[@id="kity_text_88"]','//*[@id="kity_text_192"]','//*[@id="kity_text_140"]']

levelcon=['测试节点1',"测试节点2","测试节点3","测试节点4",'','测试节点4@!']
level2con=['测试节点11','测试节点12','测试节点21','测试节点22','测试节点31']
levelqz=['0.4','0.2','0.3','0.1','','0.3001','0.0999','-0.2','0','0.55454','0.09','0.1a']
levelqz2=['','','0.6','0.4','']
levelsz=['10','20','30','40','','0','-20.45','20.455','20.45','40a','20.46']
levelsz2=['10.11','20','88','30.25','100.99']

expected_func=['100.0(F)','25.0(F)','10.0(F)','40.0(F)','20.46(F)']
expected_weights=['21.0(W)','20.0(W)','19.05(W)','17.0(W)','25.0(F)','14.96(W)']
expected_message=['节点权重值之和不为1','格式错误','不能为空','格式错误','请填写节点名称','名称有重复']




#######################################test_script############################################################################################################
script1='if(#测试节点1#>=1&#测试节点1#<=4){return 3}else if(#测试节点2#>4){return (#测试节点2#+4)/2*3}else if(#测试节点4#>5){return  -10}else if(#测试节点4#>5){return  -1000}'
script2='if(#测试节点6#>=1&#测试节点1#<=4){return 3}else if(#测试节点2#>4){return (#测试节点2#+4)/2*3}else if(#测试节点4#>5){return  -10}else if(#测试节点4#>5){return  -1000}'
script3='if(##>=1&#测试节点1#<=4){return 3}else if(#测试节点2#>4){return (#测试节点2#+4)/2*3}else if(#测试节点4#>5){return  -10}else if(#测试节点4#>5){return  -1000}'
script4='if(#测试节点1#>=1&#测试节点1#<=4){return 3}else if(#测试节点2#>4){return -1.567}else if(#测试节点4#>5){return  -10}else if(#测试节点4#>5){return  -1000}'
script5='if(#测试节点1#>=1&#测试节点1#<=4){return 3}elseif(#测试节点2#>4){return (#测试节点2#+4)/2*3}else if(#测试节点4#>5){return  -10}else if(#测试节点4#>5){return  -1000}'
script6='if(#测试节点11#>=1&#测试节点11#<=4){return 3}else if(#测试节点12#>4){return (#测试节点12#+4)/2*3}else if(#测试节点12#>5){return  -10}else if(#测试节点12#>5){return  -1000}'
expected_script=['36.0(S)','找不到','不能为空','-1.57(S)','脚本错误']



######################################test_modify###############################
levelmodify=['//*[@id="kity_text_157"]','//*[@id="kity_text_38"]','//*[@id="kity_text_99"]','//*[@id="kity_text_101"]','//*[@id="kity_text_34"]']
expected_modify=['83.0(W)','370.0(F)']
