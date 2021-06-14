"""
TO-DO
load_data
Create check for empty file and load properly if so.
input_data
Create check whether the is data for the ID of transaction

Checks for categories, accounts,

plots
GUI
Google drive
"""



# All required imports
import pandas as pd
import datetime

# Settings file - will be changed later to not python
import settings


class PaymentsFrame:
    def __init__(self):
        self.payments = pd.DataFrame(columns=settings.dataframe_columns)

    def show_data(self):
        print(self.payments.head())
        #print(self.payments.dtypes)
        return 0

    # Calculate current balance
    def calculate_balance(self):
        print(self.payments['Amount'].sum())
        return 0

    # Calculate balance per month
    def calculate_balance_per_month(self):
        temp_data = self.payments
        temp_data['Year'] = pd.DatetimeIndex(temp_data['Transaction Date']).year
        temp_data['Month'] = pd.DatetimeIndex(temp_data['Transaction Date']).month
        temp_data.index = pd.DatetimeIndex(temp_data['Transaction Date'])
        print(temp_data.groupby([temp_data.index.year.values, temp_data.index.month.values])['Amount'].sum())
        return 0

    def calculate_balance_per_account(self):
        temp_data = self.payments
        print(temp_data.groupby([temp_data['Account']])['Amount'].sum())
        return 0
    # Plot data
    def plot_data(self):
        pass

    # Input new data to dataframe
    def input_data(self):
        # Data structure:
        # ID, Date, Accout, Amout,Cat,Trans_date,Prio,Comment
        # input data from user
        input_data = []
        input_data.append(datetime.datetime.now().strftime('%x'))
        input_data.append(input("Please input account for the transaction: "))
        input_data.append(input("Please input amount for the transaction: "))
        print("Available Categories: {}".format(settings.categories))
        input_data.append(input("Please input category of the transaction: "))
        date = input("Please input Transaction date (in format DD/MM/YYYY) : ")
        input_data.append(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%x'))
        input_data.append(input("Please input priority of the transaction: "))
        input_data.append(input("Please input additional comments for the transaction: "))

        # print(input_data)
        # add data to payments dataframe and save it
        input_frame = pd.DataFrame(
            [
                input_data
            ]
            , columns=settings.dataframe_columns)

        self.payments = self.payments.append(input_frame)
        self.payments['Amount'] = pd.to_numeric(self.payments['Amount'], downcast='float')
        self.refresh_data_types()
        return ("Following data inputted: {}".format(input_data))

    # Delete data (?) - Not sure if needed? Modification needed? Who knows...
    def delete_data(self):
        # select data to be removed

        # delete data from dataframe (safe?)
        pass

    # Save data to csv
    def save_data(self):
        # Select excel file - default if not given

        # Save data to excel
        '''
        if excel given:
            save data to excel
        else:
        '''
        self.payments.to_csv(settings.data_location)

    def refresh_data_types(self):
        self.payments = self.payments.convert_dtypes()
        self.payments['Input Date'] = pd.to_datetime(self.payments['Input Date'])
        self.payments['Transaction Date'] = pd.to_datetime(self.payments['Transaction Date'])

    # Load data from csv
    def load_data(self):
        self.payments = pd.read_csv(settings.data_location, index_col=[0])
        self.refresh_data_types()

    # Exit program
    def exit(self):
        print("Exiting program")
        return -1

    # Save and Exit program
    def save_and_exit(self):
        print("Saving data...")
        self.save_data()
        print("Saving complete, data saved at: {}".format(settings.data_location))
        return self.exit()

    # Create test data
    def create_test_data(self):
        test_data = pd.DataFrame(
            [
                [datetime.datetime.now().strftime('%x'), 'MBANK', 300, settings.categories[0],
                 datetime.datetime(2021, 5, 26).strftime('%x'), 'Medium', 'TEST'],
                [datetime.datetime.now().strftime('%x'), 'MBANK', 310, settings.categories[0],
                 datetime.datetime(2021, 5, 25).strftime('%x'), 'High', 'TEST']
            ]
            , columns=settings.dataframe_columns)
        # print(test_data.head())
        self.payments = test_data
