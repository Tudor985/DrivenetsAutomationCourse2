# test if a number is prime

num = 2
i = 2
while i < num//i:
    if num % i == 0:
        print(f"{num} is NOT prime")
        break
    i += 1
else:  # this is else for the while statement
    print(f"{num} is prime")
