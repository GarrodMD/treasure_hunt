print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input("You find yourself on a darkened path, trees stretching either side but a lone swinging lantern ahead reveals a sign post. Pointing to the left you see faded words but it seems to say 'La..e'. On the right you see the words written 'Inn'. Do you go left or right?\n").lower()
if choice1 == "left":
    choice2 = input("You find yourself at a lake side as you go over the close ridge and down the bank, the still dark expanse of water stretches out but you spot two things, an island at the centre and a boat headed your way. Do you swim or wait?\n").lower()
    if choice2 == "wait":
        choice3 = input("The boatman picks you up, a bit of a sketchy character but you soon arrive at the island in the centre. A vast mansion is infront of you, old and creaking, 3 doors lead into the building. One painted red, one yellow, one green. Which do you go through?\n").lower()
        if choice3 == "yellow":
            print("You push open the door and step inside, as the door closes behind you candles ignite as if by magic glittering off the piles of gold and gems. The stories were true and the treasure is yours! YOUR WIN!   Hopefully you can carry enough and find your way home....")
        elif choice3 == "red":
            print("You push open the door and step inside, as the door closes beind you candles ignite as if by magic illuminating the body of an armoured man, all bones and sinew. As you turn to leave the door does not budge. The sound of metal clanking turns you around and before you can scream skeletal hands close on your throat, cutting off your cry....forever....Game Over")
        elif choice3 == "green":
            print("You psuh open the door and step inside to darkness, your first step meets nothing but empty air and you tumble down into a deep pit and impact at the bottom hearing a snap, a broken leg by the feel of it. You feel around and find a single coin....too bad your cannot climb out of the pit to spend it....Game Over")
    elif choice2 == "swim":
        print("Your arms grow tired from swimming, the cold sinks into your bones, you sink beneath the surface, never to return....Game Over")
    else:
        print("That is not a valid answer, your adventure is cut short by a typo, the treasure was going to be great just so you know...Game Over")
elif choice1 == "right":
    print("The encroaching darkness closes in, you didn't see the inn was 20 miles away and by that time the hungry wolves had already picked up your trail even running wouldn't save you....Game Over")
else:
    print("That is not a valid answer, your adventure ends before it has begun due to your inability to decide or spell....Game Over")