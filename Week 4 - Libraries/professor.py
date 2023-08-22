import random
def main():

    level = get_level()
    correct_answers = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y} = "
        answer = input(problem)
        for j in range(2):
            try:
                if int(answer) == x + y:
                    correct_answers += 1
                    break
                else:
                    answer = input("EEE\n" + problem)
            except ValueError:
                answer = input("EEE\n" + problem)
        else:
            print(f"{problem}{x+y}")
    print(f"Score: {correct_answers}")

# getting level input from user
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2,3]:
                break
        except:
            pass
    return level
# generating integer for levels
def generate_integer(level):
    if level == 1:
        return random.randint(0,9)

    elif level == 2:
       return random.randint(10,99)

    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()