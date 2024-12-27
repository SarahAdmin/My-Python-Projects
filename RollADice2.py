import random 
num = random.randrange(1,7)
name = input("Enter your name: ")
print("Roll-A-Dice")
if num == 1: 
    print(num)
    print(name+' You rolled One')
elif num == 2: 
    print(num)
    print(name+' You rolled Two')
elif num == 3:
    print(num)
    print(name+' You rolled Three')
elif num == 4:
    print(num)
    print(name+' You rolled Four')
elif num == 5:
    print(num)
    print(name+' You rolled Five')
elif num == 6: 
    print(num)
    print(name+' You rolled Six')
else:
    print(num)
    print(name+' You have no number')
