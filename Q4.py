n=int(input("Enter a number : "))
i=1
f=1
if(n<0):
    print("Sorry, factorial does not exist for negative numbers")
elif(n==0):
    print("The factorial of 0 is 1")
else:
    for i in range(1,n+1):
        f=f*i
    print("The factorial of",n,"is",f)