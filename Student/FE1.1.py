import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import datetime
import configparser
import os
import GPBT
import random,getpass
import hashlib
import pandas
#常量赋值部分
nyear = datetime.datetime.now().year
nmonth = datetime.datetime.now().month
nday = datetime.datetime.now().day
apploc = str(os.getcwd())
ver = "1.0.1"#版本号
#定义部分
config = configparser.ConfigParser()
isexcelexist = False
#变量初始化
global con1
inf1={}
inf2={}
inf3={}
inf4={}
inf5={}
con1 = {}
autosetting={}
contentreader = {}
contentlist = {}
acinfo = {}
paid = False
data = []#诗词数据库 存储诗词内容
stname = []
stid = []
stpwd = []
request = []
#Sdata = {}#诗词暂存库 打包诗词内容并添加到数据库
sq = False
#自定义函数 
def isElementExist(xpath):
    try:
        browser.find_element_by_xpath(xpath)
        return True
    except:
        return False
def cprint(msg):
    print('[' + time.strftime("%H:%M:%S", time.localtime()) + '] ' + str(msg))
def msleep(timee,title):
    st = 0
    while st < timee:
        cprint(str(int(timee) - st) +' 秒后将' + title)
        time.sleep(1)
        st = st + 1
def checkgabage():
    while True:
        wi = 0
        browser.get('http://zhpj.hnedu.cn/zhpj/lxSbSh/lxlist?lxzt=0&pageList.orderBy=cjsj&pageList.sort=desc')
        cprint('wait the website loading.....')
        time.sleep(3)
        if isElementExist('//*[@id="example_info"]') == False:
            cprint('没有残留遴选项需要删除')
            break
        time.sleep(3)
        try:
            subinfo = browser.find_element_by_xpath('//*[@id="example_info"]')
            info = subinfo.text
            b = info.find('共')
            a = info.rfind('项')
            classnumber = int(info[b + 2:a - 1])
            cprint('5 s后即将开始 已检测存在 ' + str(classnumber) + ' 项待删除项')
            time.sleep(5)
            while classnumber > 0 :
                wi = wi + 1
                cprint('等待网页加载')
                time.sleep(2)
                try:
                    subinfo = browser.find_element_by_xpath('//*[@id="example_info"]')
                    info = subinfo.text
                    b = info.find('共')
                    a = info.rfind('项')
                    classnumber = int(info[b + 2:a - 1])
                    cprint('已经重读取剩余项 剩余 '+str(classnumber)+' 项')
                except:
                    break

                cprint('正在删除 ')
                cprint('现在正在删除第 '+ str(wi) + ' 项')
                browser.find_element_by_xpath('//*[@id="example"]/tbody/tr[1]/td[5]/button[3]').click()
                cprint('等待确认提示')
                time.sleep(2)
                browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click()
                cprint('等待网页重载')
                time.sleep(2)
                cprint('已操作 '+ str(wi) + ' 项')
            
            break
        except:
            cprint('删除操作存在异常 正在处理……')
            msleep(5,'重试')

def pause():
    os.system('pause')

def sx(name,founder,start,end,actid,foundertype,content,pic):#思想品德活动管理
    browser.get('http://zhpj.hnedu.cn/zhpj/sxpdHdjl/update?id=')
    browser.find_element_by_xpath('//*[@id="file"]').send_keys(pic)
    print('正在等待图片上传完成')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="hdmc"]').send_keys(name)#活动名称
    browser.find_element_by_xpath('//*[@id="zzjg"]').send_keys(founder)#活动单位
    browser.find_element_by_xpath('//*[@id="ksrq"]').send_keys(start)#开始时间
    browser.find_element_by_xpath('//*[@id="jsrq"]').send_keys(end)#结束时间
    se1 = Select(browser.find_element_by_xpath('//*[@id="hdlx"]'))
    se1.select_by_value(actid)#1001001党员 002志愿 003公益 004社团
    se2 = Select(browser.find_element_by_xpath('//*[@id="jb"]'))
    se2.select_by_value(foundertype)#1001班级 1002学校 1003区 1004市 1005省
    browser.find_element_by_xpath('//*[@id="msysm"]').send_keys(content)
    browser.find_element_by_xpath('//*[@id="editForm"]/div/div/div/div/div/div/div[2]/div/div[13]/div/input[1]').click()
def rcxg(name,founder,start,foundertype,content,pic):
    browser.get('http://zhpj.hnedu.cn/zhpj/sxjkRcxgjl/update?id=')#身心健康日常习惯管理
    browser.find_element_by_xpath('//*[@id="file"]').send_keys(pic)
    print('正在等待图片上传完成')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="mc"]').send_keys(name)#活动名称
    browser.find_element_by_xpath('//*[@id="dw"]').send_keys(founder)#活动单位
    browser.find_element_by_xpath('//*[@id="jlsj"]').send_keys(start)#开始时间
    #browser.find_element_by_xpath('//*[@id="jsrq"]').send_keys(end)#结束时间
    #se1 = Select(browser.find_element_by_xpath('//*[@id="hdlx"]'))
    #se1.select_by_value(actid)#1001001党员 002志愿 003公益 004社团
    se2 = Select(browser.find_element_by_xpath('//*[@id="jb"]'))
    se2.select_by_value(foundertype)#1001班级 1002学校 1003区 1004市 1005省
    browser.find_element_by_xpath('//*[@id="msysm"]').send_keys(content)
    browser.find_element_by_xpath('//*[@id="editForm"]/div/div/div/div/div/div/div[2]/div/div[11]/div/input[1]').click()
def jsgl(name,founder,start,foundertype,content,pic):#学业水平竞赛管理
    browser.get('http://zhpj.hnedu.cn/zhpj/xyspJsjl/update?id=')
    browser.find_element_by_xpath('//*[@id="file"]').send_keys(pic)
    print('正在等待图片上传完成')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="jshjmc"]').send_keys(name)#活动名称
    browser.find_element_by_xpath('//*[@id="dw"]').send_keys(founder)#活动单位
    browser.find_element_by_xpath('//*[@id="jlsj"]').send_keys(start)#开始时间
    #browser.find_element_by_xpath('//*[@id="jsrq"]').send_keys(end)#结束时间
    #se1 = Select(browser.find_element_by_xpath('//*[@id="hdlx"]'))
    #se1.select_by_value(actid)#1001001党员 002志愿 003公益 004社团
    se2 = Select(browser.find_element_by_xpath('//*[@id="jb"]'))
    se2.select_by_value(foundertype)#1001班级 1002学校 1003区 1004市 1005省
    browser.find_element_by_xpath('//*[@id="msysm"]').send_keys(content)
    browser.find_element_by_xpath('//*[@id="editForm"]/div/div/div/div/div/div/div[2]/div/div[11]/div/input[1]').click()
def shsj(name,founder,start,end,actid,foundertype,content,pic):#社会实践活动管理
    browser.get('http://zhpj.hnedu.cn/zhpj/shsjSjhdjl/update?id=')
    browser.find_element_by_xpath('//*[@id="file"]').send_keys(pic)
    print('正在等待图片上传完成')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="hdmc"]').send_keys(name)#活动名称
    browser.find_element_by_xpath('//*[@id="jgmc"]').send_keys(founder)#活动单位
    browser.find_element_by_xpath('//*[@id="ksrq"]').send_keys(start)#开始时间
    browser.find_element_by_xpath('//*[@id="jsrq"]').send_keys(end)#结束时间
    se1 = Select(browser.find_element_by_xpath('//*[@id="lx"]'))
    se1.select_by_value(actid)#1001001党员 002志愿 003公益 004社团
    se2 = Select(browser.find_element_by_xpath('//*[@id="jb"]'))
    se2.select_by_value(foundertype)#1001班级 1002学校 1003区 1004市 1005省
    browser.find_element_by_xpath('//*[@id="msysm"]').send_keys(content)
    browser.find_element_by_xpath('//*[@id="editForm"]/div/div/div/div/div/div/div[2]/div/div[13]/div/input[1]').click()


def login(id,pwd):
    browser.switch_to.frame('login_iframe')
    browser.find_element_by_xpath('//*[@id="username"]').send_keys(id)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="login-submit"]').click()
    time.sleep(1)
    try:
        subinfo = browser.find_element_by_xpath('/html/body/div[3]/div')
        info = subinfo.text
        if info == '请输入账号' or info == '请输入密码':
            return 401#401：缺少凭据
        elif info == '密码错误' or info == 'EEID或手机号不存在':
            return 402#凭据错误
        else:
            return 403#意外错误导致的登录失败
    except:
        title = browser.title
        if title == '普通高中综合素质评价':
            return 200
    browser.switch_to.default_content()

def lx():
    while True:
        wi = 0
        browser.get('http://zhpj.hnedu.cn/zhpj/lxSbSh/lxlist?lxzt=0&pageList.orderBy=cjsj&pageList.sort=desc')
        cprint('wait the website loading.....')
        time.sleep(3)
        try:
            subinfo = browser.find_element_by_xpath('//*[@id="example_info"]')
            info = subinfo.text
            b = info.find('共')
            a = info.rfind('项')
            classnumber = int(info[b + 2:a - 1])
            cprint('5 s后即将开始 已检测存在 ' + str(classnumber) + ' 项待遴选项')
            time.sleep(5)
            while classnumber > 0 :
                wi = wi + 1
                cprint('等待网页加载')
                time.sleep(2)
                try:
                    subinfo = browser.find_element_by_xpath('//*[@id="example_info"]')
                    info = subinfo.text
                    b = info.find('共')
                    a = info.rfind('项')
                    classnumber = int(info[b + 2:a - 1])
                    cprint('已经重读取剩余项 剩余 '+str(classnumber)+' 项')
                except:
                    break

                cprint('正在遴选 ')
                cprint('现在正在遴选第 '+ str(wi) + ' 项')
                browser.find_element_by_xpath('//*[@id="example"]/tbody/tr[1]/td[5]/button[4]').click()
                cprint('等待确认提示')
                time.sleep(2)
                browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click()
                cprint('等待网页重载')
                time.sleep(2)
                cprint('已操作 '+ str(wi) + ' 项')
            
            break
        except:
            cprint('遴选操作存在异常 正在处理……')
            msleep(5,'重试')
def submit():
    browser.get('http://zhpj.hnedu.cn/zhpj/lxSbSh/sblist?sbzt=0&pageList.orderBy=cjsj&pageList.sort=desc&xnxq=')
    browser.switch_to.default_content()
    browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[1]/div/button[1]').click()
    time.sleep(3)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click()

def main():
    #读取配置文件
    time.sleep(2)
    cprint('为防止程序出现错误 正在检查错误……')
    cprint('清除的材料都是因为早期综测平台材料数目限制导致的垃圾材料，超过编辑时效无法使用，只得废弃。Ferrum会尽量保证所上报材料有效')
    checkgabage()
    time.sleep(2)
    h = int(con1['constart'])
    while h < int(con1['conend']) + 1:
        nowsetting = autosetting[h]
        if int(nowsetting['class']) == 1:
            cprint('现在进行的是第' + str(h) + '项活动，类别思想品德')
            if int(nowsetting['isgpbt']) == 1:
                cprint('已经设置使用狗屁不通生成器生成')
                contentw = GPBT.gpbt(nowsetting['actname'])
                content = contentw[:200]
            else:
                nowcontent = contentlist[h]
                contentnum = int(nowsetting['contentnum'])
                cprint('正在生成该部分的特征码，请稍后……')
                if contentnum < 5:
                    cprint('描述段数小于五段，启动随机组合模式……')
                    tzm = random.randint(1,contentnum)
                    cprint('特征码为：' + str(tzm) + '-GPBT')
                    contentw = nowcontent[tzm] + GPBT.gpbt(nowsetting['actname'])
                    content = contentw[:200]
                else:
                    tzm1 = random.randint(1,contentnum)
                    tzm2 = random.randint(1,contentnum)
                    tzm3 = random.randint(1,contentnum)
                    tzm4 = random.randint(1,contentnum)
                    cprint('特征码为：')
                    print(tzm1,tzm2,tzm3,tzm4,sep="-")
                    contentw = nowcontent[tzm1] + nowcontent[tzm2] + nowcontent[tzm3] + nowcontent[tzm4]
                    if len(contentw) > 200:
                        content = contentw[:200]
                    else:
                        content = contentw

            cprint('生成的描述为:' + content)

            tpm = random.randint(int(nowsetting['picstart']),int(nowsetting['picstop']))#输入图片码
            cprint('图片特征码为：'+str(tpm))
            pic = apploc +'\\'+ str(tpm) + '.jpg'
            if os.path.exists(pic) == True:#检测图片是否存在
                cprint('Ferrum学生客户端提醒您：位于 ' + pic + ' 图片本地合法性已通过，但请自行甄别图片内容')
            else:
                cprint('该图片不存在！')
                pic = ""
                raise Exception('FE-PICERROR Ferrum学生客户端所选图片不存在')

            msleep(5,'进行操作')
            while True:
                try:
                    sx(nowsetting['actname'],nowsetting['group'],nowsetting['time1'],nowsetting['time2'],nowsetting['select1'],nowsetting['select2'],content,pic)
                    time.sleep(2)
                    break
                except:
                    cprint('出现意外错误，正在准备重新完成该部分操作')
                    msleep(5,'重试该部分操作')

        elif int(nowsetting['class']) == 2:
            cprint('现在进行的是第' + str(h) + '项活动，类别日常习惯管理')
            if int(nowsetting['isgpbt']) == 1:
                cprint('已经设置使用狗屁不通生成器生成')
                contentw = GPBT.gpbt(nowsetting['actname'])
                content = contentw[:200]
            else:
                nowcontent = contentlist[h]
                contentnum = int(nowsetting['contentnum'])
                cprint('正在生成该部分的特征码，请稍后……')
                if contentnum < 5:
                    cprint('描述段数小于五段，启动随机组合模式……')
                    tzm = random.randint(1,contentnum)
                    cprint('特征码为：' + str(tzm) + '-GPBT')
                    contentw = nowcontent[tzm] + GPBT.gpbt(nowsetting['actname'])
                    content = contentw[:200]
                else:
                    tzm1 = random.randint(1,contentnum)
                    tzm2 = random.randint(1,contentnum)
                    tzm3 = random.randint(1,contentnum)
                    tzm4 = random.randint(1,contentnum)
                    cprint('特征码为：')
                    print(tzm1,tzm2,tzm3,tzm4,sep="-")
                    contentw = nowcontent[tzm1] + nowcontent[tzm2] + nowcontent[tzm3] + nowcontent[tzm4]
                    if len(contentw) > 200:
                        content = contentw[:200]
                    else:
                        content = contentw
            
            cprint('生成的描述为:' + content)

            tpm = random.randint(int(nowsetting['picstart']),int(nowsetting['picstop']))#输入图片码
            cprint('图片特征码为：'+str(tpm))
            pic = apploc +'\\'+ str(tpm) + '.jpg'
            if os.path.exists(pic) == True:#检测图片是否存在
                cprint('Ferrum学生客户端提醒您：位于 ' + pic + ' 图片本地合法性已通过，但请自行甄别图片内容')
            else:
                cprint('该图片不存在！')
                pic = ""
                raise Exception('FE-PICERROR Ferrum学生客户端所选图片不存在')

            while True:
                try:
                    rcxg(nowsetting['actname'],nowsetting['group'],nowsetting['time1'],nowsetting['select2'],content,pic)
                    time.sleep(2)
                    break
                except:
                    cprint('出现意外错误，正在准备重新完成该部分操作')
                    msleep(5,'重试该部分操作')

        elif int(nowsetting['class']) == 3:
            cprint('现在进行的是第' + str(h) + '项活动，类别竞赛管理')
            if int(nowsetting['isgpbt']) == 1:
                cprint('已经设置使用狗屁不通生成器生成')
                contentw = GPBT.gpbt(nowsetting['actname'])
                content = contentw[:200]
            else:
                nowcontent = contentlist[h]
                contentnum = int(nowsetting['contentnum'])
                cprint('正在生成该部分的特征码，请稍后……')
                if contentnum < 5:
                    cprint('描述段数小于五段，启动随机组合模式……')
                    tzm = random.randint(1,contentnum)
                    cprint('特征码为：' + str(tzm) + '-GPBT')
                    contentw = nowcontent[tzm] + GPBT.gpbt(nowsetting['actname'])
                    content = contentw[:200]
                else:
                    tzm1 = random.randint(1,contentnum)
                    tzm2 = random.randint(1,contentnum)
                    tzm3 = random.randint(1,contentnum)
                    tzm4 = random.randint(1,contentnum)
                    cprint('特征码为：')
                    print(tzm1,tzm2,tzm3,tzm4,sep="-")
                    contentw = nowcontent[tzm1] + nowcontent[tzm2] + nowcontent[tzm3] + nowcontent[tzm4]
                    if len(contentw) > 200:
                        content = contentw[:200]
                    else:
                        content = contentw
            
            cprint('生成的描述为:' + content)

            tpm = random.randint(int(nowsetting['picstart']),int(nowsetting['picstop']))#输入图片码
            cprint('图片特征码为：'+str(tpm))
            pic = apploc +'\\'+ str(tpm) + '.jpg'
            if os.path.exists(pic) == True:#检测图片是否存在
                cprint('Ferrum学生客户端提醒您：位于 ' + pic + ' 图片本地合法性已通过，但请自行甄别图片内容')
            else:
                cprint('该图片不存在！')
                pic = ""
                raise Exception('FE-PICERROR Ferrum学生客户端所选图片不存在')
                
            while True:
                try:
                    jsgl(nowsetting['actname'],nowsetting['group'],nowsetting['time1'],nowsetting['select2'],content,pic)
                    time.sleep(2)
                    break
                except:
                    cprint('出现意外错误，正在准备重新完成该部分操作')
                    msleep(5,'重试该部分操作')
            
        elif int(nowsetting['class']) == 4:
            cprint('现在进行的是第' + str(h) + '项活动，类别学期实践活动')
            if int(nowsetting['isgpbt']) == 1:
                cprint('已经设置使用狗屁不通生成器生成')
                contentw = GPBT.gpbt(nowsetting['actname'])
                content = contentw[:200]
            else:
                nowcontent = contentlist[h]
                contentnum = int(nowsetting['contentnum'])
                cprint('正在生成该部分的特征码，请稍后……')
                if contentnum < 5:
                    cprint('描述段数小于五段，启动随机组合模式……')
                    tzm = random.randint(1,contentnum)
                    cprint('特征码为：' + str(tzm) + '-GPBT')
                    contentw = nowcontent[tzm] + GPBT.gpbt(nowsetting['actname'])
                    content = contentw[:200]
                else:
                    tzm1 = random.randint(1,contentnum)
                    tzm2 = random.randint(1,contentnum)
                    tzm3 = random.randint(1,contentnum)
                    tzm4 = random.randint(1,contentnum)
                    cprint('特征码为：')
                    print(tzm1,tzm2,tzm3,tzm4,sep="-")
                    contentw = nowcontent[tzm1] + nowcontent[tzm2] + nowcontent[tzm3] + nowcontent[tzm4]
                    if len(contentw) > 200:
                        content = contentw[:200]
                    else:
                        content = contentw
            
            cprint('生成的描述为:' + content)

            tpm = random.randint(int(nowsetting['picstart']),int(nowsetting['picstop']))#输入图片码
            cprint('图片特征码为：'+str(tpm))
            pic = apploc +'\\'+ str(tpm) + '.jpg'
            if os.path.exists(pic) == True:#检测图片是否存在
                cprint('Ferrum学生客户端提醒您：位于 ' + pic + ' 图片本地合法性已通过，但请自行甄别图片内容')
                time.sleep(2)
            else:
                cprint('该图片不存在！')
                pic = ""
                raise Exception('FE-PICERROR Ferrum学生客户端所选图片不存在')


            while True:
                try:
                    shsj(nowsetting['actname'],nowsetting['group'],nowsetting['time1'],nowsetting['time2'],nowsetting['select1'],nowsetting['select2'],content,pic)
                    time.sleep(2)
                    break
                except:
                    cprint('出现意外错误，正在准备重新完成该部分操作')
                    msleep(5,'重试该部分操作')

        h = h + 1
    lx()
    submit()
    sq = False
    cprint('操作已经完成！')
    time.sleep(2)
    browser.quit()

#测试部分代码
connumber = 0
contentreader = {}
dtp = ""



#FE时间电子围栏。
if os.path.exists('FE_COF.ini') == False:
    f= open("FE_COF.ini","w+",encoding='utf-8')
    print('这是你第一次启动Ferrum学生客户端，记得更改配置文件哦，配置文件在本目录的FE_COF.ini')
    config.add_section('FUCKEEID')
    config.set('FUCKEEID','ver',ver)
    config.set('FUCKEEID','constart','1')
    config.set('FUCKEEID','conend','1')
    config.write(f)
if os.path.exists('EEID.csv') == True:
    cprint('Ferrum检测到本目录存在学生ID表 使用团体账号可以自动登录哦')
    isexcelexist = True
    df = pandas.read_csv('EEID.csv',encoding ='gbk')
    listn = df.values.tolist()
    listlen = len(listn)
    cprint('正在预读取文件……')
    j = 0
    while j < listlen :
        now = listn[j]
        stname.append(now[0])#学生姓名
        stid.append(now[1])#学生账号
        stpwd.append(now[2])#学生密码
        print('预读取' + stname[j] + '成功')
        j = j + 1

config.read(apploc + '/FE_COF.ini',encoding='utf-8')
con1 = {'ver':config.get('FUCKEEID','ver'),'constart':config.getint('FUCKEEID','constart'),'conend':config.getint('FUCKEEID',"conend")}
i = con1['constart']
while i <con1['conend'] + 1:
    try:
        cprint('正在读取配置文件：' + apploc + '\\'+str(i)+'.ini')
        config.read(apploc + '\\'+str(i)+'.ini',encoding='utf-8')
        autosetting[i] = {'class':config.get('FUCKEEID','活动类别'),'actname':config.get('FUCKEEID','名称'),'isgpbt':config.get('FUCKEEID','是否使用狗屁不通生成'),'group':config.get('FUCKEEID','单位'),'time1':config.get('FUCKEEID',"时间1"),'time2':config.get('FUCKEEID','时间2'),'select1':str(config.getint('FUCKEEID',"选择框1")),'select2':str(config.getint('FUCKEEID',"选择框2")),'picstart':config.getint('FUCKEEID',"图片开始"),'picstop':config.getint('FUCKEEID',"图片结束"),'picnameadd':config.get('FUCKEEID',"图片文件前缀"),'contentnum':config.getint('FUCKEEID',"描述段数")}
        if int(config.get('FUCKEEID','是否使用狗屁不通生成')) == 0:
            connumber = config.get('FUCKEEID','描述段数')
            j = 1
            while j<int(connumber) + 1 :
                contentreader[j] = config.get('content',str(j))
                j=j+1
            
        contentlist[i] = contentreader
        contentreader = {}
        
        i = i+1
    except:
        cprint('读取配置文件失败，请检查配置文件是否存在')
        cprint('Windows10电脑有一定几率存储配置文件不在根目录，按任意键为您打开存储目录……')
        pause()
        os.system('explorer "'+apploc+'"')
        exit()

print('''
=======================
选择
    1 一个人登录（保证无EEID.csv后选择）
    2 一堆人一起登录
=======================
请键入指定数字……
''')
f2 = int(input())
si = 0
while True:
    cprint('即将运行软件……')
    browser = webdriver.Chrome()
    browser.get('http://zhpj.hnedu.cn/')
    if isexcelexist == True:
        cprint('正在进行学生' + stname[si]+'的操作……')
        code = login(stid[si],stpwd[si])
        if code == 200:
            cprint('登录成功')
            request.append('登录成功')
            main()
        elif code == 401 or code == 402:
            request.append('凭据错误')
            cprint('登录出错：登录凭据错误')
            browser.quit()
        else:
            request.append('未知错误')
            cprint('登录出错：未知错误')
            browser.quit()
        si = si + 1
        sumlen = len(stname) - 1
        if si > sumlen:
            cprint('已全部执行完毕 正在写入数据')
            dataframe = pandas.DataFrame({'学生姓名':stname,'学生EEID':stid,'状态':request})
            dataframe.to_csv("result.csv",encoding ='gbk')
            cprint("保存成功！")
            cprint('出错记录和团体账号执行日志以及保存至Result.csv。')
            pause()
            
            break
    else:
        cprint("请在弹出的Chrome窗口登录你的EEID账号 然后按下回车")
        pause()
        main()
    if f2 == 1 or f2 == 3:
        break
    elif f2 == 2 and isexcelexist == False:
        cprint('10秒后将进行下一次扣费运行,如果无需下一步请关闭……')
        time.sleep(10)





''''
start.rcxg("test","test","2020-01-06","1001","",'D:\\1.png')
print("已完成一项操作")
start.jsgl('test','test','2020-01-09','1001',"",'D:\\1.png')
start.shsj('test','test','2020-01-07','2020-02-04','1001001','1002','test','D:\\1.png')
'''
#=========================================
#               FUCKEEID
#            gwzkj & log 2020-2020
#Base on Python 3.6 designed by gwzkj&log
#=========================================
#感谢列表：
#罗颖泉 刘宇杰 阳卓成 邬亿舒 赵凯言 张攸浩
#刘兰   谭诗婷 欧阳菁 易征   阳宇轩 王琛 
#段晨宇 李博  
#致敬：
#埃隆·马斯克 尼古拉·特斯拉 比尔·盖茨 贾跃亭
#
#杨宇 易巧 《哪吒之魔童降世》 《西虹市首富》
#
#
#
