"""
TicTacToe Oyuncusu
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Oyun tahtasının başlangıç durumunu döndürür.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Tahtada bir sonraki sıraya sahip olan oyuncuyu döndürür.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O

def actions(board):
    """
    Tahtada mevcut olan tüm olası eylemlerin (i, j) kümesini döndürür.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    """
    Tahta üzerinde (i, j) hamlesini yaptıktan sonra ortaya çıkan tahtayı döndürür.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError("Geçersiz hamle!")
    
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Eğer varsa, oyunun galibini döndürür.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

def terminal(board):
    """
    Oyun bittiyse True, bitmediyse False döndürür.
    """
    return winner(board) is not None or not any(EMPTY in row for row in board)

def utility(board):
    """
    X oyunu kazandıysa 1, O kazandıysa -1, aksi takdirde 0 döndürür.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0

def minimax(board):
    """
    Tahtadaki mevcut oyuncu için en uygun eylemi döndürür.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        best_value = float('-inf')
        best_move = None
        for action in actions(board):
            value = minimax_value(result(board, action), False)
            if value > best_value:
                best_value = value
                best_move = action
    else:
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            value = minimax_value(result(board, action), True)
            if value < best_value:
                best_value = value
                best_move = action
    
    return best_move

def minimax_value(board, is_maximizing):
    if terminal(board):
        return utility(board)
    
    if is_maximizing:
        value = float('-inf')
        for action in actions(board):
            value = max(value, minimax_value(result(board, action), False))
    else:
        value = float('inf')
        for action in actions(board):
            value = min(value, minimax_value(result(board, action), True))
    
    return value
