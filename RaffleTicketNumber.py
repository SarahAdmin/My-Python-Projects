import random
name = input('Enter your name: ') 
rafflenum = random.randrange(1,100) 

if rafflenum < 10: 
  print(rafflenum) 
  print(name + ' Your raffle ticket number is between 0 and 9')
elif rafflenum < 20: 
  print(rafflenum) 
  print(name + ' Your raffle ticket number is between 10 and 19.')
elif rafflenum < 30: 
    print(rafflenum) 
    print(name + ' Your raffle ticket number is between 20 and 29.')
elif rafflenum < 40: 
  print(rafflenum) 
  print(name + ' Your raffle ticket number is between 30 and 39.')
elif rafflenum < 50: 
  print(rafflenum) 
  print(name + ' Your raffle ticket number is between 40 and 49.')
else: 
  print(rafflenum) 
  print(name + ' Your raffle ticket number is more than 50.')
