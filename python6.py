#Create a list with 5 branches in SOIS. Try to do the following operations a) append b) insert c) sort d) reverse sort 

branches = ['EWT', 'ESI', 'AES', 'VLSI',]
branches.append('BIG DATA')

#append
print('Appended List is: ', branches)

#insert
branches.insert(1, 'IOT')
print('Inserted List is: ',branches)
branches.sort()

#sort
print('Sorted list: ', branches)
branches.sort(reverse = True)

#reverse sort 
print('Sorted list(Descending Order): ', branches)



