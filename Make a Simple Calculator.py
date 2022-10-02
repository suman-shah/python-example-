
def extract_from_text(text):

    l=[]

    for t in text.split(' '):

        try:

            l.append(float(t))

        except ValueError:

            pass

    return l

# calculating LCM

def lcm(x,y):

    L=x if x>y else y

    while L<=x*y:

        if L%x==0 and L%y==0:

            return L

        L+=1

# calculating HCF

def hcf(x,y):

    H=x if x=1:

        if x%H==0 and y%H==0:

            return H

        H-=1

  

# Addition

def add(x,y):

    return x+y

  

# Subtraction

def sub(x,y):

    return x-y

  

# Multiplication

def mul(x,y):

    return x*y

  

# Division

def div(x,y):

    return x/y

  

# Remainder

def mod(x,y):

    return x%y

  

# Response to command

# printing - "Thanks for enjoy with me" on exit

def end():

    print(response[2])

    input('press enter key to exit')

    exit()

   

def myname():

    print(response[1])

def sorry():

    print(response[3])

   

# Operations - performed on the basis of text tokens

operations={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add,

            'SUB':sub,'SUBTRACT':sub, 'MINUS':sub,

            'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf,

            'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul,

            'DIVISION':div,'MOD':mod,'REMANDER'

            :mod,'MODULAS':mod}

  

# commands

commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end}

           

print('--------------'+response[0]+'------------')

print('--------------'+response[1]+'--------------------')

   

while True:

    print()

    text=input('enter your queries: ')

    for word in text.split(' '):

        if word.upper() in operations.keys():

            try:

                l = extract_from_text(text)

                r = operations[word.upper()] (l[0],l[1])

                print(r)

            except:

                print('something went wrong going plz enter again !!')

            finally:

                      break

        elif word.upper() in commands.keys():

                      commands[word.upper()]()

                      break

    else:         

        sorry()



Output:

enter your queries: tell me the LCM of 18,8

72
