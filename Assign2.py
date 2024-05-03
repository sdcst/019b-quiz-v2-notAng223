"""
Write a program that uses a for loop.
Each iteration will ask the user to enter a name
Add the input to the provided list
"""
names = []
number_of_names=5
for i in range(number_of_names):
    names.append(input("enter name "+str(i+1)+" / "+str(number_of_names)+": "))

print(names)