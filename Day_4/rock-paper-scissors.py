import random as r
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_shape=[rock,paper,scissors]

Computer_choice=r.randint(0,2)
print("Computer_choice\n"+str(game_shape[Computer_choice])+"\n")

user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: "))
print("user_choice\n"+str(game_shape[user])+"\n")

try:
    if Computer_choice==2 and user==0:
        print("user win")
        
    elif Computer_choice==0 and user==2:
        print("computer win")

    elif Computer_choice==2 and user==1:
        print("user win")

    elif Computer_choice==1 and user==2:
        print("computer win")

    elif Computer_choice==1 and user==0:
        print("computer win")
        
    elif Computer_choice==0 and user==1:
        print("user win")    
    elif Computer_choice == user:
        print("It's a draw")    
except:
    print('Enter a valid number, please.')   