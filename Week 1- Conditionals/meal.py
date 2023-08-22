def main():

    meal_time  = input("What time it is? ")

    meal_time = convert(meal_time)

    if 7.0 <= meal_time <=8.0:
        print("Breakfast time")
    elif 12.0 <= meal_time <=13.0:
        print("lunch time")
    elif  18.0 <= meal_time <= 19.0:
        print("dinner time")
    else:
        exit


def convert(meal_time):
    ''' This convert function is taking the time input(string) from user in 24hr format and then spliting string using the split function
    and assigning the values to hours and minutes then changing the data type to int. after that converting the minutes to hours and adding
    it to hours
    '''
    hours, minutes = meal_time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + minutes/60

if __name__ == "__main__":
    main()