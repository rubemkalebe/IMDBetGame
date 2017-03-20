'''
Created on 19 de mar de 2017

@author: rubemkalebe
'''
from random import randint

class Dice(object):
    '''
    It represents a traditional dice with six different faces
    Each face has an integer between 1 and 6
    '''
    
    def __init__(self):
        '''
        Constructor where the threshold variables are initialized
        '''
        self.__MIN = 1
        self.__MAX = 6
        
    '''
    The act of throw a dice is done by simply generating a random integer from 1 to 6
    '''
    def throw(self):
        return randint(self.__MIN, self.__MAX)