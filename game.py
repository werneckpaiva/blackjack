# -*- coding: utf-8 -*-

from __future__ import print_function
from blackjack.blackjack_game import BlackjackGame, GameBustedException,\
    GameUserBlackjackException


class GameEndException(Exception):
    pass


class CommandLineGame():

    command_line_game = None

    @classmethod
    def main(cls):
        cls.command_line_game = CommandLineGame()

    def __init__(self):
        self.new_game()
        self.run_game()


    def run_game(self):
        while True:
            option = _input('\nHit(h) or Stand(s) or Quit(q): ').lower()
            try:
                if option == 's':
                    self.do_stand()
    
                elif option == 'h':
                    self.do_hit()

                elif option == 'q':
                    break

                else:
                    _output('Wrong option (s, h or q)')

            except GameEndException:
                if not self.restart_game_option():
                    break

    def do_hit(self):
        try:
            self.game.hit()
            self.print_hands()
        except GameBustedException:
            self.print_hands(print_all=True)
            _output('You lose!!')
            raise GameEndException()

    def new_game(self):
        try:
            self.game = BlackjackGame()
            self.game.init_game(shuffle=True)
            self.print_hands()
        except GameUserBlackjackException:
            self.print_hands()
            _output("You win! Blackjack!")
            raise GameEndException()


    def restart_game_option(self):
        option = _input('\nPlay again?\nYes(y) or No(n): ').lower()
        if option == 'y':
            try:
                self.new_game()
                return True
            except GameEndException:
                return self.restart_game_option()

    def print_hands(self, print_all=False):
        _output('\nDealer cards: ', [self.game.dealer_cards[0]] + ['X'] if not print_all else self.game.dealer_cards)
        _output('My cards: ', self.game.my_cards, ' \n')

    def do_stand(self):
        self.game.do_stand()
        self.print_hands(print_all=True)
        result = self.game.win()
        if result == BlackjackGame.WIN:
            _output('You win!\n')
        elif result == BlackjackGame.LOSE:
            _output('You lose!\n')
        else:
            _output('Draw match!\n')
        raise GameEndException()


def _output(*args):
    print(*args)


def _input(msg):
    return raw_input(msg)


if __name__ == '__main__':
    CommandLineGame.main()
