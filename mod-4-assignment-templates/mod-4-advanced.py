def relationship_status(from_member, to_member, social_graph):
    fromFollow = social_graph[from_member]['following']
    toFollow = social_graph[to_member]['following']
    if from_member in toFollow and to_member in fromFollow:
        relationship = 'friends'
    elif from_member in toFollow:
        relationship = 'followed by'
    elif to_member in fromFollow:
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
    col_sums = np.sum(board, axis=1)

    #Horizontal check
    for col_sum in col_sums:
        if col_sum == SIZE:
            return "X"
        elif col_sum == -SIZE:
            return "O"

    #Vertical check
    row_sums = np.sum(board, axis=0)
    for row_sum in row_sums:
        if row_sum == SIZE:
            return "X"
        elif row_sum == -SIZE:
            return "O"

    #Diagonal check
    primary_diag_sum = 0  # going down to the right diagonal
    for i in range(SIZE):
        primary_diag_sum += board[i][i]
    if primary_diag_sum == SIZE:
        return "X"
    elif primary_diag_sum == -SIZE:
        return "O"

    #Inverse diagonal check
    secondary_diag_sum = 0
    for i in range(SIZE):
        secondary_diag_sum += board[i, (SIZE - 1) - i]
    if secondary_diag_sum == SIZE:
        return "X"
    elif secondary_diag_sum == -SIZE:
        return "O"
    else:
        return "No Winner"

def eta(first_stop, second_stop, route_map):
    parameters = (first_stop, second_stop)
    travelTime = 0

    for i in route_map:
        if parameters == i:
            travelTime += route_map[i]['travel_time_mins']
            break

    return (travelTime)
