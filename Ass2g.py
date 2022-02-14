#Write a program to calculate simple interest. Accept values from user.(si=pnr/100)
p=float(input("Enter the principal amount:"))
n=float(input("Enter the number of years:"))
r=float(input("Enter the rate of interest:"))
SI=(p*n*r)/100
print("Simple Interest:{}".format(SI))