import numpy as np
import os
import  pandas as  pd
import  matplotlib.pyplot as plt
def TroughBaselineCorrection(path,savepath):
    dir1 = path
    data = np.loadtxt(dir1)
    x = data[:, 0]
    y = data[:, 1]
    j = 1
    label = []
    for i in range(len(y) - 2):
        if y[j] <= y[j - 1] and y[j] <= y[j + 1]:
            label.append(j)
            # print(j,y[j])
            j += 1
        else:
            j += 1

    h = label[len(label) - 1]
    k = 0
    y2 = []
    for g in range(len(label)):
        slope = (y[label[g]] - y[k]) / (x[label[g]] - x[k])
        b = y[label[g]] - x[label[g]] * slope
        for g1 in range(k, label[g]):
            y1 = slope * x[g1] + b
            y1 = round(y1, 0)
            y2.append(y1)
        k = label[g]
        if k == h:
            f = len(y) - 1
            slope = (y[f] - y[k]) / (x[f] - x[k])
            b = y[f] - x[f] * slope
            for g1 in range(k, f + 1):
                y1 = slope * x[g1] + b
                y1 = round(y1, 0)
                y2.append(y1)
    y_2 = np.array(y2)
    y11 = y - y_2
    for i in range(len(y11)):
        if y11[i] < 0:
            y11[i] = 0
    # plt.plot(x, y, label='original datas')  # 对原始数据画散点图
    # plt.plot(x, y2, ls='--', c='red', label='fitting ')
    # plt.plot(x, y11, label='original-fitting ')
    # plt.legend()
    # plt.show()
    np.savetxt(savepath, np.column_stack((x, y11)), fmt='%0.4f')
if __name__ == "__main__":
    dir1 = 'D:\pycharm\Hg2\原始\\3ms-100per-10mm-hg\\1.txt'
    savedir="E:\\2019-1\大气\Hg10mm-拟合基底\\原始去除波谷拟合数据1.txt"
    TroughBaselineCorrection(dir1,savedir)