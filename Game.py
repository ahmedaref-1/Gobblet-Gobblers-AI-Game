import Gobblet
import BoardItem
from Gobblet import CurrentGobblet
from Action import MoveID

class Game:
    def __init__(self, player1_name, player2_name, NumberOfGobbletsperPlayerInitValue=12, BoardSizeInitValue=16):
        """
        Represents the Gobblet Gobblers game.

        Parameters:
        - player1_name              (str): Name of player 1
        - player2_name              (str): Name of player 2
        - NumberOfGobbletsInitValue (int): Total number of gobblets per player (default is 12)
        - BoardSizeInitValue        (int): Size of the game board (default is 16)
        """
        self.PlayerNames = [player1_name, player2_name]  # List containing names of both players
        self.GameState = "OnGoing"  # State of the game (OnGoing, Draw, Player1Won, Player2Won)
        self.Winner = None  # Winner of the game (initially None)
        self.NumberOfGobbletsperPlayer = NumberOfGobbletsperPlayerInitValue  # Number of gobblets per player
        self.BoardSize = BoardSizeInitValue  # Size of the game board (number of cells)
        self.FirstPlayerGobbletsArray = []  # List to store Gobblet objects of the First Player
        self.SecondPlayerGobbletsArray = [] # List to store Gobblet objects of the Second Player
        self.BoardItemsArray = []  # List to store BoardItem objects
        self.CurrentPlayerIndex = 0  # Index of the current player (0 or 1)
        self.SelectedGobbletID = None  # ID of the selected Gobblet for the current move
        self.SelectedBoardItemIndex = None  # Index of the selected BoardItem for the current move
    
    def Initialize(self):
        """
        Initialize the game.
        """
        # Initialize the Gobblets for both players
        self.InitializeGobblets()
        # Initialize the Board Items
        self.InitializeBoardItems()
        # Set the current player index to 0
        self.CurrentPlayerIndex = 0
        # Set the selected Gobblet ID to None
        self.SelectedGobbletID = None
        # Set the selected Board Item index to None
        self.SelectedBoardItemIndex = None
        # Set the game state to OnGoing
        self.GameState = "OnGoing"
        # Set the winner to None
        self.Winner = None
    
    def InitializeGobblets(self):
        """
        Initialize the Gobblets for both players.
        """
        # Initialize the Gobblets for the First Player
        self.InitializeGobbletsForPlayer(0)
        # Initialize the Gobblets for the Second Player
        self.InitializeGobbletsForPlayer(1)
    
    def InitializeGobbletsForPlayer(self, player_index):
        """
        Initialize the Gobblets for the specified player.

        Parameters:
        - player_index (int): Index representing the player (0 or 1)
        """
        # Initialize the CreatedGobbletSize to 4
        CreatedGobbletSize = 4
        # Loop through the number of Gobblets per player
        for i in range(self.NumberOfGobbletsperPlayer):
            # Create a new Gobblet object
            gobblet = Gobblet.Gobblet(i, player_index, CreatedGobbletSize)

            # Decrement the CreatedGobbletSize by 1
            CreatedGobbletSize-=1

            # Reset the CreatedGobbletSize to 4 if it is less than 1
            if CreatedGobbletSize < 1:
                CreatedGobbletSize = 4

            # Set the isOnTop flag to True if the current Gobblet is of the size 4
            if gobblet.Size == 4:
                gobblet.IsOnTop = True

            # Add the new Gobblet object to the appropriate list
            if player_index == 0:
                self.FirstPlayerGobbletsArray.append(gobblet)
            else:
                self.SecondPlayerGobbletsArray.append(gobblet)
    
    def InitializeBoardItems(self):
        """
        Initialize the Board Items.
        """
        # Loop through the BoardSize
        for i in range(self.BoardSize):
            # Create a new BoardItem object
            board_item = BoardItem.BoardItem(i)

            # Add the new BoardItem object to the list
            self.BoardItemsArray.append(board_item)


    def ListPossibleGoblets(self) -> list:
        """
        Determines and returns a list of all Goblets that can be placed of a specific player.

        Args:
        CurrentPlayerIndex: To indicate the player.

        Returns:
        A list containing the IDs of all Goblets that can be moved.
        """
        possible_goblets = []
        # Check for Player 1
        if self.CurrentPlayerIndex is 0 :
            # Iterate through all available Goblet IDs of player 1, considering both internal and external ones.
            for goblet_id in range(self.FirstPlayerGobbletsArray):
                # Check if the gobblet is on top.
                if self.FirstPlayerGobbletsArray[goblet_id].IsOnTopOfStack:
                    possible_goblets.append(goblet_id)

        # Check for Player 2
        if self.CurrentPlayerIndex is 1 :
            # Iterate through all available Goblet IDs of player 2, considering both internal and external ones.
            for goblet_id in range(self.SecondPlayerGobbletsArray):
                # Check if the gobblet is on top.
                if self.SecondPlayerGobbletsArray[goblet_id].IsOnTopOfStack:
                    possible_goblets.append(goblet_id)            

        return possible_goblets
    

    def ListPossibleMoves(self, Gobblet: CurrentGobblet) -> list[MoveID]:
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
        for SquareID in range(self.BoardSizeInitValue):
            # Check if the gobblet can move to the position on board
            if CurrentGobblet.IsPossibleGobbletMovement(self, SquareID):
                # Create an object with the current gobblet and the possible squareID it can move to
                NewValidMove = MoveID(Gobblet, SquareID)
                # Add MoveID to the array
                possible_moves.append(NewValidMove)
        # Return the array of possible moves
        return possible_moves    

    def AllValidMoves(self) -> list[MoveID]:
        """
        Determines and returns a list of all Valid moves for all available gobblet IDs that can be placed on the specified position.

        Returns:
            A list containing the valid positions of all available gobblets

        """
        AllAvailableGobblets = self.ListPossibleGoblets
        ValidActions = []
        for goblet in AllAvailableGobblets:
            ValidActions.extend(self.ListPossibleMoves(goblet))
        return ValidActions


    def MoveExternalGobblet (self,CuurentGobbler:Gobblet, RequiredPosition:BoardItem):
        """
        Moves an external Gobblet from its current position to the specified target position on the board,
        ensuring preconditions are met before execution.

        Args:
        current_gobblet: The Gobblet to be moved.
        required_position: The target position on the board where the Gobblet should be moved.
        """
        # Check that the gobblet on top and that it is NOT placed on board
        if CuurentGobbler.IsOnTopOfStack is True and CuurentGobbler.IsOnBoard is False:
            # Check that it is possible to move the gobbled to the specified position
            if CuurentGobbler.IsPossibleGobbletMovement(self, RequiredPosition.index) is True:
                # Call Function PlaceExternalGobblet to place the gobblet on board
                self.PlaceExternalGobblet

    def PlaceExternalGobblet (self,CuurentGobbler:Gobblet, RequiredPosition:BoardItem): 
        """
        Places an external Gobblet onto the specified position on the game board, ensuring valid placement.

        Args:
        current_gobblet: The Gobblet to be placed on the board.
        required_position: The target position where the Gobblet should be placed.
        """
        # If the position on board can the gobblet be placed on
        if RequiredPosition.IsPossibleBoardMovement(self, CuurentGobbler) is True:
            # Add the gobblet to the top of the new postion
            RequiredPosition.AddGobbletOnTop(self, CuurentGobbler)   

    def MoveInternalGobblet (self,CuurentGobbler:Gobblet, RequiredPosition:BoardItem):
        """
        Moves an internal Gobblet from its current position to the specified target position on the board.

        Args:
        current_gobblet: The Gobblet to be moved, which must already be on the board.
        required_position: The target position where the Gobblet should be moved.
        """
        # Check that the gobblet on top of stack and that it is already on the board
        if CuurentGobbler.IsOnTopOfStack is True and CuurentGobbler.IsOnBoard is True:
            # Check that the gobblet can be placed on the board
            if CuurentGobbler.IsPossibleGobbletMovement(self, RequiredPosition.index) is True:
                # Call the function PlaceInternalGobblet to place the gobblet on board
                self.PlaceInternalGobblet


    def PlaceInternalGobblet (self,CuurentGobbler:Gobblet, RequiredPosition:BoardItem): 
        """
        Places a Gobblet onto a specified BoardItem position, following game rules.

        Args:
       - CuurentGobbler (Gobblet): The Gobblet to be placed.
       - RequiredPosition (BoardItem): The BoardItem position where the Gobblet should be placed.
        """
        # If the position on board can the gobblet be placed on
        if RequiredPosition.IsPossibleBoardMovement(self, CuurentGobbler) is True:
            # Remove the goblet from the top of its current position
            RequiredPosition.RemoveGobbletOnTop(self)
            # Add the gobblet to the top of the new postion
            RequiredPosition.AddGobbletOnTop(self, CuurentGobbler)          

    def checkWinner1 (self, RequiredPosition:BoardItem):
        for positions in range (self.BoardItemsArray):
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[0] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[1] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[2] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[3] is not None:
                            self.GameState = "Player1Won"
                            break
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[4] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[5] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[6] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[7] is not None:
                            self.GameState = "Player1Won"        
                            break  
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[8] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[9] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[10] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[11] is not None:
                            self.GameState = "Player1Won"
                            break
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[12] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[13] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[14] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[15] is not None:
                            self.GameState = "Player1Won"
                            break
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[0] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[4] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[8] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[12] is not None:
                            self.GameState = "Player1Won"
                            break
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[1] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[5] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[9] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[13] is not None:
                            self.GameState = "Player1Won"
                            break
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[2] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[6] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[10] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[14] is not None:
                            self.GameState = "Player1Won"
                            break
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[3] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[7] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[11] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[15] is not None:
                            self.GameState = "Player1Won"
                            break
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[0] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[5] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[10] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[15] is not None:
                            self.GameState = "Player1Won"
                            break
            if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[3] is not None:
                if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[6] is not None: 
                    if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[9] is not None: 
                        if RequiredPosition.GetOwnerIndex is False and self.BoardItemsArray[12] is not None:
                            self.GameState = "Player1Won"   


    def checkWinner2 (self, RequiredPosition:BoardItem):
        for positions in range (self.BoardItemsArray):
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[0] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[1] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[2] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[3] is not None:
                            self.GameState = "Player2Won"
                            break
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[4] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[5] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[6] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[7] is not None:
                            self.GameState = "Player2Won"
                            break          
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[8] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[9] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[10] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[11] is not None:
                            self.GameState = "Player2Won"
                            break
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[12] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[13] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[14] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[15] is not None:
                            self.GameState = "Player2Won"
                            break
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[0] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[4] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[8] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[12] is not None:
                            self.GameState = "Player2Won"
                            break
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[1] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[5] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[9] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[13] is not None:
                            self.GameState = "Player2Won"
                            break
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[2] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[6] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[10] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[14] is not None:
                            self.GameState = "Player2Won"
                            break
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[3] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[7] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[11] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[15] is not None:
                            self.GameState = "Player2Won"
                            break
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[0] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[5] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[10] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[15] is not None:
                            self.GameState = "Player2Won"
                            break
            if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[3] is not None:
                if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[6] is not None: 
                    if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[9] is not None: 
                        if RequiredPosition.GetOwnerIndex is True and self.BoardItemsArray[12] is not None:
                            self.GameState = "Player2Won" 
                                                                                                                                                         





    




    


