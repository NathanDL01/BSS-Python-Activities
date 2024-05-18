#Collatz Conjecture
d=0
while d==0:
    n=eval(input("Enter a positive integer (or 0 to exit): "))
    if n==0:
        print("Goodbye!")
        break
    if n!=0:
        steps=0
        while n!=1:
            steps+=1
            if n%2==0:
                n==n//2
            else:
                n==(n*3)+1
    
    






















