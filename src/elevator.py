'''
Created on 19 de mar de 2017

@author: rubemkalebe
'''

class Elevator(object):
    '''
    It simulates an elevator which starts at some floor, cannot go below zero,
    and should not have a maximum floor
    '''


    def __init__(self, current_floor = 0):
        '''
        Constructor that receives a current_floor and defines the minimum floor
        '''
        self.__MIN = 0
        self.__current_floor = current_floor
    
    '''
    It simulates the elevator going up x floors
    '''    
    def move_up(self, x):
        if(x > 0):
            self.__current_floor += x
        else:
            raise ValueError('Cannot move up with the value: ' + str(x))
    
    '''
    It simulates the elevator going down x floors
    '''
    def move_down(self, x = 1):
        if(self.__current_floor - x >= 0 and x > 0):
            self.__current_floor -= x
        else:
            raise ValueError('Cannot move down with the value: ' + str(x))
    
    
    def get_current_floor(self):
        return self.__current_floor

    def set_current_floor(self, value):
            self.__current_floor = value
            
    current_floor = property(get_current_floor, set_current_floor, None, None)
