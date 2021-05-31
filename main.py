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


DATAFRAME STRUCTURE SUGGESTION:
Input_date,Account, Amount('+' or '-'), Category, Transaction_date, Priority, Comment

Account - all your accounts, with that can transfer money in between

CALCULATIONS:
Current Balance

Classes - required?
Amount, Category, Comment (?), Priority :
Low - own wants, not required for living
Medium - It is important (but not required f.e ???)
High - absolutely required (Apartment, Bills, Food)
Is uber-eats required? High or medium?

After inputting, put into excel with current date - do I need hours? very detailed analysis???
Retroactive


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

#Settings file - will be changed later to not python
import settings


class PaymentsFrame:
    def __init__(self):
        self.payments = pd.DataFrame(columns=settings.dataframe_columns)

    def calculate_average(self):
        print(self.payments['Amount'].mean())


def init():
# Import data from excel
    # Create Dataframe
    data = PaymentsFrame()

    #Fill dataframe with data / test data if required
    #payments = payments.append(create_test_data())
    data.payments = data.payments.append(load_data())

    return data

# Input new data to dataframe
def input_data(data):
    #input data from user
    input_data = []
    #add data to payments dataframe and save it
    data = data.payments.append(input_data)
    return data

# Delete data (?) - Not sure if needed? Modification needed? Who knows...
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
    data.to_csv(settings.data_location)

def create_test_data():
    test_data = pd.DataFrame(
    [
      [1,datetime.datetime.now().strftime('%x'),'MBANK',300,settings.categories[0],datetime.datetime(2021,5,26).strftime('%x'),'Medium','TEST'],
      [2,datetime.datetime.now().strftime('%x'),'MBANK',310,settings.categories[0],datetime.datetime(2021,5,25).strftime('%x'),'High','TEST']
    ]
    ,columns=settings.dataframe_columns)
    return test_data

def load_data():
    load_data = pd.read_csv(settings.data_location,index_col=[0])
    return load_data

def main(data):
    #Test - print data
    print(data.payments)
    #Main loop
    print('Please select the action you\'d like')
    #print(settings.available_actions)
    #action = input()

    data.calculate_average()

    #TBD - selecting data file.
    #input data
    input_data(data)



if __name__ == '__main__':
    data = init()
    main(data)




