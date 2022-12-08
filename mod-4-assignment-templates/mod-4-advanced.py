def relationship_status(from_member, to_member, social_graph):
    x = social_graph[from_member]['following']
    y = social_graph[to_member]['following']
    if from_member in y and to_member in x:
        relationship = 'friends'
    elif from_member in y:
        relationship = 'followed by'
    elif to_member in x:
        relationship = 'follower'
    else:
        relationship = 'no relationship'
    return (str(relationship))


import numpy as np
def tic_tac_toe(board):
    SIZE = len(board)

    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == "X":
                board[i][j] = 1
            elif board[i][j] == "O":
                board[i][j] = -1
            else:
                board[i][j] = 0

    board = np.array(board)
    cs = np.sum(board, axis=1)

    #Horizontal check
    for col_sum in cs:
        if col_sum == SIZE:
            return "X"
        elif col_sum == -SIZE:
            return "O"

    #Vertical check
    rs = np.sum(board, axis=0)
    for row_sum in rs:
        if row_sum == SIZE:
            return "X"
        elif row_sum == -SIZE:
            return "O"

    #Diagonal check
    pds = 0  # going down to the right diagonal
    for i in range(SIZE):
        pds += board[i][i]
    if pds == SIZE:
        return "X"
    elif pds == -SIZE:
        return "O"

    #Inverse diagonal check
    sds = 0
    for i in range(SIZE):
        sds += board[i, (SIZE - 1) - i]
    if sds == SIZE:
        return "X"
    elif sds == -SIZE:
        return "O"
    else:
        return "No Winner"

def eta(first_stop, second_stop, route_map):
    par = (first_stop, second_stop)
    tt = 0

    for i in route_map:
        if par == i:
            tt += route_map[i]['travel_time_mins']
            break

    return (tt)
