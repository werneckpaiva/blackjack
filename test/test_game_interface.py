# -*- coding: utf-8 -*-

import game
import unittest

from game import CommandLineGame
from mock import call, Mock


class TestGameInterface(unittest.TestCase):

    old_output = None
    old_input = None

    def setUp(self):
        self.old_output = game._output
        self.old_input = game._input
        game._output = Mock()
        game._input = Mock()

    def tearDown(self):
        game._output = self.old_output
        game._input = self.old_input

    def test_start_game(self):
        game._input = lambda x: "q"
        cmd_line_game = CommandLineGame()
        game._output.assert_has_calls([
            call("\nDealer cards: ", [cmd_line_game.game.dealer_cards[0] + 'X']),
            call("My cards: ", cmd_line_game.game.my_cards, ' \n')
        ])
