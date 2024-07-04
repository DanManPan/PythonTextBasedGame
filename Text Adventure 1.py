import random
from threading import Timer
import time
from time import sleep
# timeout = 3
# t = Timer(timeout, print, ["You were hit!"])
# t.start()
# start_time = time.time()
# prompt = f"You have {timeout} seconds to dodge, press enter...\n"
# answer = input(prompt)
# t.cancel()
# end_time = time.time()
# reaction_time = end_time - start_time
# if reaction_time > timeout:
#     print("You didn't dodge!")
#     dodge = False
# else:
#     if "joey" in answer:
#         print("You dodged")
#         dodge = True
#     else:
#         print("You didn't dodge!")
#         dodge = False
# print(dodge)

items = ["Fists"]
progression = []
# .append(item name) adds
# .remove(item name) deletes
you = 10
choou = ["10"]
# Notes - cool death stuff
#image1 = climage.convert('insidethehousefirstroom.jpeg')

def startingarea():
    if "Spider" in progression:
        print("You run back into the cave")
    writing1 = input("\nDo you want to walk into the " + "\u0332".join("CAVE ") + "or out in the " + "\u0332".join("RAIN\n"))
    if 'cave' in writing1.lower():
        startingcave()
    if 'rain' in writing1.lower():
        startingrain()
    if 'item' in writing1.lower():
        print(items)
        startingarea()
    if 'skip' in writing1.lower():
       YouWin()
    else:
        startingarea()

def startingcave():
    print("You walk in the cave to find a...  house?\n")
    writing2 = input("Do you want to inspect your " + "\u0332".join("SURROUNDINGS ") + ", open the door to the " + "\u0332".join("HOUSE ")   + ", or walk " + "\u0332".join("BACK ") + "out the cave?\n")
    if 'surrounding' in writing2.lower():
        aroundfrontdoor()
    if 'house' in writing2.lower():
        frontdoor()
    if 'back' in writing2.lower():
        startingarea()
    if 'item' in writing2.lower():
        print(items)
        startingcave()
    else:
        startingcave()

def frontdoor(): # add entering house with key
    if "Housedooropen" in progression:
        insidehousefront()
    if "Ring Piece?" in items:
        print("You attempt to open the door\n...\nit is still locked\nif only you had the k...\n")
        print("You just notice that the weirdly smooth ring you have been holding\ncan perfectly in the snub\nthe newly created handle easily turns and the door opens")
        items.remove("Ring Piece?")
        progression.append("Housedooropen")
        insidehousefront()
        
    else:
        print("You attempt to open the door\n...\nyou notice that the doorknob is not a knob at all, but a weirdly smooth stub")
        print("You try to turn the knob but it won't budge\nmaybe you could find something to open it...\n")
        writing3 = input("Do you want to inspect your " + "\u0332".join("SURROUNDINGS ") + ", or walk " + "\u0332".join("BACK ") + "out the cave?\n")
        if 'surrounding' in writing3.lower():
            aroundfrontdoor()
        if 'back' in writing3.lower():
            startingarea()
        if 'item' in writing3.lower():
            print(items)
            frontdoor()
        else:
            frontdoor()

def aroundfrontdoor():
    if "Umbrella" in items:
        print("There is nothing here\n")
        startingcave()
    if "Broken Umbrella" in items:
        print("There is nothing here\n")
        startingcave()
    else:
        print("You look around the area and see a umbrella leaning next to the wall\n")
        writing4 = input("Do you want to take the " + "\u0332".join("UMBRELLA ") + ", or walk " + "\u0332".join("BACK ") + "\n")
        if 'umbrella' in writing4.lower():
            items.append("Umbrella")
            print("You have collected an umbrella!")
            print(items)
            startingcave()
        if 'back' in writing4.lower():
            frontdoor()
        if 'item' in writing4.lower():
            print(items)
            aroundfrontdoor()
        else:
            aroundfrontdoor()

def insidehousefrontforwarddoor():
    print("You unlock the door and enter the pitch black room")
    print("\n...\nit looks ...scary\n")
    print("Suddenly!")
    print("A mysterious man says 'You Shall not Pass'")
    finalboss()

def insidehousefrontforward(): # boss battle
    if "Bossclearance" in progression:
        insidehousefrontforwarddoor()
    if "Right Door Key" and "Left Door Key" not in items:
        print("The Door is huge with one huge slot for a big key\n")
        print("You do not have a key\n")
        insidehousefront()
    if "Right Door Key" in items and "Left Door Key" not in items:
        print("The Door is huge with one huge slot for a big key\n")
        print("You look at the key you got from the right door\n")
        print("It is missing the left half\n")
        insidehousefront()
    if "Right Door Key" not in items and "Left Door Key" in items:
        print("The Door is huge with one huge slot for a big key\n")
        print("You look at the key you got from the left door\n")
        print("It is missing the right half\n")
        insidehousefront()
    if "Right Door Key" and "Left Door Key" in items:
        print("The Door is huge with one huge slot for a big key\n")
        print("You look at both the key pieces you collected\n")
        print("You angle them both right and press on it so it stays\n")
        print("You feel power with the boss key\n")
        items.remove("Left Door Key")
        items.remove("Right Door Key")
        items.append("Boss Key")
        progression.append("Bossclearance")
        print(items)
        insidehousefront()
    else:
        insidehousefront()

def insidehousefrontright(): # number guessing game
    if "Right Door Key" in items:
        print("You already collected this key")
        insidehousefront()
    if "GuessingGame" not in progression:
        print("You approach the right room\n...\n")
        print("Suddenly, the peephole of the door slides open and reveals a masked face\n")
    print("The Masked Man speaks to you")
    print("\033[1;33mChoose a number from 1 through 10... \033[0;37m\n")
    numbergame = ["1","2","3","4","5","6","7","8","9","10"]
    numbergamecomputer = random.choice(numbergame)
    # print(numbergamecomputer)
    writingguessgame = input("")
    if writingguessgame not in numbergame:
        print("Type a number...")
        insidehousefrontright()
    if writingguessgame == numbergamecomputer:
        print("Good Job, here is a key you might want")
        items.append("Right Door Key")
        print(items)
        insidehousefront()
    else:
        print("Try again")
        progression.append("GuessingGame")
        insidehousefrontright()
    writing3 = input("Do you want to inspect your " + "\u0332".join("SURROUNDINGS ") + ", or walk " + "\u0332".join("(any direction) ") + "?\n")
    print("left, forward, back, and right are the directions")
    #print("Your eyes seemed to be accustomed to your surroundings! You can now type VISUAL to get a good look around where you are ")
    match writing3.lower():
        case 'surroundings':
            aroundinsidehousefront()
        case 'back':
            frontdoor()
        case 'left':
            aroundinsidehousefront()
        case 'forward':
            aroundinsidehousefront()
        case 'right':
            aroundinsidehousefront()
        case 'items':
            print(items)
            insidehousefront()
        #case 'visual':
        #    something
        case _:
            insidehousefront()

def dodge1():
    print()

def insidehousefrontleft(): # timing minigame
    print("You enter the left room\n...\nit is extremely bright with few shadows to speak of\n")
    timeout = 5
    timer3 = Timer(timeout, dodge1)
    print("Suddenly, you notice a lightbulb falling from the celing!")
    print("\t\ttype DODGE quickly! (Be precise)")
    timer3.start()
    start_time = time.time()
    prompt = f"You have 5 seconds to dodge, press enter...\n"
    answer = input(prompt)
    timer3.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time > timeout:
        print("You didn't dodge!")
        print("You tumble out the room")
        insidehousefront()
    else:
        if "DODGE" in answer:
            print("You jump out of the way of the lightbulb")
            print("Inside of it is a key")
            items.append("Left Door Key")
            print(items)
            insidehousefront()  
        else:
            print("You didn't dodge!")
            print("You tumble out the room")
            insidehousefront()
            
def insidehousefront(): # add house stuff
    if "HouseEnter" not in progression:
        print("You enter the house\n...\nit looks ...normal\n")
    print("There is a staircase on your left, a door in front of you, and a door to your right")
    print("left, forward, back, and right are the directions")
    progression.append("HouseEnter")
    #print("Your eyes seemed to be accustomed to your surroundings! You can now type VISUAL to get a good look around where you are ")
    writing3 = input("Do you want to inspect your " + "\u0332".join("SURROUNDINGS ") + ", or walk " + "\u0332".join("(any direction)") + "?\n")
    match writing3.lower():
        case 'surroundings':
            aroundinsidehousefront()
        case 'back':
            frontdoor()
        case 'left':
            insidehousefrontleft()
        case 'forward':
            insidehousefrontforward()
        case 'right':
            insidehousefrontright()
        case 'items':
            print(items)
            insidehousefront()
        #case 'visual':
        #    something
        case _:
            insidehousefront()

def aroundinsidehousefront():
    print("You look around\n...\nit looks ...about the same\n")
    insidehousefront()

# above is all in the cave

def startingrain():
    if "Broken Umbrella" in items:
        print("You do not want to get soaked\n")
        print("Maybe you can find a way to fix your umbrella")
        startingarea()
    if "Spider" in progression:
        startingarea()
    if "Umbrella" in items:
        print("You open your umbrella and walk into the misty rain\n")
        print("...\n")
        print("Oh no, there seems to be a spider in front of you!\n")
        writing5 = input("Do you want to " + "\u0332".join("FIGHT ") + "the spider or " + "\u0332".join("RUN ") + "away\n" )
        if 'run' in writing5.lower():
            print("You try to run but you trip and the spider attacks you!\n")
            you - 1
            progression.append("SpiderRun")
            spiderfight()
        if 'item' in writing5.lower():
            print(items)
            aroundfrontdoor()
        if 'fight' in writing5.lower():
            print("You ready your fists\n")
            spiderfight()
        else:
            startingrain()
  
    else:
        print("You do not want to get soaked\n")
        startingarea()
    
def YouWin():
    print("You Win, Congrats!")
    exit()
    
# above is all the rain
def finalboss(you=you):
    boss = 12
    while boss > 0 and you > 0:
        print("\t\tYOU: {}  MAN: {}\t\t".format(you,boss))
        writing6 = input("Do you want to " + "\u0332".join("PUNCH ") + "the MAN or " + "\u0332".join("DEFEND ") + "\n" )
        # if 'die' in writing6.lower():
        #     spider = spider - 10 # make sure to remove this later
        if 'punch' in writing6.lower():
            boss = boss - 1
        if 'defend' in writing6.lower():
            print("you hold up your arm in defense")
            print("+3 armor")
            you = you + 3
        attackchoose = ["1","2","3"]
        choice = random.choice(attackchoose)
        if choice == "1":
            print("The MAN prepares to slash at you!")
            slashing = ["0","1","2","3","4","5","6","7","8","9","10"]
            numbergamecomputer = random.choice(slashing)
            if numbergamecomputer == "0":
                print("The MAN slaps himself!")
                boss = boss - 1
            elif numbergamecomputer == "1" or numbergamecomputer =="2" or numbergamecomputer=="3":
                print("The MAN slashes at you!")
                print("You dodge out of the way")
            elif numbergamecomputer == "4" or numbergamecomputer =="5" or numbergamecomputer =="6" or numbergamecomputer =="7":
                print("The MAN slashes at you!")
                print("You get hit by the slash")
                you = you - 1
            elif numbergamecomputer == numbergamecomputer =="8" or numbergamecomputer =="9":
                print("The MAN slashes at you!")
                print("The slash hits you in your chest")
                you = you -2    
            elif numbergamecomputer == "10":
                print("The MAN slashes at you!")
                print("The slash hits you straight in the face!")
                you = you -3
        if choice == "2":
            print("The MAN prepares to kick you!")
            kicking = ["0","1","2","3","4","5","6","7","8","9","10"]
            numbergamecomputer = random.choice(kicking)
            if numbergamecomputer == "0":
                print("The MAN trips!")
                boss = boss - 1
            elif numbergamecomputer == "1" or numbergamecomputer == "2" or numbergamecomputer == "3":
                print("The MAN tries to kick you!")
                print("You dodge out of the way")
            elif numbergamecomputer == "4" or numbergamecomputer == "5" or numbergamecomputer == "6" or numbergamecomputer == "7":
                print("The MAN tries to kick you!")
                print("You get kicked in the arm")
                you = you - 1
            elif numbergamecomputer == "8" or numbergamecomputer == "9":
                print("The MAN tries to kick you!")
                print("You get kicked in the ribs")
                you = you -2   
            elif numbergamecomputer == "10":
                print("The MAN tries to kick you!")
                print("Your Balls!!!")
                you = you -3
        if choice == "3":
            print("The MAN prepares to jump on you!")
            jumping = ["0","1","2","3","4","5","6","7","8","9","10"]
            numbergamecomputer = random.choice(jumping)
            if numbergamecomputer == "0":
                print("The MAN sprains his ankle from missing the jump!")
                boss = boss - 1
            elif numbergamecomputer == "1" or numbergamecomputer == "2" or numbergamecomputer == "3":
                print("The MAN jumps at you!")
                print("You dodge out of the way")
            elif numbergamecomputer == "4" or numbergamecomputer == "5" or numbergamecomputer == "6" or numbergamecomputer == "7":
                print("The MAN jumps at you!")
                print("You get hit on your foot!")
                you = you - 1
            elif numbergamecomputer == "8" or numbergamecomputer == "9":
                print("The MAN jumps at you!")
                print("You get hit on your shoulder!")
                you = you -2    
            elif numbergamecomputer == "10":
                print("The MAN jumps at you!")
                print("You get hit on your head!")
                you = you -3
    if boss <=0:
        print("\t\tBOSS DEFEATED")
        progression.append("Boss")
        print("\nThe MAN falls on the floor with a thud")
        YouWin()
        # choou.clear()
        # choou.append(you)
        # rainroad1()
    if you <= 0:
        dead()

def spiderfight(you=you):
    spider = 4
    if "SpiderRun" in progression:
        you = you - 1
    while spider > 0 and you > 0:
        print("\t\tYOU: {}  SPIDER: {}\t\t".format(you,spider))
        writing6 = input("Do you want to " + "\u0332".join("PUNCH ") + "the spider or " + "\u0332".join("CRY ") + "\n" )
        # if 'die' in writing6.lower():
        #     spider = spider - 10 # make sure to remove this later
        if 'punch' in writing6.lower():
            spider = spider - 2
        if 'cry' in writing6.lower():
            print("\nThe spider feels indifferent to your feelings")
            print("\nThe spider bites you for one damage \n \tOuch!\n")
            you = you - 1
    if spider <=0:
        print("\t\tSPIDER DEFEATED")
        progression.append("Spider")
        print("\nThe spider falls on the floor with a thud")
        choou.clear()
        choou.append(you)
        rainroad1()
    if you <= 0:
        dead()        
# bosses above
def rainroad1(you=you):
    if "Ringkeypart" not in progression:
        print("\nYou walk down the road")
        print("...")
        print("...")
        print("\n\nS w o o s h ! ! !")
        print("\nThe road suddenly stops with a pale grey wall blocking the natural foilage and mud")
        print("\nJust before you turn back you see 3/4ths of a round ring sticking out of the smooth wall about as big as your hand, \nproviding the only amount of texture you can see\n")
    writing7 = input("Do you want to inspect your " + "\u0332".join("SURROUNDINGS ") + ", or walk " + "\u0332".join("BACK ") + "down the road?\n")
    if 'surrounding' in writing7.lower():
        aroundrainroad1()
    if 'back' in writing7.lower():
        if "Ringkeypart" in progression: 
            print("\n\tYour umbrella breaks from the intense conditions!")
            items.remove("Umbrella")
            items.append("Broken Umbrella")
            startingarea()
        else:
            print("You try to walk away\n...\n...\n\tYou slip down the wet road!\nYou stand up next to the weird structure")
            aroundrainroad1()            
    if 'item' in writing7.lower():
        print(items)
        rainroad1()
    # if 'health' in writing7.lower():
    #     you = choou[0]
    #     print(you)
    #     rainroad1()    
    else:
        rainroad1()

def aroundrainroad1():
    if "Ring Piece?" in items:
        print("The wall is as smooth as ever\n")
        rainroad1()
    if "Ring Key" in items:
        print("The wall is the smoothest it has ever been\n")
        rainroad1()
    else:
        print("\nYou inspect the ring on the wall when you notice that it is loose\n")
        writing8 = input("Do you want to loosen the " + "\u0332".join("RING ") + "or " + "\u0332".join("IGNORE ") + "it?\n")
        if 'ring' in writing8.lower():
            items.append("Ring Piece?")
            progression.append("Ringkeypart")
            print("The ring slides out like a keycard with some warmth coming off of it")
            print(items)
            rainroad1()
        if 'ignore' in writing8.lower():
            print("The ring incentivises you...")
            aroundrainroad1()
        if 'item' in writing8.lower():
            print(items)
            aroundrainroad1()
        else:
            aroundrainroad1()

def main():
    print("What is your name?\n")
    name = input("My name is ")
    print("\nwelcome " + name)
    print("\nyou can check your inventory at any time by typing " + "\u0332".join("ITEMS "))
    print("\nYou wake up inside of a cave\nIt is pouring rain outside")
    startingarea()
def dead():
    items.clear()
    progression.clear()
    items.append("fists")
    print("\n\tYou have DIED\t\t\t\n\n-------------------------")
    main()

if __name__ == '__main__':
    main()

# notes - add a tester name to unlock all items and events
# make a turtle map if you want