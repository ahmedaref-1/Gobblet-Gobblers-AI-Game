# Import the Gobblet class from the Gobblet module
import Gobblet
# Import the BoardItem class from the BoardItem module
import BoardItem
# Import the MoveID class from the Action module
from Action import MoveID


class Game:
    def __init__(self):
        """
        Represents the Gobblet Gobblers game.

        """
        # List containing names of both players
        self.PlayerNames = ["Player1", "Player2"]
        # State of the game (OnGoing, Draw, Player1Won, Player2Won)
        self.GameState = "OnGoing"
        # Winner of the game (initially None)
        self.Winner = None

        # Flag used to skip the current round
        self.SkipRoundFlag = False
        # Flag used to notify the user that the move is invalid
        self.InvalidMoveFlag = False

        # Number of gobblets per player
        self.NumberOfGobbletsPerPlayer = 12
        # Size of the game board (number of cells)
        self.BoardSize = 16
        # List to store Gobblet objects of the First Player
        self.FirstPlayerGobbletsArray = []
        # Create Gobblet objects for the First Player
        created_gobblet_size = 4
        for i in range(self.NumberOfGobbletsPerPlayer):
            temp_gobblet = Gobblet.Gobblet(i, 0, created_gobblet_size)
            created_gobblet_size -= 1
            if created_gobblet_size < 1:
                created_gobblet_size = 4
            if temp_gobblet.Size == 4:
                temp_gobblet.IsOnTop = True
            self.FirstPlayerGobbletsArray.append(temp_gobblet)

        # List to store Gobblet objects of the Second Player
        self.SecondPlayerGobbletsArray = []
        # Create Gobblet objects for the Second Player
        created_gobblet_size = 4
        for i in range(self.NumberOfGobbletsPerPlayer):
            temp_gobblet = Gobblet.Gobblet(i, 1, created_gobblet_size)
            created_gobblet_size -= 1
            if created_gobblet_size < 1:
                created_gobblet_size = 4
            if temp_gobblet.Size == 4:
                temp_gobblet.IsOnTop = True
            self.SecondPlayerGobbletsArray.append(temp_gobblet)

        # List to store BoardItem objects
        self.BoardItemsArray = []
        # Create BoardItem objects
        for i in range(self.BoardSize):
            temp_board_item = BoardItem.BoardItem(i)
            self.BoardItemsArray.append(temp_board_item)

        # Index of the current player (0 or 1)
        self.CurrentPlayerIndex = 0
        # ID of the selected Gobblet for the current move
        self.SelectedGobbletID = None
        # Index of the selected BoardItem for the current move
        self.SelectedBoardItemIndex = None

        self.ROW_COL_LENGTH = 4

        # Diagonals
        self.left_diagonal = [i for i in range(0, self.BoardSize, self.ROW_COL_LENGTH + 1)]
        self.right_diagonal = [i for i in range(self.ROW_COL_LENGTH - 1, self.BoardSize - 1, self.ROW_COL_LENGTH - 1)]

        # Rows
        self.rows = [[j for j in range(i, i + self.ROW_COL_LENGTH)] for i in range(0, self.BoardSize, self.ROW_COL_LENGTH)]

        # Columns
        self.columns = [[j for j in range(i, self.BoardSize, self.ROW_COL_LENGTH)] for i in range(self.ROW_COL_LENGTH)]

        # Concatenate everything
        self.lines = [self.left_diagonal, self.right_diagonal] + self.rows +self.columns

    def list_possible_gobblets(self) -> list:
        """
        Determines and returns a list of all Goblet ID's that can be placed of a specific player.

        Args:
        CurrentPlayerIndex: To indicate the player.

        Returns:
        A list containing the IDs of all Goblets that can be moved.
        """
        possible_gobblets = []
        # Check for Player 1
        if self.CurrentPlayerIndex == 0:
            # Iterate through all available Goblet IDs of player 1, considering both internal and external ones.
            for gobblet_id in range(self.NumberOfGobbletsPerPlayer):
                # Check if the gobblet is on top.
                if self.FirstPlayerGobbletsArray[gobblet_id].is_on_top_of_stack():
                    possible_gobblets.append(gobblet_id)

        # Check for Player 2
        if self.CurrentPlayerIndex == 1:
            # Iterate through all available Goblet IDs of player 2, considering both internal and external ones.
            for gobblet_id in range(self.NumberOfGobbletsPerPlayer):
                # Check if the gobblet is on top.
                if self.SecondPlayerGobbletsArray[gobblet_id].is_on_top_of_stack():
                    possible_gobblets.append(gobblet_id)

        return possible_gobblets

    def list_possible_moves(self, current_gobblet: Gobblet) -> list[MoveID]:
        """
        Checks the positions on board that the gobblet can move to.

        Args:
        current_gobblet: The gobblet which I want what are the possible positions on board to place it on

        Returns:
        - List of possible positions on board that the goblet can move to.
        """

        # Initialize an empty array to store possible moves
        possible_moves = []
        # Iterate around all squares on board
        for SquareID in range(self.BoardSize):
            # Check if the gobblet can move to the position on board
            if current_gobblet.is_possible_gobblet_movement(self.BoardItemsArray[SquareID]):
                # Create an object with the current gobblet and the possible squareID it can move to
                new_valid_move = MoveID(current_gobblet, self.BoardItemsArray[SquareID])
                # Add MoveID to the array
                possible_moves.append(new_valid_move)
        # Return the array of possible moves
        return possible_moves

    def all_valid_moves(self) -> list[MoveID]:
        """
        Determines and returns a list of all valid moves for all available gobblet IDs 
        that can be placed on the specified position.

        Returns:
        A list containing the valid positions of all available gobblets.
        """
        # Get a list of all available gobblets
        all_available_gobblets = self.list_possible_gobblets()

        # Initialize the list to store valid moves
        valid_actions = []

        # Iterate through each available gobblet
        for gobblet in all_available_gobblets:
            if self.CurrentPlayerIndex == 0:
                # Get the list of possible moves for the current gobblet
                possible_moves = self.list_possible_moves(self.FirstPlayerGobbletsArray[gobblet])
            else:
                # Get the list of possible moves for the current gobblet
                possible_moves = self.list_possible_moves(self.SecondPlayerGobbletsArray[gobblet])
            # Extend the valid_actions list with the possible moves for the current gobblet
            valid_actions.extend(possible_moves)

        # Return the final list of valid moves
        return valid_actions

    def make_move(self, current_gobblet: Gobblet, required_position: BoardItem):
        """
        Moves a Gobblet from its current position to the specified target position on the board.

        Args:
        current_gobblet: The Gobblet to be moved.
        required_position: The target position on the board where the Gobblet should be moved.
        """
        # Check for the corner case and return SkipRoundFlag
        self.corner_case(self)
        # initially set the invalid move flag to false
        self.InvalidMoveFlag = False

        # Check if the gobblet is on top of stack and that it is already on the board
        if current_gobblet.is_on_top_of_stack() and current_gobblet.is_on_board():
            # Check if the gobblet can be placed on the board
            if current_gobblet.is_possible_gobblet_movement(required_position):
                # Call the function place_internal_gobblet to place the gobblet on board
                self.SkipRoundFlag = False
                self.place_internal_gobblet(current_gobblet, required_position,
                                            self.BoardItemsArray[current_gobblet.get_gobblet_position()])
            else:
                self.InvalidMoveFlag = True

        # Check if the gobblet is on top and that it is NOT placed on board (External Goblet)
        elif current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and required_position.is_empty():
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(required_position):
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(self, current_gobblet, required_position)
            else:
                self.InvalidMoveFlag = True

        # Additional conditions for specific board positions (Checkmate state)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[1].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[1].CurrentOpponentIndex == self.BoardItemsArray[0].CurrentOpponentIndex ==
                       self.BoardItemsArray[2].CurrentOpponentIndex) or (self.BoardItemsArray[1].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[2].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[3].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[5].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[5].CurrentOpponentIndex == self.BoardItemsArray[4].CurrentOpponentIndex ==
                       self.BoardItemsArray[6].CurrentOpponentIndex) or (self.BoardItemsArray[5].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[6].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[7].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[9].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[9].CurrentOpponentIndex == self.BoardItemsArray[8].CurrentOpponentIndex ==
                       self.BoardItemsArray[10].CurrentOpponentIndex) or (
                              self.BoardItemsArray[9].CurrentOpponentIndex ==
                              self.BoardItemsArray[10].CurrentOpponentIndex == self.BoardItemsArray[
                                  11].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[13].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[13].CurrentOpponentIndex == self.BoardItemsArray[12].CurrentOpponentIndex ==
                       self.BoardItemsArray[14].CurrentOpponentIndex) or (
                              self.BoardItemsArray[13].CurrentOpponentIndex ==
                              self.BoardItemsArray[14].CurrentOpponentIndex == self.BoardItemsArray[
                                  15].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[4].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[4].CurrentOpponentIndex == self.BoardItemsArray[0].CurrentOpponentIndex ==
                       self.BoardItemsArray[8].CurrentOpponentIndex) or (self.BoardItemsArray[4].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[8].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[12].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[5].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[5].CurrentOpponentIndex == self.BoardItemsArray[1].CurrentOpponentIndex ==
                       self.BoardItemsArray[9].CurrentOpponentIndex) or (self.BoardItemsArray[5].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[9].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[13].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[6].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[6].CurrentOpponentIndex == self.BoardItemsArray[2].CurrentOpponentIndex ==
                       self.BoardItemsArray[10].CurrentOpponentIndex) or (
                              self.BoardItemsArray[6].CurrentOpponentIndex ==
                              self.BoardItemsArray[10].CurrentOpponentIndex == self.BoardItemsArray[
                                  14].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[7].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[7].CurrentOpponentIndex == self.BoardItemsArray[3].CurrentOpponentIndex ==
                       self.BoardItemsArray[11].CurrentOpponentIndex) or (
                              self.BoardItemsArray[7].CurrentOpponentIndex ==
                              self.BoardItemsArray[11].CurrentOpponentIndex == self.BoardItemsArray[
                                  15].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[5].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[5].CurrentOpponentIndex == self.BoardItemsArray[0].CurrentOpponentIndex ==
                       self.BoardItemsArray[10].CurrentOpponentIndex) or (
                              self.BoardItemsArray[5].CurrentOpponentIndex ==
                              self.BoardItemsArray[10].CurrentOpponentIndex == self.BoardItemsArray[
                                  15].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)

        # Repeat the pattern of checks for other specific board positions, consider refactoring for clarity
        # Check if it is possible to move the gobblet to the specified position for specific board positions
        elif (current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and  current_gobblet.is_possible_gobblet_movement(required_position) and
              (self.BoardItemsArray[6].CurrentOpponentIndex is not None) and (
                      (self.BoardItemsArray[6].CurrentOpponentIndex == self.BoardItemsArray[3].CurrentOpponentIndex ==
                       self.BoardItemsArray[9].CurrentOpponentIndex) or (self.BoardItemsArray[6].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[9].CurrentOpponentIndex ==
                                                                         self.BoardItemsArray[12].CurrentOpponentIndex)
              )):
            # Call Function place_external_gobblet to place the gobblet on board
            self.place_external_gobblet(self, current_gobblet, required_position)
        else:
            self.InvalidMoveFlag = True
        # Update the board list array cells current opponent index
        self.update_board_array_opponent_index(self)
        # Check the game state
        self.check_state()

        # If the move is valid alternate player
        if self.InvalidMoveFlag is not True or self.SkipRoundFlag is True:
            self.alternate_current_player_index(self)

    @staticmethod
    def place_external_gobblet(self, current_gobblet: Gobblet, required_position: BoardItem):
        """
        Places an external Gobblet onto the specified position on the game board, ensuring valid placement.

        Args:
        - current_gobblet (Gobblet): The Gobblet to be placed on the board.
        - required_position (BoardItem): The target position where the Gobblet should be placed.
        """
        # Check if the gobblet can be placed on the specified position on the board
        if required_position.is_possible_board_movement(current_gobblet):
            next_gobblet_index = current_gobblet.get_gobblet_index() + 1
            if next_gobblet_index < 12:
                # Set the flag indicating that the next gobblet is on top of the stack
                if self.CurrentPlayerIndex == 0:
                    self.FirstPlayerGobbletsArray[next_gobblet_index].set_gobblet_on_top_of_stack_flag(True)
                else:
                    self.SecondPlayerGobbletsArray[next_gobblet_index].set_gobblet_on_top_of_stack_flag(True)
                # Add the gobblet to the top of the new position
                required_position.add_gobblet_on_top(current_gobblet)
                # Update the gobblet's position information
                current_gobblet.update_gobblet_position(required_position)

    @staticmethod
    def place_internal_gobblet(current_gobblet: Gobblet, required_position: BoardItem, old_position: BoardItem):
        """
        Places a Gobblet onto a specified BoardItem position, following game rules.

        Args:
        - current_gobblet (Gobblet): The Gobblet to be placed.
        - required_position (BoardItem): The BoardItem position where the Gobblet should be placed.
        - old_position (BoardItem): The BoardItem position from which the Gobblet is being moved.

        """
        # Check if the gobblet can be placed on the specified position on the board
        if required_position.is_possible_board_movement(current_gobblet):
            # Remove the goblet from the top of its old position
            old_position.remove_gobblet_on_top()
            # Add the gobblet to the top of the new position
            required_position.add_gobblet_on_top(current_gobblet)
            # Update the gobblet's position information
            current_gobblet.update_gobblet_position(required_position)

    def check_state(self):
        """
        Checks the current state of the game based on the ownership of positions on the game board.

        The function checks for various winning conditions, such as having a complete row, column, or diagonal
        filled with Gobblets of the same player. If a winning condition is met, it updates the game state and
        declares the winner accordingly.

        If no winning conditions are met and the board is not fully occupied, the game state remains "OnGoing."

        """
        player1_count = 0  # Counter for Player 1's winning positions
        player2_count = 0  # Counter for Player 2's winning positions

        # Check for a complete row of the same player in each row
        for row in range(4):
            if (
                    self.BoardItemsArray[row * 4].CurrentOwnerIndex is not None
                    and self.BoardItemsArray[row * 4].CurrentOwnerIndex
                    == self.BoardItemsArray[row * 4 + 1].CurrentOwnerIndex
                    == self.BoardItemsArray[row * 4 + 2].CurrentOwnerIndex
                    == self.BoardItemsArray[row * 4 + 3].CurrentOwnerIndex
            ):
                if self.BoardItemsArray[row * 4].CurrentOwnerIndex == 0:
                    player1_count += 1
                else:
                    player2_count += 1

        # Check for a complete column of the same player in each column
        for col in range(4):
            if (
                    self.BoardItemsArray[col].CurrentOwnerIndex is not None
                    and self.BoardItemsArray[col].CurrentOwnerIndex
                    == self.BoardItemsArray[col + 4].CurrentOwnerIndex
                    == self.BoardItemsArray[col + 8].CurrentOwnerIndex
                    == self.BoardItemsArray[col + 12].CurrentOwnerIndex
            ):
                if self.BoardItemsArray[col].CurrentOwnerIndex == 0:
                    player1_count += 1
                else:
                    player2_count += 1

        # Check for a complete diagonal from top-left to bottom-right
        if (
                self.BoardItemsArray[0].CurrentOwnerIndex is not None
                and self.BoardItemsArray[0].CurrentOwnerIndex
                == self.BoardItemsArray[5].CurrentOwnerIndex
                == self.BoardItemsArray[10].CurrentOwnerIndex
                == self.BoardItemsArray[15].CurrentOwnerIndex
        ):
            if self.BoardItemsArray[0].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        # Check for a complete diagonal from top-right to bottom-left
        if (
                self.BoardItemsArray[3].CurrentOwnerIndex is not None
                and self.BoardItemsArray[3].CurrentOwnerIndex
                == self.BoardItemsArray[6].CurrentOwnerIndex
                == self.BoardItemsArray[9].CurrentOwnerIndex
                == self.BoardItemsArray[12].CurrentOwnerIndex
        ):
            if self.BoardItemsArray[3].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        # Update game state based on winning conditions
        if player1_count == 1 and player2_count == 1:
            self.GameState = "Draw"
            self.Winner = None
        elif player1_count == 1:
            self.GameState = "Player1Won"
            self.Winner = 0
        elif player2_count == 1:
            self.GameState = "Player2Won"
            self.Winner = 1
        else:
            self.GameState = "OnGoing"
            self.Winner = None

    @staticmethod
    def corner_case(self):
        """
        Checks for a corner case where SkipRoundFlag is set to True if all positions on the board are filled.

        This function iterates through all positions on the game board. If any position is not filled
        (CurrentOwnerIndex is None),it sets SkipRoundFlag to False, indicating that the game can proceed with the
        current round. Otherwise, if all positions are filled,SkipRoundFlag is set to True, indicating that
        the current round should be skipped as there is no available space for a small piece.

        Returns:
        bool: The value of SkipRoundFlag after the check.
        """
        # Initialize SkipRoundFlag to True
        self.SkipRoundFlag = True

        # Iterate through all positions on the game board
        for position in range(self.BoardSize):
            # Check if the current position is not filled
            if self.BoardItemsArray[position].CurrentOwnerIndex is None:
                # Set SkipRoundFlag to False and return its value
                self.SkipRoundFlag = False
                return self.SkipRoundFlag

        # If all positions are filled, SkipRoundFlag remains True
        return self.SkipRoundFlag

    @staticmethod
    def update_board_array_opponent_index(self):
        """
        Updates the opponent index for all BoardItem objects on the game board.

        This method iterates through all positions on the game board and calls the 'update_opponent_index'
        method for each corresponding BoardItem. The 'update_opponent_index' method is responsible for setting
        the opponent index based on the current state of the board.

        Returns:
        None
        """
        # Iterate through all positions on the game board
        for position in range(self.BoardSize):
            # Call the 'update_opponent_index' method for the corresponding BoardItem
            self.BoardItemsArray[position].update_opponent_index()

    @staticmethod
    def alternate_current_player_index(self):
        """
        Alternates the current player index between 0 and 1.

        This method is used to switch between players in the game. The current player index is toggled between
        0 and 1 using the XOR (^) operation. If the current index is 0, it becomes 1, and if it is 1, it becomes 0.

        Returns:
        None
        """
        # Toggle the current player index using the XOR (^) operation
        self.CurrentPlayerIndex = self.CurrentPlayerIndex ^ 1
