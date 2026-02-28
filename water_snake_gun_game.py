import random
options=["water","snake","gun"]

while True:
    print("\nWELCOME IN WATER SNAKE GUN GAME\n")
    print("1.play")
    print("2.exit")
    try:
        player=int(input("enter your choice :"))
    except:
        print("invalid choice")
        continue
    if player==1:
        rand=random.choice(options)
        print("\n1.water")
        print("2.snake")
        print("3.gun")
        try:
            player_choice=int(input("enter your choice:"))
        except:
            print("invalid choice!")
            continue

        if player_choice not in(1,2,3):
            print("invalid choice")
            continue
        player_move=options[player_choice-1]

        print("computer chose ",rand)
        print("you chose ",player_move)
        
        if player_move==rand:
            print("it's a draw")
        elif(player_move=="water" and rand=="gun") or (player_move=="snake" and rand=="water") or (player_move=="gun" and rand=="snake"):
            print("you win\n")
        else:
            print("you lose")
    elif player==2:
        print("thank you for playing")
        break
    else:
        print("invalid choice")

        

            