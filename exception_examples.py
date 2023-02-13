# do a division
try:
    num1 = input("What is the first number? ")
    num2 = input(f"What is the second number? ")  # get a str
    num1 = int(num1)
    num2 = int(num2)
    result = num1 // num2
except ValueError:
    print("that was not a valid number")
    print("please be more careful")
except ZeroDivisionError:
    print("The second number can not be zero!")
except Exception as e:
    print(e)
    print("This is something I did not see coming!")
    raise e
else:
    # this runs if no exception was thrown
    print(f"The result is {result}")
finally:
    # this always executes at the end
    print("thank you for using this tool")

# this is outside the try except block
print("this is the end!!")
