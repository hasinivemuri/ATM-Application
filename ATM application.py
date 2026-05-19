#ATM APPLICATION

amount=100000
a=input("insert the card")
if a=="c":
    print("Welcome Hasini")
else :
    print("Invalid card")
b=int(input("Enter the password"))
if b==1234:
    print("login successful")
else:
    print("login invalid")
c=int(input("choose the option 1.Account Balance 2.Withdraw"))
if c==1:
    print("Your Account Balance is",amount)
elif c==2:
    d=int(input("Amount to be Withdrawn"))
    print("The remaining balance is",amount-d)
else:
    print("Option not found")   
        
        



                    
