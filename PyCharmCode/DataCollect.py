def findBudinessData(ID, df): #input: ID-business_id string, df-dataframe with business_id column
    return df[df['business_id']==ID]

def findBudinessMultiData(ID, dfs):
    data={}
    for df in dfs:
        typ=df.type[0]
        data[typ]=findBudinessData(ID, df) #input: ID-business_id string, dfs-list of dataframed with business_id column
    return data

def findMultyBusinessData(IDs, dfs): #input:  IDs- list of business_id strings, dfs-dataframe with business_id column
    data={}
    for ID in IDs:
        data[ID]=findBudinessMultiData(ID, dfs)
    return data