#Alejandro Rodriguez
#8/13/21
#custom block coloring or standard coloring of Z_n and [n]

#import my coloring class
from coloring import Coloring

#############
# main loop #
#############
while True:

    #promt user for choice
    print("Choose your structure.")
    print("(1): [n]")
    print("(2): Z_n")
    print("(3): exit")

    choice = int(input("choice: "))

    #############
    # [n] block #
    #############
    if choice == 1:
        print("we are in [n] block")

        #promt user for which coloring
        print("what type of coloring?")
        print("(1): for standard coloring")
        print("(2): for block coloring")

        choice = int(input("choice: "))

        #################
        # standad block #
        #################
        if choice == 1:
            print("we are in standard coloring block")

            #promt user for n
            n = int(input("n = "))

        ###############
        # block block #
        ###############
        elif choice == 2:
            print("we are in block coloring block")

            #promt user for block_n
            block_n = int(input("n = "))

        else:
            continue

    #############
    # Z_n block #
    #############
    elif choice == 2:
        print("we are in Z_n block")

        #promt user for which coloring
        print("what type of coloring?")
        print("(1): for standard coloring")
        print("(2): for block coloring")

        choice = int(input("choice: "))

        #################
        # standad block #
        #################
        if choice == 1:
            print("we are in standard coloring block")

            #promt user for n
            n = int(input("n = "))

            #prompt user for custom coloring
            print("input for custom coloring: ex: '123' will be repeated 123123123...")
            custom_coloring = input("custom coloring: ")

            #need functin to buid custom colored list in z_n given n and above coloring

        ###############
        # block block #
        ###############
        elif choice == 2:
            print("we are in block coloring block")

            #promt user for block_n
            block_n = int(input("n = "))

        else:
            continue

    ##############
    # exit block #
    ##############
    elif choice == 3:
        print("Bye!!")
        break
    else:
        print("BYE!!")
        break
    pass




