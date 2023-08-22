amount_due = 50
# while loop the amount unitl amount due is > 0
while amount_due > 0:
        # print the due amount
        print(f"Amount Due: {amount_due}")
        # Ask the user to enter the coin
        insert_coin = int(input("Insert Coin: "))
        # check if the coin is acceptable or not. if yes then subtract the amount
        if insert_coin in [5,10,25]:
            amount_due -= insert_coin


# calculating change owned to user (abs function will positive value)
change_own = abs(amount_due)
print(f"Change Owed: {change_own}")