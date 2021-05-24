"""
Finance project
Kamil Bąkała

-Add a amount you spent and which category it was
-Calculate your overall spendings since last payroll
-Show charts for how much you spent over which
-Calculate average (yearly, overall, half-yearly)

Data saved in excel? Pandas/numpy/sns?
Categories - predetermined, can be added?
Gui - at first easy
Phone/mbank/revolut integration??? - future


Classes - required?
Amount, Category, Comment (?), Priority :
Low - own wants, not required for living
Medium - It is important (but not required f.e ???)
High - absolutely required (Apartment, Bills, Food)
Is uber-eats required? High or medium?

After inputting, put into excel with current date - do I need hours? very detailed analysis???

Subscritpions - add as they get paid or add automatically?


"""
import pandas as pd
from datetime import date
import datetime



# Import data from excel
data = {'Date':[],'Amount':[],'Category':[],'Priority':[],'Comment':[]}

# Create Dataframe
payments = pd.DataFrame(data=data)

#Fill dataframe with data / test data if empty
test = pd.DataFrame(data={'Date':[datetime.datetime.now().strftime('%x'),datetime.datetime.now().strftime('%x')],'Amount':[350.00,100.51],'Category':['Food','Entertainment'],'Priority':['High','Low'],'Comment':['Food ordered','Game :))']})
payments = test

print(payments)


# Input new data to dataframe

# Save data to excel





