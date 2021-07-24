# 1st : Calculate the odds of having a MD in the first 5 hand

class Deck_true:
    cards = ["MBD", "D", "d", "f", "Th", "trash"]
    def __init__(self):
        self.deck = 40
        self.MBD = 0
        self.D = 5
        self.d = 6
        self.f = 2
        self.Th = 4

        self.trash = self.deck - self.MBD - self.D - self.d - self.f - self.Th

    def probabilities(self, draw):
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
            string += f'{draw_power} | {" | ".join(self.probabilities(draw_power).values())} |\n'

        return string



class Deck:
    def __init__(self):
        self.deck = 40
        self.MBD = 3
        self.trash = 40

    def starting_hand(self,deck, card_count, drawing):
        probability = (deck - card_count) / deck
        for card in range(1, 5):
            no_MBD = self.deck - card_count - card
            remaining = self.deck - card
            probability *= (no_MBD)/(remaining)
        return round((1 - probability)*100, 2)


    def __str__(self):
        string = ""
        for card in range(self.deck, 0, -1):
            string += f'{card:2} | {self.starting_hand(card, self.MBD, 5):5} % |\n'

        
        return f'{string}'

test = Deck_true()

print(test)
