def cameltosnake(n):
    res = ""
    for i in range(len(n)):
        if n[i].isupper():
            res += "_" + n[i].lower()
        else:
            res += n[i]
    return res

name_camel_case = input("Enter a variable name in camel case: ")
snake_case = cameltosnake(name_camel_case)
print(snake_case)