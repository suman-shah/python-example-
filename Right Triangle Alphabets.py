rows = int(input("Enter Right Triangle Alphabets Pattern Rows = "))

print("====Right Angled Triangle Alphabets Pattern ====")

alphabet = 65

for i in range(0, rows):   
    for j in range(0, i + 1):
        print('%c' %(alphabet + j), end = ' ')
    print()
