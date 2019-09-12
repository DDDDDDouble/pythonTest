# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:41:39 2019

@author: Li Weisheng
"""

def loadDataSet():
    dataSet = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
    return dataSet


def init_c1(data_set_dict, min_support):
    c1 = []
    freq_dic = {}
    for trans in data_set_dict:
        for item in trans:
            freq_dic[item] = freq_dic.get(item, 0) + data_set_dict[trans]
    # 优化初始的集合，使不满足最小支持度的直接排除
    c1 = [[k] for (k, v) in freq_dic.items() if v >= min_support]
    c1.sort()
    return list(map(frozenset, c1))


def scan_data(data_set, ck, min_support, freq_items):
    """
    计算Ck中的项在数据集合中的支持度，剪枝过程
    :param data_set:
    :param ck:
    :param min_support: 最小支持度
    :param freq_items: 存储满足支持度的频繁项集
    :return:
    """
    ss_cnt = {}
    # 每次遍历全体数据集
    for trans in data_set:
        for item in ck:
            # 对每一个候选项集， 检查是否是 term中的一部分（子集），即候选项能否得到支持
            if item.issubset(trans):
                ss_cnt[item] = ss_cnt.get(item, 0) + 1
    ret_list = []
    for key in ss_cnt:
        support = ss_cnt[key]  # 每个项的支持度
        if support >= min_support:
            ret_list.insert(0, key)  # 将满足最小支持度的项存入集合
            freq_items[key] = support  #
    return ret_list, freq_items


def apriori_gen(lk, k):
    """
    由Lk的频繁项集生成新的候选项集  连接过程
    :param lk:  频繁项集集合
    :param k:  k 表示集合中所含的元素个数
    :return: 候选项集集合
    """
    ret_list = []
    for i in range(len(lk)):
        for j in range(i+1, len(lk)):
            l1 = list(lk[i])[:k-2]
            l2 = list(lk[j])[:k-2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                ret_list.append(lk[i] | lk[j])  # 求并集
    # retList.sort()
    return ret_list


def apriori_zc(data_set, data_set_dict, min_support):
    """
    Apriori算法过程
    :param data_set: 数据集
    :param min_support: 最小支持度，默认值 0.5
    :return:
    """
    c1 = init_c1(data_set_dict, min_support)
    print('c1 ', c1)
    data = map(set, data_set)  # 将dataSet集合化，以满足scanD的格式要求
    freq_items = {}
    l1, freq_items = scan_data(data, c1, min_support, freq_items)  # 构建初始的频繁项集
    print('l1 ', l1)
    print('frequ_items ', freq_items)
    l = [l1]
    print('l ', l)
    print('l[0] ', l[0])
    # 最初的L1中的每个项集含有一个元素，新生成的项集应该含有2个元素，所以 k=2
    k = 2
    while len(l[k - 2]) > 0:
        print('len( l[ k - 2 ] ) ', len(l[k - 2]), ' ', k - 2, '->', l[k - 2])
        print(' l[k - 2] ', l[k - 2])
        ck = apriori_gen(l[k - 2], k)
        print('ck ', ck)
        lk = scan_data(data, ck, min_support, freq_items)
        l.append(lk)
        k += 1  # 新生成的项集中的元素个数应不断增加
    print("over")
    return freq_items

if __name__ == '__main__':
    dataSet = loadDataSet()
    print(dataSet)