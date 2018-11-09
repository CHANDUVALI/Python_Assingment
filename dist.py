#Implement a python program to find distance between two point.

import math
	
p1 = [1, 2]
p2 = [3, 3]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print(distance)
