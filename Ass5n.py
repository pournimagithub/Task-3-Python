#Write a Menu driven program for following
#Area of circle(pi*r2)
#Area of Rectangle(l*b)
#Area of triangle(b*h/2)
#Area of Square(a^2)
print("1.Area of Circle")
print("2.Area of Rectangle")
print("3.Area of Triangle")
print("4.Area of Square")
choice=int(input("Enter your choice"))
if choice==1:
    r=int(input("Enter radius of circle:"))
    print("Area of Circle:",3.14*r*r)
elif choice==2:
    l=int(input("Enter length of Rectangle:"))
    b=int(input("Enter breadth of Rectangle:"))
    print("Area of Rectangle:",l*b)   
elif choice==3:
    b=int(input("Enter breadth of Triangle:")) 
    h=int(input("Enter height of Triangle:"))
    print("Area of Triangle:",b*h/2)  
elif choice==4:
    a=int(input("Enter side of Square:"))
    print("Area of Square",a*a)
          