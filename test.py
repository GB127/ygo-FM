from math import factorial, comb

class Deck_true:
    cards = ["MBD", "D", "d", "f", "Th", "trash"]
    def __init__(self):
        self.deck = 40

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
        dragon_1 = comb(self.D, 1)
        thunder_1 = comb(self.Th, 1)
        trash_1 = comb(self.trash, draw_power - 2)

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




test = Deck_true()

print(test)