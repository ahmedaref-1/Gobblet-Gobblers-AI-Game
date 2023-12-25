import Gobblet
class BoardItem:
    def __init__(self, Index, CurrentOwnerIndexInitValue=None, OnTopGobbletSizeInitValue=None, GobbletsStack=None, NumberOfGobbletsInStack=None):
        """
        Represents a piece on the Gobblet Gobblers board.

        Parameters:
        - Index (int): Index of the board item position
        - CurrentOwnerIndexInitValue (int): Index representing the player (0 or 1)
        - OnTopGobbletSizeInitValue (int): Size of the piece on top of this piece in the stack
        - GobbletsStack (list): List representing the stack of pieces at this position
        - NumberOfGobbletsInStack (int): Number of pieces in the stack
        """
        self.Index = Index  # Index of the board item position
        self.CurrentOwnerIndex = CurrentOwnerIndexInitValue  # Index representing the player (0 or 1)
        self.OpponentIndex = not self.CurrentOwnerIndex      # Index of the opponent of the current player
        self.OnTopGobbletSize = OnTopGobbletSizeInitValue  # Size of the piece on top of this piece in the stack
        self.GobbletsStack = GobbletsStack if GobbletsStack is not None else []  # List representing the stack of pieces at this position
        self.NumberOfGobbletsInStack = NumberOfGobbletsInStack if NumberOfGobbletsInStack is not None else 0  # Number of pieces in the stack

    def IsEmpty(self):
        """
        Check if the stack of the current board item position is empty.

        Returns:
        - True if the stack is empty, False otherwise.
        """
        # Check if the count of Gobblets in the stack is zero.
        # If zero, the stack is considered empty; otherwise, it is not empty.
        return self.NumberOfGobbletsInStack == 0

    def IsFull(self):
        """
        Check if the stack of the current board item position is full.

        Returns:
        - True if the stack is full, False otherwise.
        """
        # Check if the count of Gobblets in the stack is equal to 4.
        # If equal to 4, the stack is considered full; otherwise, it is not full.
        return self.NumberOfGobbletsInStack == 4
    
    def IsOwnedByPlayer(self, player_index):
        """
        Check if the current board item position is owned by the specified player.

        Parameters:
        - player_index (int): Index representing the player (0 or 1)

        Returns:
        - True if the current board item position is owned by the specified player, False otherwise.
        """
        # Check if the current owner index is equal to the specified player index.
        # If equal, the current board item position is owned by the specified player; otherwise, it is not.
        return self.CurrentOwnerIndex == player_index 

    def IsPossibleBoardMovement(self, gobblet):
        """
        Check if the specified Gobblet can be moved to the current board item position.

        Parameters:
        - gobblet (Gobblet): The Gobblet to be moved.

        Returns:
        - True if the specified Gobblet can be moved to the current board item position, False otherwise.
        """
        # Check if the stack is empty or if the size of the specified Gobblet is greater than
        # the size of the Gobblet on top of the stack.
        # If so, the specified Gobblet can be moved to the current board item position; otherwise, it cannot.
        return self.IsEmpty() or ( not self.IsFull() and gobblet.Size > self.OnTopGobbletSize )  

    def AddGobbletOnTop(self, gobblet):
        """
        Add a Gobblet to the stack.

        Parameters:
        - gobblet (Gobblet): The Gobblet to be added.
        """
        # Check if the stack is not full and if the size of the new Gobblet is greater than
        # the size of the Gobblet on top of the stack.
        if not self.IsFull() and gobblet.Size > self.OnTopGobbletSize:
            if not self.IsEmpty():
                # Set the IsOnTop flag of the Gobblet on top of the stack to False. 
                self.GobbletsStack[-1].gobblet.IsOnTop = False
                
            # Append the new Gobblet to the stack.
            self.GobbletsStack.append(gobblet)

            # Update the current owner index based on the new Gobblet.
            self.CurrentOwnerIndex = gobblet.OwnerIndex

            # Update the size of the Gobblet on top of the stack to the size of the new Gobblet.
            self.OnTopGobbletSize = gobblet.Size

            # Increment the count of Gobblets in the stack.
            self.NumberOfGobbletsInStack += 1

    def RemoveGobbletOnTop(self):
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

            # Set the IsOnTop flag of the Gobblet on top of the stack to True.
            self.GobbletsStack[-1].gobblet.IsOnTop = True

            # Decrement the count of Gobblets in the stack.
            self.NumberOfGobbletsInStack -= 1

            # Return the removed Gobblet.
            return RemovedGobblet
        else:
            # If the stack is empty, return None.
            return None

    def GetOwnerIndex(self):
        """
        Get the current owner index of the board item position.

        Returns:
        - The current owner index of the board item position.
        """
        return self.CurrentOwnerIndex
    
    def GetOnTopGobbletSize(self):
        """
        Get the size of the Gobblet on top of the stack.

        Returns:
        - The size of the Gobblet on top of the stack.
        """
        return self.OnTopGobbletSize
    
