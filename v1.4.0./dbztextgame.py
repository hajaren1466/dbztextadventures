#Dragon Ball Text Adventure Version 1.4.0
#By Jaren Edwards
#First digit is a seperation between game copies
#Version 2.0.0 is vastly separated from 1.0.0 in its edition
#Version 1.3.0 would be very close to 1.3.1 and close to 1.2.0
#Second digit stands for update version of an edition
#The third digit stands for a patch to a version incase of bugs or unwanted things.
#So follow this:
# Edition, Version, Patch Number
import random
import pickle

def do_save(self, arg):
    saveGame = open('savegame.txt', 'wb')
    saveValues = (pl, e1ft, e2ft, e3ft, e4ft)
    pickle.dump(saveValues, saveGame)
    saveGame.close()

def do_load(self, arg):
    loadGame = open('savegame.txt', 'rb')
    loadValues = pickle.load(loadGame)
    pl = loadValues[0]
    e1ft = loadValues[1]
    e2ft = loadValues[2]
    e3ft = loadValues[3]
    e4ft = loadValues[4]
    loadGame.close()
pl = (5)
hdb = (pl*0.075)
hst = (pl*0.1)
hag = (pl*0.15)
hitl = (0)
hhp = (pl*0.05)
#e stands for enemy, 1 stands for the enemy number.
#s is strength, d is durability, h is health, a is agility.

#Enemy 1 stats
e1ft = (0)
e1s = (10)
e1d = (25)
e1h = (15)
e1a = (10)
#Closing of Enemy 1 stats

#Enemy 2 stats
e2ft = (0)
e2d = (30)
e2s = (35)
e2h = (25)
e2a = (20)
#Closing of Enemy 2 stats

#Enemy 3 stats
e3ft = (0)
e3d = (200)
e3s = (185)
e3h = (225)
e3a = (150)
#Closing of Enemy 3 stats

#Enemy 4 stats
e4ft = (0)

rc = input("Enter a race human saiyan majin frieza namekian demon ")

while (rc == "human" and pl <= 500):
    e1ft = (0)
    print("Type A to train with martial artists. Press B to lift weights.")
    print("Type C-Z for set of enemies. Then do AA-ZZ for next set of enemies.")
    print("to save your game type the word save. to load your saved game type the word load")
    th1 = input("Select a choice. ")
    if (th1 == "A"):
        pl = (pl + random.randint(1,25))
        print(pl)
        hst = (pl*0.1)
        hhp = (pl*0.05)
        hag = (pl*0.15)
        hdb = (pl*0.075)
        print("Str: " + str(hst) + " ")
        print("HP: " + str(hhp) + " ")
        print("Agl: " + str(hag) + " ")
        print("Dura: " + str(hdb) + " ")
    elif (th1 == "B"):
        pl = (pl + random.randint(1, 15))
        print(pl)
        hst = (pl*0.1)
        hhp = (pl*0.05)
        hag = (pl*0.15)
        hdb = (pl*0.075)
        print("HP: " + str(hhp) + " ")
        print("Agl: " + str(hag) + " ")
        print("Dura: " + str(hdb) + " ")
        print("Str: " + str(hst) + " ")
    elif (th1 == "C"):
        elft = (0)
        eld = (10)
        els = (25)
        elh = (15)
        ela = (10)
        if (e1ft == 1):
            print("You have already beaten this opponent.")
        elif (hst >= e1d and hag >= e1a and hhp >= e1s and e1ft == 0):
            print("You are fighting Goku Raditz Saga")
            print("You win this fight.")
            e1ft = (1)
            pl = (pl + 200)
        elif (e1ft == 0 and hst < eld or elft == 0 and hag < ela or elft == 0 and hhp < els):
            print("You are fighting Goku Raditz Saga")
            print("You have died.")
            break
    elif(th1 == "D"):
        e2ft = (e2ft)
        e2d = (90)
        e2s = (120)
        e2h = (60)
        e2a = (180)
        if (e2ft == 1):
            print("You have already beaten this opponent.")
        elif (hst >= e2d and hag >= e2a and hhp >= e2s and e2ft == 0):
            print("You are fighting Raditz")
            print("You win this fight.")
            e2ft = (1)
            pl = (pl + 500)
        elif (e2ft == 0 and hst < e2d or e2ft == 0 and hag < e2a or e2ft == 0 and hhp < e2s):
            print("You are fighting Raditz.")
            print("You have died.")
            break
    elif(th1 == "E"):
        e3ft = (e3ft)
        e3d = (200)
        e3s = (185)
        e3h = (225)
        e3a = (150)
        if (e3ft == 1):
            print("You have already beaten this opponent.")   
        elif (hst >= e3d and hag >= e3a and hhp >= e3s and e3ft == 0):
            print("You are fighting Nappa.")     
            print("You win this fight.")
            e3ft = (1)
            pl = (pl + 1000)
        elif (e3ft == 0 and hst < e3d or e3ft == 0 and hag < e3a or e3ft == 0 and hhp < e3s):
            print("You are fighting Nappa.")
            print("You have died.")
            break
    elif(th1 == "F"):
        e4ft = (e4ft)
        e4d = (1350)
        e4s = (1800)
        e4h = (900)
        e4a = (2700)
        if (e4ft == 1):
            print("You have already beaten this opponent.")
        elif (hst >= e4d and hag >= e4a and hhp >= e4s and e4ft == 0):
            print("You are fighting Vegeta Saiyan Saga.")     
            print("You win this fight.")
            e3ft = (1)
            pl = (pl + 2500)
        elif (e4ft == 0 and hst < e4d or e4ft == 0 and hag < e4a or e4ft == 0 and hhp < e4s):
            print("You are fighting Vegeta Saiyan Saga.")
            print("You have died.")
            break
    elif(th1 == "save"):
        saveGame = open('savegame.txt', 'wb')
        saveValues = (pl, e1ft, e2ft, e3ft, e4ft)
        do_save(saveValues, saveGame)
    elif(th1 == "load"):
        loadGame = open('savegame.txt', 'rb')
        loadValues = pickle.load(loadGame)
        pl = loadValues[0]
        e1ft = loadValues[1]
        e2ft = loadValues[2]
        e3ft = loadValues[3]
        e4ft = loadValues[4]
        do_load(loadValues, loadGame)
        print(pl)

else:
    while (rc == "human" and pl <= 2000 and pl > 500):
        print("Type A to train with chi masters. Press B to lift giant boulders.")
        print("Type C-Z for set of enemies. Then do AA-ZZ for next set of enemies.")
        print("to save your game type the word save. to load your saved game type the word load")
        th2 = input("Select a choice. ")
        if (th2 == "A"):
            pl = (pl + random.randint(5, 40))
            print(pl)
            hst = (pl*0.1)
            hhp = (pl*0.05)
            hag = (pl*0.15)
            hdb = (pl*0.075)
            print("Str: " + str(hst) + " ")
            print("HP: " + str(hhp) + " ")
            print("Agl: " + str(hag) + " ")
            print("Dura: " + str(hdb) + " ")
        elif (th2 == "B"):
                    pl = (pl + random.randint(5, 30))
                    print(pl)
                    hst = (pl*0.1)
                    hhp = (pl*0.05)
                    hag = (pl*0.15)
                    hdb = (pl*0.075)
                    print("Str: " + str(hst) + " ")
                    print("HP: " + str(hhp) + " ")
                    print("Agl: " + str(hag) + " ")
                    print("Dura: " + str(hdb) + " ")
        elif (th2 == "C"):
            e1ft = (e1ft)
            eld = (10)
            els = (25)
            elh = (15)
            ela = (10)
            if (e1ft == 1):
                print("You have already beaten this opponent.")
            elif (hst >= eld and hag >= ela and hhp >= els and e1ft == 0):
                print("You are fighting Goku Raditz Saga")
                print("You win this fight.")
                e1ft = (1)
                pl = (pl + 200)
            elif (elft == 0 and hst < eld or elft == 0 and hag < ela or elft == 0 and hhp < els):
                print("You are fighting Goku Raditz Saga")
                print("You have died.")
                break
        elif(th2 == "D"):
            e2ft = (e2ft)
            e2d = (90)
            e2s = (120)
            e2h = (60)
            e2a = (180)
            if (e2ft == 1):
                print("You have already beaten this opponent.")
            elif (hst >= e2d and hag >= e2a and hhp >= e2s and e2ft == 0):
                print("You are fighting Raditz")
                print("You win this fight.")
                e2ft = (1)
                pl = (pl + 500)
            elif (e2ft == 0 and hst < e2d or e2ft == 0 and hag < e2a or e2ft == 0 and hhp < e2s):
                print("You are fighting Raditz")
                print("You have died.")
                break
        elif(th2 == "E"):
            e3ft = (e3ft)
            e3d = (200)
            e3s = (185)
            e3h = (225)
            e3a = (150)
            if (e3ft == 1):
                print("You have already beaten this opponent.")   
            elif (hst >= e3d and hag >= e3a and hhp >= e3s and e3ft == 0):
                print("You are fighting Nappa.")     
                print("You win this fight.")
                e3ft = (1)
                pl = (pl + 1000)
            elif (e3ft == 0 and hst < e3d or e3ft == 0 and hag < e3a or e3ft == 0 and hhp < e3s):
                print("You are fighting Nappa.")
                print("You have died.")
                break
            elif(th2 == "F"):
                e4ft = (e4ft)
                e4d = (1350)
                e4s = (1800)
                e4h = (900)
                e4a = (2700)
        if (e4ft == 1):
            print("You have already beaten this opponent.")
        elif (hst >= e4d and hag >= e4a and hhp >= e4s and e4ft == 0):
            print("You are fighting Vegeta Saiyan Saga.")     
            print("You win this fight.")
            e3ft = (1)
            pl = (pl + 2500)
        elif (e4ft == 0 and hst < e4d or e4ft == 0 and hag < e4a or e4ft == 0 and hhp < e4s):
            print("You are fighting Vegeta Saiyan Saga.")
            print("You have died.")
            break
        elif(th1 == "save"):
            saveGame = open('savegame.txt', 'wb')
            saveValues = (pl, e1ft, e2ft, e3ft, e4ft)
            do_save(saveValues, saveGame)
        elif(th1 == "load"):
            loadGame = open('savegame.txt', 'rb')
            loadValues = pickle.load(loadGame)
            pl = loadValues[0]
            e1ft = loadValues[1]
            e2ft = loadValues[2]
            e3ft = loadValues[3]
            e4ft = loadValues[4]
            do_load(loadValues, loadGame)
            print(pl)
        else:
                while (rc == "human" and pl <= 9000 and pl > 2000):
                    print("Type A to train with Shadow Clones. Press B to lift mountains.")
                    print("Type C-Z for set of enemies. Then do AA-ZZ for next set of enemies.")
                    print("to save your game type the word save. to load your saved game type the word load")
                    th3 = input("Select a choice. ")
                    if (th3 == "A"):
                        pl = (pl + random.randint(25, 75))
                        print(pl)
                        hst = (pl*0.1)
                        hhp = (pl*0.05)
                        hag = (pl*0.15)
                        hdb = (pl*0.075)
                        print("Str: " + str(hst) + " ")
                        print("HP: " + str(hhp) + " ")
                        print("Agl: " + str(hag) + " ")
                        print("Dura: " + str(hdb) + " ")
                    elif (th3 == "B"):
                        pl = (pl + random.randint(15, 50))
                        print(pl)
                        hst = (pl*0.1)
                        hhp = (pl*0.05)
                        hag = (pl*0.15)
                        hdb = (pl*0.075)
                        print("Str: " + str(hst) + " ")
                        print("HP: " + str(hhp) + " ")
                        print("Agl: " + str(hag) + " ")
                        print("Dura: " + str(hdb) + " ")
                    elif (th3 == "C"):
                        e1ft = (e1ft)
                        eld = (10)
                        els = (25)
                        elh = (15)
                        ela = (10)
                        if (e1ft == 1):
                            print("You have already beaten this opponent.")
                        elif (hst >= eld and hag >= ela and hhp >= els and e1ft == 0):
                            print("You are fighting Goku Raditz Saga")
                            print("You win this fight.")
                            e1ft = (1)
                            pl = (pl+200)
                        elif (elft == 0 and hst < eld or elft == 0 and hag < ela or elft == 0 and hhp < els):
                            print("You are fighting Goku Raditz Saga")
                            print("You have died.")
                            break
                    elif(th3 == "D"):
                        e2ft = (e2ft)
                        e2d = (90)
                        e2s = (120)
                        e2h = (60)
                        e2a = (180)
                        if (e2ft == 1):
                            print("You have already beaten this opponent.")
                        elif (hst >= e2d and hag >= e2a and hhp >= e2s and e2ft == 0):
                            print("You are fighting Raditz")
                            print("You win this fight.")
                            e2ft = (1)
                            pl = (pl+500)
                        elif (e2ft == 0 and hst < e2d or e2ft == 0 and hag < e2a or e2ft == 0 and hhp < e2s):
                            print("You are fighting Raditz")
                            print("You have died.")
                            break
                    elif(th3 == "E"):
                        e3ft = (e3ft)
                        e3d = (200)
                        e3s = (185)
                        e3h = (225)
                        e3a = (150)
                        if (e3ft == 1):
                            print("You have already beaten this opponent.")   
                        elif (hst >= e3d and hag >= e3a and hhp >= e3s and e3ft == 0):
                            print("You are fighting Nappa.")     
                            print("You win this fight.")
                            e3ft = (1)
                            pl = (pl + 1000)
                        elif (e3ft == 0 and hst < e3d or e3ft == 0 and hag < e3a or e3ft == 0 and hhp < e3s):
                            print("You are fighting Nappa.")
                            print("You have died.")
                            break
                    elif(th3 == "F"):
                        e4ft = (e4ft)
                        e4d = (1350)
                        e4s = (1800)
                        e4h = (900)
                        e4a = (2700)
                        if (e4ft == 1):
                            print("You have already beaten this opponent.")
                        elif (hst >= e4d and hag >= e4a and hhp >= e4s and e4ft == 0):
                            print("You are fighting Vegeta Saiyan Saga.")     
                            print("You win this fight.")
                            e3ft = (1)
                            pl = (pl + 2500)
                        elif (e4ft == 0 and hst < e4d or e4ft == 0 and hag < e4a or e4ft == 0 and hhp < e4s):
                            print("You are fighting Vegeta Saiyan Saga.")
                            print("You have died.")
                            break
                    elif(th1 == "save"):
                        saveGame = open('savegame.txt', 'wb')
                        saveValues = (pl, e1ft, e2ft, e3ft, e4ft)
                        do_save(saveValues, saveGame)
                    elif(th1 == "load"):
                        loadGame = open('savegame.txt', 'rb')
                        loadValues = pickle.load(loadGame)
                        pl = loadValues[0]
                        e1ft = loadValues[1]
                        e2ft = loadValues[2]
                        e3ft = loadValues[3]
                        e4ft = loadValues[4]
                        do_load(loadValues, loadGame)
                        print(pl)
                       

