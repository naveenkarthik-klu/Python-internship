try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(num1+num2)
except NameError:
    print("\nNameError: Please Use Numbers Only\n")
