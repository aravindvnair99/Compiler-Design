n1=int(input("give size of first lang"))
n2=int(input("give size of second lang"))
l1=[]
l2=[]
for i in range(0,n1):
    l1.insert(i,input())
for i in range(0,n2):
    l2.insert(i,input())

print("1.union")
print("2.intersection")
print("3.difference")
print("4.concatenation")
print("5.kleen closure")
print("6.positive closure")
print("0.stop")

def union(l1,l2):
    print(list(set(l1) | set(l2)))

def intersection(l1,l2):
    print(list(set(l1) & set(l2)))

def difference(l1,l2):
    print(list(set(l1) - set(l2)))

def concatenation(l1,l2):
    l3=[]
    for i in range(0,n1):
        for j in range(0,n2):
            l3.append(l1[i]+l2[j])
    print(l3)
def concatenate(l1,l2):
    l3=[]
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            l3.append(l1[i]+l2[j])
    return l3        
def kleen_closure(l1):
    n=int(input("give limit ma"))
    temp=l1
    l4=temp
    for i in range(1,n):
        l4=list(set(l4) | set(concatenate(temp,l1)))
        temp=l4;
    l4.append("*")
    print(l4)      
def positive_closure(l1):
    n=int(input("give limit ma"))
    temp=l1
    l4=temp
    for i in range(1,n):
        l4=list(set(l4) | set(concatenate(temp,l1)))
        temp=l4;
    print(l4)           
          

opt = int(input("select option"))
while(opt!=0):
    if(opt==1):
        union(l1,l2)
    elif(opt==2):
        intersection(l1,l2)
    elif(opt==3):
        difference(l1,l2)
    elif(opt==4):
        concatenation(l1,l2)
    elif(opt==5):
        kleen_closure(l1)
    elif(opt==6):
        positive_closure(l1)
    opt = int(input("select option"))
