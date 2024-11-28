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
# time.sleep(2.5)

adventure_run = True

# Emoji Variables - https://www.unicode.org/emoji/charts/full-emoji-list.html
# Unicode Emoji Replace + with 000 e.g. U+1F480 = \U0001F480
chicken_emoji = "\U0001F414"
skull_emoji = "\U0001F480"
prohibited_emoji = "\U0001F6AB"
police_car_light_emoji = "\U0001F6A8"

# ready = input("\nAre you ready to explore and see what is in store for you? (yes/no): ")[0].lower()
ready = "yes"

if ready == "yes":
    # time.sleep(1)
    print(colored("\nHow to play:", attrs=["bold"]))
    print("• Read the story")
    print("• Input your decision (A, B, C)")
    print("• Read the outcome")

elif ready == "no":
    print(f"Run run little chicken! {chicken_emoji}")
    quit()


# Decision 1: Choosing Your Vehicle
print(colored("\nDecision 1: Choosing Your Vehicle", attrs=["underline", "bold"]))
print(colored("The thief is getting away! You need to pick a vehicle quickly to pursue him.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "A sleek black BMW M3, known for its speed.")
print(colored("B: ", "green", attrs=["bold"])+ "A motorbike, agile but risky since you’re not an expert rider.")
print(colored("C: ", "green", attrs=["bold"])+ "An electric mountain bike, slower but you're comfortable with it.")

while adventure_run:
    decision_one = input("What will you choose?: ").upper()

    if decision_one == "A":
        print(f"\nYou zoom through traffic, but the thief notices you’re chasing him. {skull_emoji}")
        quit()
    elif decision_one == "B":
        print("\nYou struggle to keep up, wobbling through turns.")
        break
    elif decision_one == "C":
        print("\nYou blend into the crowd but lag behind.")
        break
    else:
        print(f"\nInvalid choice. Please try again! {prohibited_emoji}")

# Delay before next Decision
time.sleep(2)


# Decision 2: The Shortcut
print(colored("\nDecision 2: The Shortcut", attrs=["underline", "bold"]))
print(colored("The thief takes a sharp turn into an alleyway.", "blue", attrs=["bold"]))
print(colored("A: ", "green", attrs=["bold"])+ "Follow him into the narrow alley.")
print(colored("B: ", "green", attrs=["bold"])+ "Take the main road and hope to cut him off.")
print(colored("C: ", "green", attrs=["bold"])+ "Stop and call for help.")


while adventure_run:
    decision_one = input("Do you: ").upper()

    if decision_one == "A":
        print("\nYour vehicle barely fits, but you keep him in sight.")
        break
    elif decision_one == "B":
        print("\nYou lose sight of him but stumble upon a clue (a dropped wallet).")
        break
    elif decision_one == "C":
        print(f"\nThe adventure ends prematurely—police take over the case. {police_car_light_emoji}")
        quit()
    else:
        print(f"\nInvalid choice. Please try again! {prohibited_emoji}")

# Delay before next Decision
time.sleep(2)


# Decision 3: The Wallet
