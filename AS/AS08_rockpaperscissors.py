import random
while True:
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    user = input("rock, paper, scissors, SHOOT!:")
    print(computer)
    if user == computer:
        continue
    elif computer == "rock" and user == "paper":
        print("computer wins")
        break
    elif computer == "paper" and user == "rock":
        print("computer wins")
        break
    elif computer == "scissors" and user == "paper":
        print("computer wins")
        break
        ##########
    elif user == "rock" and computer == "paper":
        print("user wins")
        break
    elif user == "paper" and computer == "rock":
        print("user wins")
        break
    elif user == "scissors" and computer == "paper":
        print("user wins")
        break
