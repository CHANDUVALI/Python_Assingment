#Implement a python program to check whether two circles interesect or not.

def circle(x1, y1, x2, y2, r1, r2): 
   
    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);  
    radSumSq = (r1 + r2) * (r1 + r2);  
    if (distSq == radSumSq): 
        return 1 
    elif (distSq > radSumSq): 
        return -1 
    else: 
        return 0 
   

x1 = 5
y1 = 8 
x2 = 14
y2 = -5 
r1 = 60
r2 = 11 
  
t = circle(x1, y1, x2, y2, r1, r2)  
if (t == 1): 
    print("Circle touch to each other.")  
elif (t < 0): 
    print("Circle not touch to each other.")  
else: 
    print("Circle intersect to each other.")
