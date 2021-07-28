from math import comb
from copy import deepcopy


# spells
# traps


class Deck:
    pairs = [("D", "T")]
    def __init__(self, deck=40, M=0, D=0, d=0, f=0, T=0, E=0, S=0):
        self.deck = deck

        # template deck for testing purpose. Normally it would start at 0.
        self.M = M
        self.D = D
        self.d = d
        self.f = f
        self.T = T
        self.E = E
        self.S = S

        # self.trash = self.deck - (sum(self.__dict__.values()) - self.deck)

    def __str__(self):
        header = f" {'X':^8}| "
        cards_in_deck = f" {self.bad_cards():^8}| "
        for card in list(self.__dict__.items())[1:]:
            header += f' {card[0]:^8}| '
            cards_in_deck += f' {card[1]:^8}| '
        for combo in self.pairs:
            header += f' {"+".join(combo):^8}| '
            cards_in_deck += f' {"":8}| '

        table = ""
        for draw_power in range(1,min(6, self.deck + 1)):
            probabilities = [self.probability_trash(draw_power)]
            for card in list(self.__dict__.keys())[1:]:
                probabilities.append(self.probability_solo(card, draw_power))
            for duo in self.pairs:
                probabilities.append(self.probability_duo(duo, draw_power))
            table += f'{" | ".join(probabilities)} |\n'

        return f'{self.deck} cards remaining\n{header}\n{cards_in_deck}\n{table}'


    def probability_solo(self,which, draw_power):
        probability = 0
        assert draw_power > 0, "Draw power must be >0"

        total_possibility = comb(self.deck, draw_power)

        for duplicate in range(1, draw_power + 1):
            wanted = comb(self.__dict__[which], duplicate)
            anything = comb(self.deck - self.__dict__[which], draw_power - duplicate)
            probability += (wanted * anything) / total_possibility
        return f'{round(probability * 100,3):6} %'


    def game(self):
        def valid_cards(cards):
            if len(cards) > 5: return False

            list_valid = list(self.__dict__.keys()) + ["X"]
            check = True
            for card in cards:
                    check = ((card in list_valid) and check)
            for card in list_valid:
                if card == "X":
                    check = ((self.bad_cards() >= cards.count(card)) and check)
                else:
                    check = ((self.__dict__[card] >= cards.count(card)) and check)
            return check

        backup = deepcopy(self.__dict__)

        while True:
            print(self)
            cards = input("What cards did you draw? [reset, exit] ")
            if cards == "reset":
                self.__dict__ = backup
            elif cards == "exit":
                break
            elif valid_cards(cards):
                for card in cards:
                    self.deck -= 1
                    if card != "X":
                        self.__dict__[card] -= 1


    def __call__(self):
        while True:
            command = input("What would you like to do?\n[game, edit, end]")
            if command == "game":
                self.game()
            elif command == "end":
                break


    def probability_duo(self, liste_combos, draw_power):
        if draw_power < 2: return f'{0:6} %'

        all_combos = []
        for first in range(1,6):
            for second in range(1,6):
                all_combos.append((first, second))
        valid_combos = []
        for combo in all_combos:
            if sum(combo) <= draw_power:
                valid_combos.append(combo)
        
        
        total_combos = comb(self.deck, draw_power)
        total = 0
        for combo in valid_combos:
            first_total = comb(self.__dict__[liste_combos[0]], combo[0])
            second_total = comb(self.__dict__[liste_combos[1]], combo[1])
            not_wanted = self.deck - self.__dict__[liste_combos[0]] - self.__dict__[liste_combos[1]]


            any_else_total = comb(not_wanted, draw_power - combo[0] - combo[1])
            total += first_total * second_total * any_else_total

        return f'{round(100 * total / total_combos, 3):6} %'

    def bad_cards(self):
        return 2*self.deck - sum(self.__dict__.values())

    def probability_trash(self, draw_power):
        probability = comb(self.bad_cards(), draw_power) / comb(self.deck, draw_power)
        return f'{round(probability * 100, 3):6} %'


test = Deck(M=3, T=5, D=2, E=9, deck=40)

test()