
import random as rp

game_components = ['s', 'w', 'g']

bot_input = rp.choice(game_components)

no_of_chances = 9
Bot_points = 0
player_points = 0
chances = 0

print("Hello!!!Welcome to Snake-Water-Gun Game")
print("You will be playing against bot./nTotal there are 9 chances given./nWhoever will be gaining highest points will be the final winner./n")
print("Press : s for Snake, w for Water, g for Gun")

while chances < no_of_chances:
    user_input = input("Enter your choice")

    # if 's' is selected
    if user_input == 's' and bot_input == 'w':
        print(f"you choose: {user_input} and bot choose: {bot_input}")
        print("Congo!!!!You are a  winner in this round and wins one point")
        player_points += 1

    elif user_input == 's' and bot_input == 'g':
        print(f"You choose: {user_input} and bot choose: {bot_input}")
        print("Bot is a winner in this round and wins one point")
        Bot_points += 1

    # if 'w' is selected
    elif user_input == 'w' and bot_input == 's':
        print(f"You choose: {user_input} and Bot choose: {bot_input}")
        print("Bot is a winner in this round and wins one point")
        Bot_points += 1

    elif user_input == 'w' and bot_input == 'g':
        print(f"You choose: {user_input} and Bot choose: {bot_input}")
        print("Congo!!!!You are a winner in this round and wins one point")
        player_points += 1

     # if g is selected
    elif user_input == 'g' and bot_input == 's':
        print(f"You choose: {user_input} and Bot choose: {bot_input}")
        print("Congo!!!!You are a winner in this round and wins one point")
        player_points += 1

    elif user_input == 'g' and bot_input == 'w':
        print(f"You choose: {user_input} and Bot choose: {bot_input}")
        print("Bot is a winner in this round and wins one point ")
        Bot_points += 1

    elif user_input == bot_input:
        print(f"You choose: {user_input} and Bot choose: {bot_input}")
        print("Both choosed same option so Tie in this round and 0 point to both of them")

    else:
        print("Wrong input!!!")

    # chances is calculated
    chances += 1
    print(f"{no_of_chances - chances} chances are remaining")
    print()

print("GAME OVER")
print(f"Bot got {Bot_points} points and you got {player_points} points")

if Bot_points > player_points:
    print("Bot is a WINNER in this game")
else:
    print("CONGRATULATIONS!!!You're the Winner of this game")















