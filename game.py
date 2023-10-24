import sys

# Story strings
opening = """
Welcome adventurer! You are embarking on a quest to find the lost treasure of the Ancient Temple. Your journey begins on a dirt road winding through a dark forest. Up ahead you see a fork in the road. Which path do you take? 
"""

left_path = """
You take the path on the left which leads deeper into the dark forest. The canopy overhead blocks most sunlight. After hiking for a mile, you come across a rickety old bridge over a raging river. Do you attempt to cross the bridge or head back?
"""

right_path = """
You take the path on the right which leads out of the forest towards the mountains in the distance. The road takes you to the entrance of a large, foreboding cave. Do you enter the cave or continue on the road? 
"""

# Game loop
while True:
  print(opening)
  choice1 = input("Enter 'left' or 'right' to make your choice:\n")
  
  if choice1.lower() == "left":
    print(left_path)
    choice2 = input("Enter 'cross' or 'back' to make your choice:\n")
    if choice2.lower() == "back":
      print("You head back and retrace your steps until you reach the fork again.")
    elif choice2.lower() == "cross":
      print("You attempt to cross the bridge but a plank breaks and you fall into the river! Game over.")
      break 
    else:
      print("Invalid choice! Game over.")
      break
        
  elif choice1.lower() == "right": 
    print(right_path)
    choice2 = input("Enter 'enter' or 'continue' to make your choice:\n")
    if choice2.lower() == "continue":
      print("You walk past the cave and continue on the road. You never reach the temple. Game over.")
      break
    elif choice2.lower() == "enter":
      print("You enter the cave and find the lost ancient treasure! You win!")
      break
    else:
      print("Invalid choice! Game over.")  
      break
  else:
    print("Invalid choice! Game over.")
    break

print("Thank you for playing!")