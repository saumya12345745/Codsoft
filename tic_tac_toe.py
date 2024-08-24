import random 
computer=["rock","paper","sicer"]

user_point=0
computer_point=0

print("Are you ready to play the rock , paper or sicer game")

for n in range(3):
    user=input("enter your choise:")
    computer_choice = random.choice(computer)
    print(f"computer choice: is: {computer_choice}")
    if user=="rock" and computer_choice=="sicer":
        user_point += 1
        print("user wins")
    elif (user=="sicer" and computer_choice=="paper"):
        user_point += 1
        print ("user wins")
    elif (user=="paper" and computer_choice=="rock"):
        user_point += 1
        print("user wins")
    elif (user==computer_choice):
        print("tie") 
    else:
        computer_point +=1 
        print("computer wins")


if user_point > computer_point:
    print("You win the game")
      
elif user_point == computer_point:
    print("Match Tie!")
else:
    print("Beta Computer se nhi jeet payga 😁😁")