import sys, time
# https://pypi.org/project/termcolor/
from termcolor import colored, cprint

# https://www.asciiart.eu/text-to-ascii-art
print(r"""\
__        __   _                            _____     
\ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   |_|\___/ 
   / \   __| |_   _____ _ __ | |_ _   _ _ __ ___| |   
  / _ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ |   
 / ___ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/_|   
/_/   \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___(_)   

                    """)

# Wait x seconds before continuing
time.sleep(2.5)

adventure_run = True

# Used for skips
skip = 0

while True:
    ready = input("\nAre you ready to explore and see what is in store for you? (yes/no): ").lower()
    # ready = "yes"

    if ready == "yes":
        time.sleep(1)
        print(colored("\nHow to play:", attrs=["bold"]))
        print("• Read the story")
        print("• Input your decision (A, B, C, D)")
        print("• Read the outcome")
        break

    elif ready == "no":
        print("Run run little chicken! 🐔")
        quit()

    else:
        print("\nInvalid! (yes/no)")


print("\nTitle: The Great Urban Pursuit")
print("""The city is alive with neon lights and chaos. You’re in a rush,
but not just any rush—someone stole a priceless artifact from your friend,
and you're determined to get it back. But the path isn’t straightforward,
and your choices will shape the story.""")

# Wait x seconds before continuing
time.sleep(2.5)

# TODO - Add a timer to have urgency in input 30seconds 🏃‍♂️💨
# Decision 1: Choosing Your Vehicle
print(colored("\nChoosing Your Vehicle", attrs=["underline", "bold"]))
print(colored("The thief is getting away! You need to pick a vehicle quickly to pursue him.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ f"A sleek black BMW M3, known for its speed.")
print(colored("B: ", "green", attrs=["bold"])+ f"A motorbike, agile but risky since you’re not an expert rider.")
print(colored("C: ", "green", attrs=["bold"])+ f"An electric mountain bike, slower but you're comfortable with it.")

while adventure_run:
    decision = input("What will you choose?: ").upper()

    if decision == "A":
        print("\nYou zoom through traffic, but the thief notices you’re chasing him. 🏎️")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    elif decision == "B":
        print("\nYou struggle to keep up, wobbling through turns. 🏍️")
        break
    elif decision == "C":
        print("\nYou blend into the crowd but lag behind. 🚴")
        break
    else:
        print("\nInvalid choice. Please try again! 🚫")

# Delay before next Decision
time.sleep(2)


# Decision 2: The Shortcut
print(colored("\nThe Shortcut", attrs=["underline", "bold"]))
print(colored("The thief takes a sharp turn into an alleyway.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "Follow him into the narrow alley.")
print(colored("B: ", "green", attrs=["bold"])+ "Take the main road and hope to cut him off.")
print(colored("C: ", "green", attrs=["bold"])+ "Stop and call for help.")

while adventure_run:
    decision = input("Do you: ").upper()

    if decision == "A":
        print("\nYour vehicle barely fits, but you keep him in sight. 🛣️")
        break
    elif decision == "B":
        print("\nYou lose sight of him but stumble upon a clue. 🚦")
        break
    elif decision == "C":
        print("\nThe adventure ends prematurely police take over the case. 🚨")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    else:
        print("\nInvalid choice. Please try again! 🚫")

# Delay before next Decision
time.sleep(2)


# Decision 3: The Wallet
print(colored("\nThe Wallet", attrs=["underline", "bold"]))
print(colored("You find a wallet dropped by the thief.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "Pick it up and keep chasing.")
print(colored("B: ", "green", attrs=["bold"])+ "Open it and check for clues.")
print(colored("C: ", "green", attrs=["bold"])+ "Leave it and focus on the chase.")

while adventure_run:
    decision = input("Do you: ").upper()

    if decision == "A":
        print("\nYou catch a glimpse of the thief entering a building. 🏠")
        break
    elif decision == "B":
        print("\nInside the wallet is an ID and a suspicious keycard. 🪪")
        break
    elif decision == "C":
        print("\nYou lose valuable time but remain on the trail. 👣")
        break
    else:
        print("\nInvalid choice. Please try again! 🚫")

# Delay before next Decision
time.sleep(2)


# Decision 4: The Fight
print(colored("\nThe Fight", attrs=["underline", "bold"]))
print(colored("You corner the thief, but he’s not giving up without a fight.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "Try to make peace and talk him down.")
print(colored("B: ", "green", attrs=["bold"])+ "Fight him with your fists.")
print(colored("C: ", "green", attrs=["bold"])+ "Use the sandwich in your bag as a distraction.")
print(colored("D: ", "green", attrs=["bold"])+ "Pull out a toy gun and hope to bluff.")

while adventure_run:
    decision = input("What do you do?: ").upper()

    if decision == "A":
        print("\nHe momentarily hesitates but escapes when you’re distracted. 🏃🏻")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    elif decision == "B":
        print("\nYou overpower him, but he calls for backup. 🤼")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    elif decision == "C":
        print("\nHe grabs the sandwich and runs, leaving behind a map. 🗺️")
        break
    elif decision == "D":
        print("\nHe laughs but surrenders, thinking you’re unpredictable. 🏳️")
        print(colored("Adventure Passed (not the real ending)", "green", attrs=["bold", "underline"]))
        quit()
    else:
        print("\nInvalid choice. Please try again! 🚫")

# Delay before next Decision
time.sleep(2)


# Decision 5: The Map
print(colored("\nThe Map", attrs=["underline", "bold"]))
print(colored("The map shows a warehouse near the docks.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "Go there immediately.")
print(colored("B: ", "green", attrs=["bold"])+ "Call a friend for backup.")
print(colored("C: ", "green", attrs=["bold"])+ "Ignore it and follow another lead.")

while adventure_run:
    decision = input("Do you: ").upper()

    if decision == "A":
        print("\nThe warehouse is a trap, and you’re ambushed. 🔪")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    # TODO - Jump to the next iteration decision
    elif decision == "B":
        print("\nYour friend helps you navigate the situation safely. 👩")
        skip = 1
        break
    elif decision == "C":
        print("\nYou lose the trail but stumble onto another clue. 🧩")
        break
    else:
        print("\nInvalid choice. Please try again! 🚫")

# Delay before next Decision
time.sleep(2)


# Decision 6: The Dropped Phone
if skip == 0:
    print(colored("\nThe Dropped Phone", attrs=["underline", "bold"]))
    print(colored("You find a phone ringing on the ground.", "blue", attrs=["bold"]))
    print(colored("A: ", "green", attrs=["bold"])+ "Answer the call.")
    print(colored("B: ", "green", attrs=["bold"])+ "Take it to the police.")
    print(colored("C: ", "green", attrs=["bold"])+ "Smash it, thinking it’s a trap.")

    while adventure_run:
        decision = input("Do you: ").upper()

        if decision == "A":
            print("\nThe caller gives cryptic clues leading to the thief’s location. 📍")
            break
        elif decision == "B":
            print("\nThe police delay action, and the thief gets away. 🏃")
            print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
            quit()
        elif decision == "C":
            print("\nYou destroyed the only lead. The thief escapes for good. ☎️")
            print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
            quit()
        else:
            print("\nInvalid choice. Please try again! 🚫")

    # Delay before next Decision
    time.sleep(2)


# Decision 7: The Final Confrontation
skip = 0
print(colored("\nThe Final Confrontation", attrs=["underline", "bold"]))
print(colored("You find the thief again at a secret hideout.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "Sneak in through the back entrance.")
print(colored("B: ", "green", attrs=["bold"])+ "Go in guns blazing.")
print(colored("C: ", "green", attrs=["bold"])+ "Wait for the thief to come out.")

while adventure_run:
    decision = input("What’s your approach?: ").upper()

    if decision == "A":
        print("\nYou successfully retrieve the artifact. 💎")
        break
    elif decision == "B":
        print("\nYou scare the thief, but reinforcements arrive. 🥷")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    elif decision == "C":
        print("\nYou lose your chance, and the thief disappears. ⌛")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    else:
        print("\nInvalid choice. Please try again! 🚫")

# Delay before next Decision
time.sleep(2)


# Decision 8: The Money Drop
print(colored("\nThe Money Drop", attrs=["underline", "bold"]))
print(colored("You see someone drop a wad of cash inside the hideout.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "Take it for yourself.")
print(colored("B: ", "green", attrs=["bold"])+ "Return it to the person.")
print(colored("C: ", "green", attrs=["bold"])+ "Ignore it and keep focused on the escaping with the artifact.")

while adventure_run:
    decision = input("Do you: ").upper()

    if decision == "A":
        print("\nYou’re caught and arrested for theft. 👮")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    elif decision == "B":
        print("\nThe person helps distract the thief, aiding your mission. 🪽")
        break
    elif decision == "C":
        print("\nYou stay on track but miss an opportunity for help. ❌")
        break
    else:
        print("\nInvalid choice. Please try again! 🚫")

# Delay before next Decision
time.sleep(2)


# Decision 9: The Escape
print(colored("\nThe Escape", attrs=["underline", "bold"]))
print(colored("The thief tries to flee on a speedboat.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "Steal another boat and give chase.")
print(colored("B: ", "green", attrs=["bold"])+ "Swim after him.")
print(colored("C: ", "green", attrs=["bold"])+ "Call the coast guard.")

while adventure_run:
    decision = input("You: ").upper()

    if decision == "A":
        print("\nYou catch up and corner the thief. 👊")
        break
    elif decision == "B":
        print("\nYou exhaust yourself and lose the chase. 🫩")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    elif decision == "C":
        print("\nThey capture the thief, but you don’t get credit. 🔒")
        print(colored("Adventure Passed (not the real ending but close)", "green", attrs=["bold", "underline"]))
        quit()
    else:
        print("\nInvalid choice. Please try again! 🚫")

# Delay before next Decision
time.sleep(2)


# Decision 10: The Artifact
print(colored("\nThe Artifact", attrs=["underline", "bold"]))
print(colored("You recover the artifact, but you’re surrounded by the thief’s gang.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "Surrender and hope for mercy.")
print(colored("B: ", "green", attrs=["bold"])+ "Use the artifact as a bargaining chip.")
print(colored("C: ", "green", attrs=["bold"])+ "Fight your way out.")

while adventure_run:
    decision = input("You: ").upper()

    if decision == "A":
        print("\nYou’re captured. Game over. 👊")
        print(colored("Adventure Failed (try again)", "red", attrs=["bold", "underline"]))
        quit()
    elif decision == "B":
        print("\nYou trick them into letting you escape without the artifact. 👿")
        print(colored("Adventure Passed (not the real ending but super close)", "green", attrs=["bold", "underline"]))
        quit()
    elif decision == "C":
        print("\nYou narrowly escape with injuries but left with the artifact and a hero! 🤕")
        print(colored("ADVENTURE PASSED! (real ending)", "green", attrs=["bold", "underline"]))
        print(r"""\
  .     '     ,
    _________
 _ /_|_____|_\ _
   '. \   / .'
     '.\ /.'
       '.'
                    """)
        quit()
    else:
        print("\nInvalid choice. Please try again! 🚫")

# Delay before next Decision
time.sleep(2)



print("That's it! I hope you enjoyed!")
