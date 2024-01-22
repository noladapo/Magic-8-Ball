# Magic 8-Ball
# Nike Oladapo
# 1/22/2023

#  Initialize 
import random 

# Function
response = ["yes", "no", "definitely", "perhaps", "only time will tell", "the future is unclear", "without a doubt", "absolutely not", "very doubtful", "ask again later", "of course!", "outlook not so good"]

# game() function prints th opening statement and starts the magic_eightball simulation
def game():
    print("Welcome to Magic 8-Ball! In this program, you will be prompted to ask a yes or no question, and the 8-ball will give you a response!")
    magic_eightball()

# magic_eightball prompts the user to ask a yes or no question, and they will be given a response
def magic_eightball():
    while True:  
        question = input("What is your question?")
        if question.endswith("?"):
            print(random.choice(response))
            ans = input("Would you like to ask another question? y/n")
            if ans == "n" or "no" or "No" or "N" :
                break
        else: 
            print("Try again! Question must end in a question mark.")


# main 
game()
