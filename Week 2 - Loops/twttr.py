# Ask user to enter the word or sentence
def main():
   user_message  = input("Input: ")
   message_without_vowels = shorten(user_message)
   print("Output: "+ message_without_vowels)

def shorten(word):
   word_without_vowels = ""
   for letter in word:
         # check if the word or sentence conatins vowles or not
      if not letter.lower() in ['a','e','i','o','u']:
         # Adding the letters without vowels
         word_without_vowels += letter
         # return the new word without vowels
   return word_without_vowels

if __name__=="__main__":
   main()
