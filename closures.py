# Closure is a function having access to the scope of its parent after the parent function has returned.

def parent_function(name, coins):

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1 :
            print("\n" + name + " has " + str(coins) + " coins left.")
        elif coins == 1:   
            print("\n" + name + " has " + str(coins) + " coin left.")
        else:
            print("\n" + name + " is out of coins.")    
    
    return play_game

sam = parent_function("sam",5)
jay = parent_function("jay",4)

sam()
sam()

jay()

sam()
