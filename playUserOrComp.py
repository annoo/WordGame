#create helpfuntion: computer or user?
###function CRASHED. I have no idea why. ??
def playUserOrComp():
    """
    Determines who gets to play: computer or user
    returns: True for user
    returns: False for computer
    """    
    answer = raw_input("Press 'u' if you want to play. Press 'c' for the computer.")
    answer = answer.lower()
    
    while True:
        if answer == 'u':
            return True
        elif answer == 'c':
            return False
        else:
            print("Input unclear")  
print playUserOrComp()