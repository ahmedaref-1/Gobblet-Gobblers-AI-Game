import Game


def main():
    game_instance = Game.Game()

    print(game_instance.CurrentPlayerIndex)
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[0], game_instance.BoardItemsArray[0])
    if(game_instance.InvalidMoveFlag):
        print("Invalid Move")

    print(game_instance.CurrentPlayerIndex)
    game_instance.make_move(game_instance.SecondPlayerGobbletsArray[0], game_instance.BoardItemsArray[4])
    if(game_instance.InvalidMoveFlag):
        print("Invalid Move")

    print(game_instance.CurrentPlayerIndex)
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[1], game_instance.BoardItemsArray[10])
    if(game_instance.InvalidMoveFlag):
        print("Invalid Move")

    print(game_instance.CurrentPlayerIndex)
    game_instance.make_move(game_instance.SecondPlayerGobbletsArray[1], game_instance.BoardItemsArray[10])
    if(game_instance.InvalidMoveFlag):
        print("Invalid Move")

    print(game_instance.CurrentPlayerIndex)
    game_instance.make_move(game_instance.SecondPlayerGobbletsArray[0], game_instance.BoardItemsArray[10])
    if(game_instance.InvalidMoveFlag is False):
        print("valid Move")

if __name__ == "__main__":
    main()
