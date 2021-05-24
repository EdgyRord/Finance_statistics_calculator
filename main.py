"""
Finance project
Kamil Bąkała

-Add a amount you spent and which category it was
-Calculate your overall spendings since last payroll
-Show charts for how much you spent over which
-Calculate average (yearly, overall, half-yearly)

Data saved in excel? Pandas/numpy/sns?
Categories - predetermined, can be added via gui?
Gui - at first easy
Phone/mbank/revolut/google pay integration??? - future


Classes - required?
Amount, Category, Comment (?), Priority :
Low - own wants, not required for living
Medium - It is important (but not required f.e ???)
High - absolutely required (Apartment, Bills, Food)
Is uber-eats required? High or medium?

After inputting, put into excel with current date - do I need hours? very detailed analysis???

Subscritpions - add as they get paid or add *because I remember*?

Gui options :
- Show all ?
- Sort by
- Filter out
- Add
- Remove ?
- show diagrams
- calculations - automatically shown


"""
#All required imports
import pandas as pd
import datetime
import settings

#Initialize settings variables - change? Init or vars in file approach? Need to be changed during program run?
#settings.init()
def init():
# Import data from excel
    data = {'Date':[],'Amount':[],'Category':[],'Priority':[],'Comment':[]}

    # Create Dataframe
    payments = pd.DataFrame(data=data)

    #Fill dataframe with data / test data if empty
    test = pd.DataFrame(data={'Date':[datetime.datetime.now().strftime('%x'),datetime.datetime.now().strftime('%x')],'Amount':[350.00,100.51],'Category':[settings.categories[0],settings.categories[1]],'Priority':['High','Low'],'Comment':['Food ordered','Game :))']})
    payments = test

    print(payments)

    save_data(payments)

# Input new data to dataframe
def input_data():
    #input data from user

    #add data to payments dataframe and save it
    pass
# Delete data (?)
def delete_data():
    #select data to be removed

    #delete data from dataframe (safe?)
    pass
# Save data to excel
def save_data(data):
    #Select excel file - default if not given

    # Save data to excel
    '''
    if excel given:
        save data to excel
    else:
    '''
    data.to_csv('data.csv')

if __name__ == '__main__':
    init()




