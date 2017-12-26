import random
import itertools

class texasholdem:

	def __init__(self):
		suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
		numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

		self.deck = [n + ' of ' + s for s in suits for n in numbers]
		random.shuffle(self.deck)

	def deal_cards(self):
		try:
			card = self.deck.pop(0)
			return card
		except ValueError:
			print("No more cards can be dealt")

	def deal_poker_hands(self,n):
		poker_hands = [list([]) for _ in range(n)]
		
		for _ in range(2):
			for i in range(n):
				poker_hands[i].append(self.deal_cards())

		return poker_hands

def display_poker_hands(poker_hands):
	player_names = ['Your' if i == 0 else 'CPU %d' % i for i, _ in enumerate(poker_hands)]

	for j, _ in enumerate(poker_hands):
		print(player_names[j], 'Poker_hand:', ', '.join(poker_hands[j]))

def card_rank(card):
	numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
	suits = ['Diamonds','Clubs','Hearts','Spades']

	card_order = [n + ' of ' + s for s in suits for n in numbers]
	return card_order.index(card)

def poker_hand_score(hand):

	def best_poker_hand(cards):
		number_ranks = {'2': 2, '3': 3, '4': 4, '5':5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
		suit_ranks = {'Diamonds': 1, 'Clubs': 2,'Hearts':3, 'Spades': 4}
		cards = [card.split(' of ') for card in cards]
		ranking_fn = lambda x: number_ranks[x[0]] * 4 + suit_ranks[x[1]]

		return max([x for x in itertools.combinations(cards, 5)], key = rank_poker_hand)

	
	poker_hand = set([tuple(x.split(' of ')) for x in hand])

	# straight sets, reversing so that the highest ranked straight is found first
	suits = ['Diamonds','Clubs','Hearts','Spades'][::-1]
	numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
	straight_check = ['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'][::-1]
	straight_flush_sets = [set([(n,s) for n in straight_check[i:(i+5)]]) for i in range(len(straight_check) - 4) for s in suits]
	straight_sets = [set([n for n in straight_check[i:(i+5)]]) for i in range(len(straight_check) - 4)]

	# royal flush
	royal_flushes = [set([('10',x), ('Jack', x), ('Queen', x), ('King',x), ('Ace',x)]) 
						for x in suits]
	four_of_a_kind = [set([(n,s) for s in suits]) for n in numbers[::-1]]

	# Small number of royal flush combinations so easy to check if they intersect with the poker_hand + flop, turn and river
	for rf in royal_flushes:
		if len(rf&poker_hand) == 5:
			return 'Royal Flush', rf

	# Check straight flush, need to change the order in which they are checked
	for stf in straight_flush_sets:
		if len(stf&poker_hand) == 5:
			return 'Straight Flush', stf

	# Four of a kind occurs when the combined poker_hand has intersection of length 4 with the list of all combinations of four of a kind. 
	# The 5th card is not required
	for fk in four_of_a_kind:
		if len(fk&poker_hand) == 4:
			return 'Four of a Kind', list(fk)[0][0]

	# Full house when an intersection
	for fh in four_of_a_kind:
		if len(fh&poker_hand) == 3 and any([len(other&poker_hand) == 2 for other in four_of_a_kind if fh != other]):
			return 'Full House', list(fh&poker_hand)[0]

	# Flush if at least 5 cards of the same colour
	for suit in suits:
		if len(([x for x in poker_hand if x[1] == suit])) >= 5:
			return 'Flush', poker_hand

	# Check the ranks for straight sequences 
	for sequence in straight_sets:
		if len(set([x[0] for x in poker_hand]) & sequence) == 5: 
			return 'Straight', sequence

	# Three of a kind
	for tk in four_of_a_kind:
		if len(tk&poker_hand) == 3:
			return 'Three of a Kind', list(tk&poker_hand)[0][0]

	# Two pair
	two_pair_combinations = [tp&poker_hand for tp in four_of_a_kind if len(tp&poker_hand) == 2]
	if len(two_pair_combinations) >= 2:
		return 'Two Pair', two_pair_combinations

	# Single Pair
	for sp in four_of_a_kind:
		if len(sp&poker_hand) == 2:
			return 'Pair', list(sp&poker_hand)[0][0]

	# Return the highest rank card if none of the above combinations apply
	return 'High Card', max(hand, key = card_rank)
	
if __name__ == '__main__':
	tex = texasholdem()
	# players = input('How many players do you want?:')
	my_poker_hands = tex.deal_poker_hands(4)
	flop = [tex.deal_cards() for _ in range(3)]
	turn = tex.deal_cards()
	river = tex.deal_cards()
	display_poker_hands(my_poker_hands)
	print('Flop:', ', '.join(flop))
	print('Turn:', turn)
	print('River:', river)

	print(poker_hand_score(my_poker_hands[0] + flop + [turn] + [river]))





