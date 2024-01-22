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
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[1], game_instance.BoardItemsArray[1])
    if(game_instance.InvalidMoveFlag):
        print("Invalid Move")

    print(game_instance.CurrentPlayerIndex)
    game_instance.make_move(game_instance.SecondPlayerGobbletsArray[0], game_instance.BoardItemsArray[1])
    if(game_instance.InvalidMoveFlag):
        print("Invalid Move")

    print(game_instance.CurrentPlayerIndex)
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[8], game_instance.BoardItemsArray[15])
    if(game_instance.InvalidMoveFlag):
        print("Invalid Move")

    print(game_instance.CurrentPlayerIndex)
    game_instance.make_move(game_instance.SecondPlayerGobbletsArray[0], game_instance.BoardItemsArray[14])
    if(game_instance.InvalidMoveFlag):
        print("Invalid Move")

if __name__ == "__main__":
    main()
