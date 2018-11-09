#Implement a program to find the euclidean distance of two points

import math
x = (1, 2, 3)
y = (3, 2, 1)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ",distance)
