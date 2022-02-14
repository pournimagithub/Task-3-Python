#Accept Marital status and print Miss or Mrs in front of name
surname=input("Enter your surname:")
gender=input("Enter in your gender information(male or female):")
maritalstatus=input("Enter in your marital status information(single or married):")
if gender=="m" or gender=="M" or gender=="male" or gender=="Male":
    if maritalstatus=="single":
        print("Mr"+surname)
    else:
        print("Mr"+surname) 
elif gender=="f" or gender=="F" or gender=="female" or gender=="Female":
    if maritalstatus=="single":
        print("Miss"+surname)
    else:
        print("Mrs"+surname)          
         