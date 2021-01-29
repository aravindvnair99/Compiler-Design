import re

count = 0
INPUT_STR = input("Enter the string: ")
if re.search("(ba)+.(a*b*|a*)", INPUT_STR):
    print('String is accepted by first expression.')
    count += 1
else:
    print('String is not accepted by first expression.')
if re.search("(ba)*.b(a)+.(b+|)", INPUT_STR):
    print('String is accepted by second expression.')
    count += 1
else:
    print('String is not accepted by second expression.')
if count == 2:
    print('Equivalent.')
else:
    print('Not equivalent.')
