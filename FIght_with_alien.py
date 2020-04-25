from random import randint # allows you to generate a random number

# variables for the alien
alive = True
stamina = 10

# this function runs each time you attack the alien
def report(stamin):
# syntactic error in if else statements
    if (stamin > 8):
        print ("The alien is strong! It resists your pathetic attack!")
    elif (stamin > 5):
        print ("With a loud grunt, the alien stands firm.")
    elif (stamin > 3):
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif (stamin > 0):
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")
        return True
        

# main function - accepts your input for fight with the alien
def fight(stam): # stamina
    while stam > 0:
      # won't enter this loop ever. The function will always return False.
        response = input(" Enter a move 1.Hit 2.attack 3.fight 4.run ==>")
        # chose a response from ( hit, attack, fight and run)
        # fight scene
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            stam -= less # subtract random int from stamina
            report(stam) # see function above
        elif ("fight" in response) :
            print ("Fight how? You have no weapons, silly space traveler!")
        elif ("run" in response) :
            print ("Sadly, there is nowhere to run")
            print ("The spaceship is not very big")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            print()
            return True
    return False

print ("A threatening alien wants to fight you!")
# quotes at the end.++

# call the function - what it returns will be the value of alive
alive = fight(stamina)

if alive: # means if alive == True
    print ("The alien lives on, and you, sadly, do not")
else:
    print ("The alien has been vanquished. Good work!")