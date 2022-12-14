# tic-tac-toe

## About tic-tac-toe

tic-tac-toe is a tiny, simple, interactive command-line based project.

*Date of creaton:* `September 10, 2019`

## Game modes

The game can be played in single-player mode and double-player mode.

The double-player mode is simple - two players get their turns one by one, and the first one to complete a Row, Column, or Diagonal to be all Naughts/Crosses wins. In the single-player mode, however, the computer plays tic-tac-toe with you, in three increasing levels of difficulty (and intelligence):
- The simple level, where it decides its moves randomly
- The medium level, where it is able to defend itself from your offensive moves
- The difficult level, where it plays **both** offensively and defensively

## Where the 'intelligence' lies

This is where (and how) the magic happens. These simple functions enable the computer to enhance its decision-making strategy. Well, almost. These are just functions XD.

```
function level_2():
    for each possible i:
        if (two boxes of ROW[i] OR COLUMN[i] OR DIAGONAL[i] == naught):
            turn = empty_box
            
    if (is_available(turn)):
        make_turn(turn)


function level_3():
    level_2()
    for each possible i:
        if (two boxes of ROW[i] OR COLUMN[i] OR DIAGONAL[i] == cross):
             turn = empty_box
    
    if (is_available(turn)):
        make_turn(turn)
```

## Footnotes

In single-player mode, the Player, and in double-player mode, Player-1, **always**:
- Gets the first turn
- Plays as 'Naughts'

## Run

To play, clone the repository on your device, navigate to the folder, and execute:

```
python3 main.py
```
