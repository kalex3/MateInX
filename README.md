# Mate In X
Chess puzzle solver

## Installation
```
$ git clone https://github.com/kalex3/MateInX
$ cd MateInX
$ pip install -r requirements.txt
```

## Usage
```
$ ./mateinx.py -h
usage: mateinx.py [-h] [-p {w,white,b,black,i,input}] [-d DEPTH] [position]

Chess puzzle solver

positional arguments:
  position              Chess position given in FEN notation
                        (if omitted, the program reads it from stdin)

options:
  -h, --help            show this help message and exit
  -p {w,white,b,black,i,input}, --player {w,white,b,black,i,input}
                        Player to win (defaults to the player on turn)
                        (if 'input' is given, the program reads it from second line of stdin)
  -d DEPTH, --depth DEPTH
                        Search depth (defaults to 5)
```
To get the [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) of a chess position, you can use the [Lichess board editor](https://lichess.org/editor).

## Example
![fen](https://github.com/kalex3/MateInX/assets/31569459/41ddfba1-72f2-405c-b139-f1d166f93cb0)

```
$ ./mateinx.py -d 7 "5rk1/2p4p/1p1p4/p2Pp3/P1P3rq/1P1Q2pP/4RbP1/5R1K b - - 0 1"
Black has mate in 7
Black's winning strategy:
. . . . . r k .
. . p . . . . p
. p . p . . . .
p . . P p . . .
P . P . . . r q
. P . Q . . p P
. . . . R b P .
. . . . . R . K
Black's move: Qxh3+
. . . . . r k .
. . p . . . . p
. p . p . . . .
p . . P p . . .
P . P . . . r .
. P . Q . . p q
. . . . R b P .
. . . . . R . K
White's move: gxh3 (the only legal move)
. . . . . r k .
. . p . . . . p
. p . p . . . .
p . . P p . . .
P . P . . . r .
. P . Q . . p P
. . . . R b . .
. . . . . R . K
Black's move: g2+
. . . . . r k .
. . p . . . . p
. p . p . . . .
p . . P p . . .
P . P . . . r .
. P . Q . . . P
. . . . R b p .
. . . . . R . K
White's move: Kh2 (the only legal move)
. . . . . r k .
. . p . . . . p
. p . p . . . .
p . . P p . . .
P . P . . . r .
. P . Q . . . P
. . . . R b p K
. . . . . R . .
Black's move: gxf1=N+
. . . . . r k .
. . p . . . . p
. p . p . . . .
p . . P p . . .
P . P . . . r .
. P . Q . . . P
. . . . R b . K
. . . . . n . .
White's move: Kh1 (the only legal move)
. . . . . r k .
. . p . . . . p
. p . p . . . .
p . . P p . . .
P . P . . . r .
. P . Q . . . P
. . . . R b . .
. . . . . n . K
Black's move: Rg1#
. . . . . r k .
. . p . . . . p
. p . p . . . .
p . . P p . . .
P . P . . . . .
. P . Q . . . P
. . . . R b . .
. . . . . n r K
Exit? (y/n) y
```
