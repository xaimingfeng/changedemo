# coding:utf-8
import configparser
import os
import shutil

#复制文件
def copyfile():
    print("输入复制文件路径和文件名")
    filepath=input()
    print("输入文件名:")
    copypath=input()
    shutil.copyfile(filepath, copypath)
    return copypath

def change_langini(copypath):
    curpath = os.path.dirname(os.path.realpath(__file__))
    cfgpath = os.path.join(curpath,copypath)
    # cfg.ini的路径
    print(cfgpath)


    # 创建管理对象
    # conf = configparser.ConfigParser()
    conf = configparser.RawConfigParser()
    # 读ini文件
    conf.read(cfgpath, encoding="utf-8")
    # 获取所有的section
    sections = conf.sections()
    print(sections)
    # 返回list

    #修改首页
    print("input title,about title,,splited by:")
    titlemain,title,statebar,= input().split(',')
    print(titlemain,title,statebar)
    conf.set("Language0804", "MainWindow.TitleMain", titlemain)  # 写入中文
    conf.set("Language0804", "mainwindow.title", title)  # 写入中文
    conf.set("Language0804", "mainwindow.title.statebar", statebar)  # 写入中文

    #修改关于
    print("input about_title,companname,copyright,splited by")
    atitle,companyname,copyright=input().split(',')
    conf.set("Language0804", "AboutDlg.Title", atitle)  # 写入中文
    conf.set("Language0804", "AboutDlg.CompanyName", companyname)  # 写入中文
    conf.set("Language0804", "AboutDlg.CopyRight", copyright)  # 写入中文

    conf.write(open(cfgpath, "r+", encoding="utf-8"))

    items = conf.items('Language0804')
    print(items)
    # list里面对象是元祖


def change_Trayini(copypath):
    curpath = os.path.dirname(os.path.realpath(__file__))
    cfgpath = os.path.join(curpath, copypath)
    print(cfgpath)
    # cfg.ini的路径
    # 创建管理对象
    conf = configparser.RawConfigParser()
    # 读ini文件
    conf.read(cfgpath, encoding="utf-8")
    # 获取所有的section
    sections = conf.sections()
    print(sections)
    # 返回list

    # 修改首页
    print("input title,about title,,splited by:")
    titlemain, title, statebar, = input().split(',')
    print(titlemain, title, statebar)
    conf.set("Language0804", "KVTray.Tip", titlemain)  # 写入中文
    conf.set("Language0804", "KVTray.Title", title)  # 写入中
    conf.write(open(cfgpath, "r+", encoding="utf-8"))

    items = conf.items('Language0804')
    print(items)
    # list里面对象是元祖

if __name__ == '__main__':
    #复制lang**.ini文件
    langepath=copyfile()
    #修改lang**.ini文件
    change_langini(langepath)
    #复制\修改托盘文件
    traypath=copyfile()
    change_Trayini(traypath)






