Sum = 0

print("Please Enter 10 Numbers\n")
for i in range(1, 11):
    num = int(input("Number %d = " %i))

    if num < 0:
        break

    Sum = Sum + num

print("The Sum of Positive Numbers = ", Sum)
