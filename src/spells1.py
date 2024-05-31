'''
Created on Oct. 18, 2023
Read a list of spells from a file then display a random one
@author: Sebastian
'''
import random 

def read_spells(file) :
    '''
    Reads a file containing multiple spells and returns them as a list
    '''
    file = open(file, "r")
    spell_list = file.readlines() #Creates a list of all spells in the provided file
    return spell_list

def get_random_spell(spell_list):
    '''
    Returns a random spell from the provided list of spells
    '''
    return spell_list[random.randint(0,(len(spell_list) - 1))] 

def main():
    '''
    Main Function
    '''
    spells = read_spells('spells.txt')
    print('Harry Potter Keyboard Trainer')
    spell = get_random_spell(spells)
    print(spell)

main()
