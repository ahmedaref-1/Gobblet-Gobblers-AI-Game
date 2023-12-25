from typing import List
import BoardItem
import Gobblet
class MoveID:
    def __init__(self, CurrentGobblet: Gobblet, NextPossibleLocation):
        self.CurrentGobblet = CurrentGobblet
        self.next = NextPossibleLocation
