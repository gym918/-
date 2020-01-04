from trough_removeBase import TroughBaselineCorrection
import os
import numpy as np
if __name__ == "__main__":
    dir = 'D:\pycharm\Hg_去基底\\'
    dir01='原始\\'
    filenames1 = os.listdir(dir+dir01)
    filenames1.sort(key=lambda x: int(x[:-5]))
    for i in filenames1:
        dir1 = i
        filenames = os.listdir(dir +dir01+ dir1)
        filenames.sort(key=lambda x: int(x[:-4]))
        # print(dir1)
        file_number = len(filenames)

        for i in filenames:
            dir_1 = dir + dir01+dir1
            # print(data_1)
            dir2 = dir_1 + '\\' + i
            savedir=dir+'去基底'+'\\'+dir1+"\\"+i
            TroughBaselineCorrection(dir2,savedir)