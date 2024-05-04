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
