months= [    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    # asking user for date
    date = input("Date: ")
        # splitting date by /
    try:
        month, day, year = date.split("/")
        # removing blank space around the year
        year = year.lstrip()
        year = year.rstrip()
        # checking the values of day and month in the range
        if (int(day) >= 1 and int(day) <=31) and (int(month) >=1 and int(month) <=12):
            break

    except:
        try:   # splitting date by space
            new_month, new_day, year = date.split(" ")
            # checking if the month is the list or not and returning the number of month
            for i in range(len(months)):
                if new_month == months[i]:
                    month = i+1
            # removing coma from day
            if not new_day.endswith(","):
                continue
            day = new_day.replace(",", "")

            # checking the values of day and month in the range
            if (int(day) >= 1 and int(day) <=31) and (int(month) >=1 and int(month) <=12):
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
