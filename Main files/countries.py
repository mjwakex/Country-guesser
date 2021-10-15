import csv, random, os, time
score = 0
lives = 5
dict = {}

with open("countries.csv", mode="r") as f:
    reader = csv.reader(f)
    dict_from_csv = {rows[0].replace('\xa0', '').lower():rows[1].lower() for rows in reader}

def cls():
    os.system("cls")

def captial_guess():
    global lives, score
    while lives != 0 :
        result = random.choice(list(dict_from_csv.keys()))
        print(result)
        answer = input("What is the capital of this country : ").lower()
        if answer == dict_from_csv[result]:
            print("You got it right!")
            score += 1
            time.sleep(2)
            cls()
        else:
            lives -= 1
            print(f"You got it wrong...\nThe correct answer is {dict_from_csv[result]}\nYou have {lives} remaining")
            time.sleep(2)
            cls()
    if lives == 0:
        print(f"You are out of lives, your score was {score}")

def country_guess():
    global lives, score
    while lives != 0 :
        result = random.choice(list(dict_from_csv.values()))
        print(result)
        answer = input("This is the capital of what country : ").lower()
        for key, value in dict_from_csv.items():
            if result == value:
                correct = key
        if answer == correct:
            print("You got it right!")
            score += 1
            time.sleep(2)
            cls()
        else:
            lives -= 1
            print(f"You got it wrong...\nThe correct answer is {correct}\nYou have {lives} remaining")
            time.sleep(2)
            cls()
    if lives == 0:
        print(f"You are out of lives, your score was {score}")


def intro():
    option = int(input("Press (1) for capital game mode\nPress (2) for country game mode\nOption:"))
    while option != 1 and option != 2: 
        option = int(input("Press (1) for capital game mode\nPress (2) for country game mode\nOption:"))   
    if option == 1:
        captial_guess()
    else:
        country_guess()

intro()
    
