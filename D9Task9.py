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



