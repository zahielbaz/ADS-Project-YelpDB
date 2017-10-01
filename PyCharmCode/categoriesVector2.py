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

def ID2catVec(allCategories,business,ID):  #returns a list of ones hot vector of categories by list&id, input is business dataframe+exact ID
    businessCategories=business[business["business_id"]==ID]["categories"].values[0]
    return cat2vec(allCategories,businessCategories)


def cat2vec(allCategories,businessCategories):   #returns a list of ones hot vector of categories by list&id, input is the list of categories of some business
    numOfCategories=len(allCategories)
    nums=[0]*numOfCategories
    #businessCategories=business[business["business_id"]==ID]["categories"].values[0]
    if businessCategories != None:
        for category in businessCategories:
            nums[allCategories.index(category)]=1
    return nums

def addCategoriesVector(allCategories, business):  #gets business dataframe and adds to it ones hot vector of all businesses
    categories_vector= business["categories"].apply(lambda x: cat2vec(allCategories,x))
    categories_frame=pd.DataFrame()
    categories_frame[allCategories]=pd.DataFrame([category for category in categories_vector])
    return pd.concat([business,categories_frame],axis=1)