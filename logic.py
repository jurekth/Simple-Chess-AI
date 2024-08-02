from enum import Enum

import numpy

class Pieces(Enum):
    W_KING = 1
    W_QUEEN = 2
    W_ROOK = 3
    W_BISHOP = 4
    W_KNIGHT = 5
    W_PAWN = 6

    B_KING = 10
    B_QUEEN = 11
    B_ROOK = 12
    B_BISHOP = 13
    B_KNIGHT = 14
    B_PAWN = 15


def initial_state():

    return [
        [Pieces.B_ROOK, Pieces.B_KNIGHT, Pieces.B_BISHOP, Pieces.B_QUEEN, Pieces.B_KING, Pieces.B_BISHOP, Pieces.B_KNIGHT, Pieces.B_ROOK],
        [Pieces.B_PAWN, Pieces.B_PAWN, Pieces.B_PAWN, Pieces.B_PAWN, Pieces.B_PAWN, Pieces.B_PAWN, Pieces.B_PAWN, Pieces.B_PAWN],
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [Pieces.W_PAWN, Pieces.W_PAWN, Pieces.W_PAWN, Pieces.W_PAWN, Pieces.W_PAWN, Pieces.W_PAWN, Pieces.W_PAWN, Pieces.W_PAWN],
        [Pieces.W_ROOK, Pieces.W_KNIGHT, Pieces.W_BISHOP, Pieces.W_QUEEN, Pieces.W_KING, Pieces.W_BISHOP, Pieces.W_KNIGHT, Pieces.W_ROOK],
    ]

def utility(state):
    pass

def actions(state):
    pass

def result(state, action):
    pass

def terminal(state):
    pass

def minimax():
    pass

def min_value():
    pass

def max_value():
    pass
