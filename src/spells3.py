'''
Created on Oct. 18, 2023
Asks the user to practice typing a randomly selected spell from a provided list now with a score system and the ability to do multiple spells
@author: Sebastian
'''
import random 

def read_spells(file) :
    '''
    Reads a list of spells from a provided file and returns a spell at random
    '''
    file = open(file, "r")
    spell_list = file.readlines() #creates a list containing all the spell names
    for idx in range(len(spell_list)) :
        spell_list[idx] = spell_list[idx].strip() #removes the new line character from every spell in the list
    return spell_list

def get_random_spell(spell_list):
    '''
    Returns a random spell from the provided list of spells
    '''
    return spell_list[random.randint(0,(len(spell_list) - 1))]

def display_header():
    '''
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    '''
    print("#"*60)
    print("Harry Potter Typing Trainer")
    print("#"*60)
    
def display_instructions() :
    '''
    Displays instructions from instructions.txt
    '''
    file = open("instructions.txt", "r") 
    lines = file.readlines()
    file.close()
    for idx in range(len(lines)) :
        print(lines[idx])
    return
    
def get_user_input(spell) :
    '''
    receives the spell as user input and returns it
    '''
    return input(f"Please type the following spell: {spell}\n")

def display_feedback(spell, user_input):
    '''
    Receives the correct spelling of a spell and the user's input and compares them to see whether or not they match
    '''
    if spell.upper() == user_input.upper() :
        return print("Correct!")
    else :
        return print(f"Incorrect!\nThe spell was: {spell}")
        
    
def play_again() :
    '''
    Asks the user if they wish to play again, returns true if y, Y otherwise returns false
    '''
    user = input("Do you want to play again y/n?: ")
    if user.lower() == "y" :
        return True
    else :
        return False
    
def main():
    '''
    Main Function
    '''
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    continue_game = True
    score = 0
    while continue_game : #Repeats the game until the player chooses not to play anymore
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        if spell.upper() == user_input.upper() :
            score += 10
        else : 
            score -= 5    
        print(f"Your Score Is: {score}")
        continue_game = play_again()
    print(f"Your Final Score Is: {score}")
main()