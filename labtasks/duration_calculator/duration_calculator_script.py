import numpy as np

def compare_dates(input_date):
    numpy_date = np.datetime64(input_date, 'D') # Input date
    today = np.datetime64('today', 'D') # Today's date
    difference = today - numpy_date
    
    return abs(difference) # Make it so that the value is not negative

input_date = input("Input date in format YYYY-MM-DD: ")

difference_in_dates = compare_dates(input_date)
print(f"The difference in dates is {difference_in_dates}.")