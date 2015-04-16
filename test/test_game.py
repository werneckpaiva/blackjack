# -*- coding: utf-8 -*-

import unittest

from blackjack.blackjack_game import BlackjackGame, GameBustedException


class TestGame(unittest.TestCase):

    def test_start_game_player_cards(self):
        game = BlackjackGame()
        self.assertEquals(len(game.my_cards), 2)
        self.assertEquals(len(game.dealer_cards), 2)

    def test_start_game_deck(self):
        game = BlackjackGame()
        self.assertEquals(len(game.deck), 52 - 4)

    def test_start_game_cards_from_deck(self):
        game = BlackjackGame()
        self.assertTrue(game.my_cards[0] in game.DECK)
        self.assertTrue(game.my_cards[1] in game.DECK)
        self.assertTrue(game.dealer_cards[0] in game.DECK)
        self.assertTrue(game.dealer_cards[1] in game.DECK)

    def test_cards_removed_from_deck(self):
        game = BlackjackGame()
        same_card_from_deck = [card for card in game.deck if card == game.my_cards[0]]
        self.assertTrue(len(same_card_from_deck) <= 3)

    def test_hit(self):
        game = BlackjackGame()
        game.my_cards = ["2", "2"]
        game.hit()
        self.assertEquals(len(game.my_cards), 3)
        self.assertEquals(len(game.deck), 52 - 5)

    def test_stand(self):
        game = BlackjackGame()
        game.stand()
        self.assertEquals(game.dealer_points, 21)
        self.assertEquals(game.my_points, 19)

    def test_win_user_21_dealer_below(self):
        game = BlackjackGame()
        game.dealer_points = 19
        game.my_points = 21
        self.assertEquals(game.win(), BlackjackGame.WIN)

    def test_win_user_20_dealer_below(self):
        game = BlackjackGame()
        game.dealer_points = 19
        game.my_points = 20
        self.assertEquals(game.win(), BlackjackGame.WIN)

    def test_win_user_20_dealer_over(self):
        game = BlackjackGame()
        game.dealer_cards = ["K", "K", "2"]
        game.my_cards = ["K", "K"]
        self.assertEquals(game.win(), BlackjackGame.WIN)

    def test_lose_user_under_dealer_21(self):
        game = BlackjackGame()
        game.dealer_cards = ["K", "9", "2"]
        game.my_cards = ["K", "K"]
        self.assertEquals(game.win(), BlackjackGame.LOSE)

    def test_lose_user_under_dealer_20(self):
        game = BlackjackGame()
        game.dealer_cards = ["K", "K"]
        game.my_cards = ["K", "9"]
        self.assertEquals(game.win(), BlackjackGame.LOSE)

    def test_lose_user_over_dealer_under(self):
        game = BlackjackGame()
        game.dealer_cards = ["K", "8", "2"]
        game.my_cards = ["K", "9", "3"]
        self.assertEquals(game.win(), BlackjackGame.LOSE)

    def test_draw_21(self):
        game = BlackjackGame()
        game.dealer_cards = ["K", "9", "2"]
        game.my_cards = ["K", "9", "2"]
        self.assertEquals(game.win(), BlackjackGame.DRAW)

    def test_draw_20(self):
        game = BlackjackGame()
        game.dealer_cards = ["K", "K"]
        game.my_cards = ["K", "K"]
        self.assertEquals(game.win(), BlackjackGame.DRAW)

    def test_on_hit_if_over_lose(self):
        game = BlackjackGame()
        game.my_cards = ['K', 'K']
        game.pick_a_card = lambda: '4'
        self.assertRaises(GameBustedException, game.hit)

    def test_as_1(self):
        game = BlackjackGame()
        s = game.sum_cards(['K', '8', 'A'])
        self.assertEquals(s, 19)

    def test_as_21(self):
        game = BlackjackGame()
        s = game.sum_cards(['K', 'A'])
        self.assertEquals(s, 21)

    def test_2_as_21(self):
        game = BlackjackGame()
        s = game.sum_cards(['9', 'A', 'A'])
        self.assertEquals(s, 21)

    def test_4_as_14(self):
        game = BlackjackGame()
        s = game.sum_cards(['A', 'A', 'A', 'A'])
        self.assertEquals(s, 14)
