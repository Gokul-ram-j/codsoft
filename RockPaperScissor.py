import random
def choice_result(opt):
    if opt=="s":
        return "SCISSOR"
    elif opt=="p":
        return "PAPER"
    elif opt=="r":
        return "ROCK"
def result(player,computer):
    if player==computer:
        print("------------------MATCH IS DRAW------------------")
    elif(player>computer):
        print("-----------------CONGRATULATION YOU WON-----------------")
    else:
        print("-------------YOU LOSE , BETTER LUCK NEXT TIME-------------")

run=True
player_point=0
computer_point=0
valid_choice=["r","p","s"]
print("----------------------STONE PAPER SCISSOR----------------------")
print("------- |R for Rock|  && |P for Paper| && |S for scissor|-------")
print("-----------------------|0(zero) for EXIT|-----------------------")
while run:
    player_choice=input("enter your choice:").strip().lower()
    computer_choice=random.choice(valid_choice)
    if player_choice=="0":
        result(player_point,computer_point)
        print("     ---------------THANKS FOR PLAYING---------------     ")
        run=False
    elif player_choice not in valid_choice:
        print("        XXXXXXXXXX      invalid choice      XXXXXXXXXX        ")
    elif player_choice==computer_choice:
        print("                --->COMPUTER CHOICE:"+choice_result(computer_choice))
        print("-------------------------TIE-----------------------")
        print("----------------------PLAYER POINT:",player_point)
        print("----------------------COMPUTER POINT:",computer_point)
    elif ((player_choice=="r" and computer_choice=="s") or (player_choice=="p" and computer_choice=="r") or (player_choice=="s" and computer_choice=="p")):
        print("                     --->COMPUTER CHOICE:"+choice_result(computer_choice))
        player_point+=1
        print("------------------- PLAYER WIN ---------------------")
        print("----------------------PLAYER POINT:",player_point)
        print("----------------------COMPUTER POINT:",computer_point)

    else:
        print("                --->COMPUTER CHOICE:"+choice_result(computer_choice))
        computer_point+=1
        print("------------------- COMPUTER WIN ---------------------")
        print("----------------------COMPUTER POINT:",computer_point)
        print("----------------------PLAYER POINT:",player_point)
        
    print("\n"+"-"*100)