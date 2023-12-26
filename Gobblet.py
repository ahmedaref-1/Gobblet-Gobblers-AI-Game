# Importing the BoardItem class from the BoardItem module
import BoardItem


# Defining a class named Gobblet
class Gobblet:
    def __init__(self, gobblet_id, gobblet_owner_index, gobblet_size):
        """
        Represents a Gobblet piece.

        Parameters:
        - ID (int): Unique ID for the Gobblet
        - OwnerIndex (int): Index representing the player (0 or 1)
        - Size (int): Size of the Gobblet piece (1, 2, 3 or 4)

        """
        # Initializing instance variables with provided values
        self.ID = gobblet_id  # Unique ID for the Gobblet
        self.OwnerIndex = gobblet_owner_index  # Index representing the player (0 or 1)
        self.Size = gobblet_size  # Size of the Gobblet piece (1, 2, 3 or 4)
        self.CurrentBoardPositionIndex = None  # Current position on the game board (initially none)
        self.PreviousBoardPositionIndex = None  # Previous position on the game board (initially none)
        self.IsOnTop = False  # Flag indicating if the Gobblet is on top of a stack (initially False)

    def is_owned_by_player(self, player_index):
        """
        Check if the current Gobblet is owned by the specified player.

        Parameters:
        - player_index (int): Index representing the player (0 or 1)

        Returns:
        - True if the current Gobblet is owned by the specified player, False otherwise.
        """
        # Check if the current owner index is equal to the specified player index.
        # If equal, the current Gobblet is owned by the specified player; otherwise, it is not.
        return self.OwnerIndex == player_index

    def is_on_top_of_stack(self):
        """
        Check if the current Gobblet is on top of a stack.

        Returns:
        - True if the current Gobblet is on top of a stack, False otherwise.
        """
        # Check if the IsOnTop flag is True.
        # If True, the current Gobblet is on top of a stack; otherwise, it is not.
        return self.IsOnTop

    def is_on_board(self):
        """
        Check if the current Gobblet is on the board.

        Returns:
        - True if the current Gobblet is on the board, False otherwise.
        """
        # Check if the CurrentBoardPositionIndex is not None.
        # If not None, the current Gobblet is on the board; otherwise, it is not.
        if self.CurrentBoardPositionIndex is not None:
            return True
        else:
            return False

    def is_possible_gobblet_movement(self, board_item):
        """
        Check if the current Gobblet can be moved to the specified board item position.

        Parameters:
        - board_item (BoardItem): The board item position to be moved to.

        Returns:
        - True if the current Gobblet can be moved to the specified board item position, False otherwise.
        """
        # Check if the specified board item position is empty.
        # If empty, the current Gobblet can be moved to the specified board item position; otherwise, it cannot.
        return board_item.is_empty() or ((not board_item.is_full()) and (self.Size > board_item.OnTopGobbletSize))

    def get_gobblet_owned_position_index(self):
        """
        Get the position of the current Gobblet.

        Returns:
        - The position of the current Gobblet.
        """
        # Check if the current Gobblet is on the board and on the top of the stack of this board position.
        # If so, return the current board position index; otherwise, return None.
        if self.is_on_board() and self.is_on_top_of_stack():
            return self.CurrentBoardPositionIndex
        else:
            return None

    def set_gobblet_on_top_of_stack_flag(self, flag_value):
        """
        Set the IsOnTop flag of the current Gobblet to the specified value.

        Parameters:
        - flag_value (bool): The value to be set for the IsOnTop flag.
        """
        self.IsOnTop = flag_value

    def update_gobblet_position(self, board_position: BoardItem):
        """
        Update the position of the current Gobblet.

        Parameters:
        - board_position (BoardItem): The new board position of the Gobblet.
        """
        if self.CurrentBoardPositionIndex is None:
            # If the Gobblet was not on the board before,
            # update the current position and set the previous position to None.
            self.CurrentBoardPositionIndex = board_position.Index
            self.PreviousBoardPositionIndex = None
        else:
            # If the Gobblet was already on the board, update both current and previous positions.
            self.PreviousBoardPositionIndex = self.CurrentBoardPositionIndex
            self.CurrentBoardPositionIndex = board_position.Index

    def get_gobblet_position(self):
        """
        Get the current position index of the Gobblet on the board.

        Returns:
        - The current position index of the Gobblet on the board.
        """
        return self.CurrentBoardPositionIndex

    def get_gobblet_index(self):
        """
        Get the unique ID (index) of the Gobblet.

        Returns:
        - The unique ID (index) of the Gobblet.
        """
        return self.ID
