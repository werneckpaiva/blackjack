# -*- coding: utf-8 -*-

import unittest
from mock import Mock, call
import game
from game import CommandLineGame


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
        CommandLineGame.main()
        game._output.assert_has_calls([
            call("My cards: ", CommandLineGame.game.my_cards),
            call("Dealer cards: ", CommandLineGame.game.dealer_cards[0])
        ]) # ("My cards: ")
