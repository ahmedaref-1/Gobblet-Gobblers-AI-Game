import random
import sys
#import State
#import Action

PLAYER1 =1
PLAYER2 =2

class ComputerPlayer():

    def __init__(self, depth: int, easy_level : bool):
            self.depth = depth
            self.easy_level = easy_level
            self.random_value = 3


    def alpha_beta_pruning(self, updated_depth, player, state: State, alpha, beta, legal_actions):
        if updated_depth == 0:      #Leaf node
            return self.heuristic(state)

        if player == PLAYER1:       #Maximizer
            for action in legal_actions:
                child = state.generate_successor(action)
                score = self.alpha_beta_pruning(updated_depth - 1, PLAYER2, child, alpha, beta, child.get_legal_actions())
            
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
                return alpha
            
        else:                       #Minimizer
            for action in legal_actions:
                child = state.generate_successor(action)
                score = self.alpha_beta_pruning(updated_depth - 1, PLAYER1, child, alpha, beta, child.get_legal_actions())
 
                beta = min(beta, score)
                if beta <= alpha:
                    break
                return beta


    def get_action(self, state: State) -> Action:
        if self.easy_level:
                return random.choice(state.get_legal_actions())
        
        actions_scores = []
        legal_actions = state.get_legal_actions()


        for action in legal_actions:
            child = state.generate_successor(action)
            score = self.alpha_beta_pruning(self.depth - 1, PLAYER2, child, alpha=-sys.maxsize, beta=sys.maxsize, legal_actions=legal_actions)
            actions_scores.append((action, score))

        best_s = float('-inf')  # Start with a very low score
        best_a = []

        for action, score in actions_scores:
            if score > best_s:
                best_s = score
                best_a = [action]
            elif score == best_s:
                best_a.append(action)

        return random.choice(best_a)