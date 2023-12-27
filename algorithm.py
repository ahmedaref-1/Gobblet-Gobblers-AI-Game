

from typing import List
import random
import sys
import time
from State import State
from Action import MoveID
import BoardItem
import Game
max_CurrSize = 0
min_OppSize = 4
PLAYER1 =1
PLAYER2 =2
class ComputerPlayer:

    def __init__(self, level : str):
            self.level = level





    def alpha_beta_pruning(self, updated_depth, player, state: State, alpha :int, beta :int) ->int:
        if updated_depth == 0:      #Leaf node
            return self.heuristic(state)

        if player == PLAYER1:       #Maximizer
            for action in state.all_valid_moves():
                child_state = state.generate_successor(action)
                score = self.alpha_beta_pruning(updated_depth - 1, PLAYER2, child_state, alpha, beta)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return alpha
            
        else:                       #Minimizer
            for action in state.all_valid_moves():
                child_state = state.generate_successor(action)
                score = self.alpha_beta_pruning(updated_depth - 1, PLAYER1, child_state, alpha, beta)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return beta


    def get_action(self, state: State) -> MoveID :
        if self.level == "EASY" :
                return random.choice(state.all_valid_moves())
        if self.level == "MEDIUM" :
                time_limit = 5
        if self.level == "HARD" :
                time_limit = 15
        
        actions_scores = []
        start_time = time.time()
        depth = 3

        while True:

            for action in state.all_valid_moves():
                child_state = state.generate_successor(action)
                score = self.alpha_beta_pruning(depth - 1, PLAYER2, child_state, alpha=-sys.maxsize, beta=sys.maxsize)
                actions_scores.append((action, score))

            depth += 1
            elapsed_time = time.time() - start_time

            if elapsed_time >= time_limit:
                break

        scores = [score for _, score in actions_scores]
        best_score = max(scores)
        best_actions = [action for action, score in actions_scores if score == best_score]
        return random.choice(best_actions)





    def heuristic(self , state: State) -> int:
        # Check if the game is finished
        state.game.check_state()
        if state.game.GameState != "OnGoing":

            if state.game.Winner == state.CurrentPlayerId:
                return sys.maxsize  # Player has won
            else:
                return -sys.maxsize  # Opponent has won

        return self.evaluate_all_lines(state, state.game.CurrentPlayerIndex)




    def evaluate_line(self , state: State, line: list[int], CurrentPlayerId: int) -> int:
        global max_CurrSize , min_OppSize
        player=0
        count = 0
        max_size=0
        for index in line:
            # There is only one player in this line and it is the CurrentPlayer
            if  state.game.BoardItemsArray[index].get_owner_index()==CurrentPlayerId and (player==0 or player==1):
                player = 1
                #if (state.game.BoardItemsArray[index].get_number_of_gobblets() != 0):
                count += 1
                max_size = max(max_size, state.game.BoardItemsArray[index].get_on_top_gobblet_size())
                max_CurrSize = max(max_CurrSize, state.game.BoardItemsArray[index].get_on_top_gobblet_size())
                
            # There is only one player in this line and it is the OpponentPlayer
            elif  state.game.BoardItemsArray[index].get_owner_index()!=CurrentPlayerId and (player==0 or player==2):
               if (state.game.BoardItemsArray[index].get_number_of_gobblets() != 0):
                    player = 2
                    count += 1
                    max_size = max(max_size,state.game.BoardItemsArray[index].get_on_top_gobblet_size())
                    min_OppSize = min(min_OppSize, state.game.BoardItemsArray[index].get_on_top_gobblet_size())

            # This line contains gobblets of both the CurrentPlayer and the OpponentPlayer
            else:
                player = 3
                # Update the max_CurrSize and the min_OppSize then break
                max_CurrSize = max(max_CurrSize, state.game.BoardItemsArray[index].get_on_top_gobblet_size())
                min_OppSize = min(min_OppSize, state.game.BoardItemsArray[index].get_on_top_gobblet_size())

        if player == 1:
            if count == 3:  # If there are 3 pieces in a line
                return max_size * 10  # Higher score for larger pieces
            elif count == 2:
                return max_size * 5
            elif count == 1:
                return max_size
            else:
                return 0
            
        elif player == 2:
            if count == 3:  # If there are 3 pieces in a line
                return -(max_size * 10)  # Higher score for larger pieces
            elif count == 2:
                return -(max_size * 5)
            elif count == 1:
                return -max_size
            else:
                return 0
        
        else:
            return 0  # No winning sequence in this line


    def evaluate_all_lines(self ,state: State, CurrentPlayerId: int):
        total_score = 0

        for line in state.game.lines:
            total_score += self.evaluate_line(state ,line, CurrentPlayerId)

        if max_CurrSize > min_OppSize:
            total_score +=  max_CurrSize*10

        return total_score

        