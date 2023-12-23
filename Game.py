import Gobblet
import BoardItem

class Game:
    def __init__(self, player1_name, player2_name, NumberOfGobbletsInitValue=24, BoardSizeInitValue=16):
        """
        Represents the Gobblet Gobblers game.

        Parameters:
        - player1_name              (str): Name of player 1
        - player2_name              (str): Name of player 2
        - NumberOfGobbletsInitValue (int): Total number of gobblets per player (default is 24)
        - BoardSizeInitValue        (int): Size of the game board (default is 16)
        """
        self.PlayerNames = [player1_name, player2_name]  # List containing names of both players
        self.GameState = "OnGoing"  # State of the game (OnGoing, Draw, Player1Won, Player2Won)
        self.Winner = None  # Winner of the game (initially None)
        self.NumberOfGobblets = NumberOfGobbletsInitValue  # Total number of gobblets per player
        self.BoardSize = BoardSizeInitValue  # Size of the game board (number of cells)
        self.GobbletsArray = []  # List to store Gobblet objects
        self.BoardItemsArray = []  # List to store BoardItem objects
        self.CurrentPlayerIndex = 0  # Index of the current player (0 or 1)
        self.SelectedGobbletID = None  # ID of the selected Gobblet for the current move
        self.SelectedBoardItemIndex = None  # Index of the selected BoardItem for the current move


