import random

choices=["s","w","g"]

Chance=10
No_of_chance=0
Computer_point=0
Human_point=0

print("\t\t\t\tSNAKE-WATER-GUN GAME\n\n")
#Making the game in while
while No_of_chance<Chance:
    _input=input("Snake(s),Water(w),Gun(g):").lower()
    
    if _input not in ["s","w","g"]:
        print("Invalid Input! Try again.\n")
        continue
    
    _random=random.choice(choices)
    
    print(f"Your guess: {_input}")
    print(f"Computer guess: {_random}")
    
    
    if _input==_random:
        print("Tie Both 0 point to each\n")
        
        
    elif (_input == "s" and _random == "w") or \
         (_input == "w" and _random == "g") or \
         (_input == "g" and _random == "s"):

        Human_point += 1
        print("You win 1 point!\n")

    else:
        Computer_point += 1
        print("Computer wins 1 point!\n")

    No_of_chance += 1

    print(f"Your Points: {Human_point}")
    print(f"Computer Points: {Computer_point}")
    print(f"{Chance - No_of_chance} chances left out of {Chance}\n")

print("GAME OVER\n")

if Human_point > Computer_point:
    print("You Win 🎉")

elif Computer_point > Human_point:
    print("Computer Wins 😢")

else:
    print("Match Tied 🤝")

print(f"\nFinal Score:")
print(f"Your Points = {Human_point}")
print(f"Computer Points = {Computer_point}")