n=int(input("Enter a number : "))
r=int(input("Enter range of table : "))
print("Multiplication Table of",n,"is")
for i in range(0,r):
      i=i+1
      print(n,"X",i,"=",n*i)

print("Loop completed")