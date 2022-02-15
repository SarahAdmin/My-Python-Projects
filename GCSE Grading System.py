print("-----------Student Information--------------")
print("Enter Your Name:       ")
name = input()
print("Enter Your Address:           ")
address = input()
print("Enter your first GCSE Subject:    ")
subject = input()
print("Enter your marks:           ")
mark = int(input())

print("Name:   "+name)
print("Address:  "+address)
print("Subjects:   "+subject)

if (mark  > 145):
    print("Grade: 9")
elif (mark  > 137): 
    print("Grade: 8")
elif (mark  > 124): 
    print("Grade: 7")
elif (mark  > 115): 
    print("Grade: 6")
elif (mark >  105): 
    print("Grade: 5")
elif (mark > 74): 
    print("Grade: 4")
elif (mark > 45): 
    print("Grade: 3")
elif (mark > 19): 
    print("Grade: 2")
elif (mark > 0): 
    print("Grade: 1")
else:
    print("Grade: U")
