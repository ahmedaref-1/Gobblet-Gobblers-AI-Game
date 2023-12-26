# Import necessary modules for the Gobblet Gobblers game implementation
import Gobblet  # Gobblet module contains the Gobblet class
import BoardItem  # BoardItem module contains the BoardItem class
from Action import MoveID  # Action module contains the MoveID class used for representing moves in the game


class Game:
    def __init__(self):
        """
        Represents the Gobblet Gobblers game.

        Initializes the game state, player information, and the game board.

        Attributes:
        - PlayerNames: List containing names of both players.
        - GameState: State of the game (OnGoing, Draw, Player1Won, Player2Won).
        - Winner: Winner of the game (initially None).
        - SkipRoundFlag: Flag used to skip the current round.

        - NumberOfGobbletsPerPlayer: Number of gobblets per player.
        - BoardSize: Size of the game board (number of cells).

        - FirstPlayerGobbletsArray: List to store Gobblet objects of the First Player.
        - SecondPlayerGobbletsArray: List to store Gobblet objects of the Second Player.
        - BoardItemsArray: List to store BoardItem objects representing the game board.

        - CurrentPlayerIndex: Index of the current player (0 or 1).
        - SelectedGobbletID: ID of the selected Gobblet for the current move.
        - SelectedBoardItemIndex: Index of the selected BoardItem for the current move.
        """
        self.PlayerNames = ["Player1", "Player2"]  # List containing names of both players
        self.GameState = "OnGoing"  # State of the game (OnGoing, Draw, Player1Won, Player2Won)
        self.Winner = None  # Winner of the game (initially None)
        self.SkipRoundFlag = False  # Flag used to skip the current round

        self.NumberOfGobbletsPerPlayer = 12  # Number of gobblets per player
        self.BoardSize = 16  # Size of the game board (number of cells)

        # Initialize FirstPlayerGobbletsArray with Gobblet objects for the First Player
        self.FirstPlayerGobbletsArray = []
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

        # Initialize SecondPlayerGobbletsArray with Gobblet objects for the Second Player
        self.SecondPlayerGobbletsArray = []
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

        # Initialize BoardItemsArray with BoardItem objects representing the game board
        self.BoardItemsArray = []
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
        Determines and returns a list of all Goblets that can be placed for the current player.

        Returns:
        A list containing the IDs of all Goblets that can be moved.
        """
        possible_gobblets = []

        # Check for the current player
        current_player_gobblets_array = (
            self.FirstPlayerGobbletsArray
            if self.CurrentPlayerIndex == 0
            else self.SecondPlayerGobbletsArray
        )

        # Iterate through all available Goblet IDs for the current player, considering both internal and external ones.
        for goblet_id in range(self.NumberOfGobbletsPerPlayer):
            # Check if the goblet is on top.
            if current_player_gobblets_array[goblet_id].is_on_top_of_stack():
                possible_gobblets.append(goblet_id)

        return possible_gobblets

    def list_possible_moves(self, current_gobblet: Gobblet) -> list[MoveID]:
        """
        Checks the positions on the board where the goblet can move to.

        Args:
        current_gobblet: The goblet for which to determine possible positions on the board.

        Returns:
        A list of possible positions on the board that the goblet can move to.
        """
        # Initialize an empty array to store possible moves
        possible_moves = []

        # Iterate through all squares on the board
        for square_id in range(self.BoardSize):
            # Check if the goblet can move to the position on the board
            if current_gobblet.is_possible_gobblet_movement(self.BoardItemsArray[square_id]):
                # Create a MoveID object with the current goblet and the possible square ID it can move to
                new_valid_move = MoveID(current_gobblet, square_id)
                # Add MoveID to the array of possible moves
                possible_moves.append(new_valid_move)

        return possible_moves

    def all_valid_moves(self) -> list[MoveID]:
        """
        Determines and returns a list of all valid moves for all available goblet IDs
        that can be placed on the specified position.

        Returns:
        A list containing the valid positions of all available goblets.
        """
        # Get a list of all available goblets
        all_available_gobblets = self.list_possible_gobblets()

        # Initialize the list to store valid moves
        valid_actions = []

        # Iterate through each available goblet
        for goblet_id in all_available_gobblets:
            # Get the list of possible moves for the current goblet
            current_player_gobblet = (
                self.FirstPlayerGobbletsArray[goblet_id]
                if self.CurrentPlayerIndex == 0
                else self.SecondPlayerGobbletsArray[goblet_id]
            )
            possible_moves = self.list_possible_moves(current_player_gobblet)

            # Extend the valid_actions list with the possible moves for the current goblet
            valid_actions.extend(possible_moves)

        return valid_actions

    def make_move(self, current_gobblet: Gobblet, required_position: BoardItem):
        """
        Moves a Gobblet from its current position to the specified target position on the board.

        Args:
        current_gobblet: The Gobblet to be moved.
        required_position: The target position on the board where the Gobblet should be moved.
        """
        # Check if the goblet is on top of the stack and is already on the board
        if current_gobblet.is_on_top_of_stack() and current_gobblet.is_on_board():
            # Check if the goblet can be placed on the board
            if current_gobblet.is_possible_gobblet_movement(required_position):
                # Call the function place_internal_gobblet to place the goblet on the board
                self.place_internal_gobblet(
                    current_gobblet, required_position, self.BoardItemsArray[current_gobblet.get_gobblet_position()]
                )

        # Check if the goblet is on top and is NOT placed on the board (External Goblet)
        if current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and required_position.is_empty():
            # Check if it is possible to move the goblet to the specified position
            if current_gobblet.is_possible_gobblet_movement(required_position):
                # Call Function place_external_gobblet to place the goblet on board
                self.place_external_gobblet(self, current_gobblet, required_position)

        # Check for specific patterns for placing external goblets
        if current_gobblet.is_on_top_of_stack() and not current_gobblet.is_on_board() and required_position.is_empty():
            if (
                    (self.BoardItemsArray[1].CurrentOpponentIndex == self.BoardItemsArray[2].CurrentOpponentIndex ==
                     self.BoardItemsArray[3].CurrentOpponentIndex) or
                    (self.BoardItemsArray[1].CurrentOpponentIndex == self.BoardItemsArray[5].CurrentOpponentIndex ==
                     self.BoardItemsArray[9].CurrentOpponentIndex) or
                    (self.BoardItemsArray[5].CurrentOpponentIndex == self.BoardItemsArray[6].CurrentOpponentIndex ==
                     self.BoardItemsArray[7].CurrentOpponentIndex) or
                    (self.BoardItemsArray[9].CurrentOpponentIndex == self.BoardItemsArray[10].CurrentOpponentIndex ==
                     self.BoardItemsArray[11].CurrentOpponentIndex) or
                    (self.BoardItemsArray[13].CurrentOpponentIndex == self.BoardItemsArray[14].CurrentOpponentIndex ==
                     self.BoardItemsArray[15].CurrentOpponentIndex)
            ):
                if current_gobblet.is_possible_gobblet_movement(required_position):
                    # Call Function place_external_gobblet to place the goblet on board
                    self.place_external_gobblet(self, current_gobblet, required_position)

            if (
                    (self.BoardItemsArray[5].CurrentOpponentIndex == self.BoardItemsArray[1].CurrentOpponentIndex ==
                     self.BoardItemsArray[9].CurrentOpponentIndex) or
                    (self.BoardItemsArray[5].CurrentOpponentIndex == self.BoardItemsArray[9].CurrentOpponentIndex ==
                     self.BoardItemsArray[13].CurrentOpponentIndex)
            ):
                if current_gobblet.is_possible_gobblet_movement(required_position):
                    # Call Function place_external_gobblet to place the goblet on board
                    self.place_external_gobblet(self, current_gobblet, required_position)

            if (
                    (self.BoardItemsArray[6].CurrentOpponentIndex == self.BoardItemsArray[2].CurrentOpponentIndex ==
                     self.BoardItemsArray[10].CurrentOpponentIndex) or
                    (self.BoardItemsArray[6].CurrentOpponentIndex == self.BoardItemsArray[10].CurrentOpponentIndex ==
                     self.BoardItemsArray[14].CurrentOpponentIndex)
            ):
                if current_gobblet.is_possible_gobblet_movement(required_position):
                    # Call Function place_external_gobblet to place the goblet on board
                    self.place_external_gobblet(self, current_gobblet, required_position)

            if (
                    (self.BoardItemsArray[7].CurrentOpponentIndex == self.BoardItemsArray[3].CurrentOpponentIndex ==
                     self.BoardItemsArray[11].CurrentOpponentIndex) or
                    (self.BoardItemsArray[7].CurrentOpponentIndex == self.BoardItemsArray[11].CurrentOpponentIndex ==
                     self.BoardItemsArray[15].CurrentOpponentIndex)
            ):
                if current_gobblet.is_possible_gobblet_movement(required_position):
                    # Call Function place_external_gobblet to place the goblet on board
                    self.place_external_gobblet(self, current_gobblet, required_position)

            if (
                    (self.BoardItemsArray[5].CurrentOpponentIndex == self.BoardItemsArray[0].CurrentOpponentIndex ==
                     self.BoardItemsArray[10].CurrentOpponentIndex) or
                    (self.BoardItemsArray[5].CurrentOpponentIndex == self.BoardItemsArray[10].CurrentOpponentIndex ==
                     self.BoardItemsArray[15].CurrentOpponentIndex)
            ):
                if current_gobblet.is_possible_gobblet_movement(required_position):
                    # Call Function place_external_gobblet to place the goblet on board
                    self.place_external_gobblet(self, current_gobblet, required_position)

            if (
                    (self.BoardItemsArray[6].CurrentOpponentIndex == self.BoardItemsArray[3].CurrentOpponentIndex ==
                     self.BoardItemsArray[9].CurrentOpponentIndex) or
                    (self.BoardItemsArray[6].CurrentOpponentIndex == self.BoardItemsArray[9].CurrentOpponentIndex ==
                     self.BoardItemsArray[12].CurrentOpponentIndex)
            ):
                if current_gobblet.is_possible_gobblet_movement(required_position):
                    # Call Function place_external_gobblet to place the goblet on board
                    self.place_external_gobblet(self, current_gobblet, required_position)

    @staticmethod
    def place_external_gobblet(self, current_gobblet: Gobblet, required_position: BoardItem):
        """
        Places an external Gobblet onto the specified position on the game board, ensuring valid placement.

        Args:
        current_gobblet: The Gobblet to be placed on the board.
        required_position: The target position where the Gobblet should be placed.
        """
        # Check if the position on the board allows the gobblet to be placed
        if required_position.is_possible_board_movement(current_gobblet):
            next_gobblet_index = current_gobblet.get_gobblet_index() + 1
            if self.CurrentPlayerIndex == 0:
                self.FirstPlayerGobbletsArray[next_gobblet_index].set_gobblet_on_top_of_stack_flag(True)
            else:
                self.SecondPlayerGobbletsArray[next_gobblet_index].set_gobblet_on_top_of_stack_flag(True)

            # Add the gobblet to the top of the new position
            required_position.add_gobblet_on_top(current_gobblet)
            current_gobblet.update_gobblet_position(required_position)

    @staticmethod
    def place_internal_gobblet(current_gobblet: Gobblet, required_position: BoardItem, old_position: BoardItem):
        """
        Places a Gobblet onto a specified BoardItem position, following game rules.

        Args:
        - current_gobblet (Gobblet): The Gobblet to be placed.
        - required_position (BoardItem): The BoardItem position where the Gobblet should be placed.
        """
        # Check if the position on the board allows the gobblet to be placed
        if required_position.is_possible_board_movement(current_gobblet):
            # Remove the goblet from the top of its old position
            old_position.remove_gobblet_on_top()
            # Add the gobblet to the top of the new position
            required_position.add_gobblet_on_top(current_gobblet)
            current_gobblet.update_gobblet_position(required_position)

    def check_state(self):
        player1_count = 0
        player2_count = 0

        # Check for horizontal wins
        for i in range(4):
            if (self.BoardItemsArray[i].CurrentOwnerIndex is not None) and \
                    (self.BoardItemsArray[i].CurrentOwnerIndex == self.BoardItemsArray[i + 4].CurrentOwnerIndex ==
                     self.BoardItemsArray[i + 8].CurrentOwnerIndex == self.BoardItemsArray[i + 12].CurrentOwnerIndex):
                if self.BoardItemsArray[i].CurrentOwnerIndex == 0:
                    player1_count += 1
                else:
                    player2_count += 1

        # Check for vertical wins
        for i in range(0, 13, 4):
            if (self.BoardItemsArray[i].CurrentOwnerIndex is not None) and \
                    (self.BoardItemsArray[i].CurrentOwnerIndex == self.BoardItemsArray[i + 1].CurrentOwnerIndex ==
                     self.BoardItemsArray[i + 2].CurrentOwnerIndex == self.BoardItemsArray[i + 3].CurrentOwnerIndex):
                if self.BoardItemsArray[i].CurrentOwnerIndex == 0:
                    player1_count += 1
                else:
                    player2_count += 1

        # Check for diagonal wins
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

        # Check for winner
        if player1_count == 1:
            self.GameState = "Player1Won"
            self.Winner = 0
        elif player2_count == 1:
            self.GameState = "Player2Won"
            self.Winner = 1
        else:
            self.GameState = "OnGoing"
            self.Winner = None

    def corner_case(self):
        """
        Function that sets SkipRoundFlag to True if all positions on the board are filled,
        indicating that small pieces cannot gobble up.
        """
        self.SkipRoundFlag = all(position.CurrentOwnerIndex is not None for position in self.BoardItemsArray)

    def update_board_array_opponent_index(self):
        """
        Updates the opponent index for all positions on the game board.
        """
        for position in self.BoardItemsArray:
            position.update_opponent_index()

    # For testing purposes
    @staticmethod
    def check_gobblet_on_top(board_position: BoardItem):
        """
        Returns the gobblet on top of the specified board position for testing purposes.
        """
        return board_position.get_gobblet_on_top()
