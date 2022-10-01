# Python program to Count Total Number of Words in a String

str1 = input("Please Enter your Own String : ")
total = 1

for i in range(len(str1)):
    if(str1[i] == ' ' or str1 == '\n' or str1 == '\t'):
        total = total + 1

print("Total Number of Words in this String = ", total)
