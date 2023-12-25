from Gobblet import Gobblet
from BoardItem import BoardItem
from Action import MoveID
from typing import List


class Game:
    def __init__(self):
        """
        Represents the Gobblet Gobblers game.

        """
        self.PlayerNames = ["Player1", "Player2"]  # List containing names of both players
        self.GameState = "OnGoing"  # State of the game (OnGoing, Draw, Player1Won, Player2Won)
        self.Winner = None  # Winner of the game (initially None)

        self.NumberOfGobbletsperPlayer = 12  # Number of gobblets per player
        self.BoardSize = 16  # Size of the game board (number of cells)

        self.FirstPlayerGobbletsArray = []  # List to store Gobblet objects of the First Player
        CreatedGobbletSize = 4
        for i in range(self.NumberOfGobbletsperPlayer):
            # Create a new Gobblet object
            tempGobblet = Gobblet.Gobblet(i, 0, CreatedGobbletSize)
            CreatedGobbletSize -= 1
            # Reset the CreatedGobbletSize to 4 if it is less than 1
            if CreatedGobbletSize < 1:
                CreatedGobbletSize = 4
            # Set the isOnTop flag to True if the current Gobblet is of size 4
            if tempGobblet.Size == 4:
                tempGobblet.IsOnTop = True
            # Add the new Gobblet object to the appropriate list
            self.FirstPlayerGobbletsArray.append(tempGobblet)

        self.SecondPlayerGobbletsArray = []  # List to store Gobblet objects of the Second Player
        CreatedGobbletSize = 4
        for i in range(self.NumberOfGobbletsperPlayer):
            # Create a new Gobblet object
            tempGobblet = Gobblet.Gobblet(i, 0, CreatedGobbletSize)
            CreatedGobbletSize -= 1
            # Reset the CreatedGobbletSize to 4 if it is less than 1
            if CreatedGobbletSize < 1:
                CreatedGobbletSize = 4
            # Set the isOnTop flag to True if the current Gobblet is of size 4
            if tempGobblet.Size == 4:
                tempGobblet.IsOnTop = True
            # Add the new Gobblet object to the appropriate list
            self.SecondPlayerGobbletsArray.append(tempGobblet)

        self.BoardItemsArray = []  # List to store BoardItem objects
        for i in range(self.BoardSize):
            # Create a new BoardItem object
            tempBoardItem = BoardItem.BoardItem(i)
            # Add the new BoardItem object to the list
            self.BoardItemsArray.append(tempBoardItem)

        self.CurrentPlayerIndex = 0  # Index of the current player (0 or 1)
        self.SelectedGobbletID = None  # ID of the selected Gobblet for the current move
        self.SelectedBoardItemIndex = None  # Index of the selected BoardItem for the current move

    def ListPossibleGobblets(self) -> list:
        """
        Determines and returns a list of all Goblets that can be placed of a specific player.

        Args:
        CurrentPlayerIndex: To indicate the player.

        Returns:
        A list containing the IDs of all Goblets that can be moved.
        """
        possible_gobblets = []
        # Check for Player 1
        if self.CurrentPlayerIndex is 0 :
            # Iterate through all available Goblet IDs of player 1, considering both internal and external ones.
            for goblet_id in range(self.NumberOfGobbletsperPlayer):
                # Check if the gobblet is on top.
                if self.FirstPlayerGobbletsArray[goblet_id].IsOnTopOfStack():
                    possible_gobblets.append(goblet_id)

        # Check for Player 2
        if self.CurrentPlayerIndex is 1 :
            # Iterate through all available Goblet IDs of player 2, considering both internal and external ones.
            for goblet_id in range(self.NumberOfGobbletsperPlayer):
                # Check if the gobblet is on top.
                if self.SecondPlayerGobbletsArray[goblet_id].IsOnTopOfStack():
                    possible_gobblets.append(goblet_id)            

        return possible_gobblets
    

    def ListPossibleMoves(self, CurrentGobblet: Gobblet) -> list[MoveID]:
        """
        Checks the positions on board that the gobblet can move to.

        Args:
        CurrentGobblet: The gobblet which I want what are the possible positions on board to place it on

        Returns:
        - List of possible positions on board that the goblet can move to.
        """

        # Initialize an empty array to store possible moves
        possible_moves = []
        # Iterate around all squares on board
        for SquareID in range(self.BoardSize):
            # Check if the gobblet can move to the position on board
            if CurrentGobblet.IsPossibleGobbletMovement(self, self.BoardItemsArray[SquareID]):
                # Create an object with the current gobblet and the possible squareID it can move to
                NewValidMove = MoveID(Gobblet, SquareID)
                # Add MoveID to the array
                possible_moves.append(NewValidMove)
        # Return the array of possible moves
        return possible_moves    

    def AllValidMoves(self) -> list[MoveID]:
        """
        Determines and returns a list of all valid moves for all available gobblet IDs that can be placed on the specified position.

        Returns:
        A list containing the valid positions of all available gobblets.
        """
        # Get a list of all available gobblets
        AllAvailableGobblets = self.ListPossibleGobblets()

        # Initialize the list to store valid moves
        ValidActions = []

        # Iterate through each available gobblet
        for gobblet in AllAvailableGobblets:
            # Get the list of possible moves for the current gobblet
            possible_moves = self.ListPossibleMoves(gobblet)

            # Extend the ValidActions list with the possible moves for the current gobblet
            ValidActions.extend(possible_moves)

        # Return the final list of valid moves
        return ValidActions

    def MakeMove(self, CurrentGobblet: Gobblet, RequiredPosition: BoardItem):
        """
        Moves a Gobblet from its current position to the specified target position on the board.

        Args:
        current_gobblet: The Gobblet to be moved.
        required_position: The target position on the board where the Gobblet should be moved.
        """
        # Check if the gobblet is on top of stack and that it is already on the board
        if (CurrentGobblet.IsOnTopOfStack() is True) and (CurrentGobblet.IsOnBoard() is True):
            # Check if the gobblet can be placed on the board
            if CurrentGobblet.IsPossibleGobbletMovement(self, RequiredPosition) is True:
                # Call the function PlaceInternalGobblet to place the gobblet on board
                self.PlaceInternalGobblet(CurrentGobblet, RequiredPosition)

        # Check if the gobblet is on top and that it is NOT placed on board
        if (CurrentGobblet.IsOnTopOfStack() is True) and (CurrentGobblet.IsOnBoard() is False ) and (RequiredPosition.IsEmpty() is True):
            # Check if it is possible to move the gobblet to the specified position
            if CurrentGobblet.IsPossibleGobbletMovement(self, RequiredPosition) is True:
                # Call Function PlaceExternalGobblet to place the gobblet on board
                self.PlaceExternalGobblet(CurrentGobblet, RequiredPosition)

    def PlaceExternalGobblet (self,CurrentGobblet:Gobblet, RequiredPosition:BoardItem): 
        """
        Places an external Gobblet onto the specified position on the game board, ensuring valid placement.

        Args:
        current_gobblet: The Gobblet to be placed on the board.
        required_position: The target position where the Gobblet should be placed.
        """
        # If the position on board can the gobblet be placed on
        if RequiredPosition.IsPossibleBoardMovement(self, CurrentGobblet) is True:
            # Add the gobblet to the top of the new postion
            RequiredPosition.AddGobbletOnTop(self, CurrentGobblet)   

    def PlaceInternalGobblet (self,CurrentGobblet:Gobblet, RequiredPosition:BoardItem): 
        """
        Places a Gobblet onto a specified BoardItem position, following game rules.

        Args:
       - CurrentGobblet (Gobblet): The Gobblet to be placed.
       - RequiredPosition (BoardItem): The BoardItem position where the Gobblet should be placed.
        """
        # If the position on board can the gobblet be placed on
        if RequiredPosition.IsPossibleBoardMovement(self, CurrentGobblet) is True:
            # Remove the goblet from the top of its current position
            RequiredPosition.RemoveGobbletOnTop(self)
            # Add the gobblet to the top of the new postion
            RequiredPosition.AddGobbletOnTop(self, CurrentGobblet)          

    # Function that checks whether the game is over or not
    def CheckWinner(self):
        if (self.BoardItemsArray[0].CurrentOwnerIndex is not None) and \
        (self.BoardItemsArray[0].CurrentOwnerIndex == self.BoardItemsArray[1].CurrentOwnerIndex ==
        self.BoardItemsArray[2].CurrentOwnerIndex == self.BoardItemsArray[3].CurrentOwnerIndex):
            if self.BoardItemsArray[0].CurrentOwnerIndex == 0:
                self.GameState = "Player1Won"
            else :
                self.GameState = "Player2Won"
        if (self.BoardItemsArray[4].CurrentOwnerIndex is not None) and \
        (self.BoardItemsArray[4].CurrentOwnerIndex == self.BoardItemsArray[5].CurrentOwnerIndex ==
        self.BoardItemsArray[6].CurrentOwnerIndex == self.BoardItemsArray[7].CurrentOwnerIndex):
            if self.BoardItemsArray[4].CurrentOwnerIndex == 0:
                self.GameState = "Player1Won"
            else :
                self.GameState = "Player2Won"

        if (self.BoardItemsArray[8].CurrentOwnerIndex is not None) and \
        (self.BoardItemsArray[8].CurrentOwnerIndex == self.BoardItemsArray[9].CurrentOwnerIndex ==
        self.BoardItemsArray[10].CurrentOwnerIndex == self.BoardItemsArray[11].CurrentOwnerIndex):
            if self.BoardItemsArray[8].CurrentOwnerIndex == 0:
                self.GameState = "Player1Won"
            else :
                self.GameState = "Player2Won"

        if (self.BoardItemsArray[12].CurrentOwnerIndex is not None) and \
        (self.BoardItemsArray[12].CurrentOwnerIndex == self.BoardItemsArray[13].CurrentOwnerIndex ==
        self.BoardItemsArray[14].CurrentOwnerIndex == self.BoardItemsArray[15].CurrentOwnerIndex):
            if self.BoardItemsArray[12].CurrentOwnerIndex == 0:
                self.GameState = "Player1Won"
            else :
                self.GameState = "Player2Won"
             
        if (self.BoardItemsArray[1].CurrentOwnerIndex is not None) and \
        (self.BoardItemsArray[1].CurrentOwnerIndex == self.BoardItemsArray[5].CurrentOwnerIndex ==
        self.BoardItemsArray[9].CurrentOwnerIndex == self.BoardItemsArray[13].CurrentOwnerIndex):
            if self.BoardItemsArray[1].CurrentOwnerIndex == 0:
                self.GameState = "Player1Won"
            else :
                self.GameState = "Player2Won"
  
        if (self.BoardItemsArray[2].CurrentOwnerIndex is not None) and \
        (self.BoardItemsArray[2].CurrentOwnerIndex == self.BoardItemsArray[6].CurrentOwnerIndex ==
        self.BoardItemsArray[10].CurrentOwnerIndex == self.BoardItemsArray[14].CurrentOwnerIndex):
            if self.BoardItemsArray[2].CurrentOwnerIndex == 0:
                self.GameState = "Player1Won"
            else :
                self.GameState = "Player2Won"
       
        if (self.BoardItemsArray[3].CurrentOwnerIndex is not None) and \
        (self.BoardItemsArray[3].CurrentOwnerIndex == self.BoardItemsArray[7].CurrentOwnerIndex ==
        self.BoardItemsArray[11].CurrentOwnerIndex == self.BoardItemsArray[15].CurrentOwnerIndex):
            if self.BoardItemsArray[3].CurrentOwnerIndex == 0:
                self.GameState = "Player1Won"
            else :
                self.GameState = "Player2Won"

        if (self.BoardItemsArray[0].CurrentOwnerIndex is not None) and \
        (self.BoardItemsArray[0].CurrentOwnerIndex == self.BoardItemsArray[5].CurrentOwnerIndex ==
        self.BoardItemsArray[10].CurrentOwnerIndex == self.BoardItemsArray[15].CurrentOwnerIndex):
            if self.BoardItemsArray[0].CurrentOwnerIndex == 0:
                self.GameState = "Player1Won"
            else :
                self.GameState = "Player2Won"

        if (self.BoardItemsArray[3].CurrentOwnerIndex is not None) and \
        (self.BoardItemsArray[3].CurrentOwnerIndex == self.BoardItemsArray[6].CurrentOwnerIndex ==
        self.BoardItemsArray[9].CurrentOwnerIndex == self.BoardItemsArray[12].CurrentOwnerIndex):
            if self.BoardItemsArray[3].CurrentOwnerIndex == 0:
                self.GameState = "Player1Won"
            else :
                self.GameState = "Player2Won"

    
    # Function that makes SkipRoundFlag is True if all positions on board are filled and so we cannot gobbel up with a small piece                        
    def CornerCase (self, CurrentGobblet:Gobblet, CurrentBoardItem:BoardItem):
        self.SkipRoundFlag = True
        for positions in range (self.BoardItemsArray):  
            if not CurrentBoardItem.IsEmpty is False:
                self.SkipRoundFlag = False
                return self.SkipRoundFlag

    # Function to return what is on top of stack regarding a specific position on board       
    def GobbletOnTop(self , BoardPosition:BoardItem):
            return BoardPosition.GobbletsStack[-1] 
        