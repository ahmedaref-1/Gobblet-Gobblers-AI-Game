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


