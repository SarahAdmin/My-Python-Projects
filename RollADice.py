import random 

print("Roll the Dice") 
dice = random.randrange(1,6)

if dice == 1: 
  print(dice)
  print("You rolled Number 1")
elif dice == 2: 
  print(dice)
  print("You rolled Number 2") 
elif dice == 3: 
  print(dice) 
  print("You rolled Number 3")
elif dice == 4: 
  print(dice) 
  print("You rolled Number 4")
elif dice == 5: 
  print(dice)
  print("You rolled Number 5")
elif dice == 6: 
  print(dice) 
  print("You rolled Number 6") 
else: 
  print("No Number")

