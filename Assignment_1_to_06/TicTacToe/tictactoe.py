def PrintBoard(xState, oState):
    # Each cell checks the corresponding index in xState and oState
    zero = 'X' if xState[0] else ('O' if oState[0] else '0')
    one = 'X' if xState[1] else ('O' if oState[1] else '1')
    two = 'X' if xState[2] else ('O' if oState[2] else '2')
    three = 'X' if xState[3] else ('O' if oState[3] else '3')
    four = 'X' if xState[4] else ('O' if oState[4] else '4')
    five = 'X' if xState[5] else ('O' if oState[5] else '5')
    six = 'X' if xState[6] else ('O' if oState[6] else '6')
    seven = 'X' if xState[7] else ('O' if oState[7] else '7')
    eight = 'X' if xState[8] else ('O' if oState[8] else '8')
    print(f" {zero} | {one} | {two} ")
    print("-----------")
    print(f" {three} | {four} | {five} ")
    print("-----------")
    print(f" {six} | {seven} | {eight} ")

def CheckWin(xState, oState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]]            # Diagonals
    for win in wins:
        # Check if X wins
        if xState[win[0]] and xState[win[1]] and xState[win[2]]:
            print("X Won the match!")
            return 1
        # Check if O wins
        if oState[win[0]] and oState[win[1]] and oState[win[2]]:
            print("O Won the match!")
            return 0
    return -1

if __name__ == "__main__":
    while True:
        # Initialize states with 9 zeros (0-8 positions)
        xState = [False] * 9
        oState = [False] * 9
        turn = 1  # 1 for X, 0 for O
        print("Welcome to Tic Tac Toe!")
        print("Player 1: X | Player 2: O")

        for move in range(9):  # Loop for a maximum of 9 moves
            PrintBoard(xState, oState)
            if turn == 1:
                print("Player X's turn")
                try:
                    pos = int(input("Enter position (0-8): "))
                    if not (0 <= pos <= 8):
                        print("Invalid input! Enter a number between 0-8.")
                        continue
                    if xState[pos] or oState[pos]:
                        print("Position already taken! Try again.")
                        continue
                    xState[pos] = True
                except ValueError:
                    print("Invalid input! Enter a number.")
                    continue
            else:
                print("Player O's turn")
                try:
                    pos = int(input("Enter position (0-8): "))
                    if not (0 <= pos <= 8):
                        print("Invalid input! Enter a number between 0-8.")
                        continue
                    if xState[pos] or oState[pos]:
                        print("Position already taken! Try again.")
                        continue
                    oState[pos] = True
                except ValueError:
                    print("Invalid input! Enter a number.")
                    continue

            # Check for win after each move
            cwin = CheckWin(xState, oState)
            if cwin != -1:
                PrintBoard(xState, oState)
                print(f"Match Over! {'X' if cwin == 1 else 'O'} won the match ✨✨😃😘!")
                break

            # Switch turns
            turn = 1 - turn
        else:
            PrintBoard(xState, oState)
            print("Match Draw 🤞💕🤷‍♀️!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'y':
            print("Thanks for playing 🎁👏!")
            break