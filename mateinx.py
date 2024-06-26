#!/usr/bin/env python3
import argparse,chess

parser=argparse.ArgumentParser(description='Chess puzzle solver',formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('position',nargs='?',type=str,help='Chess position given in FEN notation\n(if omitted, the program reads it from stdin)')
parser.add_argument('-p','--player',choices=['w','white','b','black','i','input'],help="Player to win (defaults to the player on turn)\n(if 'input' is given, the program reads it from second line of stdin)",default='d')
parser.add_argument('-d','--depth',type=int,help="Search depth (defaults to 5)", default=5)
args = parser.parse_args()

strategy = {}

def solve(board,player,d,depth):
    if board.is_checkmate() and board.outcome().winner==player:
        return 1
    if d>=depth:
        return 0
    if board.turn==player:
        for move in board.legal_moves:
            board.push(move)
            b=solve(board,player,d+1,depth)
            board.pop()
            if b:
                strategy[board.fen()]=move
                return 1
        return 0
    else:
        for move in board.legal_moves:
            board.push(move)
            b=solve(board,player,d+1,depth)
            board.pop()
            if not b:
                return 0
        return 1

board = chess.Board(input() if args.position is None else args.position)
if not board.is_valid():
    raise ValueError("Invalid position")
player = {'w':1,'b':0}.get(input()[:1].lower() if args.player[0]=='i' else args.player[0], board.turn)

for i in range(1,args.depth+1):
    strategy={}
    if solve(board,player,0,i):
        print(f"{['Black','White'][player]} has mate in {i}")
        print(f"{['Black','White'][player]}'s winning strategy:")
        original=board.copy()
        while True:
            print(board)
            while not board.is_checkmate():
                if board.turn==player:
                    print(f"{['Black','White'][player]}'s move: {board.san(strategy[board.fen()])}")
                    board.push(strategy[board.fen()])
                else:
                    if board.legal_moves.count()>1:
                        print([board.san(move) for move in board.legal_moves])
                        board.push_san(input(f"Enter {['black','white'][player^1]}'s move: "))
                    else:
                        move=list(board.legal_moves)[0]
                        print(f"{['Black','White'][player^1]}'s move: {board.san(move)} (the only legal move)")
                        board.push(move)
                print(board)
            board=original.copy()
            if input("Exit? (y/n) ")[:1].lower()=='n':
                continue
            else:
                break
        break
else:
    print(f"{['Black','White'][player]} doesn't have mate in {i}")
