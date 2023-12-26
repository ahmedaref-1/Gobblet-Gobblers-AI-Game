import Game


def main():
    game_instance = Game.Game()

    possible_gobblets_list = []
    possible_gobblets_list.extend(game_instance.list_possible_gobblets())
    possible_moves_list = []
    possible_moves_list.extend(game_instance.list_possible_moves(game_instance.FirstPlayerGobbletsArray[0]))
    print("Done")

if __name__ == "__main__":
    main()
