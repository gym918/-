import numpy as np
#np.set_printoptions(suppress=True)
import os
import matplotlib.pyplot as plt
import  pandas as  pd
import  matplotlib.pyplot as plt
def resolution(path,n,savepath):
    dir = path
    data = np.loadtxt(dir)
    j = 1
    label = []
    x = data[:, 0]
    y = data[:, 1]
    for i in range(len(y) - 2):
        if y[j] < y[j - 1] and y[j] < y[j + 1]:
            label.append(j)

            # print(j,y[j])
            j += 1
        else:
            j += 1
    # print(label)

    # label2记录了极小值点小于1.5的数值
    k = 0
    label2 = []
    for i in range(len(label) - 1):
        a = label[k]
        b = label[k + 1]
        if x[b] - x[a] <= n:
            # print(x[b]-x[a],a,b)
            label2.append(a)
            label2.append(b)
            k += 1
        else:
            k += 1
    # 包含了相邻的两组数
    # print(label2)
    m = 0
    n = 1
    np.set_printoptions(threshold=np.inf)
    #  对label2内的极小值点归零
    for i in range(len(label2) // 2):
        a = label2[m]
        b = label2[n]
        for j in range(a, b + 1):
            y[j] = 0
        m += 2
        n += 2
    y[0] = 0
    np.savetxt(savepath, np.column_stack((x, y)), fmt='%0.4f')
    # plt.plot(x, y)
    # plt.title("1.5nm")
    # plt.show()
if __name__ == "__main__":
    dir1 = "E:\\2019-1\大气\Hg10mm-拟合基底\\原始去除波谷拟合数据1.txt"
    savedir="E:\\2019-1\大气\Hg10mm-拟合基底\\原始去除波谷拟合数据1.5分辨率.txt"
    resolution(dir1,2,savedir)