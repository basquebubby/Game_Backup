import random
import sys
import time
playerhealth = 200
monster1health = 100
monster2health = 175
monster3health = 300
monster4health = 600
monster5health = 2000
monster1attack = random.randint(10,30)
monster2attack = random.randint(20,50)
monster3attack = random.randint(20,100)
monster45move = random.randint(1,5)
monster4heal = random.randint(10,75)
monster5heal = random.randint(20,150)
monster4attack = random.randint(20,125)
monster5attack = random.randint(50,300)
heal = 125
punchAttk = 10
swordAttk = 30
fireballAttk = 100
TITANattk = 250
helmet = 175
gauntlet = 50
chestplate =250
boots = 25
TITAN_ARMOUR = 3000
while playerhealth > 0:
    print '~~~~~~~f~~~~~~~~~~~~y~~~~~~~~~~~n~~~~~~~~~~~~y~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    playername = raw_input('Welcome young warrior, what is your name?: ')
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print "King: You've came at the right time " + playername + ", monsters"
    print "have been attacking our villages for years and we need your help."
    print "You can find the first monster in that cave down yonder, be careful."
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print "Always answer CAPITALIZED if there is a capital in question."
    answer1 = raw_input("You find the monster in the cave, do you wake it (Y) or (N): ")
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    time.sleep(1) 
    if answer1 == str('Y'):
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'You wake the Cave Monster and you start to fight him!'
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        while monster1health > 0:
            print playername + "'s Health: " + str(playerhealth)
            print "Cave Monster's Health: " + str(monster1health)
            print ""
            attack = raw_input("Which attack do you use, punch(P), or smite with sword(S)?: ")
            if attack == str('P'):
                print "You punch the Cave Monster with your mighty fists!"
                monster1health = monster1health - punchAttk
            if attack == str('S'):
                print "You smite the Cave Monster with your sword!"
                monster1health = monster1health - swordAttk
            if monster1health > 0:
                print "The Cave Monster fights back!"
                print ""
                playerhealth = playerhealth - monster1attack
            if playerhealth <= 0:
                print "You have died a painful death and will be missed. RIP: " + playername
                sys.exit()
    time.sleep(1)        
    if answer1 == str('N'):
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'The monser smells you and awakens from his sleep! Fight him to save your life!'
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        while monster1health > 0:
            print playername + "'s Health: " + str(playerhealth)
            print "Cave Monster's Health: " + str(monster1health)
            print ""
            attack = raw_input("Which attack do you use, punch(P), or smite with sword(S)?: ")
            if attack == str('P'):
                print "You punch the Cave Monster with your mighty fists!"
                monster1health = monster1health - punchAttk
            if attack == str('S'):
                print "You smite the Cave Monster with your sword!"
                monster1health = monster1health - swordAttk
            if monster1health > 0:
                print "The Cave Monster fights back!"
                print ""
                playerhealth = playerhealth - monster1attack
            if playerhealth <= 0:
                print "You have died a painful death and will be missed. RIP: " + playername
                sys.exit()
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print "Old Man: 'That was the most amount of Bravery I have ever seen! There are still"
    print "other monsters though that you need to defeat. Here's an item that should help "
    print "you on your way, and some honey to get your health back up. Good Luck!'        "
    print ""
    print "You just recived a steel helmet. Your health has been raised by 175!"
    playerhealth = 375
    print playername + "'s Health: " + str(playerhealth)
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print "As you go down the path you hear a screaming off in the distance..."
    answer2 = raw_input("Do you go investigate, Yes (Y) or No (N)?: ")
    time.sleep(1) 
    if answer2 == str('Y'):
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print "You find a cottage with the door broken down and find a Troll Theif! He is trying"
        print "to take something from the old women crying for help! You go attack the Troll... "
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        while monster2health > 0:
            print playername + "'s Health: " + str(playerhealth)
            print "Troll Theifs's Health: " + str(monster2health)
            print ""
            attack = raw_input("Which attack do you use, punch(P), or smite with sword (S)?: ")
            if attack == str('P'):
                print "You punch the Troll Theif with your mighty fists!"
                monster2health = monster2health - punchAttk
            if attack == str('S'):
                print "You smite the Troll Theif with your sword!"
                monster2health = monster2health - swordAttk
            if monster2health > 0:
                print "The Troll Theif fights back!"
                print ""
                playerhealth = playerhealth - monster2attack
            if playerhealth <= 0:
                print "You have died a painful death and will be missed. RIP: " + playername
                sys.exit()
    time.sleep(1)
    if answer2 == str('N'):
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print "You see a Troll Theif running through the forest carrying something valuable. "
        print "A frail old women is chasing him so you decide to help by fighting the Troll!"
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        while monster2health > 0:
            print playername + "'s Health: " + str(playerhealth)
            print "Troll Theifs's Health: " + str(monster2health)
            print ""
            attack = raw_input("Which attack do you use, punch(P), or smite with sword (S)?: ")
            if attack == str('P'):
                print "You punch the Troll Theif with your mighty fists!"
                monster2health = monster2health - punchAttk
            if attack == str('S'):
                print "You smite the Troll Theif with your sword!"
                monster2health = monster2health - swordAttk
            if monster2health > 0:
                print "The Troll Theif fights back!"
                print ""
                playerhealth = playerhealth - monster2attack
            if playerhealth <= 0:
                print "You have died a painful death and will be missed. RIP: " + playername
                sys.exit()
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print "Old Women: 'Thankyou, thankyou, thankyou. That Troll Theif took my magic book "
    print "away from me. Since you showed so much bravery, I bestow this book to you. You"
    print "will be able to heal your self in battle now. And here is some honey to get"
    print "your energy back, be safe!"
    print ""
    playerhealth = 375
    print playername  + "'s Health: " + str(playerhealth)
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    time.sleep(1)
    print "You travel to a near by town and visit the tavern. An wise monk runs into you."
    print ""
    print "Wise Monk: 'The secret to true power starts at the start, can not be used"
    print "until the end, and reads reverse. It watches over your path, but not your life.'"
    print ""
    print "He runs away and disapeers..."
    print "The bar keeper see's that you are tired,"
    rest = raw_input("Do you sleep(S) or drink coffee(C)?: ")
    if rest == str('S'):
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print "You wake up to your room on fire and people screaming in fear. A dragon has"
        print "taken over the town. Fight it and win to save the town!"
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        while monster3health > 0:
            print playername + "'s Health: " + str(playerhealth)
            print "Dragon's Health: " + str(monster3health)
            print ""
            attack = raw_input("Which attack do you use, punch(P), smite with sword (S), or heal(H)?: ")
            if attack == str('P'):
                print "You punch the Dragon with your mighty fists!"
                monster3health = monster3health - punchAttk
            if attack == str('S'):
                print "You smite the Dragon with your sword!"
                monster3health = monster3health - swordAttk
            if attack == str('H'):
                if playerhealth < 300:
                    print "75 Health points have been restored to you!"
                    playerhealth = playerhealth + 75
                if playerhealth > 300:
                    more = 375 - playerhealth
                    playerhealth = more + playerhealth
                    print "Your health has been restored!"
            if monster3health > 0:
                print "The Dragon fights back!"
                print ""
                playerhealth = playerhealth - monster3attack
            if playerhealth <= 0:
                print "You have died a painful death and will be missed. RIP: " + playername
                sys.exit()
    if rest == str('C'):
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print "You wonder through the town and see something ominous pass by a window..."
        print "You enter the room, it's pitch black with only a small bed. You slowly walk over"
        print "When something grabs your foor and pulls you under. The Boogie Monster has mistakend"
        print "you for a midnight snack, you start to fight him!"
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        while monster3health > 0:
            print playername + "'s Health: " + str(playerhealth)
            print "Boogie Man's Health: " + str(monster3health)
            print ""
            attack = raw_input("Which attack do you use, punch(P), smite with sword (S), or heal(H)?: ")
            if attack == str('P'):
                print "You punch the Boogie Man with your mighty fists!"
                monster3health = monster3health - punchAttk
            if attack == str('S'):
                print "You smite the Boogie Man with your sword!"
                monster3health = monster3health - swordAttk
            if attack == str('H'):
                if playerhealth < 300:
                    print "75 Health points have been restored to you!"
                    playerhealth = playerhealth + heal
                if playerhealth > 300:
                    more = 375 - playerhealth
                    playerhealth = more + playerhealth
                    print "Your health has been restored!"
            if monster3health > 0:
                print "The Boogie Man fights back!"
                print ""
                playerhealth = playerhealth - monster3attack
            if playerhealth <= 0:
                print "You have died a painful death and will be missed. RIP: " + playername
                sys.exit()
    if rest == str('S'):
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print "The Dragon's bowls were released dropping some boots and a gauntlet. You clean"
        print "them off and put them on!"
        print ""
        playerhealth = 375 + gauntlet + boots
        print playername + "'s Health: " + str(playerhealth)
    if rest == str('C'):
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print "The Kids trapped in the cages see your bravery and reward you with the boots"
        print "and gauntlets they had collected hoping they would escape!"
        print ""
        playerhealth = 375 + gauntlet + boots
        print playername + "'s Health: " + str(playerhealth)
    print "After what happend in that town you vowed to never go back, and to"
    print "continue on your jorney. There is a fork in the road along your journey"
    answer3 = raw_input(",do you take a right (Y) or a  left (L)?: ")
    time.sleep(1)
    print "It turns out which road you took didn't really matter. You do however "
    print "encounter a massive field of horses! There is something riling them all"
    print "up though... You go to investigate and find out it's a demon bull! He  "
    print "charges at you wanting to fight!"
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    while monster4health > 0:
        print playername + "'s Health: " + str(playerhealth)
        print "Demon Bull's Health: " + str(monster4health)
        print ""
        attack = raw_input("Which attack do you use, punch(P), smite with sword (S), or heal(H)?: ")
        if attack == str('P'):
            print "You punch the Demon Bull with your mighty fists!"
            monster4health = monster4health - punchAttk
        if attack == str('S'):
            print "You smite the Demon Bull with your sword!"
            monster4health = monster4health - swordAttk
        if attack == str('H'):
            if playerhealth < 450:
                print "75 Health points have been restored to you!"
                playerhealth = playerhealth + heal
            if playerhealth > 450:
                more = 450 - playerhealth
                playerhealth = more + playerhealth
                print "Your health has been restored!"
        if monster4health > 0:
            print "The Demon Bull fights back!"
            print ""
            if monster45move == 1 or 2 or 4 or 5:
                playerhealth = playerhealth - monster4attack
            if monster45move == 3:
                if monster4health < 525:
                    monster4health = monster4health + monster4heal
                elif monster4health > 525:
                    monster4health = 600
        if playerhealth <= 0:
            print "You have died a painful death and will be missed. RIP: " + playername
            sys.exit()
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print "As soon as you deafeated the Demon Bull, something fell from the sky..."
    print "When you go and pick it up you figure out it's a Fire Ball spell, and a chestplate!"
    playerhealth = 200 + helmet + gauntlet + boots + chestplate
    print playername + "'s Health: " + str(playerhealth)
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print "You travel to the final monsters dungeon lair, and find him waiting for you."
    print ""
    time.sleep(1)
    print "Devil: 'I've been watching you fight young warrior, you are very brave and powerful"
    print "but not powerfull enough to defeat me. Join me and we can conquor this world, or"
    print "fight me and die.'"
    answer4 = raw_input("Do you join the Devil (J) or fight him and save the Kingodm (F)?: ")
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    if answer4 == str('J'):
        print "Devil: 'Clever mortal, together we will destroy everything. MWAHAHAHAHA!'"
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        time.sleep(1)
        print "You have failed the Kindom, everyone is dead. Your family, friends, everyone... You are"
        print "now one of the monsters you once faught to destroy."
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print "                                   The End                                    "
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    if answer4 == str('F'):
        print "Devil: 'You fool! How dare you defy me, I will have your sould for this!'"
        if (answer1 == str('Y')) and (answer2 == str('N')) and (answer3 == str('Y')) and (answer4 == str('F')):
            print "SUDDENLY! A gian suit of Titan armour had fallen fro the ceiling!"
            print "You put it on and gain an emense amount of power!"
            playerhealth = TITAN_ARMOUR
            print playername + "'s Health: " + str(playerhealth)
            print playername + "'s Attack: " + str(TITANattk)
            print ""
            print "Devil: 'No amount of weaponds can deafeat me, prepare to die!'"
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            while monster5health > 0:
                print playername + "'s Health: " + str(playerhealth)
                print "Devil's Health: " + str(monster5health)
                print ""
                attack = raw_input("Which attack do you use, punch(P), smite with sword (S), heal(H), fireball(F), or TITAN ATTACK (TITAN)?: ")
                if attack == str('P'):
                    print "You punch the Devil with your mighty fists!"
                    monster5health = monster5health - punchAttk
                if attack == str('S'):
                    print "You smite the Devil with your sword!"
                    monster5health = monster5health - swordAttk
                if attack == str('H'):
                    if playerhealth < 3000:
                        print "500 Health points have been restored to you!"
                        playerhealth = playerhealth + 500
                    if playerhealth > 3000:
                        playerhealth = 3000
                        print "Your health has been restored!"
                if attack == str('F'):
                    print "You set the Devil ablaze!"
                    monster5health = monster5health - fireballAttk
                if attack == str('TITAN'):
                    print "You fired rocket launchers at his face while shooting him with a machine gun!"
                    monster5health = monster5health - TITANattk
                if monster5health > 0:
                    print "The Devill fights back!"
                    print ""
                    if monster45move == 1 or 2 or 4 or 5:
                        playerhealth = playerhealth - monster5attack
                    if monster45move == 3:
                        if monster4health < 525:
                            monster5health = monster5health + monster5heal
                        elif monster5health > 525:
                            monster5health = 600
                if playerhealth <= 0:
                    print "Devil: 'I told you nothing can defeat me, you are nothing you are weak.'"
                    time.sleep(1)
                    print "You have died a painful death and will be missed. RIP: " + playername
                    sys.exit()
        else:
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            while monster5health > 0:
                print playername + "'s Health: " + str(playerhealth)
                print "Devil's Health: " + str(monster5health)
                print ""
                attack = raw_input("Which attack do you use, punch(P), smite with sword (S), heal(H), fireball(F)?: ")
                if attack == str('P'):
                    print "You punch the Devil with your mighty fists!"
                    monster5health = monster5health - punchAttk
                if attack == str('S'):
                    print "You smite the Devil with your sword!"
                    monster5health = monster5health - swordAttk
                if attack == str('H'):
                    if playerhealth < 700:
                        print "75 Health points have been restored to you!"
                        playerhealth = playerhealth + heal
                    if playerhealth > 700:
                        playerhealth = 700
                        print "Your health has been restored!"
                if attack == str('F'):
                        print "You set the Devil ablaze!"
                        monster5health = monster5health - fireballAttk
                if monster5health > 0:
                    print "The Demon Bull fights back!"
                    print ""
                    if monster45move == 1 or 2 or 4 or 5:
                        playerhealth = playerhealth - monster5attack
                    if monster45move == 3:
                        if monster4health < 525:
                            monster5health = monster5health + monster5heal
                        elif monster5health > 525:
                            monster5health = 600
                if playerhealth <= 0:
                    print "Devil: 'I told you nothing can defeat me, you are nothing you are weak.'"
                    time.sleep(1)
                    print "You have died a painful death and will be missed. RIP: " + playername
                    sys.exit()
    playerhealth = 0
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print "King: 'Thank you young hero, you have saved our town and we owe our lives to you."
print "For your vast amount of bravery and servitude to your kindom I dub you as King!. "
print "Long live " + playername + ", the new king!"
print ""
print "You have taken away all evil from this world and have become ruler of it."
print "There is no need for your Titan suit anymore so you lock it up in storage."
print "Your brave deeds will never be forgotten..."
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print "                                   The End                                    "
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'