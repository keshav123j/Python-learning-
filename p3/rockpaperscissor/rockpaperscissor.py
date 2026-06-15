#We are designing rock paper scissor
import random
a = input("CHOOSE BETWEEN ROCK PAPER SCISSOR : rock, paper ,scissor - ")
computer = random.choice(["rock","paper","scissor"])
if(a==computer):
    print("Tie")
elif(a=="paper" and computer=="rock"):
    print("You win - computer chose rock , rock captured")
elif(a=="paper" and computer=="scissor"):
    print("You lose - computer chose scissor, scissor cut paper")
elif(a=="rock" and computer=="paper"):
    print("You lose computer chose paper ")
elif(a=="rock" and computer=="scissor"):
    print("You win - computer chose scissor")
elif(a=="scissor"and computer=="rock"):
    print("You lose - computer chose rock")
elif(a=="scissor"and computer=="paper"):
    print("You win - computer chose paper")
else:
    print("Choose between rock , paper, scissor")