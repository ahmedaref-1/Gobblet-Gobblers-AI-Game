import Gobblet
import BoardItem
from Action import MoveID


###############################################################
# List type problem                                           #
###############################################################
class Game:
    def __init__(self):
        """
        Represents the Gobblet Gobblers game.

        """
        self.PlayerNames = ["Player1", "Player2"]  # List containing names of both players
        self.GameState = "OnGoing"  # State of the game (OnGoing, Draw, Player1Won, Player2Won)
        self.Winner = None  # Winner of the game (initially None)
        self.SkipRoundFlag = False  # Flag used to skip the current round

        self.NumberOfGobbletsPerPlayer = 12  # Number of gobblets per player
        self.BoardSize = 16  # Size of the game board (number of cells)

        self.FirstPlayerGobbletsArray = []  # List to store Gobblet objects of the First Player
        created_gobblet_size = 4
        for i in range(self.NumberOfGobbletsPerPlayer):
            # Create a new Gobblet object
            temp_gobblet = Gobblet.Gobblet(i, 0, created_gobblet_size)
            created_gobblet_size -= 1
            # Reset the CreatedGobbletSize to 4 if it is less than 1
            if created_gobblet_size < 1:
                created_gobblet_size = 4
            # Set the isOnTop flag to True if the current Gobblet is of size 4
            if temp_gobblet.Size == 4:
                temp_gobblet.IsOnTop = True
            # Add the new Gobblet object to the appropriate list
            self.FirstPlayerGobbletsArray.append(temp_gobblet)

        self.SecondPlayerGobbletsArray = []  # List to store Gobblet objects of the Second Player
        created_gobblet_size = 4
        for i in range(self.NumberOfGobbletsPerPlayer):
            # Create a new Gobblet object
            temp_gobblet = Gobblet.Gobblet(i, 0, created_gobblet_size)
            created_gobblet_size -= 1
            # Reset the CreatedGobbletSize to 4 if it is less than 1
            if created_gobblet_size < 1:
                created_gobblet_size = 4
            # Set the isOnTop flag to True if the current Gobblet is of size 4
            if temp_gobblet.Size == 4:
                temp_gobblet.IsOnTop = True
            # Add the new Gobblet object to the appropriate list
            self.SecondPlayerGobbletsArray.append(temp_gobblet)

        self.BoardItemsArray = []  # List to store BoardItem objects
        for i in range(self.BoardSize):
            # Create a new BoardItem object
            temp_board_item = BoardItem.BoardItem(i)
            # Add the new BoardItem object to the list
            self.BoardItemsArray.append(temp_board_item)

        self.CurrentPlayerIndex = 0  # Index of the current player (0 or 1)
        self.SelectedGobbletID = None  # ID of the selected Gobblet for the current move
        self.SelectedBoardItemIndex = None  # Index of the selected BoardItem for the current move

    def list_possible_gobblets(self) -> list:
        """
        Determines and returns a list of all Goblets that can be placed of a specific player.

        Args:
        CurrentPlayerIndex: To indicate the player.

        Returns:
        A list containing the IDs of all Goblets that can be moved.
        """
        possible_gobblets = []
        # Check for Player 1
        if self.CurrentPlayerIndex == 0:
            # Iterate through all available Goblet IDs of player 1, considering both internal and external ones.
            for goblet_id in range(self.NumberOfGobbletsPerPlayer):
                # Check if the gobblet is on top.
                if self.FirstPlayerGobbletsArray[goblet_id].is_on_top_of_stack():
                    possible_gobblets.append(goblet_id)

        # Check for Player 2
        if self.CurrentPlayerIndex == 1:
            # Iterate through all available Goblet IDs of player 2, considering both internal and external ones.
            for goblet_id in range(self.NumberOfGobbletsPerPlayer):
                # Check if the gobblet is on top.
                if self.SecondPlayerGobbletsArray[goblet_id].is_on_top_of_stack():
                    possible_gobblets.append(goblet_id)

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
                new_valid_move = MoveID(current_gobblet, SquareID)
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
            # Get the list of possible moves for the current gobblet
            possible_moves = self.list_possible_moves(gobblet)

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
        # Check if the gobblet is on top of stack and that it is already on the board
        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is True):
            # Check if the gobblet can be placed on the board
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call the function place_internal_gobblet to place the gobblet on board
                self.place_internal_gobblet(current_gobblet, required_position)

        # Check if the gobblet is on top and that it is NOT placed on board (External Goblet)
        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) and \
                (required_position.is_empty() is True):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) \
                and (self.BoardItemsArray[1].OpponentIndex is not None) and \
                (self.BoardItemsArray[0].OpponentIndex == self.BoardItemsArray[1].OpponentIndex == self.BoardItemsArray[
                    2].OpponentIndex) or \
                (self.BoardItemsArray[1].OpponentIndex == self.BoardItemsArray[2].OpponentIndex == self.BoardItemsArray[
                    3].OpponentIndex):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) and (
                self.BoardItemsArray[5].OpponentIndex is not None) and \
                (self.BoardItemsArray[4].OpponentIndex == self.BoardItemsArray[5].OpponentIndex == self.BoardItemsArray[
                    6].OpponentIndex) or \
                (self.BoardItemsArray[5].OpponentIndex == self.BoardItemsArray[6].OpponentIndex == self.BoardItemsArray[
                    7].OpponentIndex):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) and (
                self.BoardItemsArray[9].OpponentIndex is not None) and \
                (self.BoardItemsArray[8].OpponentIndex == self.BoardItemsArray[9].OpponentIndex == self.BoardItemsArray[
                    10].OpponentIndex) or \
                (self.BoardItemsArray[9].OpponentIndex == self.BoardItemsArray[10].OpponentIndex ==
                 self.BoardItemsArray[11].OpponentIndex):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) and (
                self.BoardItemsArray[13].OpponentIndex is not None) and \
                (self.BoardItemsArray[12].OpponentIndex == self.BoardItemsArray[13].OpponentIndex ==
                 self.BoardItemsArray[14].OpponentIndex) or \
                (self.BoardItemsArray[13].OpponentIndex == self.BoardItemsArray[14].OpponentIndex ==
                 self.BoardItemsArray[15].OpponentIndex):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) and (
                self.BoardItemsArray[5].OpponentIndex is not None) and \
                (self.BoardItemsArray[1].OpponentIndex == self.BoardItemsArray[5].OpponentIndex == self.BoardItemsArray[
                    9].OpponentIndex) or \
                (self.BoardItemsArray[5].OpponentIndex == self.BoardItemsArray[9].OpponentIndex == self.BoardItemsArray[
                    13].OpponentIndex):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) and (
                self.BoardItemsArray[6].OpponentIndex is not None) and \
                (self.BoardItemsArray[2].OpponentIndex == self.BoardItemsArray[6].OpponentIndex == self.BoardItemsArray[
                    10].OpponentIndex) or \
                (self.BoardItemsArray[6].OpponentIndex == self.BoardItemsArray[10].OpponentIndex ==
                 self.BoardItemsArray[14].OpponentIndex):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) and (
                self.BoardItemsArray[7].OpponentIndex is not None) and \
                (self.BoardItemsArray[3].OpponentIndex == self.BoardItemsArray[7].OpponentIndex == self.BoardItemsArray[
                    11].OpponentIndex) or \
                (self.BoardItemsArray[7].OpponentIndex == self.BoardItemsArray[11].OpponentIndex ==
                 self.BoardItemsArray[15].OpponentIndex):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) and (
                self.BoardItemsArray[5].OpponentIndex is not None) and \
                (self.BoardItemsArray[0].OpponentIndex == self.BoardItemsArray[5].OpponentIndex == self.BoardItemsArray[
                    10].OpponentIndex) or \
                (self.BoardItemsArray[5].OpponentIndex == self.BoardItemsArray[10].OpponentIndex ==
                 self.BoardItemsArray[15].OpponentIndex):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

        if (current_gobblet.is_on_top_of_stack() is True) and (current_gobblet.is_on_board() is False) and (
                self.BoardItemsArray[6].OpponentIndex is not None) and \
                (self.BoardItemsArray[3].OpponentIndex == self.BoardItemsArray[6].OpponentIndex == self.BoardItemsArray[
                    9].OpponentIndex) or \
                (self.BoardItemsArray[6].OpponentIndex == self.BoardItemsArray[9].OpponentIndex == self.BoardItemsArray[
                    12].OpponentIndex):
            # Check if it is possible to move the gobblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(self, required_position) is True:
                # Call Function place_external_gobblet to place the gobblet on board
                self.place_external_gobblet(current_gobblet, required_position)

    def place_external_gobblet(self, current_gobblet: Gobblet, required_position: BoardItem):
        """
        Places an external Gobblet onto the specified position on the game board, ensuring valid placement.

        Args:
        current_gobblet: The Gobblet to be placed on the board.
        required_position: The target position where the Gobblet should be placed.
        """
        # If the position on board can the gobblet be placed on
        if required_position.IsPossibleBoardMovement(self, current_gobblet) is True:
            # Add the gobblet to the top of the new position
            required_position.AddGobbletOnTop(self, current_gobblet)

    def place_internal_gobblet(self, current_gobblet: Gobblet, required_position: BoardItem):
        """
        Places a Gobblet onto a specified BoardItem position, following game rules.

        Args:
       - current_gobblet (Gobblet): The Gobblet to be placed.
       - required_position (BoardItem): The BoardItem position where the Gobblet should be placed.
        """
        # If the position on board can the gobblet be placed on
        if required_position.IsPossibleBoardMovement(self, current_gobblet) is True:
            # Remove the goblet from the top of its current position
            required_position.RemoveGobbletOnTop(self)
            # Add the gobblet to the top of the new position
            required_position.AddGobbletOnTop(self, current_gobblet)

            # Function that checks whether the game is over or not

    def check_state(self):
        player1_count = 0
        player2_count = 0
        if (self.BoardItemsArray[0].CurrentOwnerIndex is not None) and \
                (self.BoardItemsArray[0].CurrentOwnerIndex == self.BoardItemsArray[1].CurrentOwnerIndex ==
                 self.BoardItemsArray[2].CurrentOwnerIndex == self.BoardItemsArray[3].CurrentOwnerIndex):
            if self.BoardItemsArray[0].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1
        if (self.BoardItemsArray[4].CurrentOwnerIndex is not None) and \
                (self.BoardItemsArray[4].CurrentOwnerIndex == self.BoardItemsArray[5].CurrentOwnerIndex ==
                 self.BoardItemsArray[6].CurrentOwnerIndex == self.BoardItemsArray[7].CurrentOwnerIndex):
            if self.BoardItemsArray[4].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        if (self.BoardItemsArray[8].CurrentOwnerIndex is not None) and \
                (self.BoardItemsArray[8].CurrentOwnerIndex == self.BoardItemsArray[9].CurrentOwnerIndex ==
                 self.BoardItemsArray[10].CurrentOwnerIndex == self.BoardItemsArray[11].CurrentOwnerIndex):
            if self.BoardItemsArray[8].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        if (self.BoardItemsArray[12].CurrentOwnerIndex is not None) and \
                (self.BoardItemsArray[12].CurrentOwnerIndex == self.BoardItemsArray[13].CurrentOwnerIndex ==
                 self.BoardItemsArray[14].CurrentOwnerIndex == self.BoardItemsArray[15].CurrentOwnerIndex):
            if self.BoardItemsArray[12].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        if (self.BoardItemsArray[1].CurrentOwnerIndex is not None) and \
                (self.BoardItemsArray[1].CurrentOwnerIndex == self.BoardItemsArray[5].CurrentOwnerIndex ==
                 self.BoardItemsArray[9].CurrentOwnerIndex == self.BoardItemsArray[13].CurrentOwnerIndex):
            if self.BoardItemsArray[1].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        if (self.BoardItemsArray[2].CurrentOwnerIndex is not None) and \
                (self.BoardItemsArray[2].CurrentOwnerIndex == self.BoardItemsArray[6].CurrentOwnerIndex ==
                 self.BoardItemsArray[10].CurrentOwnerIndex == self.BoardItemsArray[14].CurrentOwnerIndex):
            if self.BoardItemsArray[2].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        if (self.BoardItemsArray[3].CurrentOwnerIndex is not None) and \
                (self.BoardItemsArray[3].CurrentOwnerIndex == self.BoardItemsArray[7].CurrentOwnerIndex ==
                 self.BoardItemsArray[11].CurrentOwnerIndex == self.BoardItemsArray[15].CurrentOwnerIndex):
            if self.BoardItemsArray[3].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        if (self.BoardItemsArray[0].CurrentOwnerIndex is not None) and \
                (self.BoardItemsArray[0].CurrentOwnerIndex == self.BoardItemsArray[5].CurrentOwnerIndex ==
                 self.BoardItemsArray[10].CurrentOwnerIndex == self.BoardItemsArray[15].CurrentOwnerIndex):
            if self.BoardItemsArray[0].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        if (self.BoardItemsArray[3].CurrentOwnerIndex is not None) and \
                (self.BoardItemsArray[3].CurrentOwnerIndex == self.BoardItemsArray[6].CurrentOwnerIndex ==
                 self.BoardItemsArray[9].CurrentOwnerIndex == self.BoardItemsArray[12].CurrentOwnerIndex):
            if self.BoardItemsArray[3].CurrentOwnerIndex == 0:
                player1_count += 1
            else:
                player2_count += 1

        if player1_count == 1:
            self.GameState = "Player1Won"
        elif player2_count == 1:
            self.GameState = "Player2Won"
        elif player1_count == 1 and player2_count == 1:
            self.GameState = "Draw"
        else:
            self.GameState = "OnGoing"

    def corner_case(self):
        """
        Function that makes SkipRoundFlag is True if all positions on board are filled,
        and so we cannot gobbel up with a small piece
        """
        self.SkipRoundFlag = True
        for positions in range(self.BoardSize):
            if self.BoardItemsArray[positions].CurrentOwnerIndex is None:
                self.SkipRoundFlag = False
                return self.SkipRoundFlag

    # For testing purposes        
    def check_gobblet_on_top(self , board_position:BoardItem):
        return board_position.GobbletsStack[-1]


    