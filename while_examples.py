# n = -10
# s = 0
# while n < 10:
#     s += n
#     n += 1
# print(s)


# s = 1
# n = 2
#
# while n < 15:
#     s = s + n
#     n = n + 7
# print(s)




# i = 1
# n = 7
#
# # while loop from i = 1 to 5
# while i <= n:
#     print(i)
#     i = i + 1


# program to calculate the sum of numbers
# until the user enters zero

total = 0

number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number  # total = total + number

    # take integer input again
    number = int(input('Enter a number: '))

print('total =', total)