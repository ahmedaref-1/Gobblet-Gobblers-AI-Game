

from typing import List
import random
import sys
import time
from State import State
from Action import MoveID

max_CurrSize = 0
min_OppSize = 4
PLAYER1 =1
PLAYER2 =2
level = "easy_level"
class ComputerPlayer():

    def __init__(self, level : str):
            self.level = level




    def alpha_beta_pruning(self, updated_depth, player, state: State, alpha, beta):
        if updated_depth == 0:      #Leaf node
            return self.heuristic(state)

        if player == PLAYER1:       #Maximizer
            for action in state.AllValidMoves():
                child_state = state.generate_successor(action)
                score = self.alpha_beta_pruning(updated_depth - 1, PLAYER2, child_state, alpha, beta)
            
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
                return alpha
            
        else:                       #Minimizer
            for action in state.AllValidMoves():
                child_state = state.generate_successor(action)
                score = self.alpha_beta_pruning(updated_depth - 1, PLAYER1, child_state, alpha, beta)
 
                beta = min(beta, score)
                if beta <= alpha:
                    break
                return beta


    def get_action(self, state: State) -> Action:
        if self.level == "EASY" :
                return random.choice(state.AllValidMoves())
        if self.level == "MEDIUM" :
                time_limit = 1000
        if self.level == "HARD" :
                time_limit = 3500
        
        actions_scores = []
        start_time = time.time()
        depth = 1

        while True:

            for action in state.AllValidMoves():
                child_state = state.generate_successor(action)
                score = self.alpha_beta_pruning(self.depth - 1, PLAYER2, child_state, alpha=-sys.maxsize, beta=sys.maxsize)
                actions_scores.append((action, score))

            depth += 1
            elapsed_time = time.time() - start_time

            if elapsed_time >= time_limit:
                break

        scores = [score for _, score in actions_scores]
        best_score = max(scores)
        best_actions = [action for action, score in actions_scores if score == best_score]
        return random.choice(best_actions)





def heuristic(state: State) -> int:
    # Check if the game is finished
    state.game.check_state()
    if state.game.GameState != "OnGoing":

        if state.game.winner == state.player_turn:
            return sys.maxsize  # Player has won
        else:
            return -sys.maxsize  # Opponent has won

    return evaluate_all_lines(state, state.game.CurrentPlayerIndex)


def evaluate_line(line: List[BoardItem], CurrentPlayerIndex: int):
    player=0
    count = 0
    max_size=0

    for index in line:
        # There is only one player in this line and it is the CurrentPlayer
        if  BoardItem(index).CurrentOwnerIndex==CurrentPlayerIndex and (player==0 or player==1):
            player = 1
            if (BoardItem(index).NumberOfGobbletsInStack != 0):
                count += 1
                max_size = max(max_size, BoardItem(index).OnTopGobbletSize)
                max_CurrSize = max(max_CurrSize, BoardItem(index).OnTopGobbletSize)
        
        # There is only one player in this line and it is the OpponentPlayer
        elif  BoardItem(index).CurrentOwnerIndex!=CurrentPlayerIndex and (player==0 or player==2):
            player = 2
            if (BoardItem(index).NumberOfGobbletsInStack != 0):
                count += 1
                max_size = max(max_size, BoardItem(index).OnTopGobbletSize)
                min_OppSize = min(min_OppSize, BoardItem(index).OnTopGobbletSize)

        # This line contains gobblets of both the CurrentPlayer and the OpponentPlayer
        else:
            player = 3
            # Update the max_CurrSize and the min_OppSize then break
            max_CurrSize = max(max_CurrSize, BoardItem(index).OnTopGobbletSize)
            min_OppSize = min(min_OppSize, BoardItem(index).OnTopGobbletSize)


    if player == 1:
        if count == 3:  # If there are 3 pieces in a line
            return max_size * 10  # Higher score for larger pieces
        if count == 2:
            return max_size * 5
        if count == 1:
            return max_size
        
    elif player == 2:
        if count == 3:  # If there are 3 pieces in a line
            return -(max_size * 10)  # Higher score for larger pieces
        if count == 2:
            return -(max_size * 5)
        if count == 1:
            return -max_size
    
    else:
        return 0  # No winning sequence in this line    


def evaluate_all_lines(state: State, CurrentPlayerIndex: int):
    total_score = 0

    for line in state.games.lines:
        total_score += evaluate_line(line, CurrentPlayerIndex)

    if max_CurrSize > min_OppSize:
        total_score += max_CurrSize*10

    return total_score


       