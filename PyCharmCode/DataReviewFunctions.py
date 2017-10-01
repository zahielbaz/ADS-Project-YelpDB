"""
This file contians several functions assosiated with the dara_review of Yelp

"""


"""
function: get the instances of a business
Input: df = data frame
       business_id = the id of the business
Output: a new data frame that contains only a certian business
"""
def GetInstancesOfGivenBusiness(df, business_id ):
    if type(business_id) == str:
        return(  df[df['business_id']==business_id ] )
    else:
        return -1


"""
function: get the final hapiness score of a certian business
Input: df = data frame
       business_id = the id of the business
Output:
"""
def HappinessScoreBasedOnStars(df, business_id):
    if type(business_id) == str:
        business_df = GetInstancesOfGivenBusiness(df, business_id )
        stars_mean = business_df['stars'].mean()
        cool_mean = business_df['cool'].mean()
        funny_mean = business_df['funny'].mean()
        useful_mean = business_df['useful'].mean()
        return(stars_mean,cool_mean,funny_mean,useful_mean)
    else:
        return -1

"""
function: normalized the data
Input: df = data frame
       field_name = field to normalized
Output: a new df
"""
def NormalizeValuesInField(df, field_name ):
    if field_name in df:
        max_item = df[field_name].max()
        if max_item != 0:
            df[field_name] = df[field_name] / max_item
        return df
    else:
        return -1

# if __name__ == '__main__':
