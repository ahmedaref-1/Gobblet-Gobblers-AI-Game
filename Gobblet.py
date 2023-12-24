class Gobblet:
    def __init__(self, ID, OwnerIndex, Size, CurrentBoardPositionIndexInitValue=None, PreviousBoardPositionIndexInitValue=None, IsOnTop=False):
        """
        Represents a Gobblet piece.

        Parameters:
        - ID (int): Unique ID for the Gobblet
        - OwnerIndex (int): Index representing the player (0 or 1)
        - Size (int): Size of the Gobblet piece (1, 2, 3 or 4)
        - CurrentBoardPositionIndex (int): Current index of the position of the Gobblet on the game board 
        - PreviousBoardPositionIndex (int): Previous index of the position of the Gobblet on the game board 
        - IsOnTop (bool): Flag indicating if the Gobblet is on top of a stack (default is False)
        """
        self.ID = ID  # Unique ID for the Gobblet
        self.OwnerIndex = OwnerIndex  # Index representing the player (0 or 1)
        self.Size = Size  # Size of the Gobblet piece (1, 2, 3 or 4)
        self.CurrentBoardPositionIndex = CurrentBoardPositionIndexInitValue  # Current position on the game board 
        self.PreviousBoardPositionIndex = PreviousBoardPositionIndexInitValue  # Previous position on the game board 
        self.IsOnTop = IsOnTop  # Flag indicating if the Gobblet is on top of a stack (default is False)

    def IsOwnedByPlayer(self, player_index):
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
    
    def IsOnTopOfStack(self):
        """
        Check if the current Gobblet is on top of a stack.

        Returns:
        - True if the current Gobblet is on top of a stack, False otherwise.
        """
        # Check if the IsOnTop flag is True.
        # If True, the current Gobblet is on top of a stack; otherwise, it is not.
        return self.IsOnTop
    
    def IsOnBoard(self):
        """
        Check if the current Gobblet is on the board.

        Returns:
        - True if the current Gobblet is on the board, False otherwise.
        """
        # Check if the CurrentBoardPositionIndex is not None.
        # If not None, the current Gobblet is on the board; otherwise, it is not.
        return self.CurrentBoardPositionIndex is not None
    
    def IsPossibleMove(self, board_item):
        """
        Check if the current Gobblet can be moved to the specified board item position.

        Parameters:
        - board_item (BoardItem): The board item position to be moved to.

        Returns:
        - True if the current Gobblet can be moved to the specified board item position, False otherwise.
        """
        # Check if the specified board item position is empty.
        # If empty, the current Gobblet can be moved to the specified board item position; otherwise, it cannot.
        return board_item.IsEmpty() or((not board_item.IsFull()) and (self.Size > board_item.OnTopGobbletSize))

    def GetGobbletOwnedPositionIndex(self):
        """
        Get the position of the current Gobblet.

        Returns:
        - The position of the current Gobblet.
        """
        # Check if the current Gobblet is on the board and on the top of the stack of this bord position.
        # If so, return the current board position index; otherwise, return None.
        if self.IsOnBoard() and self.IsOnTopOfStack():
            return self.CurrentBoardPositionIndex
        else:
            return None
    