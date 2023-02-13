try:
    a = int(input("Give me a number "))
    if (a > 0) and (a < 10):
        print(f"{a} is positive")
        print(f"{a} is less than 10")
    elif (a > 0) and (a > 10):
        print(f"{a} is positive")
        print(f"{a} is greater than 10")
    elif a < -100:
        print(f"{a} is negative and smaller than -100")
    elif a < 0:
        print(f"{a} is just negative")
    else:
        print(f"{a} must be either 0 or 10")

except ValueError:
    print("that was not a number")

# if can also be inside an if
try:
    a = int(input("Give me a number "))
    if a > 0:
        if a < 10:
            print(f"{a} is positive")
            print(f"{a} is less than 10")
        elif a > 10:
            print(f"{a} is positive")
            print(f"{a} is greater than 10")
    elif a < -100:
        print(f"{a} is negative and smaller than -100")
    elif a < 0:
        print(f"{a} is just negative")
    else:
        print(f"{a} must be either 0 or 10")

except ValueError:
    print("that was not a number")

a = 10
b = 10
if a < b:
    print(f"{a} < {b}")
elif a == b:
    print(f"{a} == {b}")
else:
    print(f"{a} > {b}")
