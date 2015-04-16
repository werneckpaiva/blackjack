from __future__ import print_function
from blackjack.blackjack_game import BlackjackGame, GameBustedException

def _output(*args):
    print(*args)

def _input(msg):
    return raw_input(msg)

class CommandLineGame():
    
    @classmethod
    def main(cls):
        cls.game = BlackjackGame(shuffle=True)
        while True:
            _output("My cards: ", cls.game.my_cards)
            _output("Dealer cards: ", cls.game.dealer_cards[0])
            option = _input('Hit(h) or Stand(s) or Quit(q): ').lower()
            if option == "s":
                cls.game.stand()
                _output("Dealer cards: ", cls.game.dealer_cards)
                _output("My cards: ", cls.game.my_cards)
                result = cls.game.win()
                if result == BlackjackGame.WIN:
                    _output("You win!")
                elif result == BlackjackGame.LOSE:
                    _output("You lose!")
                else:
                    _output("Draw match!")
                break
            elif option == "h":
                try:
                    _output("My cards: ", cls.game.my_cards)
                    cls.game.hit()
                except GameBustedException:
                    _output("You lose!!")
                    break
            elif option == "q":
                break
            else:
                _output("Wrong option (s or h)")

if __name__ == '__main__':
    CommandLineGame.main()