# not, and, or, xor
'''
Not
'''
print('===== Not =====\n')
a = True
print('Data a =', not a)
b = False
print('Data b =', not b)

'''
And (output will be false if one is false)
'''
print('\n===== And =====\n')
a = True
b = True
print('Hasil True and True =', a and b)

a = True
b = False
print('Hasil True and False =', a and b)

a = False
b = True
print('Hasil False and True =', a and b)

a = False
b = False
print('Hasil False and False =', a and b)

'''
Or (output will be true if one is true)
'''
print('\n===== Or =====\n')
a = True
b = True
print(a, 'or', b, '=', a or b)

a = True
b = False
print(a, 'or', b, '=', a or b)

a = False
b = True
print(a, 'or', b, '=', a or b)

a = False
b = False
print(a, 'or', b, '=', a or b)

'''
Xor (cannot be the same to output true)
'''
print('\n===== Xor =====\n')

a = True
b = True
c = a ^ b
print(a, 'xor', b, '=', c)

a = True
b = False
c = a ^ b
print(a, 'xor', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'xor', b, '=', c)

a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c)

