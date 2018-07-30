## @file LoadASTM.py
#  @brief Loads a cTSD and cSDF
#  @date 07/30/2018

import pytest
from ContoursADT import ContoursT
from FunctADT import FuncT

def LoadTSD ( s ):
    infile = open(s, "r")
    w_list = infile.readline()
    qAndSD = infile.readlines()
    infile.close()

    w_list = w_list.split()
    q_list, SD_list = [], []
    for item in qAndSD:
        if item == "\n":
            q_list.append([])
            SD_list.append([])
        else:
            item = item.strip().split()
            q_list[-1].append(item[0])
            SD_list[-1].append(item[1])

    out = ContoursT(1)
    for i in range(len(q_list)):
        q, SD = [], []
        for j in range(len(q_list[i])):
            q.append(q_list[i][j])
            SD.append(SD_list[i][j])
        out.add(FuncT(q, SD, 1), w_list[i])
    return out

#def LoadSDF ( s ):