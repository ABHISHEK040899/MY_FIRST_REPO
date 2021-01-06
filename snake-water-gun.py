

import random
a=["snake","water","gun"]
print("enter snake ,water or gun")
b=input()
c=random.choice(a)
h=0
comp=0
i=1
while i<=10:
    print("enter snake ,water or gun")
    b=input()
    c=random.choice(a)
    
    if b=="snake" and c=="water":
        print("computer choice",c)
        print("************ \n YOU WON \n ****************")
        i+=1
        h+=1
    elif b=="water" and c=="gun":
        print("computer choice",c)
        print("************ \n YOU WON \n *****************")
        i+=1
        h+=1
    elif b=="gun" and c=="snake":
        print("computer choice",c)
        #print("************ \n YOU WON  \n *****************")
        i+=1
        h+=1
    elif b=="snake" and c=="gun":
        print("computer choice",c)
        #print("************ \n YOU LOSE \n ******************")
        i+=1
        comp +=1
    elif b=="water" and c=="snake":
        print("computer choice",c)
        #print("************ \n YOU LOSE \n ******************")
        i+=1
        comp +=1
    elif b=="gun" and c=="water":
        print("computer choice",c)
        #print("************ \n YOU LOSE \n ******************")
        i+=1
        comp +=1
    elif b=="snake" and c=="snake":
        print("computer choice",c)
        #print("************ \n DRAW \n ******************")
        i+=1
        
    elif b=="water" and c=="water":
        print("computer choice",c)
       # print("************ \n DRAW \n ******************")
        i+=1
        
    elif b=="gun" and c=="gun":
        print("computer choice",c)
       # print("************ \n DRAW \n ******************")
        i+=1
print(f"computer won {comp} times")
print(f"you won {h} times")
print("hellow")        
        
    




