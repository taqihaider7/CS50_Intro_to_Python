grocery_list = {}   # making empty dict for items to store
while True:
# adding try block to take input from user

    try:
        item = input()
       # except block for any error. if user wants to breakout of code
    except EOFError:
        break
        # lower casing the input string. but here it is not necessary
    item = item.lower()
    # adding te item,s in dictionary with their frequency
    if item not in grocery_list:
        grocery_list[item] = 1
    else:
        grocery_list[item] += 1
# soting the items in dictionary alphabatically and then printing the them with their frequency
for item in sorted(grocery_list.keys()):
    print(f"{grocery_list[item]} {item.upper()}")
