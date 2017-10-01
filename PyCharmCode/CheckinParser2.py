import pandas as pd
import numpy as np


def chekinByDaysNP(ch):     #gets a checkin list, inputs numpy array
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    ins = np.zeros(7 * 24)
    for i in ch:
        temp = i.split("-")
        day = temp[0]
        temp2 = temp[1].split(":")
        hour = temp2[0]
        num = temp2[1]
        ins[days.index(day) * 24 + int(hour)] = num
    return ins


def chekinByDaysList(ch):       #gets a checkin list, inputs list
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    ins = [0] * (7 * 24)
    for i in ch:
        temp = i.split("-")
        day = temp[0]
        temp2 = temp[1].split(":")
        hour = temp2[0]
        num = temp2[1]
        ins[days.index(day) * 24 + int(hour)] = num
    return ins


def chekinByDaysFrame(checkin):     #gets checkin dataframe, adds columns to every hour with num of checkins
    timeVector = checkin["time"].apply(lambda x: chekinByDaysList(x))
    times = pd.DataFrame()
    times = pd.DataFrame([t for t in timeVector])
    return pd.concat([checkin, times], axis=1)
