import random
import lists

# The wordlist the game can choose from
wordlist = ["elephant", "tower", "gang", "plate", "car", "ultraviolet"]

# A random word is chosen
rand_word = random.choice(wordlist)

# A list full of blanks is generated
guess_list = []
for i in range(0, len(rand_word)):
    guess_list.append('_')


# Print the welcome statement
lists.welcome()



lives = 6
state = False
# Main 'while' loop starts
while state == False:
    #Check if the lives are > 0
    if lives > 0:
        
        # Check at the start of each loop if there are blanks left
        if '_' in guess_list:
            
            # Take an input guess from the user
            guess = input("Guess a letter: ").lower()
    
            # Loop through the random word to see if the guess matches
            tally = 0
            for i in range(0, len(rand_word)):
                if guess == rand_word[i]:
                    guess_list[i] = guess
                    tally += 1

            #When you guess wrong
            if tally == 0:
                lives -= 1
                lists.print_hangman(lives)
                
            print(guess_list)
        
        
        # The winning condition    
        else:
            print("You win!")
            state = True
    # When you run out of lives
    else:
        print("You lose!")
        state = True
    
    

    
    


