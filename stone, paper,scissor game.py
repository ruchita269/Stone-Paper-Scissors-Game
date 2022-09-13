import random

def game(comp,you):
    if comp==you:
     return None
    elif comp=="s":
        if you=="p":
          return False
        elif you=="sci":
            return False
    elif comp=="p":
        if you=="s":
          return False
        elif you=="sci":
            return True
    elif comp=="sci":
        if you=="s":
          return True
        elif you=="p":
            return False
                    
                    
print("computer turn: stone(s) paper(p) scissor(sci)?")
randomno=random.randint(1,3) 
if randomno==1:
   comp="s"
elif randomno==2:
   comp="p"
elif randomno==3:
    comp="sci"

you=input("your turn: stone(s),paper(p), scissor(sci)?")
a=game(comp,you)
print(f"computer choose: {comp}")
print(f"you choose:{you}")
if a ==None:
    print("the game is tie")
elif a:
    print("you win!")    
else:
    print("you lose...")