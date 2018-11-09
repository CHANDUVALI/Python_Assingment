#Implement a program to convert the input string to upper case (without using standard library)

Str1=input("Enter the string to be converted uppercase: ")

for i in range (0,len(Str1)):

   x=ord(Str1[i])
   if x>=97 and x<=122:
       x=x-32
   y=chr(x)
   print(y,end="")
