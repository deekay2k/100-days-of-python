print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road, Which way to go?")

# 1. Choice1 = Left or Right
choice1 = input('\tType "left" or "right"\n')
print("You chose " + choice1)
if choice1.lower() == "left":

# 2. Choice2 = Swim or Wait
    print("You've come to a lake.  "
          "There is an island in the middle of a lake.")
    choice2 = input('\tType "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n')
    print("You chose " + choice2)
    if choice2.lower() == "wait":
        print("You arrive at the island unharmed. "
              "There is a house with 3 doors.")
        choice3 = input("\tOne red, one yellow and one blue. "
                        "Which colour do you choose?\n")
# 3. Choice3 = Door
        print("You chose " + choice3)
        if choice3.lower() == "yellow":
            print("You found the treasure! You Win!")
        elif choice3.lower() == "red":
            print("It's a room full of fire. Game Over.")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout, Game Over!")
else:
    print("You fell into a hole.  Game Over!")
