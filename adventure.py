import sys, time, textwrap, subprocess, os
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


adventure_run = True

tts_enabled = False

# skip = 0

#### FUNCTIONS ####
# Wait Here
def wait(x):
    time.sleep(x)

# Rules
def rules():
    wait(1)
    print(colored("\nHow to play:", attrs=["bold"]))
    print("• Read the story")
    print("• Input your decision (A, B, C, D)")
    print("• Read the outcome")
    wait(2.5)


def toggle_tts():
    global tts_enabled
    tts_enabled = not tts_enabled  # Toggle the TTS setting
    print("TTS is now turned", "ON" if tts_enabled else "OFF")
    # tts("TTS is now turned ON!")
    if tts_enabled:
        tts("TTS is now turned On")
    else:
        tts("TTS is now turned Off")
    main_menu()


# en-US-JennyNeural
# Function to suppress unwanted output from the subprocess
def tts(text, voice="en-GB-SoniaNeural"):
    # if not tts_enabled:
    #     return
    # Create the command to run in the background
    command = [
        "edge-playback",
        "--text", text,
        "--voice", voice
    ]
    
    # Open a subprocess and redirect output to null
    with open(os.devnull, 'w') as devnull:
        subprocess.run(command, stdout=devnull, stderr=devnull)
    



# ============================================
#            🧟 The Last Refuge 🧟
# ============================================
# ============================================
#            Decision 1: Entering the Safehouse
# ============================================
def the_safehouse():
# --- Plot ---
    print(colored("\nEntering the Safehouse", attrs=["underline", "bold"]))
    text = """
        You approach the Safehouse, an old, crumbling building that once offered shelter to many.
        Now, it’s a silent monument to the apocalypse. Zombies roam outside, their groans cutting through the stillness of the night.
        Inside, the Safehouse is dark and foreboding.
    """
    cleaned_text = textwrap.dedent(text).strip()
    print(colored(cleaned_text, 'blue'))
    tts(text)

# --- Choices ---
    print(colored("A: ", "green", attrs=["bold"])+ "Enter the Main Hall 🏚️")
    print(colored("B: ", "green", attrs=["bold"])+ "Go to the Basement 🪔")
    print(colored("C: ", "green", attrs=["bold"])+ "Check the Upstairs Rooms 🔼")

    while adventure_run:
        tts("What do you do?")
        decision = input("What do you do?: ").upper()

# --- Decision A ---
        if decision == "A":
            print("\nYou push open the creaking door and step into the main hall. The smell of decay fills the air, and your footsteps echo through the empty space. Broken furniture and debris litter the floor. Suddenly, you hear a scratching noise coming from the shadows.")
            tts("You push open the creaking door and step into the main hall. The smell of decay fills the air, and your footsteps echo through the empty space. Broken furniture and debris litter the floor. Suddenly, you hear a scratching noise coming from the shadows.")

            print(colored("A: ", "green", attrs=["bold"])+ "Hide Behind the Counter 🤫")
            print(colored("B: ", "green", attrs=["bold"])+ "Check the Source of the Noise 🔍")
            print(colored("C: ", "green", attrs=["bold"])+ "Block the Entrance 🔒")
            tts("What do you do?")
            sub_decision = input("What do you do?: ").upper()

            if sub_decision == "A":
                print("\nYou crouch behind the counter, heart pounding. The scratching grows louder, and a decaying hand reaches over the counter. You hold your breath as a zombie shuffles by, missing you by inches.")
                tts("You crouch behind the counter, heart pounding. The scratching grows louder, and a decaying hand reaches over the counter. You hold your breath as a zombie shuffles by, missing you by inches.")

                print(colored("A: ", "green", attrs=["bold"])+ "Stay Hidden 🕰️")
                print(colored("B: ", "green", attrs=["bold"])+ "Run for It 🏃")
                tts("What do you do?")
                sub_sub_decision = input("What do you do?: ").upper()
                    
                if sub_sub_decision == "A":
                    print("\nYou wait in silence as the zombie moves away. Hours pass, and you realize you’re safe, but the lack of food and water weakens you. 🌑🧟‍♂️")
                    print("Outcome: Safe but hungry.")
                    tts("You wait in silence as the zombie moves away. Hours pass, and you realize you’re safe, but the lack of food and water weakens you.")
                    break

                elif sub_sub_decision == "B":
                    print("\nYou dash out from behind the counter, making noise. The zombie turns and chases you, but you manage to escape. However, the effort leaves you exhausted. 🏃‍♂️💨")
                    print("Outcome: Escaped but exhausted.")
                    tts("You dash out from behind the counter, making noise. The zombie turns and chases you, but you manage to escape. However, the effort leaves you exhausted.")
                    break
            
            
            elif sub_decision == "B":
                print("\nCheck the Source of the Noise You gather your courage and approach the noise. You discover a hidden room filled with supplies, but your presence alerts a zombie lurking nearby. 🧟‍♂️")
                tts("Check the Source of the Noise You gather your courage and approach the noise. You discover a hidden room filled with supplies, but your presence alerts a zombie lurking nearby.")
            break




















# --- Decision B ---
        elif decision == "B":
            print("\nThe back room is dark and cramped, with overturned shelves and broken crates.")
            print("You manage to find a can of beans and an old flashlight, but the noise of your search draws attention.")
            tts("The back room is dark and cramped, with overturned shelves and broken crates. You manage to find a can of beans and an old flashlight, but the noise of your search draws attention.")
            print(colored("A: ", "green", attrs=["bold"])+ "Fight")
            print(colored("B: ", "green", attrs=["bold"])+ "Flee")
            tts("What do you do?")
            sub_decision = input("What do you do?: ").upper()

            if sub_decision == "A":
                print("\nA zombie bursts in, and you barely fend it off with a nearby crowbar. 💔")
                print("You survive the encounter but your injuries slow you down.")
                tts("A zombie bursts in, and you barely fend it off with a nearby crowbar. You survive the encounter but your injuries slow you down.")
            elif sub_decision == "B":
                print("\nIn your panic, you drop the flashlight while running out, leaving you more vulnerable later. 🕯️")
                print("You escape, but the lack of light will make your next steps more dangerous.")
                tts("In your panic, you drop the flashlight while running out, leaving you more vulnerable later. You escape, but the lack of light will make your next steps more dangerous.")
            break

# --- Decision C ---
        elif decision == "C":
            print("\nThe alley is narrow and reeks of decay. The faint sound of dripping water masks your footsteps, but every shadow feels like a threat.")
            tts("The alley is narrow and reeks of decay. The faint sound of dripping water masks your footsteps, but every shadow feels like a threat.")
            print(colored("A: ", "green", attrs=["bold"]) + "Use the flashlight")
            print(colored("B: ", "green", attrs=["bold"]) + "Move quietly")
            tts("What do you do?")
            sub_decision = input("What do you do?: ").upper()

            if sub_decision == "A":
                print("\nYou spot a lurking zombie in time and slip past it safely, conserving your strength. 🔦")
                print("Your decision saved you from danger, and you feel a bit safer now.")
                tts("You spot a lurking zombie in time and slip past it safely, conserving your strength. Your decision saved you from danger, and you feel a bit safer now.")
            elif sub_decision == "B":
                print("\nYou trip over a pile of debris, the noise alerting a small group of infected that begin to pursue you. ⚠️")
                print("You barely escape, but now you're on the run with little time to spare.")
                tts("You trip over a pile of debris, the noise alerting a small group of infected that begin to pursue you. You barely escape, but now you're on the run with little time to spare.")
            break

        else:
            print("\nInvalid choice. Please try again! 🚫")
            tts("Invalid choice. Please try again!")
    wait(2)


# ============================================
#            Decision 2: The Streets
# ============================================





## Adventures
# The Great Urban Pursuit
def the_great_urban_pursuit():

    # Used for skips
    skip = 0

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
    wait(2)


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
    wait(2)


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
    wait(2)


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
    wait(2)


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
    wait(2)


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
        wait(2)


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
    wait(2)


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
    wait(2)


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
    wait(2)


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
    wait(2)



def the_last_refuge():
    the_safehouse()






### Scary

### Mystery

### Kids


# Main Menu Screen Selection
def main_menu():
    global tts_enabled

    while True:
        print("\nSelect a adventure! (1-4)")
        print("1: The Great Urban Pursuit")
        print("2: The Last Refuge")
        # print("3: xxxxx")
        # print("4: xxxxx")
        print("5: Exit")
        print("")
        print("##### SOUND SETTINGS #####")
        print("X: Toggle TTS (current: {})".format("ON" if tts_enabled else "OFF"))

        # choice = "2"
        choice = input("Adventure on: ").strip().upper()

        if choice == "1":
            print("Context: The city is alive with neon lights and chaos. You’re in a rush, but not just any rush—someone stole a priceless artifact from your friend, and you're determined to get it back. But the path isn’t straightforward, and your choices will shape the story.")
            confirm = input("Continue with this adventure? (yes/no): ").lower()
            if confirm == "yes":
                pass
            elif confirm == "no":
                main_menu()
            else:
                print("\Invalid choice. (yes/no)")
            rules()
            the_great_urban_pursuit()

        elif choice == "2":
            print("Context: The city you once knew is now a haunting wasteland, overrun by the undead. Every corner hides a potential threat, and survival is a constant struggle. As night falls, the Safehouse stands as your only refuge amidst the chaos. But safety comes with its own set of horrors.")
            # confirm = input("Continue with this adventure? (yes/no): ").lower()
            # if confirm == "yes":
            #     pass
            # elif confirm == "no":
            #     main_menu()
            # else:
            #     print("\Invalid choice. (yes/no)")
            # rules()
            the_last_refuge()

        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            print("\nRun run little chicken! 🐔")
            break
        elif choice == "X":
            toggle_tts()
        else:
            print("\Invalid choice. Please select a valid story (1-4) or exit (5)")





# Wait x seconds before continuing
wait(2.5)

main_menu()



# TODO - Story options
# 1 - The Great Urban Pursuit
# 2 - Scary theme
# 3 - Mystery theme
# 4- Kids theme


print("That's it! I hope you enjoyed!")
