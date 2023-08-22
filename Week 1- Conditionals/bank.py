greet = input("Greetings ")


if greet.startswith(("Hello", "Hello,", " Hello ")):
    print("$0")
elif greet.startswith("H"):
    print("$20")
else:
    print("$100")