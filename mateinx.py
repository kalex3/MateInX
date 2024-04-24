#!/usr/bin/env python3
import chess

strategy={}

def solve(board,player,d=0,depth=5):
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

board = chess.Board(input())
player=int(input())
depth=int(input())
if not board.is_valid():
    raise ValueError("Invalid position")
print(solve(board,player,0,depth))
# for key,value in strategy.items():
#     print(f"{key} : {value}")
