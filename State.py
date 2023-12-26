import pickle
import Game
import MoveID


class State:
    def __init__(self, CurrentPlayerId : int, game: Game ):
        #taking deep copy of the game without affecting the actual result
        self.game = pickle.loads(pickle.dumps(Game))
        self.CurrentPlayerId   = CurrentPlayerId  

   
    def generate_successor(self, action: MoveID):  #  action is valid
        if self.CurrentPlayerId  == 1:
            child_state = State(0, self.game)
        else:
            child_state = State(1, self.game)

        child_state.apply_move(action)
        return child_state


    def AllValidMoves(self) -> List[MoveID]:
        return self.game.AllValidMoves()

    def apply_move(self, action: MoveID):
        self.game.apply_move(action)


    
