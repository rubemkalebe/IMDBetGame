'''
Created on 20 de mar de 2017

@author: rubemkalebe
'''
from dice import Dice
from elevator import Elevator
from random import randint
import numpy

class Simulator(object):
    '''
    It simulates the Bet Game
    '''


    def __init__(self):
        '''
        Constructor
        Initializes the threshold variables and the array which will store the
        result
        '''
        self.__ROUNDS = 500
        self.__EPOCH = 100
        self.__result = numpy.zeros(shape = (self.__ROUNDS, self.__EPOCH), dtype = numpy.int)
        
    '''
    Runs simulation
    '''
    def run(self):
        dice = Dice()
        for i in range(self.__ROUNDS):
            elevator = Elevator()
            for j in range(self.__EPOCH):
                '''
                There is a 0,1% probability that assign the step to 0 (zero)
                in each step.
                '''
                if randint(1, 1000) == 1:
                    elevator.current_floor = 0
                else:
                    dots = dice.throw()
                    try:
                        if dots == 1 or dots == 2:
                            elevator.move_down() # move one floor down
                        elif dots > 2 and dots < 6:
                            elevator.move_up(1) # move one floor up
                        else:
                            x = dice.throw()
                            elevator.move_up(x) # move 1..6 floors up
                    except ValueError:
                        pass
                numpy.put(self.__result[i], j, elevator.current_floor)
                    
                    
    def get_result(self):
        return self.__result
    
    def get_rounds(self):
        return self.__ROUNDS

    def get_epoch(self):
        return self.__EPOCH
    
    result = property(get_result, None, None, None)
    ROUNDS = property(get_rounds, None, None, None)
    EPOCH = property(get_epoch, None, None, None)
