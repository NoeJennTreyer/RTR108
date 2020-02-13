import os
from colorama import Fore

gold = 500
tavernlevel = 1
manorlevel = 1
graveyardlevel = 1


def town():
    print("*************Ashenfell*************")
    print("* 1- Tavern              Level",tavernlevel," *")
    print("* 2- Manor               Level",manorlevel," *")
    print("*                                 *")
    print("* 3- Graveyard                    *")
    print("* 4- Adventurers                  *")
    print("* 5- Prepare an expedition        *")
    print("***********************************")
    while (True):
        a = input("")
        if (a == "1"):
            tavern()
        if (a == "2"):
            manor()
        if (a == "3"):
            graveyard()
        if (a == "4"):
            adventurers()
        if (a == "5"):
            expedition()


def menu():
    print(Fore.BLACK+"****************Menu***************")
    print("*                                 *")
    print("* 1-          "+Fore.RED+"NEW GAME"+Fore.BLACK+"            *")
    print("* 2-         "+Fore.RED+"LOAD  GAME"+Fore.BLACK+"           *")
    print("*                                 *")
    print("* 3-            QUIT              *")
    print("***********************************")
    while(True):
        a = input()
        if (a == "1"):
            town()
            
            
def intro():
    print("")
    input()
    print("To play this game: press 'Enter' to continue reading.")
    input()
    print("Welcome to the city of Ashenfell. An old city, in ruins.")
    input()
    print("You are the new lord of this city. A new hope against the darkness of this world...")
    input()
    print("You must rebuild it. Defeat the lord of Vinshaka, the source of all evil, and reclaim you land anew!")
    input()
    print("But for now, you must build to rise from the ashes.")
    input()
    town()
    
    

    
    
    
    
    
    
menu()
