from random_word_generator import pick_random_word

def change_current_word_state(selected_word,input_char,current_word_state):
    modified_word_state="" 

    for i in range(len(selected_word)):
        if current_word_state[i]=="_" and selected_word==input_char:
            modified_word_state+=selected_word[i]

        else:
            modified_word_state+=current_word_state[i]

    return modified_word_state        

                   



def input_char_in_word(selected_word,input_char,current_word_state,atttempts_remaining):
    if input_char in selected_word:
        current_word_state= change_current_word_state(selected_word,input_char,current_word_state)
    else:
        atttempts_remaining-=1

    return current_word_state,atttempts_remaining        



def print_current_state(current_word_state,attempts_remaining):
    #This function will print the current status of the game that is the alphabets guessed so far  and attempts remaining.

    print('current_word_state: ',end=' ')

    for i in current_word_state:
        print(i,end=' ')

    print("\t Attemts_remainig: {}".format(attempts_remaining))    


def check_game_status(selected_word,current_word_state,atttempts_remaining):
    if atttempts_remaining<=0:
        print("sorry you lost ! :( ")
        print("The word was : {}".format(selected_word))
    return False

    if selected_word == current_word_state:
        print("congratulations ! You won.. ")
        return False

    return True  





def play_game(attempt=5):
    # This function will conatain main logic of the game

    #To store the randomly picked word we declare a variable named as 'selected_word'
    selected_word = pick_random_word()

    #To show current state of the picked word
    current_word_state=""

    for i in selected_word:
        if i==' ' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            current_word_state+=i
        else:
            current_word_state+='_'
            
    atttempts_remaining = attempt 

    print_current_state(current_word_state,atttempts_remaining)

    while True:
        input_char = input("guess the character: ")
        print("")  

        current_word_state,atttempts_remaining = input_char_in_word(selected_word,input_char,current_word_state,atttempts_remaining)      

        print_current_state(current_word_state,atttempts_remaining)

        game_end_checker = check_game_status(selected_word,current_word_state,atttempts_remaining)

        if game_end_checker == False:
            break







if __name__ == '__main__':
    play_game()
    
    