from random import choice, random
from time import sleep


def game_set():
    """sets up game constants"""

    global AVAILABLE, box, cross, naught, again, count, rows, r1, r2, r3

    box, naught, cross = "▢", "🄾", "🅇"
    count, again = 0, 1

    r1, r2, r3 = [box, box, box], [box, box, box], [box, box, box]
    rows = [r1, r2, r3]

    # initialize a list of available moves, i.e. all boxes available for a turn
    AVAILABLE = list(range(1, 10))


def winning_con():
    """game will end as soon as any of the listed conditions becomes True,
    i.e. a DIAGONAL, ROW or COLUMN is filled with all Naughts or all Crosses"""

    global diagonal_win, row_win, column_win

    # check both DIAGONALS
    diagonal_win = (
        (r1[0] == r2[1] == r3[2] != box) or    # DIAGONAL 1
        (r1[2] == r2[1] == r3[0] != box)       # DIAGONAL 2
    )

    # check all ROWS
    row_win = (
        (r1[0] == r1[1] == r1[2] != box) or    # ROW 1
        (r2[0] == r2[1] == r2[2] != box) or    # ROW 2
        (r3[0] == r3[1] == r3[2] != box)       # ROW 3
    )

    # check all COLUMNS
    column_win = (
        (r1[0] == r2[0] == r3[0] != box) or    # COLUMN 1
        (r1[1] == r2[1] == r3[1] != box) or    # COLUMN 2
        (r1[2] == r2[2] == r3[2] != box)       # COLUMN 3
    )


def display():
    """display the GRID row-wise"""

    for row in rows:
        for element in row:
            print(element, end="")
        print()


def tie():
    """if a round ends in a tie, ask Player to Re-play"""

    print("\nTHIS MATCH WAS A TIE \nWant to Play Again?")
    print("\nEnter 1. for YES \nEnter 2. for NO")

    while True:
        again = int(input("\nEnter your choice \n>>> "))
        if again == 1:
            # resetting the Game
            game_set()
            display()
        if again in {1, 2}:
            break
        else:
            print("\nPlease enter 1 or 2")


def smart_turn1():
    """Difficulty Level: 2 - Computer will counter the moves of the Player
    if two boxes in a DIAGONAL, ROW or COLUMN are Naughts, then counter by
    occupying the third box by a Cross"""

    global temp_turn, turn2

    temp_turn = 0

    if ((r1[1] == r1[2] == naught) or
        (r2[0] == r3[0] == naught) or
        (r2[1] == r3[2] == naught)) and r1[0] == box:
            temp_turn = 1

    if ((r1[0] == r1[2] == naught) or
        (r2[1] == r3[1] == naught)) and r1[1] == box:
            temp_turn = 2

    if ((r1[0] == r1[1] == naught) or
        (r2[2] == r3[2] == naught) or
        (r2[1] == r3[0] == naught)) and r1[2] == box:
            temp_turn = 3

    if ((r2[1] == r2[2] == naught) or
        (r1[0] == r3[0] == naught)) and r2[0] == box:
            temp_turn = 4

    if ((r2[0] == r2[2] == naught) or
        (r1[1] == r3[1] == naught) or
        (r1[0] == r3[2] == naught) or
        (r1[2] == r3[0] == naught)) and r2[1] == box:
            temp_turn = 5

    if ((r2[0] == r2[1] == naught) or
        (r1[2] == r3[2] == naught)) and r2[2] == box:
            temp_turn = 6

    if ((r3[1] == r3[2] == naught) or
        (r1[0] == r2[0] == naught) or
        (r1[2] == r2[1] == naught)) and r3[0] == box:
            temp_turn = 7

    if ((r3[0] == r3[2] == naught) or
        (r1[1] == r2[1] == naught)) and r3[1] == box:
            temp_turn = 8

    if ((r3[0] == r3[1] == naught) or
        (r1[2] == r2[2] == naught) or
        (r1[0] == r2[1] == naught)) and r3[2] == box:
            temp_turn = 9

    # if the box is empty, make the move
    if temp_turn in AVAILABLE:
        turn2 = temp_turn


def smart_turn2():
    """Difficulty Level: 3 - Computer will attempt to win
    if two boxes in a DIAGONAL, ROW or COLUMN are Crosses, then attempt
    to occupy the third by a Cross if that box is Empty"""

    global temp_turn, turn2

    if ((r1[1] == r1[2] == cross) or
        (r2[0] == r3[0] == cross) or
        (r2[1] == r3[2] == cross)) and r1[0] == box:
            temp_turn = 1

    if ((r1[0] == r1[2] == cross) or
        (r2[1] == r3[1] == cross)) and r1[1] == box:
            temp_turn = 2

    if ((r1[0] == r1[1] == cross) or
        (r2[2] == r3[2] == cross) or
        (r2[1] == r3[0] == cross)) and r1[2] == box:
            temp_turn = 3

    if ((r2[1] == r2[2] == cross) or
        (r1[0] == r3[0] == cross)) and r2[0] == box:
            temp_turn = 4

    if ((r2[0] == r2[2] == cross) or
        (r1[1] == r3[1] == cross) or
        (r1[0] == r3[2] == cross) or
        (r1[2] == r3[0] == cross)) and r2[1] == box:
            temp_turn = 5

    if ((r2[0] == r2[1] == cross) or
        (r1[2] == r3[2] == cross)) and r2[2] == box:
            temp_turn = 6

    if ((r3[1] == r3[2] == cross) or
        (r1[0] == r2[0] == cross) or
        (r1[2] == r2[1] == cross)) and r3[0] == box:
            temp_turn = 7

    if ((r3[0] == r3[2] == cross) or
        (r1[1] == r2[1] == cross)) and r3[1] == box:
            temp_turn = 8

    if ((r3[0] == r3[1] == cross) or
        (r1[2] == r2[2] == cross) or
        (r1[0] == r2[1] == cross)) and r3[2] == box:
            temp_turn = 9

    # try to make first move at the centre to maximise chances of winning
    if count == 1:
        temp_turn = 5

    # if the box is empty, make the move
    if temp_turn in AVAILABLE:
        turn2 = temp_turn


def main():
    """__main__ function"""

    print("Welcome to TIC-TAC-TOE \n")
    print("Press 1. for Single Player \nPress 2. for Double Player \n")

    while True:
        ch = int(input("Enter your choice\n>>> "))
        if ch in {1, 2}:
            game_set()
            break
        else:
            print("\nPlease enter 1 or 2\n")

    # SINGLE PLAYER: choose difficulty level
    if ch == 1:
        levels = ["EASY", "BASIC", "ADVANCED"]

        print("\nChoose a Difficulty Level:")
        [print(f"Press {i+1}. for {levels[i]}") for i in range(3)]

        while True:
            level = int(input("\nEnter your choice \n>>> "))
            if level == 1:
                text = "\nI'm actually Easy to defeat!"
            elif level == 2:
                text = "\nRemember that I can counter your moves!"
            else:
                text = "\nI play like a Human! Underestimation not allowed!"

            if level in {1, 2, 3}:
                print(text)
                break
            else:
                print("\nPlease enter 1, 2 or 3")

    else:
        print("\nPlease Enter Your Names!")
        P1 = input("PLAYER 1: ").title()
        P2 = input("PLAYER 2: ").title()

    print("\nTHE GRID IS FORMATTED as: \n①②③ \n④⑤⑥ \n⑦⑧⑨ \n")
    display()

    # START THE GAME
    while True:
        if ch == 1:

            # if the Player wants to quit after tie
            if again == 2:
                break

            # Player's turn
            while True:
                turn1 = int(input(
                    "\nEnter the number of box you want to fill \n>>> "
                ))
                try:
                    AVAILABLE.remove(turn1)
                    print()
                    break
                except ValueError:
                    print("Please enter a number from", AVAILABLE)

            # update the Grid
            if turn1 in {1, 2, 3}:
                r1[turn1-1] = naught
            elif turn1 in {4, 5, 6}:
                r2[turn1-4] = naught
            else:
                r3[turn1-7] = naught

            display()
            count += 1

            # check for Winning Condition
            winning_con()
            if any({diagonal_win, row_win, column_win}):
                # Player wins
                print("\nYOU HAVE WON!!")
                break

            elif count > 8:
                # after 8 turns, game is tied
                tie()

            else:
                # Computer's turn
                print("\nMY TURN")
                turn2 = choice(AVAILABLE)

                # optimize Computer's move according to the level chosen by Player
                if level in (2, 3):
                    smart_turn1()
                    if level == 3:
                        smart_turn2()

                # update the Grid
                if turn2 in {1, 2, 3}:
                    r1[turn2-1] = cross
                elif turn2 in {4, 5, 6}:
                    r2[turn2-4] = cross
                else:
                    r3[turn2-7] = cross

                AVAILABLE.remove(turn2)

                # wait before making the move
                if count != 8:
                    sleep(random())

                display()
                count += 1

                # check for Winning Condition
                winning_con()
                if any({diagonal_win, row_win, column_win}):
                    # Computer wins
                    print("\nHAHA SORRY! I WON!!")
                    break

        else:
            # if the Player wants to quit after tie
            if again == 2:
                break

            # turn of Player 1
            while True:
                turn1 = int(input(
                    f"\n{P1}, Enter the number of box you want to fill \n>>> "
                ))
                try:
                    AVAILABLE.remove(turn1)
                    print()
                    break
                except ValueError:
                    print("Please enter a number from", AVAILABLE)

            # update the Grid
            if turn1 in {1, 2, 3}:
                r1[turn1-1] = naught
            elif turn1 in {4, 5, 6}:
                r2[turn1-4] = naught
            else:
                r3[turn1-7] = naught

            display()
            count += 1

            # check for Winning Conditon
            winning_con()
            if any({diagonal_win, row_win, column_win}):
                # Player 1 wins
                print(f"\n{P1} HAS WON!!")
                break

            elif count > 8:
                # after 8 turns, game is tied
                tie()

            else:
                # turn of Player 2
                while True:
                    turn2 = int(input(
                        f"\n{P2}, Enter the number of box you want to fill \n>>> "
                    ))
                    try:
                        AVAILABLE.remove(turn2)
                        print()
                        break
                    except ValueError:
                        print("Please enter a number from", AVAILABLE)

                # update the Grid
                if turn2 in {1, 2, 3}:
                    r1[turn2-1] = cross
                elif turn2 in {4, 5, 6}:
                    r2[turn2-4] = cross
                else:
                    r3[turn2-7] = cross

                display()
                count += 1

                # check for Winning Condition
                winning_con()
                if any({diagonal_win, row_win, column_win}):
                    # Player 2 Wins
                    print(f"\n{P2} HAS WON!!")
                    break

    # Game ends on Exiting, Losing or Winning
    print("THANK YOU FOR PLAYING!")


if __name__ == "__main__":
    main()