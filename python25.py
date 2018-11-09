# Implement a function to count the number of vowels present in the file. 

fileName = input("Enter the file to check: ")
infile = open(fileName, "r")
vowels = set("AEIOUaeiou")


count = 0

for c in infile.read():
    if c in vowels:
        count += 1
   
print("The number of Vowels is: ",count)
