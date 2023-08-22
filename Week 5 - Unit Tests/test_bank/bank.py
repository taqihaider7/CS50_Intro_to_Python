def main():
    greet = input("Greetings ")
    new_value = value(greet)
    print(f"${new_value}")


def value(greetings):
    greetings= greetings.lower().strip()

    if "hello" in greetings:
        return 0
    elif "h"== greetings[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()