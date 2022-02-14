#WAP to determine if the seller has made profit or loss. Display amount of profit/loss.
cp=float(input("Enter the cost price:"))
sp=float(input("Enter the selling price:"))
if cp==sp:
    print("No Profit No Loss")
else:
    if sp>cp:
        print("Profit of",sp-cp)
    else:
        print("Loss of",cp-sp)        