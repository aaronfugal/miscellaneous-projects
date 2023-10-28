import itertools
import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
values = {'ace': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13}

# Function to get a new deck and shuffle it
def get_new_deck():
    deck = list(itertools.product(ranks, suits))
    random.shuffle(deck)
    return deck

# Function to evaluate a hand and return its rank
def evaluate_hand(hand):
    # Check for Royal Flush
    royal_flush = [('10', suit) for suit in suits]
    if set(royal_flush).issubset(set(hand)):
        return 10

    # Check for Straight Flush
    flush_suits = [card[1] for card in hand]
    flush_ranks = [card[0] for card in hand]
    for suit in suits:
        if flush_suits.count(suit) >= 5:
            flush_cards = [(rank, suit) for rank, suit in hand if suit == flush_suits[0]]
            for i in range(len(flush_cards) - 4):
                if flush_ranks.index(flush_cards[i][0]) == flush_ranks.index(flush_cards[i + 4][0]) - 4:
                    return 9

    # Check for Four of a Kind
    for rank in ranks:
        if [card for card in hand if card[0] == rank].__len__() >= 4:
            return 8

    # Check for Full House
    for rank in ranks:
        if [card for card in hand if card[0] == rank].__len__() == 3:
            for other_rank in ranks:
                if rank != other_rank and [card for card in hand if card[0] == other_rank].__len__() >= 2:
                    return 7

    # Check for Flush
    for suit in suits:
        if flush_suits.count(suit) >= 5:
            return 6

    # Check for Straight
    unique_ranks = list(set(ranks.index(card[0]) for card in hand))
    unique_ranks.sort()
    for i in range(len(unique_ranks) - 4):
        if unique_ranks[i] == unique_ranks[i + 4] - 4:
            return 5

    # Check for Three of a Kind
    for rank in ranks:
        if [card for card in hand if card[0] == rank].__len__() == 3:
            return 4

    # Check for Two Pair
    pairs = []
    for rank in ranks:
        if [card for card in hand if card[0] == rank].__len__() == 2:
            pairs.append(rank)
    if pairs.__len__() >= 2:
        return 3

    # Check for One Pair
    for rank in ranks:
        if [card for card in hand if card[0] == rank].__len__() == 2:
            return 2

    # Return High Card
    return 1

# Function to deal cards to players and evaluate
def play_game():
    games_played = 0
    while True:
        deck = get_new_deck()
        player1_hand = deck[:5]
        player2_hand = deck[5:10]
        player1_rank = evaluate_hand(player1_hand)
        player2_rank = evaluate_hand(player2_hand)
        if player1_rank == 10 or player2_rank == 10:
            games_played += 1
            print(f"Royal flush obtained after {games_played} games!")
            return
        games_played += 1

play_game()
