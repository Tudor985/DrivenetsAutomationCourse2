# "infinte" while with escape mechanism
# keep reading and adding numbers until the number entered is 0
s = 0
while True:
    try:
        num = int(input("Please give me a number (0 to quit) "))
        if num == 0:
            break
        s += num
    except ValueError:
        print("That was not a valid number")
        continue
    print(f"Intermediate sum so far is {s}")

print(s)
