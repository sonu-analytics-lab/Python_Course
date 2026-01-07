
# # 1. Write a program that asks the user for a number and prints whether it is
# #
# print("positive, negative, or zero.")

# number = int(input("Enter your number: "))

# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")


# # 2 Create a program that checks if a person is eligible to vote (age >= 18).

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# # 3 Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.

# number = int(input("Enter your number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# 2. Match Case Statements

num = int(input("Enter a day number (1 to 7) "))

match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
