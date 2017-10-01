import pandas as pd
import numpy as np


def chekinByDays(ch):
    days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    ins=np.zeros(7*24)
    for i in ch:
        temp=i.split("-")
        day=temp[0]
        temp2=temp[1].split(":")
        hour=temp2[0]
        num=temp2[1]
        ins[days.index(day)*24+int(hour)]=num
    return ins
