word=input("give a string")
print("1.prefix")
print("2.suffix")
print("3.proper prefix")
print("4.proper suffix")
print("5.substring")
print("6.proper substring")
print("0.stop")
opt=int(input("give an option"))

def prefix(word):    
    print(word)
    for i in range(1,len(word)):
        s=word[:-i]
        print(s)
    print("*")
    
def suffix(word):
    print(word)
    for i in range(1,len(word)):
        s=word[i:]
        print(s)
    print("*")

def p_prefix(word):
    for i in range(1,len(word)):
        s=word[:-i]
        print(s)

def p_suffix(word):
    for i in range(1,len(word)):
        s=word[i:]
        print(s)
        
def substring(word):
    for i in range(1,len(word)):
        for j in range(0,len(word)-i+1):
            s=word[j:j+i]
            print(s)
    print(word)
    print("*")
    
def p_substring(word):
    for i in range(1,len(word)):
        for j in range(0,len(word)-i+1):
            s=word[j:j+i]
            print(s)
        
while(opt!=0):
    if(opt==1):
        prefix(word)

    elif(opt==2):
        suffix(word)

    elif(opt==3):
        p_prefix(word)

    elif(opt==4):
        p_suffix(word)

    elif(opt==5):
        substring(word)

    elif(opt==6):
        p_substring(word)

    opt=int(input("give an option"))    


        
        
    
