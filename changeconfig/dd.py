import os
from xml.etree.ElementTree import ElementTree, Element
import logging

logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='newall.log',
                    filemode='w',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(levelname)s: %(message)s'
                    #日志格式
                    )
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


def get_node_by_keyvalue(nodelist, kv_map):
    '''''根据属性及属性值定位符合的节点，返回节点
    nodelist: 节点列表
    kv_map: 匹配属性及属性值map'''
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes


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


def findelement(nodelist, kv_map):
  '''''查找节点属性并返回
  nodelist: 节点列表
  kv_map:属性及属性值map'''
  for node in nodelist:
    for key in kv_map:
        if key in node.attrib:
          print("1chakey:", key)
          print(node.attrib[key])
          temp=node.attrib[key]
  return temp

def change_node_text(nodelist, text, is_add=False, is_delete=False):
    '''''改变/增加/删除一个节点的文本
    nodelist:节点列表
    text : 更新后的文本'''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text


def create_node(tag, property_map, content):
    '''''新造一个节点
    tag:节点标签
    property_map:属性及属性值map
    content: 节点闭合标签里的文本内容
    return 新节点'''
    element = Element(tag, property_map)
    element.text = content
    return element


def add_child_node(nodelist, element):
    '''''给一个节点添加子节点
    nodelist: 节点列表
    element: 子节点'''
    for node in nodelist:
        node.append(element)


def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    '''''同过属性及属性值定位一个节点，并删除之
    nodelist: 父节点列表
    tag:子节点标签
    kv_map: 属性及属性值列表'''
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                parent_node.remove(child)


def find_node_by_tagkeyvalue(nodelist, tag, kv_map):
    '''''同过属性及属性值定位一个节点，并删除之
    nodelist: 父节点列表
    tag:子节点标签
    kv_map: 属性及属性值列表'''
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                print("newpath:", child)

#
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

# KvService, UIFrame, KvTray, PackgeManager， KvState, VistaSpi,  *.sys，skin\, InfoDlg
def XMfFunc(xml_file_path):
    # 1. 读取xml文件
    xml_root = read_xml(xml_file_path)
    # 2. 属性修改
    # A. 找到父节点
    file_nodes = find_nodes(xml_root, "Config/Files/file")
    print(file_nodes)
    in_path = read_conf("package2/delete_h3c.txt")
    print("in_path:",in_path)
    # B. 通过属性准确定位子节点
    # result_nodes = get_node_by_keyvalue(file_nodes, {"newpath": "antivirus\FileGuardEx.dll"})
    # print("result:", result_nodes)
    #找到所有的<file>
    for iter_file_node in file_nodes:
        try:
            # {"newpath": "antivirus\FileGuardEx.dll"}
            attr_newpath = iter_file_node.attrib["newpath"]

            # {"path": "antivirus\FileGuardEx_h3c.dll"}
            attr_path = iter_file_node.attrib["path"]
            if attr_path in in_path:
                # 在这里过滤上面那些文件
                print("Begin to change path value, Path: {}, NewPath: {}".format(attr_path, attr_newpath))
                # 找到newpath的value
                # temp_path = findelement(iter_file_node, {"newpath": attr_newpath})
                # print("temp_path,temp_path")
                # 把path 的value 改成 newpath的value
                change_node_properties([iter_file_node], {"path": attr_newpath})
                logging.debug('change {}'.format(attr_path))
                # 删除newpath
                change_node_properties([iter_file_node], {"newpath": ""}, True)
            else:
                print("Do not need change. Filename: {}".format(attr_path))
                logging.info('{} Not change'.format(attr_path))

        except:
            print("Do not have new path. ")

    print("Change value done.")
    write_xml(xml_root, xml_file_path)

    # #C. 修改节点属性
    # change_node_properties(result_nodes, {"age": "1"})
    # #D. 删除节点属性
    # change_node_properties(result_nodes, {"value":""}, True)
    #
    # #6. 输出到结果文件
    # write_xml(tree, "xiuga1.config")
if __name__ == "__main__":
    print("System start.")
    config_dir = r"E:\ECMP\package/"
    for root, dirs, files in os.walk(config_dir):
        for iter_file in files:
            xml_file_path = os.path.join(root, iter_file)
            print("Now, working on: {}", xml_file_path)
            #logging.debug('Now,working on:{}'.format(xml_file_path))
            XMfFunc(xml_file_path)
    print("System done.")
    