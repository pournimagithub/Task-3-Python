#Write a program to check if a triangle is valid or not
a=int(input("Enter the first angle of a triangle:"))
b=int(input("Enter the second angle of a triangle:"))
c=int(input("Enter the third angle of triangle:"))
total=a+b+c
if total==180:
    print("\n This is a Valid Triangle")
else:
    print("\n This is an Invalid Triangle")    