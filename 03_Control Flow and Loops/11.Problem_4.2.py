# Write a program that keeps asking the user to enter a password until they enter the correct one
entered_pass = input("Enter password: ")

password = 'Y2k123'

while entered_pass != password:
    entered_pass = input("Wrong password! Try again and Enter password: ")

print("Success! You are logged in")
