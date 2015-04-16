from blackjack.blackjack_game import BlackjackGame, GameBustedException
import sys

def main():
    game = BlackjackGame(shuffle=True)
    while True:
        sys.stdout.write("My cards: " + str(game.my_cards)+"\n")
        print "Dealer cards: ", game.dealer_cards[0]
        option = raw_input('Hit(h) or Stand(s) or Quit(q): ')
        if option == "s":
            game.stand()
            print "Dealer cards: ", game.dealer_cards
            print "My cards: ", game.my_cards
            result = game.win()
            if result == BlackjackGame.WIN:
                print "You win!" 
            elif result == BlackjackGame.LOSE:
                print "You lose!"
            else:
                print "Draw match!"
            break
        elif option == "h":
            try:
                print "My cards: ", game.my_cards
                game.hit()
            except GameBustedException:
                print "You lose!!"
                break
        elif option == "q":
            break
        else:
            print "Wrong option (s or h)"

if __name__ == '__main__':
    main()