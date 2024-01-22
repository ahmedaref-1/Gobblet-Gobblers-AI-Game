from typing import List
import random
import sys
import time
from State import State
from Action import MoveID
import BoardItem
import Gobblet
import Game
import math
import pickle
import copy



"""
TODO:
    - finish check_state function
    trace all code again
    put alpha beta algorithim
    trace all code
    put a proper heuristic
    handle the three in row case in is_valid_move function
    itirative deepining

"""

class ComputerPlayer:
 
    def __init__(self, level : str, playerID):
        self.level = level
        self.current_player = playerID
        self.opponent_player = playerID ^ 1
        self.ComputerGobbletsArray = {}
        self.OpponentGobbletsArray = {}

            
    def alpha_beta_pruning(self, updated_depth, player, GobbletBoard, alpha, beta):
        winning_state = self.check_state(GobbletBoard) # Base case
        if winning_state == "OppositPlayerWins":
            if player == self.opponent_player:
                return sys.maxsize
            else:
                return -sys.maxsize
        elif winning_state == "Player1Won":
            return -sys.maxsize
        elif winning_state == "Player2Won":
            return sys.maxsize
        
        if updated_depth == 0:      #Leaf node
            heuristic = self.heuristic(GobbletBoard, player)
            return heuristic
 
        if player == self.current_player:       #Maximizer
            # maxval  = -sys.maxsize
            AllValid_GobbletBoard = self.get_all_valid_boards(GobbletBoard, player)
            for Valid_GobbletBoard in AllValid_GobbletBoard:
                score = self.alpha_beta_pruning(updated_depth - 1, self.opponent_player, Valid_GobbletBoard, alpha, beta)
                # maxval = max(maxval, score)
                if beta <= alpha:
                    break
                alpha = max(alpha, score)
            return alpha
           
        else:                       #Minimizer
            # minval  = sys.maxsize
            AllValid_GobbletBoard = self.get_all_valid_boards(GobbletBoard, player)
            for Valid_GobbletBoard in AllValid_GobbletBoard:
                score = self.alpha_beta_pruning(updated_depth - 1, self.current_player, Valid_GobbletBoard, alpha, beta)
                # minval = min(minval, score)
                if beta <= alpha:
                    break
                beta = min(beta, score)
            return beta
        
    def heuristic(self , GobbletBoard, player) -> int:

        winning_state = self.check_state(GobbletBoard)

        if winning_state == "OppositPlayerWins":
            if player == self.opponent_player:
                return sys.maxsize
            else:
                return -sys.maxsize
        elif winning_state == "Player1Won":
            return -sys.maxsize
        elif winning_state == "Player2Won":
            return sys.maxsize
        else:
            if (self.level == "EASY"):
                return 0
            else:
                return self.hard_level_heuristic(GobbletBoard)

    def easy_level_heuristic(self , GobbletBoard) -> int:
        score = [0, 0]  # Initialize scores for owner indices 0 and 1

        for i, stack in enumerate(GobbletBoard):
            if stack:
                top_gobblet = stack[0]
                owner_index = top_gobblet["owner_index"]
                gobblet_id = top_gobblet["gobblet_id"]

                # Evaluate score based on criteria
                if owner_index is not None:
                    score_increment = gobblet_id + i  # You can adjust this formula based on your scoring criteria
                    score[owner_index] += score_increment
        return score[1]
    
    def hard_level_heuristic(self , GobbletBoard) -> int:
        """
        if direction consists only of SINGLE COLOR:
            - each empty field Scored 1
            - For each piece multiple with 10 or any number

        if there exists MIXED COLORS in the direction:
         - size of Pieces of MIN player < #Pieces of MAX outside the board
            do the same as above
         - otherwise 0 rate
        """
        score = 0
        score += self.evaluate_rows(GobbletBoard)*1000
        score += self.evaluate_columns(GobbletBoard)*1000
        score += self.evaluate_left_diagonal(GobbletBoard)
        score += self.evaluate_right_diagonal(GobbletBoard)

        corner = [0,3,12,15]
        # non_gobble_up_gobbblets = [0,4,8]

        computer_external_count = 0
        opponent_external_count = 0
        computer_corner_count = 0
        opponent_corner_count = 0
        

        for i in range(12):
            if(self.ComputerGobbletsArray[i]):
                if(i in corner):
                    computer_corner_count += 1
            else:
                computer_external_count += 1

            if(self.OpponentGobbletsArray[i]):
                if(i in corner):
                    opponent_corner_count += 1
            else:
                opponent_external_count += 1
        
        score -=  computer_external_count*1000
        score +=  opponent_external_count*1000

        score += computer_corner_count*10000
        score -= opponent_corner_count*10000


        return score
    
    def evaluate_rows(self, GobbletBoard) -> int:

        score_mappings = {
            (0, 4, 8): 50,
            (1, 5, 9): 30,
            (2, 6, 10): 20,
            (3, 7, 11): 10
        }

        computer_score = 0
        opponent_score = 0

        computer_count = 0
        opponent_count = 0

        # Check rows
        for i, stack in enumerate(GobbletBoard):
            if stack:
                for categories, score in score_mappings.items():
                    if stack[0]["gobblet_id"] in categories:
                        if stack[0]["owner_index"] == self.opponent_player:
                            opponent_score += score
                            opponent_count += 1
                        else:
                            computer_score += score
                            computer_count += 1

            if((i%4) == 3):
                if (opponent_count == 3):
                    opponent_score *= 20
                if (computer_count == 3):
                    computer_score *= 20

                if (opponent_count == 2):
                    opponent_score *= 10
                if (computer_count == 2):
                    computer_score *= 10
                    
                computer_count = 0
                opponent_count = 0
    
        return (computer_score - opponent_score)
    
    def evaluate_columns(self, GobbletBoard) -> int:

        score_mappings = {
            (0, 4, 8): 50,
            (1, 5, 9): 30,
            (2, 6, 10): 20,
            (3, 7, 11): 10
        }

        computer_score = 0
        opponent_score = 0

        computer_count = 0
        opponent_count = 0

        # Check columns
        for i in range(4):
            computer_count = 0
            opponent_count = 0

            for j in range(4):
                stack = GobbletBoard[i + j * 4]
                if stack:
                    for categories, score in score_mappings.items():
                        if stack[0]["gobblet_id"] in categories:
                            if stack[0]["owner_index"] == self.opponent_player:
                                opponent_score += score
                                opponent_count += 1
                            else:
                                computer_score += score
                                computer_count += 1

            if (opponent_count == 3):
                opponent_score *= 20
            if (computer_count == 3):
                computer_score *= 20

            if (opponent_count == 2):
                opponent_score *= 10
            if (computer_count == 2):
                computer_score *= 10
                        
        return (computer_score - opponent_score)
    
    def evaluate_diagonals(self, GobbletBoard) -> int:

        score_mappings = {
            (0, 4, 8): 50,
            (1, 5, 9): 30,
            (2, 6, 10): 20,
            (3, 7, 11): 10
        }

        computer_score = 0
        opponent_score = 0

        computer_count_d1 = 0
        opponent_count_d1 = 0
        computer_count_d2 = 0
        opponent_count_d2 = 0


        # Check columns
        for i in range(4):
            stack = GobbletBoard[i + i * 4]
            if stack:
                for categories, score in score_mappings.items():
                    if stack[0]["gobblet_id"] in categories:
                        if stack[0]["owner_index"] == self.opponent_player:
                            opponent_score += score
                            opponent_count_d1 += 1
                        else:
                            computer_score += score
                            computer_count_d1 += 1

            stack = GobbletBoard[i + (3 - i) * 4]
            if stack:
                for categories, score in score_mappings.items():
                    if stack[0]["gobblet_id"] in categories:
                        if stack[0]["owner_index"] == self.opponent_player:
                            opponent_score += score
                            opponent_count_d2 += 1
                        else:
                            computer_score += score
                            computer_count_d2 += 1

            if (opponent_count_d1 == 3):
                opponent_score *= 20
            if (computer_count_d1 == 3):
                computer_score *= 20

            if (opponent_count_d1 == 2):
                opponent_score *= 10
            if (computer_count_d1 == 2):
                computer_score *= 10
            
            if (opponent_count_d2 == 3):
                opponent_score *= 20
            if (computer_count_d2 == 3):
                computer_score *= 20

            if (opponent_count_d2 == 2):
                opponent_score *= 10
            if (computer_count_d2 == 2):
                computer_score *= 10
                        
        return (computer_score - opponent_score)

    def evaluate_left_diagonal(self, GobbletBoard) -> int:

        score_mappings = {
            (0, 4, 8): 50,
            (1, 5, 9): 30,
            (2, 6, 10): 20,
            (3, 7, 11): 10
        }

        computer_score = 0
        opponent_score = 0

        computer_count_d1 = 0
        opponent_count_d1 = 0

        for i in range(4):
            stack = GobbletBoard[i + i * 4]
            if stack:
                for categories, score in score_mappings.items():
                    if stack[0]["gobblet_id"] in categories:
                        if stack[0]["owner_index"] == self.opponent_player:
                            opponent_score += score
                            opponent_count_d1 += 1
                        else:
                            computer_score += score
                            computer_count_d1 += 1

            if (opponent_count_d1 == 3):
                opponent_score *= 20
            if (computer_count_d1 == 3):
                computer_score *= 20

            if (opponent_count_d1 == 2):
                opponent_score *= 10
            if (computer_count_d1 == 2):
                computer_score *= 10
                        
        return (computer_score - opponent_score)

    def evaluate_right_diagonal(self, GobbletBoard) -> int:

        score_mappings = {
            (0, 4, 8): 50,
            (1, 5, 9): 30,
            (2, 6, 10): 20,
            (3, 7, 11): 10
        }

        computer_score = 0
        opponent_score = 0

        computer_count_d2 = 0
        opponent_count_d2 = 0


        # Check columns
        for i in range(4):
            stack = GobbletBoard[i + (3 - i) * 4]
            if stack:
                for categories, score in score_mappings.items():
                    if stack[0]["gobblet_id"] in categories:
                        if stack[0]["owner_index"] == self.opponent_player:
                            opponent_score += score
                            opponent_count_d2 += 1
                        else:
                            computer_score += score
                            computer_count_d2 += 1

            if (opponent_count_d2 == 3):
                opponent_score *= 20
            if (computer_count_d2 == 3):
                computer_score *= 20

            if (opponent_count_d2 == 2):
                opponent_score *= 10
            if (computer_count_d2 == 2):
                computer_score *= 10
                        
        return (computer_score - opponent_score)
    
    def check_state(self, GobbletBoard) -> str:
        """
        Checks the current state of the game based on the ownership of positions on the game board.

        The function checks for various winning conditions, such as having a complete row, column, or diagonal
        filled with Gobblets of the same player. If a winning condition is met, it updates the game state and
        declares the winner accordingly.

        If no winning conditions are met and the board is not fully occupied, the game state remains "OnGoing."

        """
        player1_wins = 0
        player2_wins = 0

        # Check rows
        row_entry = False
        row_count =0
        for i, stack in enumerate(GobbletBoard):
            if stack:
                if ((i%4) == 0):
                    top_gobblet = stack[0]
                    owner_index = top_gobblet["owner_index"]
                    row_entry = True
                    row_count = 1
                elif (row_entry):
                    if (stack[0]["owner_index"] == owner_index):
                        row_count += 1
                    else:
                        row_count = 0

                if (row_count == 4):
                    if (stack[0]["owner_index"] == self.opponent_player):
                        player1_wins += 1
                        row_count = 0
                    else:
                        player2_wins += 1
                        row_count = 0

                if ((i%4) == 3):
                    row_count = 0
                    row_entry = False

            else:
                row_count = 0
                row_entry = False
                
        # Check columns
        for i in range(4):
            col_count = 0
            owner_index = None
            for j in range(4):
                if GobbletBoard[i + j * 4] and GobbletBoard[i + j * 4][0]["owner_index"] is not None:
                    if owner_index is None:
                        owner_index = GobbletBoard[i + j * 4][0]["owner_index"]
                        col_count = 1
                    elif GobbletBoard[i + j * 4][0]["owner_index"] == owner_index:
                        col_count += 1
                    else:
                        col_count = 0

                    if col_count == 4:
                        if (owner_index == self.opponent_player):
                            player1_wins += 1
                        else:
                            player2_wins += 1
                else:
                    col_count = 0
                    owner_index = None

        # Check diagonals
        diag_count1 = 0
        diag_count2 = 0
        diag_owner1 = None
        diag_owner2 = None

        for i in range(4):
            if GobbletBoard[i + i * 4] and GobbletBoard[i + i * 4][0]["owner_index"] is not None:
                if diag_owner1 is None:
                    diag_owner1 = GobbletBoard[i + i * 4][0]["owner_index"]
                    diag_count1 = 1
                elif GobbletBoard[i + i * 4][0]["owner_index"] == diag_owner1:
                    diag_count1 += 1
                else:
                    diag_count1 = 0

                if diag_count1 == 4:
                    if (diag_owner1 == self.opponent_player):
                        player1_wins += 1
                    else:
                        player2_wins += 1
            else:
                diag_count1 = 0
                diag_owner1 = None

            if GobbletBoard[i + (3 - i) * 4] and GobbletBoard[i + (3 - i) * 4][0]["owner_index"] is not None:
                if diag_owner2 is None:
                    diag_owner2 = GobbletBoard[i + (3 - i) * 4][0]["owner_index"]
                    diag_count2 = 1
                elif GobbletBoard[i + (3 - i) * 4][0]["owner_index"] == diag_owner2:
                    diag_count2 += 1
                else:
                    diag_count2 = 0

                if diag_count2 == 4:
                    if (diag_owner2 == self.opponent_player):
                        player1_wins += 1
                    else:
                        player2_wins += 1
            else:
                diag_count2 = 0
                diag_owner2 = None


        if player1_wins > 0 and player2_wins > 0:
            winner = "OppositPlayerWins"
        elif player1_wins > 0:
            winner = "Player1Won"
        elif player2_wins > 0:
            winner = "Player2Won"
        else:
            winner = "OnGoing"

        return winner
    
    
    def get_all_valid_boards(self, GobbletBoard, CurrPlayerIndex) -> list:
        """
        This function should get the array of GobbletBoard with the CurrPlayerIndex and
        iterate for each gobblet of the CurrPlayerIndex to know what valid move the player 
        may take, for each valid move the function creates a new GobbletBoard with the board
        that has the valid move player could make, and returns a list of all these possible moves
        """
        AllValid_GobbletBoard = []

        all_possible_gobblets = self.possible_gobblets(GobbletBoard, CurrPlayerIndex)

        for board_index, stack in enumerate(GobbletBoard):
            for possible_gobblet in all_possible_gobblets:
                valid_move = self.is_valid_move(GobbletBoard, possible_gobblet[0], board_index, possible_gobblet[1], CurrPlayerIndex)
                if (valid_move):
                    child_board = self.create_new_board(GobbletBoard, possible_gobblet[0], board_index, possible_gobblet[1], CurrPlayerIndex)
                    AllValid_GobbletBoard.append(child_board)

        return AllValid_GobbletBoard
    
    def possible_gobblets(self, GobbletBoard, owner_index) -> list:
        """
        Return a list of possible gobblets that a player with the given owner_index can move.

        The list contains goblets on top of the stacks and their next goblets satisfying the conditions.
        Each entry in the list contains two elements: the GobbletBoard index and the goblet on it.
        """
        possible_moves = []

        # Gobblet IDs that can always move
        always_movable_ids = [0, 4, 8]

        # Gobblet IDs that can move if the previous gobblet is on the board
        movable_after_previous = [1, 2, 3, 5, 6, 7, 9, 10, 11]

        on_board_gobblets = [[None, None] for _ in range(len(GobbletBoard) * 4)]
        top_stack_gobblets = [[None, None] for _ in range(len(GobbletBoard))]
        non_top_stack_gobblets = [[None, None] for _ in range(len(GobbletBoard) * 3)]

        on_board_index = 0
        top_index = 0
        non_top_index = 0

        for i, stack in enumerate(GobbletBoard):
            if stack:
                for j, gobblet in enumerate(stack):
                    if (stack[j]["owner_index"] == owner_index):
                        on_board_gobblets[on_board_index][0] = i
                        on_board_gobblets[on_board_index][1] = stack[j]["gobblet_id"]
                        on_board_index += 1
                        if j == 0:
                            top_stack_gobblets[top_index][0] = i
                            top_stack_gobblets[top_index][1] = stack[j]["gobblet_id"]
                            top_index += 1
                        else:
                            non_top_stack_gobblets[non_top_index][0] = i
                            non_top_stack_gobblets[non_top_index][1] = stack[j]["gobblet_id"]
                            non_top_index += 1

        # Append the goblet if it satisfy the conditions
        for goblet_id in range(12):
            if goblet_id in always_movable_ids:
                for i, top_stack_gobblet in  enumerate(top_stack_gobblets):
                    if goblet_id == top_stack_gobblets[i][1]:
                        possible_moves.append((top_stack_gobblets[i][0], goblet_id))
                        break
                else:
                    possible_moves.append((None, goblet_id))
            else:
                for i, top_stack_gobblet in  enumerate(top_stack_gobblets):
                    if goblet_id == top_stack_gobblets[i][1]:
                        possible_moves.append((top_stack_gobblets[i][0], goblet_id))

            for i, gobblet in  enumerate(on_board_gobblets):
                if goblet_id == on_board_gobblets[i][1]:
                    next_gobblet_id = goblet_id + 1
                    movable_gobblet = True
                    for j, on_board_gobblet in  enumerate(on_board_gobblets):
                        if next_gobblet_id == on_board_gobblets[j][1]:
                            movable_gobblet = False
                    if (movable_gobblet):
                        if next_gobblet_id in movable_after_previous:
                            possible_moves.append((None, next_gobblet_id))

        return possible_moves

    def is_valid_move(self, GobbletBoard, current_position, new_position, gobblet_id, owner_index) -> bool:
        """
        Get a list of valid moves for a specific goblet.
        """

        valid_move = False

        XL = [0,4,8]
        L = [1,5,9]
        M = [2,6,10]
        S = [3,7,11]

        stack = GobbletBoard[new_position]

        if(gobblet_id>11 or gobblet_id<0):
            return False
        if(new_position>15 or new_position<0):
            return False


        # If the cell has a gobblet on it
        if (stack):
            # If the gobblet is internal
            if (current_position):
                # If the size of the new gobblet is bigger than the current then gobble up
                if (gobblet_id in S):
                    return False
                elif (gobblet_id in M):
                    if (stack[0]["gobblet_id"] in S):
                        return True
                    else:
                        return False
                elif (gobblet_id in L):
                    if (stack[0]["gobblet_id"] in XL) or (stack[0]["gobblet_id"] in L):
                        return False
                    else:
                        return True
                elif (gobblet_id in XL):
                    if(stack[0]["gobblet_id"] in XL):
                        return False
                    else:
                        return True
                

            # If the gobblet is external
            else:
                return False
                # To gobble up three conditions must happen

                # The gobblet should be of the opponent
                if (stack[0]["owner_index"] == owner_index):
                    return False
                
                # The size of the new gobblet must be bigger than the current one
                if (gobblet_id in S):
                    return False
                elif (gobblet_id in M):
                    if (stack[0]["gobblet_id"] in S):
                        return True
                    else:
                        return False
                elif (gobblet_id in L):
                    if (stack[0]["gobblet_id"] in XL) or (stack[0]["gobblet_id"] in L):
                        return False
                    else:
                        return True
                elif (gobblet_id in XL):
                    if(stack[0]["gobblet_id"] in XL):
                        return False
                    else:
                        return True
                else:
                    return False
                
                # The gobblet should be one of three gobblets on a row

        # If the cell is empty then the move is valid
        else:
            return True

        return valid_move

    def create_new_board(self, GobbletBoard, current_position, new_position, gobblet_id, owner_index) -> list:
        """
        Create a new GobbletBoard with the specified move.
        """
        # Copy the existing GobbletBoard to create a new one
        new_board = [stack.copy() if stack else [] for stack in GobbletBoard]

        # If current_position is None, place the specified goblet_id in the new_position
        if current_position is None:
            goblet = {"gobblet_id": gobblet_id, "owner_index": owner_index}
            new_board[new_position].insert(0, goblet)
        else:
            # Move the goblet from current_position to new_position
            goblet = new_board[current_position].pop(0)
            goblet["owner_index"] = owner_index
            new_board[new_position].insert(0, goblet)

        return new_board


    def get_action(self, state: State) -> MoveID :

        if self.level == "EASY" :
            time_limit = 0.5
        if self.level == "MEDIUM" :
            time_limit = 0.75
        if self.level == "HARD" :
            time_limit = 1.5

        # if self.level == "EASY" :
        # return random.choice(state.all_valid_moves())
        # if self.level == "MEDIUM" :
        #         time_limit = 4
        # if self.level == "HARD" :
        #         time_limit = 8
       
        # actions_scores = []
        # start_time = time.time()
        # depth = 2

        # player = state.CurrentPlayerId

        # while True:
 
        #     for action in state.all_valid_moves():
        #         print(action)
        #         print(state.CurrentPlayerId)
        #         child_state = state.generate_successor(action)
        #         print(child_state.CurrentPlayerId)
        #         child_state.game.check_state()
        #         if child_state.game.GameState != "OnGoing":
        #             if child_state.game.Winner == child_state.CurrentPlayerId:
        #                 return action
        #             else:
        #                 continue
        #         score = self.alpha_beta_pruning(depth - 1, PLAYER2, child_state, alpha=-sys.maxsize, beta=sys.maxsize)
        #         actions_scores.append((action, score))
        #     break
        #     depth += 1
        #     elapsed_time = time.time() - start_time
 
        #     if elapsed_time >= time_limit:
        #         break

        # # Creating a 2D array to represent the game board
        # GobbletBoard = [[] for _ in range(16)]

        # # Filling the GobbletBoard with the values from GobbletBoardItemsArray
        # for i in range(16):
        #     board_item = state.game.BoardItemsArray[i]
        #     stack_entries = [
        #         {"gobblet_id": gobblet.ID, "owner_index": gobblet.OwnerIndex}
        #         for gobblet in board_item.GobbletsStack
        #     ][:4]

        #     # Sorting the stack entries based on Gobblet IDs
        #     stack_entries.sort(key=lambda entry: entry["gobblet_id"])

        #     GobbletBoard[i] = stack_entries



        
        start_time = time.time()
        # Creating a 2D array to represent the game board
        GobbletBoard = [[] for _ in range(16)]

        # Filling the GobbletBoard with the values from GobbletBoardItemsArray
        for i in range(16):
            board_item = state.game.BoardItemsArray[i]
            
            if board_item.GobbletsStack is not None:
                stack_entries = [
                    {"gobblet_id": gobblet.ID, "owner_index": gobblet.OwnerIndex}
                    for gobblet in reversed(board_item.GobbletsStack)  # Reverse the order
                ][:4]
            else:
                stack_entries = []

            GobbletBoard[i] = stack_entries

        # Displaying the resulting GobbletBoard
        for i, stack in enumerate(GobbletBoard):
            print(f"Cell {i}: {stack}")

        for i in range(12):
            if(self.opponent_player == 0):
                self.OpponentGobbletsArray[i] = state.game.FirstPlayerGobbletsArray[i].get_gobblet_position()
                self.ComputerGobbletsArray[i] = state.game.SecondPlayerGobbletsArray[i].get_gobblet_position()
            else:
                self.ComputerGobbletsArray[i] = state.game.FirstPlayerGobbletsArray[i].get_gobblet_position()
                self.OpponentGobbletsArray[i] = state.game.SecondPlayerGobbletsArray[i].get_gobblet_position()
        
        actions_scores = []        
        
        depth = 2
        
        all_next_moves = state.all_valid_moves()
        while True:
            
            for action in all_next_moves:

                gobblet_id = action.CurrentGobblet.get_gobblet_index()
                OwnerIndex = 1
                current_position = action.CurrentGobblet.get_gobblet_owned_position_index()
                new_position = action.next.get_Board_Index()

                if( self.is_valid_move(GobbletBoard, current_position, new_position, gobblet_id, OwnerIndex)):

                    new_board = self.create_new_board(GobbletBoard, current_position, new_position, gobblet_id, OwnerIndex)
                    if self.level != "EASY" :
                        winning_state = self.check_state(new_board)
                        if winning_state == "OppositPlayerWins":
                            actions_scores.append((action, -sys.maxsize))
                            continue
                        elif winning_state == "Player1Won":
                            actions_scores.append((action, -sys.maxsize))
                            continue
                        elif winning_state == "Player2Won":
                            return action

                    score = self.alpha_beta_pruning(depth - 1, self.opponent_player, new_board, alpha=-sys.maxsize, beta=sys.maxsize)
                    actions_scores.append((action, score))
            depth += 1
            elapsed_time = time.time() - start_time
 
            if elapsed_time >= time_limit:
               break
            
        scores = [score for _, score in actions_scores]
        best_score = max(scores)
        best_actions = [action for action, score in actions_scores if score == best_score]
        return random.choice(best_actions)