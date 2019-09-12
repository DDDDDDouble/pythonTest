# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:53:26 2019

@author: Li Weisheng
"""

import matplotlib.pyplot as plt
import FP_growth
import apriori_duibi
import eclat
import time


def loadDblpData(inFile, flag=' ', row_num=1):
    '''
    加载dblp的数据
    :param inFile:
    :return:
    '''
    dataSetDict = {}
    dataSet = []
    count = 0
    for line in inFile:
        # if count > row_num:
        #     break
        #line = line.strip().split(':')
        line = line.strip().split(flag)
        dataSet.append(line)
        dataLine = [word for word in line]
        dataSetDict[frozenset(dataLine)] = dataSetDict.get(frozenset(dataLine), 0) + 1
        count += 1
    return dataSetDict, dataSet

def plot_pic(x_value, y_value, title, x_name):
    plt.plot(x_value, y_value[0], 'r', label='FP-Growth')  # use pylab to plot x and y
    plt.plot(x_value, y_value[1], 'g', label='ECLAT')  # use pylab to plot x and y
    plt.plot(x_value, y_value[2], 'b', label='Apriori')  # use pylab to plot x and y
    plt.title(title)  # give plot a title
    plt.xlabel(x_name)  # make axis labels
    plt.ylabel('Use Time(s) ')
    plt.legend(loc='upper right')  # make legend

    plt.show()  # show the plot on the screen

def t_fp_growth(minSup, dataSetDict, dataSet):
    #print("33333333333333333")
    freqItems = FP_growth.fp_growth(dataSetDict, minSup)
    #print("66666666666666666666666666666")
    freqItems = sorted(freqItems.items(), key=lambda item: item[1])
    return freqItems


def t_apriori(minSup, dataSetDict, dataSet):
    freqItems = apriori_duibi.apriori_zc(dataSet, dataSetDict, minSup)
    freqItems = sorted(freqItems.items(), key=lambda item: item[1])
    return freqItems


def t_eclat(minSup, dataSetDict, dataSet):
    #print("33333333333333333")
    freqItems = eclat.eclat_zc(dataSet, minSup)
    #print("77777777777777777")
    freqItems = sorted(freqItems.items(), key=lambda item: item[1])
    return freqItems

def do_experiment_min_support():

    data_name = 'unixData8_pro.txt'
    x_name = "Min_Support"
    data_num = 500
    minSup = data_num / 5

    dataSetDict, dataSet = loadDblpData(open("datasets/" + data_name), ',', data_num)
    step = minSup / 5  # #################################################################
    all_time = []
    x_value = []
    for k in range(5):

        x_value.append(minSup)  # #################################################################
        if minSup < 0:  # #################################################################
            break
        time_fp = 0
        time_et = 0
        time_ap = 0
        freqItems_fp = {}
        freqItems_eclat = {}
        freqItems_ap = {}
        for i in range(10):
            #ticks0 = time.time()
            #freqItems_fp = t_fp_growth(minSup, dataSetDict, dataSet)
            #time_fp += time.time() - ticks0
            #ticks0 = time.time()
            #freqItems_eclat = t_eclat(minSup, dataSetDict, dataSet)
            #time_et += time.time() - ticks0
            ticks0 = time.time()
            freqItems_ap = t_apriori(minSup, dataSetDict, dataSet)
            time_ap += time.time() - ticks0
        print ("minSup :", minSup, "      data_num :", data_num, \
            "  freqItems_fp:", len(freqItems_fp), " freqItems_eclat:", len(freqItems_eclat), "  freqItems_ap:", len(freqItems_ap))
        print ("fp_growth:", time_fp / 10, "       eclat:", time_et  / 10, "      apriori:", time_ap / 10)
        # print_freqItems("show", freqItems_eclat)
        minSup -= step   # #################################################################
        use_time = [time_fp / 10, time_et / 10, time_ap / 10]
        all_time.append(use_time)
        # print use_time
    y_value = []
    print('len(all_time[0]) ',len(all_time[0]))
    print('all_time ', all_time)
    for i in range(len(all_time[0])):
        tmp = []
        for j in range(len(all_time)):
            tmp.append(all_time[j][i])
        y_value.append(tmp)
        print('tmp ', tmp)
    print('x_value: ', x_value)
    print('y_value: ', y_value)
    plot_pic(x_value, y_value, data_name, x_name)
    return x_value, y_value


def do_experiment_data_size():

    data_name = 'unixData8_pro.txt'
    x_name = "Data_Size"
    data_num = 1500

    minSup = data_num * 0.010
    dataSetDict, dataSet = loadDblpData(open("datasets/" + data_name), ',', data_num)
    step = data_num / 5  # #################################################################
    all_time = []
    x_value = []
    for k in range(5):
        x_value.append(data_num)  # #################################################################
        if data_num < 0:  # #################################################################
            break
        #print("2222222222222222222222")
        time_fp = 0
        time_et = 0
        time_ap = 0
        freqItems_fp = {}
        freqItems_eclat = {}
        freqItems_ap = {}
        for i in range(2):
            ticks0 = time.time()
            freqItems_fp = t_fp_growth(minSup, dataSetDict, dataSet)
            time_fp += time.time() - ticks0
            ticks0 = time.time()
            freqItems_eclat = t_eclat(minSup, dataSetDict, dataSet)
            time_et += time.time() - ticks0
            ticks0 = time.time()
            freqItems_ap = t_apriori(minSup, dataSetDict, dataSet)
            time_ap += time.time() - ticks0
        print ("minSup :", minSup, "      data_num :", data_num, \
            "  freqItems_fp:", len(freqItems_fp), " freqItems_eclat:", len(freqItems_eclat), "  freqItems_ap:", len(freqItems_ap))
        print ("fp_growth:", time_fp  / 2, "       eclat:", time_et / 2 , "      apriori:", time_ap / 2 )
        # print_freqItems("show", freqItems_eclat)
        data_num -= step   # #################################################################
        use_time = [time_fp / 2, time_et / 2, time_ap / 2]
        all_time.append(use_time)
        # print use_time

    y_value = []
    print('len(all_time[0]) ', len(all_time[0]))
    for i in range(len(all_time[0])):
        tmp = []
        for j in range(len(all_time)):
            tmp.append(all_time[j][i])
        y_value.append(tmp)
        print('tmp ', tmp)
    print('x_value: ', x_value)
    print('y_value: ', y_value)
    plot_pic(x_value, y_value, data_name, x_name)
    return x_value, y_value

if __name__ == '__main__':
    x_value, y_value = do_experiment_min_support()
    #x_value, y_value = do_experiment_data_size()

