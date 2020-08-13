# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 08:27:03 2020
@title: Giving Card liklihood to continue giving to organization when first gift was giving card, by year
@author: Diana McSpadden
"""

"""
Question I want to answer: 
    of first gifts that were GIVING CARD gifts in the years 2016, 2017, and 2018 
    how do additional gifts from people who initially gave via giving card compare?
    
Background:
    A Constituent is a person, organization, fund, foundation, etc that has a relationship with the museum/non-profit.
        A Constituent may have already giving a gift, or they may be a prospective donor.
    
    A Giving Card is a piece of paper with donation instructions, including an envelope to mail a donation
        at a later date. Giving Cards are provided on site, typically at points of interest at the museum, 
        by tour guides, or by key historic site staff. Donors who give a gift by GIVING CARD are typically 
        very interested guests who enjoyed their experience at the historic site.
        
    Why ask this question?
        Giving Card practices may have changed between the year, or guests may be different between the years.
        Are giving cards still an effective means to find new donors?
        
    This question will not answer WHY there are differences between the years of repeat giving by first-time
        Giving Card donors, but since this question has never been asked before it can provide a baseline
        and if we know that Giving Card procedures have changed it may tell us whether they became more or 
        less effective.
        
    Background:
        The data set was extracted to contain constituents that gave a FIRST GIFT via giving card. 
        The data set contains:
            Constituent ID (unique ID for the constituent)
                ** To anonymize: I removed Constituent Name and Org Name
            Org or Person Indicator: because I removed the Person Name, and Org Name columns I added a P, or O
                to tell me if the Constituent is a person or organization
            First Gift Date: date of first gift to historic site
            First Gift Amount: amount of first gift
            2016 Total Giving: total amount GIFT CARD giving in 2016
            2017 Total Giving: total amount GIFT CARD giving in 2016
            2018 Total Giving: total amount GIFT CARD giving in 2016
            2019 Total Giving: total amount GIFT CARD giving in 2016
            2020 Total Giving: total amount GIFT CARD giving in 2016
            Total Giving All Years: Res and Unres: Total giving (restricted and unrestricted)
                from the Constituent in all years of giving
            
        We only have Giving Card data for 2016 - 2020
            I can really only compare repeat giving in years 2017, 2018, and 2019
            This is not enough information for a real analysis, but it is a start
          
           
"""

# import needed libraries and configure
import pandas as pd
pd.set_option('display.max_columns', None)

import matplotlib.pyplot as plt
from datetime import datetime


# load data set into a data frame
df =  pd.read_csv("Lifetime_Giving_First_Gift_Giving_Card_Anon.csv")

#show the first 5 rows
print(df.head())

# see the summary of the fields
print(df.describe(include = 'all'))

# confirm data types
print(df.dtypes)

# let's plot the mean of the giving for 

# create FirstGiftYear
df = df.assign(FirstGiftYear = lambda dataframe: dataframe['FirstGiftDate'].map(lambda giftdate: datetime.strptime(giftdate, '%m/%d/%Y').year))
          

#show the year column from head to confirm new column
print(df.head()["FirstGiftYear"])

# create a TotalGiving > FirstGiving column called AdditionalDonations
# f = lambda x, y: x * y
df = df.assign(AdditionalDonations = (df['TotalGivingResUnres'] - df['FirstGiftAmount']))

# create a histograms from First Gift Year and More Donations

dfGroupedMean = df.groupby(['FirstGiftYear'])['AdditionalDonations'].mean()
ax = dfGroupedMean.plot(kind='bar', figsize=(10,6), color="indigo", fontsize=13);
ax.set_alpha(0.8)
ax.set_title("Average Additional Gift By First Year Giving", fontsize=22)
ax.set_ylabel("Average Additional Gift Amounts", fontsize=15);
plt.show()

dfGroupedCount = df.groupby(['FirstGiftYear'])['AdditionalDonations'].count()
ax = dfGroupedCount.plot(kind='bar', figsize=(10,6), color="indigo", fontsize=13);
ax.set_alpha(0.8)
ax.set_title("Number Additional Gift By First Year Giving", fontsize=22)
ax.set_ylabel("Number Additional Gift Donors", fontsize=15);
plt.show()

"""
the bummer is that I don't have my answer yet, because we would assume that with
additional year opportunities for giving, a donor would be more likely to give an additional
gift. But I have started the analysis.
"""