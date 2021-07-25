from math import factorial, comb

class Deck:
    def __init__(self):
        self.deck = 20

        # template deck for testing purpose. Normally it would start at 0.
        self.MBD = 2
        self.D = 2
        self.d = 6
        self.f = 2
        self.Th = 4

        self.trash = self.deck - self.MBD - self.D - self.d - self.f - self.Th

    def probability_solo(self,which, draw_power):
        probability = 0
        assert draw_power > 0, "Draw power must be >0"

        total_possibility = comb(self.deck, draw_power)

        for duplicate in range(1, draw_power + 1):
            wanted = comb(self.__dict__[which], duplicate)
            anything = comb(self.deck - self.__dict__[which], draw_power - duplicate)
            probability += (wanted * anything) / total_possibility
        return probability


class Deck_true:
    cards = ["MBD", "D", "d", "f", "Th", "trash"]
    def __init__(self):
        self.deck = 35

        # template deck for testing purpose. Normally it would start at 0.
        self.MBD = 2
        self.D = 5
        self.d = 6
        self.f = 2
        self.Th = 4

        self.trash = self.deck - self.MBD - self.D - self.d - self.f - self.Th


    def combo_probabilities(self, draw_power):  # Currently, this calculate the chance of having a Dragon AND a thunder and only trashes.
        if draw_power < 2: return 0
        total_combo = comb(self.deck, draw_power)
        dragon_1 = comb(self.D, 1)  # Calculate all using iteration!
        thunder_1 = comb(self.Th, 1)
        trash_1 = comb(self.deck -2, draw_power - 2)

        total = dragon_1 * thunder_1 * trash_1

        return round((total / total_combo) * 100, 2)


    def probabilities(self, draw):  # Probability for each card alone. Should be working correctly.
        probability = {}
        for cartype in Deck_true.cards:
            probability[cartype] = (self.deck - self.__dict__[cartype]) / self.deck
            for card in range(1, draw):
                no_MBD = self.deck - self.__dict__[cartype] - card
                remaining = self.deck - card
                if remaining > 0:
                    probability[cartype] *= (no_MBD)/(remaining)
                else:
                    probability[cartype] *= 0

            probability[cartype] = f'{round((1 - probability[cartype]) * 100, 2):5} %'
        return probability

    def __call__(self):
        while self.deck > 0:
            print(self)
            command = input("Please enter a command ")
            if command == "reset" or self.deck == 0:
                break
            elif command in Deck_true.cards:
                self.__dict__[command] -= 1
                self.deck -= 1

    def __str__(self):
        #for draw in range(1, 6):
        string = f'{self.deck} cards remaining\n  |'
        for card in Deck_true.cards:
            string += f'{card:^9}|'
        string += "\n   "
        for card in Deck_true.cards:
            string += f'{self.__dict__[card]:^9}|'
        string += "\n"

        for draw_power in range(1,6):
            string += f'{draw_power} | {" | ".join(self.probabilities(draw_power).values())} |{self.combo_probabilities(draw_power):5} %'      
            string += "\n"

        return string




test = Deck()

for testing in range(1,6):
    print(test.probability_solo("Th", testing))