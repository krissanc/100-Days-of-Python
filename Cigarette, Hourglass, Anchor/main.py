# * Anchor, Cigarette, Hourglass Game *

import random
import ascii_art

player_choice = int(input("Choose your destiny: "))
if player_choice >= 1 and player_choice <= 3:
  pc_choice = random.randint(1, 3)

  
  print("You chose: ",  ascii_art.choices[player_choice - 1])
  print("The PC chose: ", ascii_art.choices[pc_choice - 1])
  
  if player_choice == pc_choice:
    print("The game is a draw.")
  
  if player_choice == 3 and pc_choice == 2:
    print("Anchor beats Hourglass. You win.")
  
  if player_choice == 3 and pc_choice == 1:
    print("Cigarette beats Anchor. You lose.")
  
  if player_choice == 2 and pc_choice == 3:
    print("Anchor beats Hourglass. You lose.")
  
  if player_choice == 2 and pc_choice == 1:
    print("Hourglass beats Cigarette. You win.")
  
  if player_choice == 1 and pc_choice == 3:
    print("Cigarette beats Anchor. You win.")
  
  if player_choice == 1 and pc_choice == 2:
    print("Hourglass beats Cigarette. You lose.")
  
else: 
  print("Please choose a number between 1 and 3")
