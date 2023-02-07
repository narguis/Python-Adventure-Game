from time import sleep


def io():
    print("Invalid Option!")


def s():
    sleep(0.5)


intel = 0
magic = 0
gold = 0


print("You blacked out and woke up in a dungeon.")
s()
print("You can't remember a single thing...")
s()
q1 = input("Do you want to try remembering harder? [Y/N] ").upper()[0]
while q1 not in 'yYnN':
    io()
    q1 = input("Do you want to try remembering harder? [Y/N] ").upper()[0]
if q1 in 'yY':
    print("I don't think this is working...")
    q2 = input("Maybe a little harder? [Y/N] ").upper()[0]
    while q2 not in 'yYnN':
        io()
        q2 = input("Maybe a little harder? [Y/N] ").upper()[0]
    if q2 in 'yY':
        print("YOUR INTELLIGENCE HAS INCREASED +1!")
        intel += 1
        s()
        print("You seem to be remembering a few things!")
        s()
        print("You remembered having a gold coin in your left pocket, it must be somewhere near.")
        s()
        print("You found your gold coin under a small rock.")
        s()
        print("YOU HAVE GAINED +1 GOLD!")
        gold += 1
    else:
        print("You dismiss the idea of thinking harder, but you feel like you should have.")
else:
    print("You dismiss the idea of thinking harder, but you feel like you should have.")

print('-' * 50)
s()

print("The first thing you notice are your boots. There's something written in your left boot.")
s()
print("You look closer... I think that's your name.")
s()
print("It's a bit dark, so you pinch your eyes to read it.")
name = input("What's written in your boot? ").capitalize()
q3 = input(f"So your name is {name}, is that right? [Y/N] ").upper()[0]
while q3 not in 'YN':
    io()
    q3 = input(f"So your name is {name}, is that right? [Y/N] ").upper()[0]
if q3 == 'Y':
    print("Hm... That's a cool name, i guess.")
else:
    while q3 != 'Y':
        print(f"Didn't think so... What mother would possibly call her son {name}?")
        s()
        name = input("So, what's ACTUALLY written there? ").capitalize()
        q3 = input(f"So your name is {name}, is that right? [Y/N] ").upper()[0]
    print("Hm... That's a cool name, i guess.")


print("You take a good look around your cell", end='')
s()
print('.', end='')
s()
print('.', end='')
s()
print('.')
s()

print("There's nothing but rubble")
s()
print("Oh? What's this? The door doesn't seem to be locked.")
q4 = input("Do you want to investigate it? [Y/N] ").upper()[0]
while q4 not in 'YN':
    io()
    q4 = input("Do you want to investigate it? [Y/N] ").upper()[0]
if q4 == 'Y':
    print("You get closer to the door and find out it's open.")
else:
    print("You refuse to try to leave your cell.")
    s()
    print("Instead, you turn around and go back to sleep, hoping it was all a bad dream.")
    quit()

right = 0
cel1 = cel2 = cel3 = cel5 = cel6 = gb = 0
hall = True
print("YOU LEFT YOUR CELL!")
while hall is True:
    print(f"There are {3 + right} cell(s) to your left and {2 - right} cell(s) to your right")
    q5 = input("Do you want to go *right* or *left*? ").lower()
    while q5 != 'right' and q5 != 'left':
        q5 = input("Do you want to go *right* or *left*? ").lower()
    if q5 == 'right' and right < 2:
        right += 1
    elif q5 == 'right' and right == 2:
        print('You can only go left from here...')
    elif q5 == 'left' and right > -3:
        right -= 1
    elif q5 == 'left' and right == -3:
        print('You can only go right from here...')

    if right == 1:
        if cel5 == 0:
            print('You see a black man in a robe')
            q8 = input('The sign above the door reads "CELL 5". Do you want to enter? [Y/N] ').upper()[0]
            while q8 not in 'YN':
                io()
                q8 = input('The sign above the door reads "CELL 5". Do you want to enter? [Y/N] ').upper()[0]
            if q8 == 'Y':
                nameb = '????'
                print('You entered CELL 5.')
                s()
                print("You see a black man, as dark as darkness itself.")
                s()
                print("His skin is shiny and he is wearing a fancy robe.")
                s()
                print("You can see he is blind and he seems to be meditating")
                s()
                print(nameb)
                s()
                print(f'"Welcome, {name}. I have been waiting for you."')
                s()
                print('[A] How do you know my name?')
                print('[B] Who are you?')
                q9 = input('What will you ask? ').upper()[0]
                while q9 not in 'AB':
                    io()
                    print('[A] How do you know my name?')
                    print('[B] Who are you?')
                    q9 = input('What will you ask? ').upper()[0]
                if q9 == 'A':
                    print(nameb)
                    print(''"I know lots of things, curious one."'')
                    s()

                else:
                    nameb = 'Baron'
                    print(nameb)
                    print(f'"Oh, right. The name is {nameb}."')
                    s()

                print(nameb)
                print("So, what do you wish to know?")
                print("[A] How do i get out of here?")
                print("[B] Why am i here?")
                q10 = input("What will you ask? ").upper()[0]
                if q10 == 'A':
                    print(nameb)
                    print("That is a question with lots of answers.")
                    s()
                    print("But first, i would like to hear an exciting tale.")
                    s()
                    if gb > 1:
                        print("[A] The tale of Gouma, The Barbarian")
                        print("[B] The tale of Princess Anya")
                        q11 = input(f"What tale will you tell? ").upper()[0]
                        while q11 not in 'AB':
                            io()
                            q11 = input(f"What tale will you tell? ").upper()[0]
                        if q11 == 'A':
                            print(f"You told {nameb} the tale of Gouma, The Barbarian.")
                            s()
                            print(nameb)
                            print('"Haha! What a delightful tale!"')
                            s()
                            print('"Ok, i will help you!"')
                            q12 = input('"But first i need to know, are you a *human* or an *elf*?"').lower()
                            while q12 != 'human' and q12 != 'elf':
                                io()
                                q12 = input('"But first i need to know, are you a *human* or an *elf*?"').lower()
                            if q12 == 'human':
                                nameb = 'Baron, The Last Human Mage'
                                print(nameb)
                                print()
                    elif gb > 0:
                        print("[A] The tale of... Gornak, The Bard???")
                        print("[B] The tale of Princess Anya")
                        q11 = input(f"What tale will you tell? ").upper()[0]
                        while q11 not in 'AB':
                            io()
                            q11 = input(f"What tale will you tell? ").upper()[0]
                        if q11 == 'A':
                            print(f"You told {nameb} a confusing tale about a Bard called Gornak, you think.")

                    else:
                        print("[A] The tale of Hondur, The Peasant")
                        print("[B] The tale of Princess Anya")
                        q11 = input(f"What tale will you tell? ").upper()[0]
                        while q11 not in 'AB':
                            io()
                            q11 = input(f"What tale will you tell? ").upper()[0]

    if right == 2:
        print("You can only go left from here...")
        print("You see nothing.")
        if cel6 == 0:
            q6 = input('The sign above the door reads "CELL 6". Do you want to enter? [Y/N]').upper()[0]
            while q6 not in 'YN':
                io()
                q6 = input('The sign above the door reads "CELL 6". Do you want to enter? [Y/N] ').upper()[0]
            if q6 == 'Y':
                cel6 = 1
                print("YOU ENTERED CELL 6.")
                s()
                print("You find an interesting book laying on the ground.")
                s()
                q7 = input("Read it? [Y/N] ").upper()[0]
                while q7 not in 'YN':
                    io()
                    q7 = input("Read it? [Y/N] ").upper()[0]
                if q7 == 'Y':
                    print("You read the tales of Gouma, The Barbarian. ")
                    gb = 2
                    intel += 1
                    s()
                    print("YOUR INTELLIGENCE HAS INCREASED BY +1!")
                else:
                    print("You choose to ignore the tales of Gouma, The Barbarian.")
                    gb += 1
            else:
                print("You choose to ignore CELL 6 for now.")
        else:
            print("You have already entered CELL 6.")

    if right == 0:
        print("That's your cell, you don't want to go back in")
    if right == -1:
        print("You see nothing.")
    if right == -2:
        print("You see something shiny.")
    if right == -3:
        print("You can only go right from here...")
        print("You see an old man.")


