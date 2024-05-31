'''
Created on Oct. 18, 2023
Asks the user to practice typing a randomly selected spell from a provided list now with a score system that grades based on time 
@author: Sebastian
'''
import random 
import time

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
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell):
    '''
    returns the target time to get the spell
    '''
    return 0.3 * len(spell)

def calculate_points(spell, user_input, user_time) :
    '''
    Calculates the total number of points that should be awarded based on correctness and the time it took to type
    '''
    target_time = get_target_time(spell)
    if spell.upper() == user_input.upper() :
        if user_time <= target_time : #Maximum value
            return 10
        elif user_time <= target_time*1.5 : #between target time and tt*1.5
            return 6
        elif user_time <= target_time*2 : #between tt*1.5 and tt*2
            return 3
        else : #less than tt*2
            return 1
    else : #wrong answer
        return -5     

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
        score += calculate_points(spell, user_input[0], user_input[1])    
        print(f"Your Score Is: {score}")
        continue_game = play_again()
    print(f"Your Final Score Is: {score}")
main()