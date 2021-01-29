'Make string of format a.(b+c)*'

print("Enter z to terminate.\n")
string = "a"
choice = ""
while choice != "z":
    choice = input("Which one? 'b' or 'c'? ")
    if choice == "b" or choice == "c":
        string += choice
    print("The current string is: " + string)
print("The final string is: " + string)
