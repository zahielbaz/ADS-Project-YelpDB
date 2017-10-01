import pandas as pd
import numpy as np


def uniqueCategories(business):  #returns a list of all unique categories
    categories_list=list(business['categories'])
    categories=[]
    for sublist in categories_list:
        if sublist != None:
            for category in sublist:
                categories.append(category)
    return list(set(categories))


def cat2vec(allCategories,business,ID):   #returns a list of ones hot vector of categories by list&id
    numOfCategories=len(allCategories)
    nums=[0]*numOfCategories
    businessCategories=business[business["business_id"]==ID]["categories"].values[0]
    if businessCategories != None:
        for category in businessCategories:
            nums[allCategories.index(category)]=1
    return nums