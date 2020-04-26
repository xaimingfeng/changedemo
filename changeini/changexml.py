import os
import shutil
from xml.etree.ElementTree import ElementTree, Element

def read_xml(in_path):
    '''''读取并解析xml文件
    in_path: xml路径
    return: ElementTree'''
    tree = ElementTree()
    tree.parse(in_path)
    return tree


def write_xml(tree, out_path):
    '''''将xml文件写出
    tree: xml树
    out_path: 写出路径'''
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


def if_match(node, kv_map):
    '''''判断某个节点是否包含所有传入参数属性
    node: 节点
    kv_map: 属性及属性值组成的map'''
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True


# ---------------search -----
def find_nodes(tree, path):
    '''''查找某个路径匹配的所有节点
    tree: xml树
    path: 节点路径'''
    return tree.findall(path)

# ---------------change -----
def change_node_properties(nodelist, kv_map, is_delete=False):
    '''''修改/增加 /删除 节点的属性及属性值
    nodelist: 节点列表
    kv_map:属性及属性值map'''
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                  print("3changekey",key)
                  del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))

def read_conf(file_path):
    file = open(file_path)
    dataMat = []
    for line in file.readlines():
        curLine = line.strip()
        # floatLine = map(float, curLine)  # 这里使用的是map函数直接把数据转化成为float类型
        if curLine.__contains__('/'):
            curLine=curLine.replace('/','\\')
        dataMat.append(curLine)
    print(dataMat)
    file.close()
    return dataMat
'''
为文件加后缀
'''
def addsuffix(str,suffix):
    str_list=list(str)
    pot = str_list.index('.')
    str_list.insert(pot, suffix)
    str2 = "".join(str_list)
    # print(str2)
    return str2

def XMfFunc(xml_file_path,file_list,file_suffix):
    # 1. 读取xml文件
    xml_root = read_xml(xml_file_path)
    # 2. 属性修改
    # A. 找到父节点
    file_nodes = find_nodes(xml_root, "Config/Files/file")
    print(file_nodes)
    #填写oem文件路径列表
    change_path = read_conf(file_list)

    print("change_path:",change_path)

    for iter_file_node in file_nodes:
        # {"path": "antivirus\FileGuardEx_h3c.dll"}
        attr_path = iter_file_node.attrib["path"]
        if attr_path in change_path:
            try:
                attr_newpath = iter_file_node.attrib["newpath"]
                # 在这里过滤上面那些文件;再修改列表里if 有newpath改newpath 没有增加 newpath
                print("要修改的文件:",attr_path)
                print("输入修改文件的1path")
                # suffix = input()
                suffix=addsuffix(attr_newpath,file_suffix)
                print("suffix:", suffix)
                change_node_properties([iter_file_node], {"path": suffix})
                # logging.debug('change {}'.format(attr_path))
            except:
                print("要修改的文件:", attr_path)
                print("输入修改文件的2path")
                # suffix = input()
                suffix=addsuffix(attr_path,file_suffix)
                print("suffix:",suffix)
                change_node_properties([iter_file_node], {"path": suffix})
                # newpath=path
                change_node_properties([iter_file_node], {"newpath": attr_path})
    print("Change value done.")
    write_xml(xml_root, xml_file_path)


def copyfile():
    shutil.copyfile('E:\ECMP\Product\\KVClientPack_offLine_AV_std3n1.bat',
                    'E:\ECMP\\Product\KVClientPack_offLine_AV_std3n1_zcah.bat')
    shutil.copyfile('E:\ECMP\Product\\Product_OffLine_AV_std3n1.config',
                    'E:\ECMP\Product\Product_OffLine_AV_std3n1_zcah.config')

    shutil.copyfile('E:\ECMP\package\\avui_std3n1.config', 'E:\ECMP\package\\avui_std3n1_zcah.config')
    shutil.copyfile('E:\ECMP\package\\base_std.config', 'E:\ECMP\package\\base_std_zcah.config')
    shutil.copyfile('E:\ECMP\package\\antivirus_std.config', 'E:\ECMP\package\\antivirus_zcah.config')
    shutil.copyfile('E:\ECMP\package\\setup_std3n1.config', 'E:\ECMP\package\\setup_std3n1_zcah.config')
    shutil.copyfile('E:\ECMP\BuildTools\SetupMaker_std3n1.ini', 'E:\ECMP\BuildTools\\SetupMaker_std3n1_zcah.ini')





if __name__ == '__main__':
    #复制配置文件
    # copyfile()
    #依次修改配置文件中file path
    XMfFunc("E:\FT\\avui_std3n1.config","E:\FT\\ui_list.txt","_zcah")