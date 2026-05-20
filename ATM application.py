#ATM APPLICATION

amount = 100000

a = input("Insert the card: ")

if a == "c":
    print("Welcome Hasini")

    b = int(input("Enter the password: "))

    if b == 1234:
        print("Login successful")

        c = int(input("Choose the option\n1. Account Balance\n2. Withdraw\n"))

        if c == 1:
            print("Your Account Balance is", amount)

        elif c == 2:
            d = int(input("Amount to be Withdrawn: "))

            if d <= amount:
                print("The remaining balance is", amount - d)
            else:
                print("Insufficient balance")

        else:
            print("Option not found")

    else:
        print("Invalid password")

else:
    print("Invalid card")
        
        



                    
