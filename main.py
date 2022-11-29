from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(compare):
    compare_name = compare["name"]
    compare_desc = compare["description"]
    compare_country = compare["country"]
    return(f"{compare_name}, a {compare_desc}, from {compare_country}")

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else: 
        return guess == "b"

print (logo)
score = 0
game_contniue = True
compare2 = random.choice(data)

while game_contniue:
    compare1 = compare2
    compare2 = random.choice(data)
    if compare1 == compare2:
        compare2 = random.choice(data)

    print(f"Compare A: {format_data(compare1)}")
    print (vs)
    print(f"Compare B: {format_data(compare2)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers_count = compare1["follower_count"]
    b_followers_count = compare2["follower_count"]
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    clear()
    print(logo)
    
    if is_correct:
        score +=1
        print(f"You're Right!  Your current score is: {score}")
    else:
        game_contniue = False
        print(f"Sorry, you got it wrong.  Your final score is {score}")