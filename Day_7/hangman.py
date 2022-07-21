from hangman_art import words,stages
import random
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')


word = random.choice(words)

blank_list =[]
for _ in range(len(word)):
        blank_list.append("_")
print(blank_list)
index=-1
end_of_game=False
while not end_of_game:
    guess=str(input("guess A Letter :").lower())

    check=True
    for i in range(len(word)):
        letter=word[i]
        if guess == letter:
            blank_list[i]=letter
            check=False
    if "_" not in str(blank_list):
        print("you are win")
        end_of_game=True              

    if check:        
        print("you are enter a wrong guess char")
        print(stages[index]) 
        print(index)
        index-=1
        
            
        if index <-7:
            print("you are lose") 
            end_of_game=True              
        
    print(blank_list)
    