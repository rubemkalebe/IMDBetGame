'''
Created on 19 de mar de 2017

@author: rubemkalebe
'''
from simulator import Simulator
from writer import WriteToFile

if __name__ == '__main__':
    print('Simulating...')
    simulator = Simulator()
    simulator.run()
    
    print('\nWriting...')
    writer = WriteToFile('result.out')
    writer.write(simulator.result, simulator.ROUNDS, simulator.EPOCH)
    
    print('\n-- END --')