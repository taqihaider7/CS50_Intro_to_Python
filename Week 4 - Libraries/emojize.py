import emoji

# asking user for input emoji string
input_string = input("Input: ")
# converting the emoji string into the emoji
print(emoji.emojize(input_string, language='alias'))