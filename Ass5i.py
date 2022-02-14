#Categorize the person depending on the height a.<150 Dwarf b.=150 Average heighted c.>=165 Tall
height=int(input("Enter the Height(in centimeters)"))
if height<150:
    print("Dwarf\n")
elif height==150:
    print("Average Heighted\n") 
elif height>=165:
    print("Tall\n")
else:
    print("Abnormal Height")          