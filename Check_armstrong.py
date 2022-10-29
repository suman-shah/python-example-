'''def evenSumPrefix(file):
    f=open(file,'r')
    r=f.readlines()
    s=0
    a=[int(i) for i in r]
    for j in a:
        s=s+j
    if s%2==0:
        return True
    else:
        return False

print(evenSumPrefix("t1.txt"))
'''
def armstrong(n):
    z=len(str(n))
    d=0
    e=n
    while n!=0:
        d+=(n%10)**z
        n=n//10
    if d==e:
       return True
    else:
        return False
import sys

m=sys.argv[1:]
print(m)
for i in m:
    if armstrong(int(i)):
        print('True')
        break
else:
    print('False')
