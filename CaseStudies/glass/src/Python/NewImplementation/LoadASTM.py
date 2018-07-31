## @file LoadASTM.py
#  @brief Loads a cTSD and cSDF
#  @date 07/30/2018

import pytest
from ContoursADT import ContoursT
from FunctADT import FuncT

## @brief Loads cTSD
#  @param s filename
def LoadTSD ( s ):
    infile = open(s, "r")
    w_list = infile.readline()
    qAndSD = infile.readlines()
    infile.close()

    w_list = w_list.split(",")[1::2]
    for i in range(len(w_list)):
        w_list[i] = w_list[i].strip("\n")
        w_list[i] = int(w_list[i])
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

## @brief Loads cSDF
#  @param s filename
def LoadSDF ( s ):
    infile = open(s, "r")
    J_list = infile.readline()
    qStarAndAR = infile.readlines()
    infile.close()

    J_list = J_list.split(",")[1::2]
    for i in range(len(J_list)):
        J_list[i] = J_list[i].strip("\n")
        J_list[i] = int(J_list[i])
    qStarAndAR = "".join(qStarAndAR).split(",")
    qStar_list, AR_list = [[]], [[]]
    for item in qStarAndAR:
        print(item)
        item = float(item)
        print(type(item))
        if item == "\n":
            qStar_list.append([])
            AR_list.append([])
        else:
            qStar_list[-1].append(item)
            AR_list[-1].append(item)

    out = ContoursT(1)
    for i in range(len(qStar_list)):
        qStar, AR = [], []
        for j in range(len(qStar_list[i])):
            qStar.append(qStar_list[i][j])
            AR.append(AR_list[i][j])
        out.add(FuncT(qStar, AR, 1), J_list[i])
    return out

LoadSDF("SDF.txt")