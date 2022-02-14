#Use type casting to check every possibility of type casting(int to other types,float to other type,..). Form a table as below to maintain track.[P:Possible N=Not Possible]
# 1 --> Converting to integer type using int()
print("1: converting to integer type")
print(int(9.6)) # float to int
print(int(True)) # bool to int
print(int(False)) # bool to int
print("123") # str to int
print('\n')
# 2 --> converting to float type using float()
print("2: converting to floating type")
print(float(12)) # int to float
print(float(True)) # bool to float
print(float(False)) # bool to float
print(float("123")) # string to float
print('\n')
# 3 --> converting to bool type using bool()
print("3: converting to boolean type")
print(bool(12)) # integer to bool
print(bool(0.0)) # float to bool
print(bool([1,2,3])) # list to bool
print(bool()) # tuple to bool
print('\n')
# 4 --> converting to string type using str()
print("4: converting to string type")
print(str(123))  # integer to string
print(str(12.12)) # float to string
print(str([10, 20, 30])) # list to stringS