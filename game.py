# -*- coding: utf-8 -*-

from __future__ import print_function
from blackjack.blackjack_game import BlackjackGame, GameBustedException


class CommandLineGame():

    @classmethod
    def main(cls):
        cls.new_game()

        while True:
            option = _input('\nHit(h) or Stand(s) or Quit(q): ').lower()
            if option == 's':
                cls.game.stand()

                _output('\nDealer cards: ', cls.game.dealer_cards)
                _output('My cards: ', cls.game.my_cards, ' \n')
                result = cls.game.win()

                if result == BlackjackGame.WIN:
                    _output('You win!\n')
                elif result == BlackjackGame.LOSE:
                    _output('You lose!\n')
                else:
                    _output('Draw match!\n')
                if not cls.restart_game_option():
                    break

            elif option == 'h':
                try:
                    cls.game.hit()
                    _output('\nMy cards: ', cls.game.my_cards, ' \n')
                except GameBustedException:
                    _output('\nMy cards: ', cls.game.my_cards, ' \n')
                    _output('You lose!!')

                    if not cls.restart_game_option():
                        break

            elif option == 'q':
                break

            else:
                _output('Wrong option (s, h or q)')

    @classmethod
    def new_game(cls):
        cls.game = BlackjackGame(shuffle=True)
        _output('\nDealer cards: ', cls.game.dealer_cards[0])
        _output('My cards: ', cls.game.my_cards)

    @classmethod
    def restart_game_option(cls):
        option = _input('\nPlay again?\nYes(y) or No(n): ').lower()
        if option == 'y':
            cls.new_game()
            return True


def _output(*args):
    print(*args)


def _input(msg):
    return raw_input(msg)


if __name__ == '__main__':
    CommandLineGame.main()
