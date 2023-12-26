import pickle
import Game
from Action import MoveID


class State:
    def __init__(self, CurrentPlayerId: int, game: Game):
        # taking deep copy of the game without affecting the actual result
        self.game = pickle.loads(pickle.dumps(game))
        self.CurrentPlayerId = CurrentPlayerId

    def generate_successor(self, action: MoveID):  # action is valid
        if self.CurrentPlayerId == 1:
            child_state = State(0, self.game)
        else:
            child_state = State(1, self.game)

        child_state.apply_move(action)
        return child_state

    def all_valid_moves(self) -> list[MoveID]:
        return self.game.all_valid_moves()

    def apply_move(self, action: MoveID):

        self.game.make_move(action.CurrentGobblet, action.next)