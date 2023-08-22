import sys
import requests

 # exiting the program if the comman line argument is missing
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
try:  # getting the number of bitcoin user want to buy and converting it to float
    value = float(sys.argv[1])
except ValueError:      # raising the error if the argumenbt is not number nd exiting the program.
    print("Command-line argument is not a number")
    sys.exit(1)
try:  # sending the request to coindesk api to get Json response
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("Error fetching Bitcoin price")
    sys.exit(1)
     # getting price of Bitcoin from the json response
data = response.json()
price = data["bpi"]["USD"]["rate_float"]
total_amount = value * price

print(f"${total_amount:,.4f}")