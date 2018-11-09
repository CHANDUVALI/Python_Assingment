#Implement a program to create a dictionary of students with Registration number and names. Perform the two operations, insert and delete. 

thisdict =	{
  "Name": "chandan",
  "Reg no": "181040015",
  "Sex": "Male",
}
print(thisdict)

#insert
thisdict["Age"] = "23"
print(thisdict)

#delete
thisdict.pop("Sex")
print(thisdict)

