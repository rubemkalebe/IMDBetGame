'''
Created on 20 de mar de 2017

@author: rubemkalebe
'''

class WriteToFile(object):
    '''
    Class for writing the simulation result to a file
    '''


    def __init__(self, path):
        '''
        Constructor with the file path
        '''
        self.__path = path
        
    '''
    Write the simulation result to a file
    '''
    def write(self, result, rows, colums):
        res_file = open(self.__path, 'w')
        for i in range(rows):
            for j in range(colums):
                res_file.write(str(result[i][j]) + ' ')
            res_file.write('\n')