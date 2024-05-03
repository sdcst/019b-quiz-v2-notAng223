#!python3
"""
Fix this program.
It should ask the user to enter in 10 numbers and see
if the number is positive or negative
"""
for n in range(10):
    print("------"+str(n+1)+"/10;")
    user_input = float(input("enter a number: "))
    if user_input > 0:
        print('that is a positive number')
    elif user_input < 0:
        print('that is a negative number')
