import random  # for random module

# Global variable Player Stats
global health
global strength
global magic
global luck
health = 5
strength = 5
magic = 5
luck = 5 # Invisible Stat

# Frequently Reused Functions

def stats():  # prints stats
    print(f"Your Stats \nHealth: {health} \nStrength: {strength} \nMagic: {magic}\n")
def default():  # If an invalid answer is given. Player is punished and moves on
    global magic
    global health
    global strength
    health -= 2
    magic -= 2
    strength -= 2
    print(
        "You were so overwhelmed that you accidentally discharged an explosion spell. \n It blew you a few feet in the air. You land painfully on your back. You are alive, but you lose 2 points for all Stats. \n ")
    stats()
    health_0()
    luck_roll_neg()
def click_enter():  # Let's player know to click enter to continue
    enter = input("Press [Enter] to Continue. \n")

# If Health is at 0, terminate program
def health_0():
    if health <= 0:
        print(f"Your Health is at {health}. You can not Continue. Game Over!")
        quit()
#Luck Rolls - Add into events
def luck_roll_50():
    global luck
    luck_stat = random.randint(-2, 2)
    luck += luck_stat
def luck_roll_neg():
    global luck
    luck_stat = random.randint(-2, 0)
    luck += luck_stat
def luck_roll_pos():
    global luck
    luck_stat = random.randint(1, 2)
    luck += luck_stat

#Default Settings Above
########################################################################################################################
# Horse/Griffin
def horse_griffin():
    global health
    global strength
    global magic
    click_enter()
    answer_1 = input(
        "You must find a way of getting to Miss GoldenDragon's house. "
        "\nDo you summon a griffin with magic or call on a horse carriage? Enter Griffin or Horse. \n ")

    if answer_1.lower().strip() != "griffin" and answer_1.lower().strip() != "horse":
        health -= 3
        print(
            f"You raise your wand and shout out '{answer_1}'! "
            f"\nUnfortunately that was not a valid spell and you summoned a grumpy griffin. It claws at you. You lose 3 Health.\n ")
        click_enter()
        stats()
        luck_roll_neg()
        health_0()
        print(
            "You call for a horse carriage instead and it takes you to the edge of the Dark Forest. "
            "\nNo matter how much money you offer the driver refuses to take you through the forest. "
            "\nSomething about insurance premiums being too high to cover trips through the Dark Forest.\n")
    elif answer_1.lower().strip() == "griffin":
        health -= 2
        print(
            "You raise your wand up to summon a griffin. "
            "\nYour magic is too low and you summoned a grumpy griffin. "
            "\nIt claws at you. You lose 2 Health.\n")
        click_enter()
        stats()
        luck_roll_neg()
        health_0()
        print(
            "You end up calling a the horse carriage instead. The horse carriage arrives and it takes you to the edge of the Dark Forest. "
            "\nNo matter how much money you offer the driver refuses to take you through the forest. "
            "\nSomething about insurance premiums being too high to cover trips through the Dark Forest.\n")
    elif answer_1.lower().strip() == "horse":
        print(
            "The horse carriage arrives and it takes you to the edge of the Dark Forest. No matter how much money you offer the driver refuses to take you through the forest. "
            "\nSomething about insurance premiums being too high to cover trips through the Dark Forest.\n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
########################################################################################################################
# Fairies Event
def magic_fairies():  # Checks with the current Magic stat and runs if statements
    global magic
    global health
    global strength
    if magic >= 9:
        magic += 2
        print(
            "You quickly casted a sleep spell on the fairies. They fall down around you like falling leaves. You tiptoe away from the pile of snoring fairies. \nYou gain 2 Magic from this. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif magic >= 5 and magic <= 8:
        health -= 1
        magic += 1
        print(
            "You can only recall the lightning spell. You zapped them with a shot from your wand. It worked! \nBut only for a few moments. \nThey quickly recover and flew towards you. You managed to run away with a scraped knee. \nYou lose 1 Health and gain 1 Magic. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
    else:
        health -= 3
        magic -= 1
        strength -= 1
        print(
            "You anxiously try to recall any spell to fight the fairies. You yell out a random spell. \n BOOM \nIt blew up in your face. Fortunately it also blasted the fairies away. \nYou lose 3 Health, 1 Magic and 1 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
def strength_fairies():  # Checks Stats
    global magic
    global health
    global strength
    if strength >= 9:
        strength += 2
        print(
            "You break off a branch from a tree and start swatting the fairies with all your might. \nThe fairies were stunned by your ferocity that they quickly clear the area. You got a good arm workout from swinging the branch. \nYou gain 2 Strength. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif strength >= 5 and strength <= 8:
        health -= 1
        strength += 1
        print(
            "You break off a branch from a tree and start swatting the fairies. \nThey screeched angrily at you. \nYou lost your nerve and started running away. You tripped on tree roots and branches scratched you, but you escaped. \nYou lost 1 Health and gained 1 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
    else:
        health -= 3
        strength -= 2
        print(
            "You tried to break off a tree branch to swat the fairies with. \nYou are too weak. The fairies are upon you. Pulling at your clothes and hair. Scratching at your eyes. \nYou run blindly through the forest, hitting tree trunks, tripping on roots and scratched by branches. You managed to get away from them. \nYou lost 3 Health and 2 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
def fairies():
    click_enter()
    print("You encounter a swarm of fairies. Fairies are mischievous and like to mess with humans. "
          "\nYou would like to avoid them if you can, but they blocked the your path through the forest. \n")
    while True:
        answer_2 = input("What do you do? Do you run away, use magic or fight? Enter Run, Magic or Fight. \n")
        if answer_2.lower().strip() == "run":
            print("You died trying to run away. \n")
            quit()
        elif answer_2.lower().strip() == "magic":
            magic_fairies()
            break
        elif answer_2.lower().strip() == "fight":
            strength_fairies()
            break
        else:
            continue
########################################################################################################################
# Hole Event
def hole_event():
    global health
    global strength
    global magic
    click_enter()
    hole_flip = random.randint(1,3)
    print("After an hour of walking, you fell into a hole! \n")
    click_enter()
    if hole_flip == 1:
        health += 5
        magic += 5
        print("You fell into a dwarve's dwelling. They are in the middle of renovating their home. "
              "\nThey are extremely apologetic and give you a Health and Magic potion for your trouble. Your Health and Magic went up by 5.\n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    else:
        health -= 3
        strength -= 3
        print("You fell into a Cannabal's trap! The crazed human hasn't eaten human flesh in weeks. "
              "\nYou barely escape with your life. You were injured during your escape. You lose 3 Health and 1 Strength. \n")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
########################################################################################################################
# Mermaids Event
def magic_mermaids():  # Checks with the current Magic stat and runs if statements
    global magic
    global health
    global strength
    if magic >= 9:
        magic += 2
        print(
            "You quickly casted a lightning spell on the mermaids. They are stunned and sink below the waters. "
            "\nYou gain 2 Magic from this. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif magic >= 5 and magic <= 8:
        health -= 1
        magic += 1
        print(
            "In the spur of the moment you can only recall the vine spell. You grew vines over the water's surface. "
            "The vines entangle the mermaids \nBut only for a few moments. "
            "\nThey claw and bite through the vines and swim towards you. "
            "You managed to flee, but you got hurt in the process. \nYou lose 1 Health and gain 1 Magic. \n")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
    else:
        health -= 3
        magic -= 1
        strength -= 1
        print(
            "You anxiously try to recall any spell to fight the mermaids. You yell out a random spell. \n BOOM \nIt blew up in your face. Fortunately it also scared the mermaids away. \nYou lose 3 Health, 1 Magic and 1 Strength. \n ")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
def strength_mermaids():  # Checks Stats
    global magic
    global health
    global strength
    if strength >= 9:
        strength += 2
        print(
            "You pick up a fist-sized rock and accurately slung it at one of the mermaid's head. It got hit and disappeared under the surface \n You aim more rocks at them. The mermaids were stunned by your aim. They quickly clear the area. You got a good arm workout. \nYou gain 2 Strength. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif strength >= 5 and strength <= 8:
        health -= 1
        strength += 1
        print(
            "You pick up a rock and started to throw it at the mermaids. You missed. \nThey smile maliciously as they swim towards you. \nYou lost your nerve and started running away. You tripped on a rock during your escape. \nYou lost 1 Health and gained 1 Strength. \n ")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
    else:
        health -= 3
        strength -= 2
        print(
            "You tried to pick up a big rock \nYou are too weak. The mermaids are quicker than you thought. They began pulling at your clothes to drag you into the water. \nYou fought with all your might against their claw-like hands. You managed to get away from them. \nYou lost 3 Health and 2 Strength. \n ")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
def mermaids():
    click_enter()
    print("You reached a lake. It has been a hot and humid day. You decide to wade into the lake to cool off and have a sip. "
          "\nsplash\n"
          "From the center of the lake, a school of mermaids emerge. "
          "They are swimming quickly towards you.\n")
    while True:
        answer_4 = input(
            "What do you do? Do you run away, use magic or fight? Enter Run, Magic or Fight. \n")
        if answer_4.lower().strip() == "run":
            print("You died trying to run away. \n")
            quit()
        elif answer_4.lower().strip() == "magic":
            magic_mermaids()
            break
        elif answer_4.lower().strip() == "fight":
            strength_mermaids()
            break
        else:
            continue
########################################################################################################################
#Granny Event
#Granny Event
def rps_game():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    images = [rock, paper, scissors]

    number_games = input("Granny asks 'How many times do you want to play "
                         "Rock, Paper, Scissors?'\n")

    for turns in range(1, int(number_games) + 1):
        player_turn = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
        if player_turn >= 3 or player_turn < 0:
            print(" You didn't follow the directions! Pick 0, 1 or 2 only! You lose! \n")
        else:
            print(images[player_turn])

            computer_turn = random.randint(0, 2)

            print("Granny chose:")
            print(images[computer_turn])

            if player_turn == computer_turn:
                print("Its a draw!")
                click_enter()
            elif player_turn == 0 and computer_turn == 1:
                print("Paper beats Rock! You lose!")
                click_enter()
            elif player_turn == 0 and computer_turn == 2:
                print("Rock beats Scissors! You win!")
                click_enter()
            elif player_turn == 1 and computer_turn == 0:
                print("Paper beats Rock! You win!")
                click_enter()
            elif player_turn == 1 and computer_turn == 2:
                print("Scissors beats Paper! You lose!")
                click_enter()
            elif player_turn == 2 and computer_turn == 0:
                print("Rock beats Scissors! You lose!")
                click_enter()
            elif player_turn == 2 and computer_turn == 1:
                print("Scissors beats Paper! You win!")
                click_enter()
def guess_number():
    # This is a guess the number game.
    import random
    number_games = input("Granny asks 'How many times do you want to play "
                         "Guess The Number'\n")

    for turns in range(1, int(number_games) + 1):
        secretNumber = random.randint(1, 20)
        print("Granny says, 'I am thinking of a number between 1 and 20.'\n")

        # Ask the player to guess 6 times.
        for guessesTaken in range(1, 7):
            print("Take a guess, dearie")
            guess = int(input())

            if guess < secretNumber:
                print("Aww shucks, your guess is low.")
            elif guess > secretNumber:
                print("Sweetie, your guess is too high.")
            else:
                break  # This condition is the correct guess!

        if guess == secretNumber:
            print("Good job dearie! You guessed my number in " + str(guessesTaken) + " guesses!\n")
            click_enter()
        else:
            print("Naw. The number I was thinking of was " + str(secretNumber))
            click_enter()
def granny_event():
    global health
    global strength
    global magic
    click_enter()
    play_or_not = input("A granny appears from out of the bushes. She looks lonely."
                       "Would you like to play some games with me dearie? \nEnter 'Y' for yes, 'N' for no \n")
    if play_or_not.lower().strip() == 'y':
        which_game = input("Oh goodie. What game would you like to play? "
                           "\nRock, Paper, Scissors or Guess the Number?"
                           "\nEnter 1 for Rock, Paper, Scissors. Enter 2 for Guess the Number. \n")
        if which_game == '1':
            rps_game()
        elif which_game == '2':
            guess_number()
        else:
            guess_number()
        print("Thank you for keeping me company dearie. Here, have a cookie."
          "\nYou eat the cookie and gained 5 Health, 5 Magic, and 5 Strength. \n")
        health += 5
        magic += 5
        strength += 5
        click_enter()
        stats()
        health_0()
        luck_roll_pos()

    else:
        print("'I'll get out of your hair', said Granny as she hobbled away. \n")
        health_0()
        luck_roll_neg()
########################################################################################################################
# Plants Event
def magic_plant():  # Checks with the current Magic stat and runs if statements
    global magic
    global health
    global strength
    if magic >= 9:
        magic += 2
        print(
            "You remember that plants are weak against fire. "
            "You shot fireballs from your wand. The plants caught on fire and burned to ash."
            "\nYou gain 2 Magic from this. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif magic >= 5 and magic <= 8:
        health -= 1
        magic += 1
        print(
            "You vaguely remember that plants are weak against fire. "
            "But you forget the fire spell. "
            "You manage to conjure up some rabbits to distract the plants as you escaped. "
            "\nYou lose 1 Health and gain 1 Magic. \n")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
    else:
        health -= 3
        magic -= 1
        strength -= 1
        print(
            "In your panic, you forgot all your spells and wave your wand frantically at the plant. "
            " Your wand shoots out some sparks and you managed to set both the plants and yourself on fire."
            " You get away and smothered the flames."
            "\nYou lose 3 Health, 1 Magic and 1 Strength. \n ")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
def strength_plant():  # Checks Stats
    global magic
    global health
    global strength
    if strength >= 9:
        strength += 2
        print(
            "You tear the vines apart with your bare hands. "
            "The plants recoil and withdraw their vines. "
            "\nYou gain 2 Strength. \n")
        click_enter()
        stats()
        luck_roll_pos()
    elif strength >= 5 and strength <= 8:
        health -= 1
        strength += 1
        print(
            "You attempt to tear the vines apart with your hands."
            " But you are too weak. The vines nearly overpower you."
            "\nYou manage to wiggle out of its grasp.\nYou lost 1 Health and gained 1 Strength. \n ")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
    else:
        health -= 3
        strength -= 2
        print(
            "You attempt to tear the vines apart with your hands."
            " But you are too weak."
            "\n It pulls you towards its mouth. In your struggle, you dropped a pepper bomb into its mouth."
            "\n It retches and tosses you aside."
            "\nYou lost 3 Health and 2 Strength. \n ")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
def plant():
    print("You took a closer inspection of one of the plant's vines."
        "It starts to move! It's a man-eating plant! \n")
    while True:
        answer_3 = input("What do you do? Do you run away, use magic or fight? Enter Run, Magic or Fight. \n")
        if answer_3.lower().strip() == "run":
            print("You died trying to run away. \n")
            quit()
        elif answer_3.lower().strip() == "magic":
            magic_plant()
            break
        elif answer_3.lower().strip() == "fight":
            strength_plant()
            break
        else:
            continue
def plant_event_50():
    global health
    global strength
    global magic
    plant_flip = random.randint(1,2)
    print("You approach a bush of brightly colored plants. "
          "They look familiar so you take a closer look. \n")
    click_enter()
    if plant_flip == '1':
        health += 5
        magic += 5
        strength += 5
        print("You recognize the plants upon a closer inspection! "
              "It is very rare plant that boosts your all stats! "
              "\nYour Health,Magic and Strength went up by 5.\n")
        click_enter()
        stats()
        luck_roll_pos()
    else:
        luck_roll_50()
        plant()
########################################################################################################################
# Mushrooms 50
def mushroom_event():
    global health
    global strength
    global magic
    click_enter()
    mushroom_flip = random.randint(1,3)
    print("All of a sudden a giant mushroom is rushing at you! \n")
    click_enter()
    if mushroom_flip == 1:
        health += 5
        magic += 5
        print("Lucky you! It was a magic mushroom! Your Health and Magic went up by 5.\n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    else:
        health -= 5
        strength -= 3
        print("Oh no! It was a cursed mushroom! It collides into you. You lose 5 Health and 3 Strength. \n")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
########################################################################################################################
# Lake 50
def lake_event():
    global health
    global strength
    global magic
    click_enter()
    lake_flip = random.randint(1,3)
    print("You stop by a lake to refill your canteen. "
          "From the distant side of the lake you can vaguely see a silvery horse. "
          "\nIt is trotting accross the water's surface to you.")
    click_enter()
    if lake_flip == 1:
        health += 5
        magic += 5
        print("As it gets closer you can see the glow of its horn."
              "It's a unicorn! It blesses and purifies the lake water. \nYour Health and Magic went up by 5.\n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    else:
        health -= 3
        strength -= 3
        print("You see that it is a beautiful horse. It invites you to ride on it."
              "\nYou put your hands out to touch it. When it grabs you and starts dragging you under the water. "
              "\n Its a Kelpie!"
              "\nYou stun it with a spell and escape, but you lose 3 Health and 3 Strength. \n")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
########################################################################################################################
# Treasure Chest 50
def treasure_chest_50():
    global health
    global strength
    global magic
    click_enter()
    chest_flip = random.randint(1,3)
    print("You stop by an ancient tree to rest. "
          "The giant tree has a big hollow above your head. "
          "You curiously peeked in and see a dusty treasure chest. \n")
    click_enter()
    if chest_flip == 1:
        health += 5
        magic += 5
        print("You shrug and decide to open the chest."
              "The top creaks open and a bright light blinds you. "
              "\nThere is nothing in the chest, but your Health and Magic went up by 5.\n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    else:
        health -= 3
        strength -= 3
        print("You shrug and decide to open the chest."
              "\nYou barely touched the top of the chest when it opens its fanged mouth. "
              "\nIts a Mimic!"
              "\nIt bites down on your hand. "
              "You managed to stun it with a spell and escape, but you lose 3 Health and 3 Strength. \n")
        click_enter()
        stats()
        luck_roll_50()
        health_0()
########################################################################################################################
# Slimes
# Slimes Event
def magic_slimes():  # Checks with the current Magic stat and runs if statements
    global magic
    global health
    global strength
    if magic >= 9:
        magic += 2
        print(
            "Slimes are weak against fire. You blast fireballs at the the slimes. "
            "They melt away into puddles. \nYou gain 2 Magic from this. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif magic >= 5 and magic <= 8:
        health -= 1
        magic += 1
        print(
            "You can only recall the lightning spell. You zapped them with a shot from your wand. It worked! "
            "\nBut only for a few moments. "
            "\nThey quickly recover and bounce towards you. You managed to run away with a scraped knee. "
            "\nYou lose 1 Health and gain 1 Magic. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
    else:
        health -= 3
        magic -= 1
        strength -= 1
        print(
            "You anxiously try to recall any spell to fight the slimes. "
            "You yell out a random spell. "
            "\n BOOM \n"
            "It blew up in your face. Fortunately it also blasted the slimes into nothing. "
            "\nYou lose 3 Health, 1 Magic and 1 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
def strength_slimes():  # Checks Stats
    global magic
    global health
    global strength
    if strength >= 9:
        strength += 2
        print(
            "You break off a thick branch from a tree and start smashing the slimes with all your might. "
            "\nThe slimes were obliterated by your might. "
            "You got a good arm workout from swinging the branch. \nYou gain 2 Strength. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif strength >= 5 and strength <= 8:
        health -= 1
        strength += 1
        print(
            "You break off a branch from a tree and start whacking at the slimes. "
            "\nYour blows bounce off their slimey surface. "
            "\nYou lost your nerve and started running away. Luckily slimes don't have great vision, so you escaped easily. "
            "\nYou lost 1 Health and gained 1 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
    else:
        health -= 3
        strength -= 2
        print(
            "You tried to break off a tree branch to smash the slimes. \nYou are too weak. The slimes are upon you. "
            "They surround you and bounce on you. "
            "\nYou run blindly through the forest, hitting tree trunks, tripping on roots and scratched by branches. "
            "You managed to get away from them. \nYou lost 3 Health and 2 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
def slimes():
    click_enter()
    print("You encounter a herd of bouncing slimes. Slimes are a low-level monster."
        "\nBut you are not an adventurer, so you would like to avoid them if you can. "
        "\nBut the slimes blocked the your path through the forest. \n")
    while True:
        answer_2 = input("What do you do? Do you run away, use magic or fight? Enter Run, Magic or Fight. \n")
        if answer_2.lower().strip() == "run":
            print("You died trying to run away. \n")
            quit()
        elif answer_2.lower().strip() == "magic":
            magic_slimes()
            break
        elif answer_2.lower().strip() == "fight":
            strength_slimes()
            break
        else:
            continue
########################################################################################################################
# Goblins
# Goblins Event
def magic_goblins():  # Checks with the current Magic stat and runs if statements
    global magic
    global health
    global strength
    if magic >= 9:
        magic += 2
        print(
            "Goblins love gold. You shoot an illusion spell on some butterflies. "
            "The butterflies appear to be made of gold. The goblins chase after the gold butterflies. "
            "\nYou gain 2 Magic from this. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif magic >= 5 and magic <= 8:
        health -= 1
        magic += 1
        print(
            "Goblins love gold. You take out some of your gold coins. "
            "You zapped the coins with a flying spell. The goblins are distracted by the flying coins! "
            "\nBut only for a few moments. Your spell wasn't strong enough and the coins fell down. "
            "\nThe goblins grab the coins and start running towards you. You managed to run away. "
            "\nYou lose 1 Health and gain 1 Magic. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
    else:
        health -= 3
        magic -= 1
        strength -= 1
        print(
            "You anxiously try to recall any spell to fight the goblins. "
            "You yell out a random spell. "
            "\n BOOM \n"
            "It blew up in your face. Fortunately it also blasted the goblins away. "
            "\nYou lose 3 Health, 1 Magic and 1 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
def strength_goblins():  # Checks Stats
    global magic
    global health
    global strength
    if strength >= 9:
        strength += 2
        print(
            "You grab a goblin and begin swinging it around like a club. "
            "\nThe goblins are thoroughly thrashed. They run off scared and bruised. "
            "You got a good arm workout from swinging goblins. \nYou gain 2 Strength. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif strength >= 5 and strength <= 8:
        health -= 1
        strength += 1
        print(
            "You swing your fists at the goblins. "
            "\nYou miss most of your swings. But when your fists hit a goblin you sent it flying. "
            "\nThe goblins eventually gave up fighting you."
            "\nYou lost 1 Health and gained 1 Strength. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
    else:
        health -= 3
        strength -= 2
        print(
            "You swing your fists at the goblins \nYou are too weak. The goblins are upon you. "
            "They surround you and start clawing at you. "
            "\nYou run blindly through the forest, hitting tree trunks, tripping on roots and scratched by branches. "
            "You managed to get away from them. \nYou lost 3 Health and 2 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
def goblins():
    click_enter()
    print("You encounter a group of goblins. Goblins are stupid, but they can overwhelm you."
    "\nYou are not an adventurer, so you would like to avoid them if you can. "
    "\nBut the goblins blocked the your path through the forest. ")
    while True:
        answer_2 = input(
            "\nWhat do you do? Do you run away, use magic or fight? Enter Run, Magic or Fight. \n")
        if answer_2.lower().strip() == "run":
            print("You died trying to run away. \n")
            quit()
        elif answer_2.lower().strip() == "magic":
            magic_goblins()
            break
        elif answer_2.lower().strip() == "fight":
            strength_goblins()
            break
        else:
            continue
########################################################################################################################
# Witch's Tea House
def magic_witch():  # Checks with the current Magic stat and runs if statements
    global magic
    global health
    global strength
    if magic >= 9:
        magic += 2
        print(
            "A witch knows a lot of spells. She would know more than you."
            "But you are younger and have quicker reflexes. You shot a fireball at her wand. "
            "\nIt burned away to ash. The witch horrified ran out the back door. "
            "\nYou gain 2 Magic from this. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif magic >= 5 and magic <= 8:
        health -= 1
        magic += 1
        print(
            "A witch knows a lot of spells. She would know more than you."
            "But you are younger and have quicker reflexes. You shot a fireball at her wand. "
            "But you missed and blasted a supporting beam."
            "\nShe is angry that you caught her off guard and zaps some spells at you."
            "\nSome spells burned as it hissed by you. "
            "A supporting beam fell on her and you escaped the burning tea shop."
            "\nYou lose 1 Health and gain 1 Magic. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
    else:
        health -= 3
        magic -= 1
        strength -= 1
        print(
            "You anxiously try to recall any spell to fight the witch. "
            "You yell out a random spell. "
            "\n BOOM \n"
            "It blew up in your face. Fortunately it also blasted the witch away. "
            "\nYou lose 3 Health, 1 Magic and 1 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
def strength_witch():  # Checks Stats
    global magic
    global health
    global strength
    if strength >= 9:
        strength += 2
        print(
            "A witch knows a lot of spells. She would know more than you."
            "But you are younger and have quicker reflexes. You lunge at her and side-stepped her spells."
            "You snapped her wand and threw her out of the tea shop. \nYou gain 2 Strength. \n")
        click_enter()
        stats()
        health_0()
        luck_roll_pos()
    elif strength >= 5 and strength <= 8:
        health -= 1
        strength += 1
        print(
            "A witch knows a lot of spells. She would know more than you."
            "But you are younger and have quicker reflexes. You lunge at her. "
            "You got hit by one of her spells. It burned, but you continue until you successfully snapped her wand."
            "\nYou lost 1 Health and gained 1 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
    else:
        health -= 3
        strength -= 2
        print(
            "You attempt to rush at the witch to snap her wand. "
            "\nYou are too slow. The witch saw your plan and she jumped back. "
            "She threw a flurry of spells at you. Most missed, but a few met their mark."
            "\nShe accidentally set herself on fire and was momentarily distracted."
            "\nYou jump through a window and ran through the forest. "
            "\nYou managed to get away from the witch. \nYou lost 3 Health and 2 Strength. \n ")
        click_enter()
        stats()
        health_0()
        luck_roll_50()
def witch():
    click_enter()
    print("You reached a tea shop in a clearing. "
        "Its been such a hot day and you see that the shop offers boba milk tea."
        "\nYou eagerly enter the shop to order a refreshing drink."
        "\nA witch cackles from behind the counter and zaps the door shut. Its a trap! \n")
    while True:
        answer_2 = input("What do you do? Do you run away, use magic or fight? Enter Run, Magic or Fight. \n")
        if answer_2.lower().strip() == "run":
            print("You died trying to run away. \n")
            quit()
        elif answer_2.lower().strip() == "magic":
            magic_witch()
            break
        elif answer_2.lower().strip() == "fight":
            strength_witch()
            break
        else:
            continue
########################################################################################################################
def got_sugar():
    click_enter()
    print("Miss GoldenDragon gives you a cup of sugar and generously teleports you home.")
def too_weak():
    click_enter()
    if luck > 0:
        got_sugar()
        print("You arrive safely home. But the whole journey has been so tiring."
              " You took a nap and woke up the next day. "
              "You rush and managed to put together a respectable tea party.")
    else:
        no_luck()
def best_ending():
    click_enter()
    print("You arrive safely home with your cup of sugar. You feel surprisingly refreshed despite your journey. "
          "\nYou baked the most delicious and moist cake. A royal did show up! "
          "\nYou shared your adventures to get the cup of sugar. "
          "\nYou impressed them so much that they offer to publish your adventures in a novel. "
          "\nYour novel is an instant success and with your profits you open up a bakery called 'Cup o' Sugar'."
          "\nThe End")
def good_ending():
    click_enter()
    print("You arrive safely home. You are a bit tired, but you go ahead and bake your cake. "
          "\nThe next day you tea party went well. No rumored royal showed up."
          "\nYour reputation goes up for your delicious cake and you are invited to more tea parties."
          "\nThe End")
def burnt_cake():
    click_enter()
    print("You arrive safely home. But you are so tired. You still went forward and baked a cake."
          "\nBut you fell asleep and the cake was burnt! "
          "You decide to serve it anyway, hiding the burnt blackness with plenty of whipped cream. "
          "\nThe tea party was a moderate success, though much cake was left uneaten.")
def walk_home():
    click_enter()
    if strength >= 10 and health >= 10:
        print("You walk yourself safely home. "
                "You are frustrated that you didn't get your sugar."
                " But you made do with store-bought baked goods. "
                "You managed to have a respectable, but mediocre tea party.")
        quit()
    elif strength < 10 and health < 10:
        print("You attempt to walk back, but you are too weak to travel. You are stuck and miss the tea party.\n")
        quit()
    else:
        print("You attempt to walk back, but you are too weak to travel. You are stuck and miss the tea party.\n")
def no_luck():
    click_enter()
    magic_walk = input("You knock and knock, but it appears that no one was home. "
            "Do you use magic to get home or walk? Enter 'M' for magic or 'W' for walk. \n")
    if magic_walk.lower().strip() == "m":
        if magic >= 15:
            print("You teleport yourself safely home. "
                    "You are frustrated that you didn't get your sugar."
                    " But you made do with store-bought baked goods. "
                    "You managed to have a respectable, but mediocre tea party.")
        else:
            print("Your teleportation spell failed.")
            walk_home()
    elif magic_walk.lower().strip() == "w":
            walk_home()
def final_stat_check():
    if health <= 5 and strength <= 0:
        too_weak()
    elif luck >= 15:
        got_sugar()
        best_ending()
    elif luck >= 6 and luck <= 10:
        got_sugar()
        good_ending()
    elif luck >= 0:
        got_sugar()
        burnt_cake()
    else:
        no_luck()

def whole_game():
    global health
    global strength
    global magic
    global luck
    health = 5
    strength = 5
    magic = 5
    luck = 5  # Invisible Stat
    horse_griffin()
    list_events = [fairies, goblins, granny_event, hole_event, lake_event, mermaids,
                   mushroom_event, plant_event_50, slimes, treasure_chest_50, witch]  # List of events
    while list_events != 0:  # To continue through list
        if magic >= 25:
            print("You suddenly remembered the teleportation spell. "
                  "You teleport yourself to Miss GoldenDragon's door.")
            break
        elif list_events == []:  # If list is empty to break out of loop
            break
        events = random.randint(0, len(list_events) - 1)  # Random number for index of stat_events list
        list_events[events]()  # This will call the function
        list_events.remove(list_events[events])  # Removes the event that was selected
    click_enter()
    print("You arrive at Miss GoldenDragon's door.")
    final_stat_check()

# Introduction

print("\n\nJourney to Miss GoldenDragon\n\n")
click_enter()
print(
    "You are hosting a tea party tomorrow with the upper echelons of society. "
    "\nWealthy wives, aristocratic ladies and there was even a rumor of one of the royals attending. "
    "\nYou intend to bake a cake to impress them all! But you do not have enough sugar! "
    "Your nearest neighbor is Miss GoldenDragon pass the Dark Forest on top of the mountain. "
    "\nYou must journey to borrow a cup of sugar!\n")
click_enter()
stats()
# Testing
# 1. While loop restart
# 2. assigning numbers to events and randomizing the events

while True:
    whole_game()
    restart = input("Do you want to restart? Enter 'Y' for yes or 'N' for No.")
    if restart.lower().strip() == 'n':
        quit()
    elif restart.lower().strip() == 'y':
        continue






