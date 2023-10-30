# 1. what is the expected output of the following python code

data = [10,501,22,37,100,999,87,351]
result = filter(lambda x:x>4,data)
print(list(result))

      # output : [10,501,22,37,100,999,87,351]

# 2. write a pyhton code using lambda function to check every element of a list is an integer or string

list1 = [23,45,"map",3,"reduce",21,24,"filter"]

        # get integer from the list
integers = filter(lambda x: type(x)==int,list1)
print("\nIntegers in the list1: ",list(integers))

         # get string in the list
strings =filter(lambda a: type(a)==str,list1)
print("\nstrings in the list1: " ,list(strings))

# 3.FIBONACCI SERIES USING LAMBDA FUNCTION

f = lambda x : x if x<=1 else f(x-1) +f(x-2)

for i in range(0,50):
    print(f(i),end=" ")

# 4.REGULAR EXPRESSIONS

import re

def ValidateEmailId(email):
    
    pattern = r'\b[a-z0-9]+@+gmail.com\b'

    if re.findall(pattern,email):
        print("Valid Email")
    else :
        print("Invalid Email")


m = "mohanapriya24898@gmail.com"
ValidateEmailId(m)

def validateBangaladesh(mobileno):
    pat = r'^8800+[0-9]{9}$'
    if re.fullmatch(pat,mobileno):
        print("Valid Mobile Number")

    else:
        print("Invalid Mobile Number")
num= "8800123456789"
validateBangaladesh(num)


def validateUSA(telephoneno):
    patt = r'^[+1]+[0-9]{10}$'
    if re.fullmatch(patt,telephoneno):
        print("Valid Telephone Number")

    else:
        print("Invalid Telephone Number")
tele= "+10123456789"
validateUSA(tele)

def validatepassword(password):
    pa ="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$"

    if re.search(pa,password):
        print("Valid Password")

    else:
        print("Invalid Password ")
p = "Mohanap@1998"
validatepassword(p)









