"""
Code to generate a figure with mana curves
"""
import random

import ertai
import matplotlib.pyplot as plt
import numpy as np


assert ertai.__version__ == "0.0.2"



def build_deck(n, L):
    """
    Given a vector n and a number of lands L build a deck.
    """
    number_of_lands = L
    deck = [ertai.BasicLand() for _ in range(number_of_lands)]

    for cost, number in enumerate(n):
        cost = ertai.Mana(*(None for _ in range(cost)))
        deck += [ertai.Card(cost=cost) for _ in range(number)]
    return deck


def play_most_expensive_cards(hand, pool):
    """
    Given a mana pool and a hand.
    
    Play as many cards as possible (playing most expensive ones first)
    
    Return hand after all possible cards are played.
    """
    sorted_hand = sorted(hand, reverse=True, key=lambda card: sum(card.cost.counter.values()))
    
    played = []
    number_cast = 0
    for card in sorted_hand:
        if (card.cost <= pool) and isinstance(card, ertai.BasicLand) is False:
            pool = card.cast(pool)
            hand.remove(card)
            played.append(card)
            number_cast += 1
    return number_cast, played, pool


def play_land(hand):
    """
    Given a hand if there is a land in the hand it will play it.
    """
    for card in hand:
        if isinstance(card, ertai.BasicLand):
            hand.remove(card)
            return card
    return None


def play(n, L, seed=0, play_until=0):
    """
    This will play a round and return the number of cards player in each turn.
    """
    deck = build_deck(n=n, L=L)
    random.seed(seed)
    random.shuffle(deck)
    
    hand, deck = deck[:7], deck[7:]
    lands = []
    number_of_cards_played = []
    number_of_mana_available = []
    cost_of_played_cards = []
    
    while (deck_length := len(deck)) > play_until:

        hand.append(deck.pop())

        if (land := play_land(hand)) is not None:
            lands.append(land)

        pool = ertai.Mana()
        for land in lands:
            land.untap()
            pool += land.generate_mana()
        
        number, cards, pool, = play_most_expensive_cards(hand=hand, pool=pool)
        
        while(len(hand)) > 7:
            random.shuffle(hand)
            hand.pop()
        
        number_of_cards_played.append(number)
        cost_of_played_cards.append(sum(sum(card.cost.counter.values()) for card in cards))
        number_of_mana_available.append(len(lands))
        
    return number_of_cards_played, cost_of_played_cards, number_of_mana_available


if __name__ == "__main__":
    L = 20
    number_of_repetitions = 5_000

    n1 = (0, 12, 12, 6, 0, 2, 4, 4)
    mana_ratio_1 = []
    for seed in range(number_of_repetitions):
        number_of_cards_played, cost_of_played_cards, number_of_mana_available = play(n1, L, seed=seed, play_until=0)
        mana_ratio_1.append(np.array(cost_of_played_cards) / np.array(number_of_mana_available))

    n2 = (0, 4, 16, 6, 4, 2, 4, 4)
    mana_ratio_2 = []
    for seed in range(number_of_repetitions):
        number_of_cards_played, cost_of_played_cards, number_of_mana_available = play(n2, L, seed=seed, play_until=0)
        mana_ratio_2.append(np.array(cost_of_played_cards) / np.array(number_of_mana_available))   

    n3 = (0, 0, 0, 10, 10, 10, 5, 5)
    mana_ratio_3 = []
    for seed in range(number_of_repetitions):
        number_of_cards_played, cost_of_played_cards, number_of_mana_available = play(n3, L, seed=seed, play_until=0)
        mana_ratio_3.append(np.array(cost_of_played_cards) / np.array(number_of_mana_available))

    plt.figure()
    plt.plot(np.nanmean(mana_ratio_1, axis=0), label=str(n1))
    plt.plot(np.nanmean(mana_ratio_2, axis=0), label=str(n2))
    plt.plot(np.nanmean(mana_ratio_3, axis=0), label=str(n3))
    plt.xlabel("Turn")
    plt.ylabel("Expected proportion of used mana")
    plt.title(f"Mana curve for decks with {L} lands (over {number_of_repetitions} repetitions)")
    plt.legend()
    plt.savefig("main.pdf", transparent=True)
