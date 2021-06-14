"""
Finance tracker project
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


Subscriptions - add as they get paid or add *because I remember*?

Gui options :
- Show all ?
- Sort by
- Filter out
- Add
- Remove ?
- show diagrams
- calculations - automatically shown

"""
import payments_frame
import sys
import settings


def init():
    # Import data from excel
    # Create Dataframe
    data = payments_frame.PaymentsFrame()

    # Fill dataframe with data / test data if required
    # data.create_test_data()
    data.load_data()

    return data


def action_switcher(data, argument):
    switch = {
        'E!': data.exit,
        'E': data.save_and_exit,
        'I': data.input_data,
        'S': data.show_data,
        'C': data.calculate_balance,
        'C2': data.calculate_balance_per_month,
        'C3': data.calculate_balance_per_account
    }
    func = switch.get(argument, lambda: "Incorrect action")
    return func()


def main(data):

    # Main loop
    while True:
        print('Please select the action you\'d like to perform')
        print(settings.available_actions)

        try:
            user_input = input("Action: ")
            result = action_switcher(data, user_input.upper())
            # End if exit called
            if result == -1:
                break
            elif result == 0:
                pass
            else:
                print(result)
        except KeyboardInterrupt:
            print("Keyboard interrupt, exiting...")
            sys.exit()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


if __name__ == '__main__':
    data = init()
    main(data)
