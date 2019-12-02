#Dragon Ball Text Adventure Version 1.3.3
#By Jaren Edwards
#First digit is a seperation between game copies
#Version 2.0.0 is vastly separated from 1.0.0 in its edition
#Version 1.3.0 would be very close to 1.3.1 and close to 1.2.0
#Second digit stands for update version of an edition
#The third digit stands for a patch to a version incase of bugs or unwanted things.
#So follow this:
# Edition, Version, Patch Number
import random
pl = (5)
hdb = (pl*0.01)
hst = (pl*0.1)
hag = (pl*0.3)
hitl = (0)
hhp = (pl*0.25)
#e stands for enemy, 1 stands for the enemy number.
#s is strength, d is durability, h is health, a is agility.

#Enemy 1 stats
e1ft = (0)
e1s = (50)
e1d = (30)
e1h = (100)
e1a = (10)
#Closing of Enemy 1 stats

#Enemy 2 stats
e2ft = (0)
e2d = (30)
e2s = (35)
e2h = (25)
e2a = (20)

rc = input("Enter a race human saiyan majin frieza namekian demon")

while (rc == "human" and pl <= 500):
    e1ft = (0)
    print("Type A to train with martial artists. Press B to lift weights.")
    print("Type C-Z for set of enemies. Then do AA-ZZ for next set of enemies.")
    th1 = input("Select a choice.")
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
        elif (e1ft == 0 and hst < eld or elft == 0 and hag < ela or elft == 0 and hhp < els):
            print("You are fighting Goku Raditz Saga")
            print("You have died.")
            break
    elif(th1 == "D"):
        e2ft = (e2ft)
        e2d = (30)
        e2s = (35)
        e2h = (25)
        e2a = (20)
        if (e2ft == 1):
            print("You have already beaten this opponent.")
        elif (hst >= e2d and hag >= e2a and hhp >= e2s and e2ft == 0):
            print("You are fighting Raditz")
            print("You win this fight.")
            e2ft = (1)
        elif (e2ft == 0 and hst < e2d or e2ft == 0 and hag < e2a or e2ft == 0 and hhp < e2s):
            print("You are fighting Raditz")
            print("You have died.")
            break
else:
    while (rc == "human" and pl <= 2000 and pl > 500):
        print("Type A to train with chi masters. Press B to lift giant boulders.")
        th2 = input("Select a choice.")
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
                elft = (1)
            elif (elft == 0 and hst < eld or elft == 0 and hag < ela or elft == 0 and hhp < els):
                print("You are fighting Goku Raditz Saga")
                print("You have died.")
                break
        elif(th2 == "D"):
            e2ft = (e2ft)
            e2d = (30)
            e2s = (35)
            e2h = (25)
            e2a = (20)
            if (e2ft == 1):
                print("You have already beaten this opponent.")
            elif (hst >= e2d and hag >= e2a and hhp >= e2s and e2ft == 0):
                print("You are fighting Raditz")
                print("You win this fight.")
                e2ft = (1)
            elif (e2ft == 0 and hst < e2d or e2ft == 0 and hag < e2a or e2ft == 0 and hhp < e2s):
                print("You are fighting Raditz")
                print("You have died.")
                break
