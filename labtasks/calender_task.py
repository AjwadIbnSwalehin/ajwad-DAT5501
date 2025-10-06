def calender(days, start_day):
    day_dictionary = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6
    }
    
    # We will need one more week if start day is late in the week
    calender_print = [
        ['S', 'M', 'T', 'W', 'T', 'F', 'S'],
        ['--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--'] 
    ]
    
    starting_index = day_dictionary[start_day]
    week = 1
    day_of_month = 1
    
    for i in range(starting_index, starting_index + days):
        # Does not attempt to access weeks beyond our array size
        if week < len(calender_print):
            calender_print[week][i % 7] = day_of_month
        day_of_month += 1
        
        # If week is full, change to a new week
        if (i + 1) % 7 == 0 and day_of_month <= days:
            week += 1
            
    # Print Calender
    for row in calender_print:
        print(row)

day = input("What day do you want to start on?")
days_in_month = input("How many days does the month have?")
calender(days_in_month, day)