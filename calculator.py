print("Welcome to Calculator")
print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
operation=input("Enter Operation:")
if operation=='1' :
    n1=int(input("Enter the 1st Number :"))
    n2=int(input("Enter the 2nd Number:"))
    print("The Addition is :",n1+n2)
elif operation == '2':
        n1 = int(input("Enter the 1st Number :"))
        n2 = int(input("Enter the 2nd Number:"))
        print("The Subtraction is :", n1 - n2)
elif operation == '3':
        n1 = int(input("Enter the 1st Number :"))
        n2 = int(input("Enter the 2nd Number:"))
        print("The Multipliction is :", n1 * n2)
elif operation == '4':
            n1 = int(input("Enter the 1st Number :"))
            n2 = int(input("Enter the 2nd Number:"))
            print("The Divition is :", n1 / n2)
else:
    print("Invalid Input")
