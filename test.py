from math import comb


# spells
# traps


class Deck:
    pairs = [("D", "Th")]
    def __init__(self):
        self.deck = 40

        # template deck for testing purpose. Normally it would start at 0.
        self.M = 1
        self.D = 10
        self.d = 3
        self.f = 2
        self.Th = 5
        self.E = 3
        self.S = 3

        # self.trash = self.deck - (sum(self.__dict__.values()) - self.deck)

    def __str__(self):
        header = ""
        cards_in_deck = ""
        for card in list(self.__dict__.items())[1:]:
            header += f' {card[0]:^8}| '
            cards_in_deck += f' {card[1]:^8}| '
        for combo in self.pairs:
            header += f' {"+".join(combo):^8}| '
            cards_in_deck += f' {"":8}| '

        table = ""
        for draw_power in range(1,min(6, self.deck + 1)):
            probabilities = []
            for card in list(self.__dict__.keys())[1:]:
                probabilities.append(self.probability_solo(card, draw_power))
            for duo in self.pairs:
                probabilities.append(self.probability_duo(duo, draw_power))
            table += f'{" | ".join(probabilities)} |\n'

        return f'{self.deck} cards remaining\n{header}\n{cards_in_deck} \n{table}'


    def probability_solo(self,which, draw_power):
        probability = 0
        assert draw_power > 0, "Draw power must be >0"

        total_possibility = comb(self.deck, draw_power)

        for duplicate in range(1, draw_power + 1):
            wanted = comb(self.__dict__[which], duplicate)
            anything = comb(self.deck - self.__dict__[which], draw_power - duplicate)
            probability += (wanted * anything) / total_possibility
        return f'{round(probability * 100,3):6} %'


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



test = Deck()


print(test)