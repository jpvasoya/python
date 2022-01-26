import random
min_val = 1
max_val = 6
roll_again = "yes"
temp=[]
count=0
while roll_again == "yes" or roll_again == "y" or roll_again=='Y':
    print("Rolling The Dices...")
    print("The Values are :")
    dice1=random.randint(min_val, max_val)
    dice2=random.randint(min_val, max_val)
    temp.extend([(dice1,dice2)])
    count+=1
    if roll_again == 'yes' or roll_again=='y':
    	print(f"({dice1} , {dice2})")
    else:
    	print(temp[count-2])
    
    roll_again = input("Roll the Dices Again?") 