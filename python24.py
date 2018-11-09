# Implement a program to read alternative characters in the file.

file = open("char_read.txt")
text = file.read()

#Extended Slice
print(text[::4])

file.close()
