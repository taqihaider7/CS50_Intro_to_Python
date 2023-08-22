def convert(input_str):
    output_str = input_str.replace(':)', '🙂').replace(':(', '🙁')
    return output_str

def main():
    user_input = input("Enter some text: ")
    converted_text = convert(user_input)
    print(converted_text)


main()