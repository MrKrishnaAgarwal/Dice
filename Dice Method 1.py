import random


def rolldice(min,max):
    while True:
            print("Rolling Dice....")
            print(f"Your Number : {random.randint(min,max)}")
            choice=input("Do you want to Roll Dice Again? (Yes/No)")
            if choice.lower()=='n':
                    break



rolldice(1,6)
