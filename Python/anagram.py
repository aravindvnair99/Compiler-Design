INPUT1 = input("Enter the first string: ")
INPUT2 = input("Enter the second string: ")

for item in INPUT2:
    if item in INPUT1:
        continue
    else:
        print("Not anagram.")
        exit(0)
print("Anagram")
