import Gobblet
class BoardItem:
    def __init__(self, CurrentOwnerIndexInitValue=None, OnTopGobbletSizeInitValue=None, GobbletsStack=None, NumberOfGobbletsInStack=None):
        """
        Represents a piece on the Gobblet Gobblers board.

        Parameters:
        - CurrentOwnerIndexInitValue (int): Index representing the player (0 or 1)
        - OnTopGobbletSizeInitValue (int): Size of the piece on top of this piece in the stack
        - GobbletsStack (list): List representing the stack of pieces at this position
        - NumberOfGobbletsInStack (int): Number of pieces in the stack
        """

        self.CurrentOwnerIndex = CurrentOwnerIndexInitValue  # Index representing the player (0 or 1)
        self.OnTopGobbletSize = OnTopGobbletSizeInitValue  # Size of the piece on top of this piece in the stack
        self.GobbletsStack = GobbletsStack if GobbletsStack is not None else []  # List representing the stack of pieces at this position
        self.NumberOfGobbletsInStack = NumberOfGobbletsInStack if NumberOfGobbletsInStack is not None else 0  # Number of pieces in the stack
