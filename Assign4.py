#!python3
"""
Billy is inviting people to his party.  He is accepting requests
from his friends, but only wants to send 1 invitation out per
person. He decides to store names in a list, and only add the
ones that are not already there.  Can you help a brother out?

Your program should keep asking the user to enter in a name 
(first and last).  If the name is not on the list, add it,
otherwise say "That name is already on the list".

if the user enters in a blank line, then stop the input.
Sort the list of names (it will be sorted by first name)
and print out all of the names on the list.  Also print out
the number of names on the list so he knows how many 
invitations to send.

This program will require you to incorporate everything we
have learned so far.
"""
IGNORE_CAPITALIZATION=True

def main():
    name_list = []
    print("----------")

    while True:
        
        proposed_name = input("enter first and last name with a space in between, enter nothing to finish: ")

        if IGNORE_CAPITALIZATION:
            proposed_name = proposed_name.lower()
        
        if proposed_name=="":
            break
        else:

            try:
                name_list.index(proposed_name)
                print("that name is already in the list!")
                
            except:
                
                name_list.append(proposed_name)
                print("added name "+proposed_name+" to the list")

    name_list.sort()
    print("----------------")
    print("you have entered "+str(len(name_list))+" names into your list, meaning you need "+str(len(name_list))+" invitations")
    print("the whole collection of names are: ",name_list)


if  __name__== "__main__":
    main()

        
