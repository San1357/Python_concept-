# problem1 : Take values of length and breadth of a rectangle from user and check if it is square or not.

length = float(input("Enter the length of rectangle"))
breadth = float(input("Enter the breadth of rectangle"))
squareoflength = length * length 
squareofbreadth = breadth * breadth 
if squareofbreadth == squareoflength:
    print ("It is Square.")
else:
    print("No,It is not square.")
