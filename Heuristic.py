from typing import List
import State
import sys

def heuristic(state: State) -> int:
    # Check if the game is finished
    if state.game.GameState != "OnGoing"

    if state.game.winner == state.player_turn:
            return sys.maxsize  # Player has won
        else:
            return -sys.maxsize  # Opponent has won

    # Evaluate based on the current state
    player_id = state.player_turn
    opponent_id = 0 if player_id == 1  else 1

    player_score = 0
    opponent_score = 0

        # Check if the line has the potential for a winning sequence for the player
        player_score += evaluate_all_lines(state, player_id)

        # Check if the line has the potential for a winning sequence for the opponent
        opponent_score += evaluate_all_lines(state, opponent_id)

    # Combine scores 
    final_score = player_score - opponent_score

    return final_score

def evaluate_line(line: List[BoardItem], CurrentPlayerIndex: int):

    count = 0
    max_size = 0

    for index in line:
        if (BoardItem(index).NumberOfGobbletsInStack != 0) and BoardItem(index).CurrentOwnerIndex==CurrentPlayerIndex:
            count += 1
            max_size = max(max_size, BoardItem(index).OnTopGobbletSize)

    if count = 3:  # If there are 3 pieces in a line
        return max_size * 10  # Higher score for larger pieces
   if count = 2 
        return max_size * 5
   if count = 1
        return max_size
    else:
        return 0  # No winning sequence in this line    

def evaluate_all_lines(state: State, CurrentPlayerIndex: int):
    total_score = 0

    for line in state.games.lines:
        total_score += evaluate_line(line, CurrentPlayerIndex)

    return total_score
