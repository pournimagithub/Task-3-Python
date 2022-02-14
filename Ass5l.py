#Accept the month number and print its name and number of days in it
def print_month_name(x):
    if(x==1):
        print("January")
    if(x==2):
        print("February")
    if(x==3):
        print("March")
    if(x==4):
        print("April")
    if(x==5):
        print("May")
    if(x==6):
        print("June")
    if(x==7):
        print("July")
    if(x==8):
        print("August")
    if(x==9):
        print("September")
    if(x==10):
        print("October")
    if(x==11):
        print("November")
    if(x==12):
        print("December")
    if(x<1 or x>12):
        print("Invalid input")
    if (x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12):
        print("\n 31 days in this month")
    elif (x==4 or x==6 or x==9 or x==11):
        print("\n 30 days in this month")
    elif (x==2):
        print("\n Either 28 or 29 days in this month")
    else:
        print("\n Please enter valid number between 1 to 12")
month=int(input("Enter the month number"))
print_month_name(month)            
        
           