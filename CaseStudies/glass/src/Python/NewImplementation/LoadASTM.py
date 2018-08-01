## @file LoadASTM.py
#  @brief Loads a cTSD and cSDF
#  @date 08/01/2018

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

    for i in range(len(qAndSD)):
        qAndSD[i] = "".join(qAndSD[i]).strip().split(",")
    q_list, SD_list = [], []
    for i in range(len(qAndSD[0])//2):
        q_entry = [item[2*i] for item in qAndSD]
        SD_entry = [item[2*i+1] for item in qAndSD]
        for j in range(len(q_entry)):
            q_entry[j] = float(q_entry[j])
            SD_entry[j] = float(SD_entry[j])
        q_list.append(q_entry)
        SD_list.append(SD_entry)

    out = ContoursT(1)
    for i in range(len(q_list)):
        q, SD = [], []
        for j in range(len(q_list[i])):
            if q_list[i][j] != 0.0:
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

    for i in range(len(qStarAndAR)):
        qStarAndAR[i] = "".join(qStarAndAR[i]).strip().split(",")
    qStar_list, AR_list = [], []
    for i in range(len(qStarAndAR[0])//2):
        qStar_entry = [item[2*i] for item in qStarAndAR]
        AR_entry = [item[2*i+1] for item in qStarAndAR]
        for j in range(len(qStar_entry)):
            qStar_entry[j] = float(qStar_entry[j])
            AR_entry[j] = float(AR_entry[j])
        qStar_list.append(qStar_entry)
        AR_list.append(AR_entry)

    out = ContoursT(1)
    for i in range(len(qStar_list)):
        qStar, AR = [], []
        for j in range(len(qStar_list[i])):
            if qStar_list[i][j] != 0.0:
                qStar.append(qStar_list[i][j])
                AR.append(AR_list[i][j])       
        out.add(FuncT(qStar, AR, 1), J_list[i])
    
    return out