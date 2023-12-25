

import random
import sys
#import State
#import Action

PLAYER1 =1
PLAYER2 =2
level = "easy_level"
class ComputerPlayer():

    def __init__(self, depth: int, level : str):
            self.depth = depth
            self.level = level
            self.random_value = 3




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
        if self.level == "easy_level" :
                return random.choice(state.AllValidMoves())
        
        actions_scores = []


        for action in state.AllValidMoves():
            child_state = state.generate_successor(action)
            score = self.alpha_beta_pruning(self.depth - 1, PLAYER2, child_state, alpha=-sys.maxsize, beta=sys.maxsize)
            actions_scores.append((action, score))

        

        scores = [score for _, score in actions_scores]
        best_score = max(scores)
        best_actions = [action for action, score in actions_scores if score == best_score]
        return random.choice(best_actions)





       