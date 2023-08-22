math_expression = input("Write your Expression? ")

x, y, z = math_expression.split()

x = int(x)
z = int(z)

if y == "+":
    result = x+z
elif y == "-":
    result = x-z
elif y == "*":
    result = x*z
elif y == "/":
    result = x/z
    
print(f"{result:.1f}")