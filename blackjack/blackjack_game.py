# -*- coding: utf-8 -*-

import random


class BlackjackGame(object):

    DECK_VALUES = {
        "A": 11, "K": 10, "Q": 10, "J": 10,
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10
    }
    DECK = "A,K,J,Q,2,3,4,5,6,7,8,9,10".split(",") * 4

    WIN = 1
    LOSE = -1
    DRAW = 0

    def init_game(self, shuffle=False):
        self.deck = list(self.DECK)

        if shuffle:
            self.shuffle_deck()

        self.initialize_cards()
        self.check_if_blackjack()

    def initialize_cards(self):
        self.my_cards = [self.pick_a_card(), self.pick_a_card()]
        self.dealer_cards = [self.pick_a_card(), self.pick_a_card()]

    def check_if_blackjack(self):
        if len(self.my_cards) == 2 and \
            self.sum_cards(self.my_cards) == 21:
            raise GameUserBlackjackException()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def pick_a_card(self):
        return self.deck.pop()

    def hit(self):
        self.my_cards.append(self.pick_a_card())
        my_sum = self.sum_cards(self.my_cards)

        if my_sum > 21:
            raise GameBustedException()

    def do_stand(self):
        while self.sum_cards(self.dealer_cards) <= 15:
            self.dealer_cards.append(self.pick_a_card())

        self._sum_all_points()

    def _sum_all_points(self):
        self.dealer_points = self.sum_cards(self.dealer_cards)
        self.my_points = self.sum_cards(self.my_cards)

    def sum_cards(self, cards):
        _sum = sum([self.DECK_VALUES[card] for card in cards])
        num_as = len([card for card in cards if card == 'A'])

        while num_as > 0:
            if _sum <= 21:
                break
            _sum -= 10
            num_as -= 1

        return _sum

    def win(self):
        self._sum_all_points()

        if self.my_points > 21:
            return BlackjackGame.LOSE
        if self.dealer_points > 21:
            return BlackjackGame.WIN

        if self.my_points == self.dealer_points:
            return BlackjackGame.DRAW
        elif self.my_points > self.dealer_points:
            return BlackjackGame.WIN
        else:
            return BlackjackGame.LOSE


class GameBustedException(Exception):
    pass

class GameUserBlackjackException(Exception):
    pass