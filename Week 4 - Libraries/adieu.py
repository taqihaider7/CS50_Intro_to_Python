# imorting inflect library
import inflect
# creating object for inflect
p = inflect.engine()


names=[]  # empty list to store names
while True:   # loop forever
    try:
        name= input("Name: ")    # asking input from user
        names.append(name)     # adding names into the list
    except EOFError:      # if user wants to exit the program
        print()   # printing new line
        break
 # printing message to the names
message = p.join(names)
print(f"Adieu, adieu, to " + message)