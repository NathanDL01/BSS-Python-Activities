print("---------------------------------------------------------")
print("\n\n\t     JERN Cleaning Services")
print("\n\t\tServices Offered")
print("\n\n   CODE   |\t   Service Name    \t  |   Price")
print("\n\n    GTC   |  Grease Trap Cleaning         |   700 Php")
print("\n    STC   |  Studio Type Condo Cleaning   |   1000 Php")
print("\n   1BR    |  1 Bedroom Condo Cleaning     |   2000 Php")
print("\n--------------------------------------------------------")

x=eval(input("\nHow many services do you want to avail? "))

a=0
b=0
c=0

for y in range(x):
    s=input("\n   Input the code of the services you want to avail: ")
    q=input("\n   Type the quantity of your appointment: ")
    if s==str("gtc"):
        print("\tYou availed",q ,"Grease Trap Cleaning")
        p=700
        t=p*q
        print=t
        t=a
    elif s==str("stc"):
        print("\tYou availed",q ,"Studio Type Condo Cleaning")
        p=1000
        t=p*q
        print=t
        t=b
    elif s==str("1br"):
        print("\tYou availed",q ," 1 Bedroom Condo Cleaning")
        p=2000
        t=p*q
        print=t
        t=c
    else:
        print("INVALID INPUT;")






