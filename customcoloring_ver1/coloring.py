#Alejandro Rodriguez
#8/13/23
#Coloring.py class hold all functions used in main.py

import math

class Coloring(object):

    #init function hold n -> for standard coloring and block_n -> block coloring
    def __init__(self, n, block_n):
        self.n = n
        self.block_n = block_n

    ##################
    # Z_n functions  #
    ##################

    #build custom coloring list
    def build_custom_coloring(self, custom_input):

        #list that will contain the custom coloring
        custom_coloring = []
        
        #list will contain each integer from custom_input
        input_list = []

        #first loop will build the list input_list with each valueof custom_input
        for x in range(len(custom_input)):
            input_list.append(int(custom_input[x]))

        #


    pass




