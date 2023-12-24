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
        # Check if the stack is empty or if the size of the new Gobblet is greater than
        # the size of the Gobblet on top of the stack.
        if self.IsEmpty() or gobblet.Size > self.OnTopGobbletSize:
            # Append the new Gobblet to the stack.
            self.GobbletsStack.append(gobblet)

            # Update the current owner index based on the new Gobblet.
            self.CurrentOwnerIndex = gobblet.OwnerIndex

            # Update the size of the Gobblet on top of the stack to the size of the new Gobblet.
            self.OnTopGobbletSize = gobblet.Size

            # Increment the count of Gobblets in the stack.
            self.NumberOfGobbletsInStack += 1

    def RemoveGobblet(self):
        """
        Remove the top Gobblet from the stack.

        Returns:
        - The removed Gobblet. If the stack is empty, returns None.
        """
        # Check if the stack is not empty before attempting to remove a Gobblet.
        if not self.IsEmpty():
            # Remove the top Gobblet from the stack using pop().
            RemovedGobblet = self.GobbletsStack.pop()

            # Update the current owner index based on the Gobblet on top of the stack.
            # If the stack is empty, set the current owner index to None.
            self.CurrentOwnerIndex = self.GobbletsStack[-1].gobblet.OwnerIndex if self.GobbletsStack else None

            # Update the size of the Gobblet on top of the stack.
            # If the stack is empty, set the OnTopGobbletSize to None.
            self.OnTopGobbletSize = self.GobbletsStack[-1].gobblet.Size if self.GobbletsStack else None

            # Decrement the count of Gobblets in the stack.
            self.NumberOfGobbletsInStack -= 1

            # Return the removed Gobblet.
            return RemovedGobblet
        else:
            # If the stack is empty, return None.
            return None
