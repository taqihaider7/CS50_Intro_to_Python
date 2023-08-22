def main():
    number = input("Enter fuel Fraction:")
    percent = convert(number)
    reading = gauge(percent)
    print(reading)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            z = x/y*100
            if z <= 100 and z >= 0:
                return z
            else:
                fraction = input('enter a fraction (x/y): ')
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'

if __name__ == '__main__':
    main()