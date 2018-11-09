#Implement a progam to convert the input string to inverse case(upper->lower, lower->upper) ( without using standard library)

line1 = input ('Enter your string: ')
g = ""
for ch in line1:
    if ord (ch) >= 97 and ord(ch) <= 122:
        x = ord(ch) - 32
        y = chr (x)
        g = g + y
    else :
        x = ord(ch) + 32
        y = chr (x)
        g = g + y
print(g)
