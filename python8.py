#Implement a program to create a list with two tuple of fruits and vegetables. Access fruits separately and vegetables separately.

tuple_fru = ('Apple', 'Banana', 'pineapple', 'Pomagrenat')
tuple_veg = ('carrot', 'Brinjal', 'tomato', 'chilly')
my_list = list(zip(tuple_fru,tuple_veg))
for x in range(len(my_list)):	
  print(my_list[x])	
	














