def check(player):
    if player.lower() == 'p' or player.lower() == 'r' or player.lower() == 's':
        return True
    else:
        return False
def rockPaperScissor(player1,player2):
    if player1.lower() == 'p':
        if player2.lower() == 'p':
            result = 'n'
        elif player2.lower() == 's':
            result = '2'
        else:
            result = '1'
    if player1.lower() == 's':
        if player2.lower() == 'p':
            result = '1'
        elif player2.lower() == 's':
            result = 'n'
        else:
            result = '2'
    if player1.lower() == 'r':
        if player2.lower() == 'p':
            result = '2'
        elif player2.lower() == 's':
            result = '1'
        else:
            result = 'n'
    return result
def main():
    roundcount = 0
    last = []
    while roundcount < 3:
        roundcount += 1
        print('Round # ',roundcount)
        player1 = input("Player 1's Choice: ")
        while check(player1) == False:
            player1 = input("Player 1's Choice: ")
        player2 = input("Player 2's Choice: ")
        while check(player2) == False:
            player2 = input("Player 2's Choice: ")
        result = rockPaperScissor(player1,player2)
        last.append(result)
        if result == '1':
            print("Player 1 wins this round")
        elif result == '2':
            print('Player 2 wins this round')
        else:
            print('No one wins this round')
    print('\n')
    if last[0] == '1':
        if '1' in last[1:]:
            print("Player 1 wins the game")
        elif 'n' in last[1:]:
            if '2' in last[1:]:
                print('No one wins the game')
            else:
                print("Player 1 wins the game")
        else:
            print("Player 2 wins the game")
    elif last[0] == '2':
        if '2' in last[1:]:
            print("Player 2 wins the game")
        elif 'n' in last[1:]:
            if '1' in last[1:]:
                print('No one wins the game')
            else:
                print("Player 2 wins the game")
        else:
            print("Player 1 wins the game")
    elif last[0] == 'n':
        if '1' in last[1:]:
            if '2' in last[1:]:
                print("No one wins the game")
            else:
                print("Player 1 wins the game")
        elif '2' in last[1:]:
            if '1' in last[1:]:
                print('No one wins the game')
            else:
                print("Player 2 wins the game")
        else:
            print("No one wins the game")
if __name__ == '__main__':
    main()
