# Importing the Gobblet and BoardItem classes from their respective modules
import Gobblet
import BoardItem


# Defining a class named MoveID
class MoveID:
    # Constructor method to initialize the MoveID object
    def __init__(self, current_gobblet: Gobblet, next_possible_location: BoardItem):
        # Initializing an instance variable 'CurrentGobblet' with the provided 'current_gobblet'
        self.CurrentGobblet = current_gobblet
        # Initializing an instance variable 'next' with the provided 'next_possible_location'
        self.next = next_possible_location
