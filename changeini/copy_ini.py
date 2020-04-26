#coding:utf-8
# import os
# os.system("xcopy LangOption2.ini LangOption3.ini")

"""
复制文件
"""
# import shutil
# shutil.copyfile('LangOption2.ini', 'LangOption4.ini')
print("input title:")
title =input()
print(title)


# 复制ini文件重命名
#修改内容
#coding:utf-8
import configparser
import os
copyfile="LangOption2.ini"
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath,copyfile)
print(cfgpath)
# cfg.ini的路径

# 创建管理对象
# conf = configparser.ConfigParser()
conf=configparser.RawConfigParser()
# 读ini文件
conf.read(cfgpath, encoding="utf-8")
# python3

# conf.read(cfgpath) # python2

# 获取所有的section
sections = conf.sections()

print(sections)
# 返回list
print("input title:")
title =input()
print(title)
conf.set("Language0804", "MainWindow.LanguageEnImg", "中文")  # 写入中文

conf.write(open(cfgpath, "r+", encoding="utf-8"))
# conf.remove_section('Language0802')
# conf.remove_option('Language0804', "MainWindow.Title")
# conf.write(open(cfgpath, 'a'))  # 追加模式写入
items = conf.items('Language0804')
print(items)
# list里面对象是元祖