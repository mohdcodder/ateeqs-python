import random
count=0
while(count<=100):
    roll=input("press 'r' to roll a dice")
    if   roll=='r':
     r=random.randint(1,6)
    
     print("your random no is",r)
     print("you are in position",count)
     count=count+r
     print(count)
    if count>100:
         print("oops the number is greater than 100")
         count=count-r
    elif count==100:
         print("u win baa")
         break
        
    if   count==100:
         print("yahoooo u won")
    elif count==8:
         count=37
         print("upsyyy diasyyy")
    elif count==11:
         count=2
         print("ouch!!!!!! was that a snake")
    elif count==13:
         count=34
         print("lets hurry up!!!!")
    elif count==25:
         count=4
         print("aghhhh not again :(....")
    elif count==38:
         count=9
         print("i wanna kill it aghhh!!!!")
    elif count==40:
         count=68
         print("here i come hehehe XD")
    elif count==52:
         count=81
         print("lets gooo mates.... follow mehh!!")
    elif count==65:
         count=46
         print("damnnn snakes!!")
    elif count==76:
         count=97
         print("iam just great hahaha")
    elif count==89:
         count=70
         print("ooopppsss...soo closee!!")
    elif count==93:
         count=64
         print("cheer up... lets go again")
    if count<100:
         print("continue playing")
    if   count>=100:
         print("game over")
