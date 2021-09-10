import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import os
import random
import webbrowser
stu = {}
zc = {}
def reWord(xpath):#返回一个字符串
    subinfo = browser.find_element_by_xpath(xpath)
    info = subinfo.text
    return str(info)

def sleep(t):
    time.sleep(t)

def isElementExist(xpath):
    try:
        browser.find_element_by_xpath(xpath)
        return True
    except:
        return False
def lid(name):
    wsi = 1
    while 1<2:
        dfh = browser.find_element_by_xpath('//*[@id="example"]/tbody/tr[' + str(wsi) + ']/td[3]')
        fh = dfh.text
        if name == fh:
            return wsi
            break
        wsi = wsi +1
        
def cprint(msg):
    print('[' + time.strftime("%H:%M:%S", time.localtime()) + '] ' + str(msg))

print('''
===============================================
              FUCKEEID (Ferrum)
 2020-2020 GWZKJ & log NEZHA.SPACE & EEID.ICU 
         FUCKEEID & Ferrum Foundation 
===============================================       
         FUCKEEID FOR TEACHER VER.1.5
             向所有教师工作者致敬！
===============================================
              免责协议和温馨提示
    请一定告知学生检查自己申报的材料内容
    该程序没有审核功能 不会进行检测 只会无脑通过
    造成的一切后果与作者无关 由用户自行负责
===============================================
同意按下回车：''')
inid = input()
if inid == 'm':
    print('''''')
browser = webdriver.Chrome()
i = 0
browser.get('http://zhpj.hnedu.cn/')
cprint('''===============================================
提示：
请确保在浏览器地址栏链接为zhpj.hnedu.cn/zhpj时按下回车
如果提示弱密码不要管，点按地址栏输入zhpj.hnedu.cn，会自动登录
===============================================''')
x = input("请在弹出的Chrome窗口登录你的EEID账号 然后按下回车")
teachername = browser.find_element_by_xpath('/html/body/div[1]/aside/section/div/div[2]/p').get_attribute('textContent')
cprint(teachername + '老师，您好')
cprint('5秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
sleep(1)
cprint('4秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
sleep(1)
cprint('3秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
sleep(1)
cprint('2秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
sleep(1)
cprint('1秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
sleep(1)
cprint('即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
#browser.get('http://zhpj.hnedu.cn/zhpj/verify/list_xs?shjb=1&xnxq=2019-2020,1')#直达审核页面
browser.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[10]/a').click()
browser.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[10]/ul/li/a').click()
cprint('进入审核模式 切换到审核单页')
sleep(2)
browser.switch_to_frame("contentFrame")#切换frame 切记切记切记
dn = Select(browser.find_element_by_xpath('//*[@id="spageSize"]'))
dn.select_by_value('100')
#xx = input('set100')
browser.find_element_by_xpath('//*[@id="example"]/thead/tr/th[8]').click()
i = i+1
'''
if isElementExist('//*[@id="example"]/tbody/tr['+str(i)+']/td[9]/button') == False:
    cprint('未找到任何一个学生存在审核')
    break
else:
    if int(browser.find_element_by_xpath('//*[@id="example"]/tbody/tr['+str(i)+']/td[8]/a').get_attribute('textContent')) !=0 :
        browser.find_element_by_xpath('//*[@id="example"]/tbody/tr['+str(i)+']/td[9]/button').click()
        ssname=browser.find_element_by_xpath('//*[@id="example"]/tbody/tr['+str(i)+']/td[3]').get_attribute('textContent')
        cprint('已找到父审核节 进入学生'+ssname +'审核单页')
    #time.sleep(2)
    '''
cprint("开始读取学生信息")
subinfo = browser.find_element_by_xpath('//*[@id="example_info"]')
info = subinfo.text
b = info.find('共')
a = info.rfind('项')
classnumber = int(info[b + 2:a - 1])
cprint("本次任务总人数：" + str(classnumber) + '人')
di = 1
uid = 1
while di < int(classnumber) or di == int(classnumber):
    dstrname = browser.find_element_by_xpath('//*[@id="example"]/tbody/tr[' + str(di) + ']/td[3]')
    strname = dstrname.text
    if isElementExist('//*[@id="example"]/tbody/tr[' + str(di) + ']/td[8]/a') == True:#若无审核项就不存在这个,0除外
        if reWord('//*[@id="example"]/tbody/tr[' + str(di) + ']/td[8]/a') != "0":
            ddshn = browser.find_element_by_xpath('//*[@id="example"]/tbody/tr[' + str(di) + ']/td[8]/a')
            dshn = ddshn.text
            cprint('学生' + strname + '下有 '+dshn+' 项审核项，分配uid为' + str(uid))
            zc['name'] = strname
            zc['dsh'] = int(dshn)
            stu[uid] = zc.copy()
            if strname == '罗颖泉' or strname == '陈文嘉':
                if random.randint(1,100)>30:
                    cprint('NB!')

            uid = uid + 1

    di = di + 1
    
cprint('总共分配uid' + str(uid) + '个')

si = 1
while True:
    try:
        if si == uid:
            break

        setnum = Select(browser.find_element_by_xpath('//*[@id="spageSize"]'))
        setnum.select_by_value('100')
        stuinfomat = stu[si]
        stunames = stuinfomat['name']
        stdsh = int(stuinfomat['dsh'])
        cprint('现在进行任务的学生信息:姓名：'+stunames + '待审核项：' + str(stdsh) )
        ilid = lid(stunames)
        cprint('该学生的LID为： ' + str(ilid))
        browser.find_element_by_xpath('//*[@id="example"]/tbody/tr['+str(ilid)+']/td[9]/button').click()
        cprint('已找到父审核节 进入学生'+ stunames +'审核单页')
        sleep(5)
        si = si + 1
        while stdsh != 0:
            if isElementExist('//*[@id="example_info"]') == True:
                actname=browser.find_element_by_xpath('//*[@id="example"]/tbody/tr[1]/td[2]/div').get_attribute('textContent')
                cprint('已找到审核节 准备开始审核 进入学生'+stunames +'下 '+actname+' 审核单页')
                
                browser.find_element_by_xpath('//*[@id="example"]/tbody/tr[1]/td[7]/button').click()
                sleep(1)
                browser.find_element_by_xpath('//*[@id="editForm"]/div/div/div[2]/div/input[1]').click()
                browser.switch_to.default_content()#执行底下部分的内容需切换回主窗体
                sleep(3)

                browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button').click()
                browser.switch_to_frame("contentFrame")#切换frame 切记切记切记
                sleep(1)
                try:
                    browser.find_element_by_xpath('//*[@id="editForm"]/div/div/div[2]/div/input[3]').click()
                    sleep(1)
                except:
                    cprint('未找到返回按钮 自动略过该错误')
                
                cprint('开始重载待审核配置')
                if isElementExist('//*[@id="example_info"]') == True:
                    subinfo = browser.find_element_by_xpath('//*[@id="example_info"]')
                    info = subinfo.text
                    b = info.find('共')
                    a = info.rfind('项')
                    stdsh = int(info[b + 2:a - 1])
                elif isElementExist('//*[@id="example_info"]') == False:
                    stdsh = 0
                    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[1]/div/button').click()
                    break
                
                cprint('剩余待审核'+str(stdsh)+'项')

    except:
        cprint('程序出现错误 正在准备重新执行')
        si = si - 1
        cprint('正在提取学生信息……')
        cprint('学生内部UID:'+ str(si) + " 学生姓名： "+ str(stu[si]) )
        cprint('准备重置当前操作')
        time.sleep(2)
        browser.refresh()
        browser.get('http://zhpj.hnedu.cn/')
        cprint('等待Google Chrome下载网页……')
        time.sleep(2)
        teachername = browser.find_element_by_xpath('/html/body/div[1]/aside/section/div/div[2]/p').get_attribute('textContent')
        cprint(teachername + '老师，您好')
        cprint('5秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
        sleep(1)
        cprint('4秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
        sleep(1)
        cprint('3秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
        sleep(1)
        cprint('2秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
        sleep(1)
        cprint('1秒后即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
        sleep(1)
        cprint('即将开始审核 请勿在审核操作进行时关闭本程序和操作Google Chrome浏览器')
        #browser.get('http://zhpj.hnedu.cn/zhpj/verify/list_xs?shjb=1&xnxq=2019-2020,1')#直达审核页面
        browser.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[10]/a').click()
        browser.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[10]/ul/li/a').click()
        cprint('进入审核模式 切换到审核单页')
        sleep(2)
        browser.switch_to_frame("contentFrame")#切换frame 切记切记切记
        dn = Select(browser.find_element_by_xpath('//*[@id="spageSize"]'))
        dn.select_by_value('100')
        #xx = input('set100')
        browser.find_element_by_xpath('//*[@id="example"]/thead/tr/th[8]').click()

webbrowser.open('http://118.178.225.9/?page_id=433')
cprint('已经执行完成了！')
os.system('pause')
