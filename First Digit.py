# Python Program to find First Digit of a Number

number = int(input("Please Enter any Number: "))

first_digit = number

while (first_digit >= 10):
    first_digit = first_digit // 10

print("The First Digit from a Given Number {0} = {1}".format(number, first_digit))
