import Gobblet
import BoardItem


class MoveID:
    def __init__(self, current_gobblet: Gobblet, next_possible_location: BoardItem):
        self.CurrentGobblet = current_gobblet
        self.next = next_possible_location
