import Gobblet
import BoardItem

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


    def ListPossibleMoves(self, CurrentGobblet:Gobblet) -> list:
        """
        Checks the positions on board that the gobblet can move to.

        Returns:
        - List of possible positions on board that the goblet can move to.
        """

        # Initialize an empty array to store possible moves
        possible_moves = []
        # Iterate around all squares on board
        for SquareID in range(self.BoardSizeInitValue):
            # Check if the gobblet can move to the position on board
            if Gobblet.IsPossibleMove(self, SquareID):
                # Add SquareID to the array if move is possible
                possible_moves.append(SquareID)

        return possible_moves

    def ListPossibleGoblets(self, current_position: BoardItem) -> list:
    """
    Determines and returns a list of all Goblet IDs that can be placed on the specified position.

    Args:
        current_position: The target position on the board where to check for legal Goblet placements.

    Returns:
        A list containing the IDs of all Goblets that can be placed at the given position.
        The list will be empty if no Goblet placement is possible.

    """
    possible_goblets = []

    # Iterate through all available Goblet IDs, considering both internal and external ones.
    for goblet_id in range(self.self.NumberOfGobbletsperPlayer):
        # Check if placing the current Goblet at the given position is a valid move.
        if BoardItem.IsPossibleMove(self, goblet_id):
            possible_goblets.append(goblet_id)

    return possible_goblets

    




    


