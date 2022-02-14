#Write a python program to calculate surface area and volume of a cylinder
pi=3.14
radius=float(input("please enter the radius of a cylinder:"))
height=float(input("please enter the height of a cylinder:"))
sa=2*pi*radius*(radius+height)
volume=pi*radius*radius*height
L=2*pi*radius*height
T=pi*radius*radius
print("\n The surface area of a cylinder=%2f"%sa)
print("The volume of a cylinder=%2f"%volume)
print("Lateral Surface area of cylinder=%2f"%L)
print("Top or Bottom Surface Area of a cylinder=%2f"%T)
