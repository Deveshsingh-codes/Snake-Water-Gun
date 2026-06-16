import random
list=["s","w","g"]

Chance=10
No_of_chance=0
Computer_point=0
Human_point=0

print("\t\t\t\t\tSNAKE-WATER-GUN GAME\n\n")
#Making the game in while
while No_of_chance<Chance:
    _input=input("Snake,Water,Gun:")
    _random=random.choice(list)
    
    if _input==_random:
        print("Tie Both 0 point to each\n")
        
    #if user enter s
    elif _input=="s" and _random=="g":
        Computer_point=Computer_point+1
        print(f"your guess{_input} and Computer guess is {_random}\n")
        print("Computer wins 1 point\n")
        print(f"Computer_point is {Computer_point} and your point is {Human_point}\n")
    elif _input=="s" and _random=="w":
        Human_point=Human_point+1
        print(f"your guess {_input} and computer guess is {_random}\n")
    
    #if user enter w
    elif _input=="w" and _random=="s":
        Computer_point=Computer_point+1
        print(f"your guess{_input} and Computer guess is {_random}\n")
        print("Computer wins 1 point\n")
        print(f"Computer_point is {Computer_point} and your point is {Human_point}\n")
    elif _input=="w" and _random=="g":
        Human_point=Human_point+1
        print(f"your guess {_input} and computer guess is {_random}\n")
        
    #if user enter w
    elif _input=="w" and _random=="s":
        Computer_point=Computer_point+1
        print(f"your guess{_input} and Computer guess is {_random}\n")
        print("Computer wins 1 point\n")
        print(f"Computer_point is {Computer_point} and your point is {Human_point}\n")
    elif _input=="w" and _random=="g":
        Human_point=Human_point+1
        print(f"your guess {_input} and computer guess is {_random}\n")
print("GAME OVER")
if Computer_point==Human_point:
    print("TIE")
elif Computer_point>Human_point:
    print("Computer wins and You loose")
else:
    print("You wins and Computer loose")
print(f"Your point is {Human_point} and Computer point is {Computer_point}")    