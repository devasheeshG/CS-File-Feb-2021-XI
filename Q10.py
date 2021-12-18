def reverse(string):
    string=string[::-1]
    return string
string=input("Enter the string : ")
print("Original string is : ",string)
rev_str=reverse(string)
print("Reversed string is : ",rev_str)
