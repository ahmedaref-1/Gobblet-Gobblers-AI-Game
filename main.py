import Game


    ##########################################################
    #Testing list_possible_gobblets
    ##########################################################

    #Since the index of the player is initialized by 0 and we are at the start of the game, 
    #we suppose that the list of gobblets will include 12 gobblets from 0 to 11
'''
def main():
    game_instance = Game.Game()

    possible_gobblets_list = []
    possible_gobblets_list.extend(game_instance.list_possible_gobblets())
    print("Done")
'''
    ##########################################################
    #Testing list_possible_moves
    ##########################################################

    #Since we are at the start of the game and the board is empty,
    #we suppose that all indexes of positions on board will be returned
'''
def main():
    game_instance = Game.Game()

    possible_moves_list = []
    possible_moves_list.extend(game_instance.list_possible_moves(game_instance.FirstPlayerGobbletsArray[0]))
    print("Done")
'''
    ##########################################################
    #Testing all_valid_moves
    ##########################################################

    #Since we are at the start of the game we expect 48 valid moves
    #3 gobblets (the ones on top of each stack) each has 16 available moves
'''
def main():
    game_instance = Game.Game()

    valid_moves = []
    valid_moves.extend(game_instance.all_valid_moves())
    print("Done")
'''

    ##########################################################
    #Testing make_move
    ##########################################################

#Scenario 1
'''
def main():
    game_instance = Game.Game()

    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[0],game_instance.self.BoardItemsArray[0])
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[1],game_instance.self.BoardItemsArray[1])
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[2],game_instance.self.BoardItemsArray[2])
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[3],game_instance.self.BoardItemsArray[3])

    game_instance.check_gobblet_on_top(game_instance.self.BoardItemsArray[0])
    game_instance.check_gobblet_on_top(game_instance.self.BoardItemsArray[1])
    game_instance.check_gobblet_on_top(game_instance.self.BoardItemsArray[2])
    game_instance.check_gobblet_on_top(game_instance.self.BoardItemsArray[3])               

    game_state = game_instance.check_state()

    print(game_state)
'''


#Scenario 2
'''
def main():
    game_instance = Game.Game()

    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[0],game_instance.self.BoardItemsArray[0])
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[1],game_instance.self.BoardItemsArray[1])
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[0],game_instance.self.BoardItemsArray[2])
    game_instance.make_move(game_instance.FirstPlayerGobbletsArray[1],game_instance.self.BoardItemsArray[3])

    game_instance.check_gobblet_on_top(game_instance.self.BoardItemsArray[0])
    game_instance.check_gobblet_on_top(game_instance.self.BoardItemsArray[1])
    game_instance.check_gobblet_on_top(game_instance.self.BoardItemsArray[2])
    game_instance.check_gobblet_on_top(game_instance.self.BoardItemsArray[3])               

    game_state = game_instance.check_state()

    print(game_state)
'''





























if __name__ == "__main__":
    main()


