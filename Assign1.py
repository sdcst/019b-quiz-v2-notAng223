#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program
num_of_inputs=5
total_sum=0
for i in range(num_of_inputs):
    curr_num = input("enter number "+str(i+1)+"/"+str(num_of_inputs)+": ")
    total_sum += float(curr_num)

print("the average of all the numbers you enterd is "+str(round(total_sum/num_of_inputs, 2)))