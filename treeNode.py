# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:46:11 2019

@author: Li Weisheng
"""



class treeNode:
    def __init__(self, name_value, num_occur, parent_node):
        self.name = name_value  # 节点元素名称
        self.count = num_occur  # 出现的次数
        self.node_link = None  # 指向下一个相似节点的指针，默认为None
        self.parent = parent_node  # 指向父节点的指针
        self.children = {}  # 指向孩子节点的字典 子节点的元素名称为键，指向子节点的指针为值

    def increase(self, num_occur):
        """
        增加节点的出现次数
        :param num_occur: 增加数量
        :return:
        """
        self.count += num_occur

    def disp(self, ind=1):
        print ('  ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind + 1)


if __name__ == '__main__':
    rootNode = treeNode('这是父节点',9,None)
    rootNode.children['这是子节点'] =  treeNode('这是子节点',13,None)
    rootNode.disp()
    rootNode.children['这是另一个子节点'] = treeNode('这是另一个子节点', 3, None)
    rootNode.disp()
    print(rootNode.children)
    print(rootNode.parent)