import os 
from random import randint

clear = lambda: os.system('cls')
gold, gems, CPn = 0, 0, 1000

class Dungeon:
    bossname = ""
    bosshp = 0
    bossmana = 0
    bossattack = 0
    bossattacktype = "none"
    bosselement = "none"
    bossskill = None

    completed = False 
    mobs = randint(0,10)
    dungeongold = 0
    dungeongems = 0
    dungeoncrystals = 0
    dungeonrubies = 0
    dungeondiamonds = 0
    dungeonores = 0

    def __init__(self, gold, gems, crystals, rubies, diamonds, ores):
        self.dungeongold = gold
        self.dungeongems = gems
        self.dungeoncrystals = crystals
        self.dungeonrubies = rubies
        self.dungeondiamonds = diamonds 
        self.dungeonores = ores

    def AddBoss(self, bossname, bosshp, bossmana, bossattack, bossattacktype, bosselement):
        self.bossname = bossname 
        self.bosshp = bosshp
        self.bossmana = bossmana 
        self.bossattack = bossattack
        self.bossattacktype = bossattacktype
        self.bosselement = bosselement

    def AddBossSkill(self, sname, smana, sdamage, sdmgtype, smulti):
        self.bossskill = BossSkill(sname,smana,sdamage,sdmgtype,smulti)

    class BossSkill:
        def __init__(self, skillname, skillmana, skilldamage, skilldamagetype, skillmultiplier):
            self.name = skillname
            self.mana = skillmana
            self.damage = skilldamage
            self.damagetype = skilldamagetype
            self.multiplier = skillmultiplier

r1, r2, r3, r4, r5, r6, r7, r8 = [False for i in range(0,10)] ,[False for i in range(0,10)] ,[False for i in range(0,10)] ,[False for i in range(0,10)], [False for i in range(0,10)], [False for i in range(0,10)], [False for i in range(0,10)], [False for i in range(0,10)] 
dungeons = [r1,r2,r3,r4,r5,r6,r7,r8]

def clearedstats(regionlist):
    cleared = 0
    notyet = 0
    for i in range(0,len(regionlist)):
        if regionlist[i] == False:
            notyet += 1
        else:
            cleared += 1
    return {"t":cleared, "f":notyet}


while True:
    clear()
    print("---------------------------------------------")
    print("Main Menu")
    print("---------------------------------------------")
    print(f"Gold: {gold}")
    print(f"Gems: {gems}")
    print(f"Combat Power: {CPn}")
    print("---------------------------------------------")
    print("Actions:")
    print("[1] Dungeon")
    print("[2] Specials")
    print("[3] Market")
    print("[4] Quit")
    print("---------------------------------------------")
    choice = int(input("Enter Numeric Choice: "))

    if choice == 1:
        while True:
            clear()
            print("---------------------------------------------")
            print("Regions")
            print("---------------------------------------------")
            for x in range(0,len(dungeons)):
                a = clearedstats(dungeons[x])
                print(f"[{x+1}] Region {x+1} | Progress [ Cleared : {a['t']} | Unfinished: {a['f']} ]")
            print("---------------------------------------------")
            regionchoice = input("Enter a region of choice, or go [back] to main menu: ")

            if regionchoice.lower() != "back":
                while True:
                    clear()
                    regionchoice = int(regionchoice)
                    if regionchoice > 8 or regionchoice < 1:
                        print("Invalid Region Choice")
                        input("Press Enter to Continue")
                        break 
                    else: 
                        print("---------------------------------------------")
                        print(f"Region {regionchoice} statistics")
                        print("---------------------------------------------")
                        for i in range(0,len(dungeons[regionchoice-1])):
                            print(f"[{i+1}] Dungeon | Status : {dungeons[regionchoice-1][i]}")
                        print("---------------------------------------------")
                        dungeonchoice = input("Enter a dungeon of choice, or go [back] to region selection: ")
                        if dungeonchoice.lower() != "back":
                            print("---------------------------------------------")
                            print(f"Dungeon {dungeonchoice} | Dungeon Name")
                            print("---------------------------------------------")
                            input("Press Enter to Continue")
                        elif dungeonchoice.lower() == "back":
                            break        
            elif regionchoice.lower() == "back":
                break
    elif choice == 2:
        clear()
        print("---------------------------------------------")
        print("Special Tab")
        print("---------------------------------------------")
        print("[1] Boss Challenge")
        print("[2] Hunters Den")
        print("[3] Raid")
        print("---------------------------------------------")
        input("Press enter to continue")
    elif choice == 3:
        clear()
        print("---------------------------------------------")
        print("Market")
        print("---------------------------------------------")
        print("[1] Swords\n[2] Bows\n[3] Daggers\n[4] Hammers")
        print("---------------------------------------------")
        input("Press enter to continue")
    elif choice == 4:
        clear()
        break

    else: 
        print("Invalid Choice")
