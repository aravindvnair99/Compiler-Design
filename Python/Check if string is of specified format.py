'Check if string is of format a.(b+c)*'

print("Enter z to terminate.\n")
string = ""
while string != "z":
    string = input("Enter the string to be checked: ")
    count = 0
    if string[0] == "a":
        for i in range(1, len(string)):
            if string[i] == "b" or string[i] == "c":
                count += 1
            else:
                print("Not of format a.(b+c)*\n")
                break
        if count == len(string) - 1:
            print("It is of format a.(b+c)*\n")
    else:
        print("Not of format a.(b+c)*\n")
