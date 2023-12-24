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

    def IsEmpty(self):
        """
        Check if the stack of the current board item position is empty.

        Returns:
        - True if the stack is empty, False otherwise.
        """
        return self.NumberOfGobbletsInStack == 0
    
    def AddGobblet(self, gobblet):
        """
        Add a Gobblet to the stack.

        Parameters:
        - gobblet (Gobblet): The Gobblet to be added.
        """
        self.GobbletsStack.append(gobblet)
        self.OnTopGobbletSize = gobblet.Size
        self.NumberOfGobbletsInStack += 1

    def RemoveGobblet(self):
        """
        Remove the top Gobblet from the stack.

        Returns:
        - The removed Gobblet.
        """
        if not self.IsEmpty():
            RemovedGobblet = self.GobbletsStack.pop()
            self.NumberOfGobbletsInStack -= 1
            self.OnTopGobblet = self.GobbletsStack[-1] if self.GobbletsStack else None
            return RemovedGobblet
        else:
            return None