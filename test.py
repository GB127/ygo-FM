# 1st : Calculate the odds of having a MD in the first 5 hand

class Deck_true:
    def __init__(self):
        self.deck = 40
        self.MBD = 3

    def probabilities(self, draw):
        probability = {}
        # MBD:
        probability["MBD"] = (self.deck - self.MBD) / self.deck
        for card in range(1, draw):
            no_MBD = self.deck - self.MBD - card
            remaining = self.deck - card
            probability["MBD"] *= (no_MBD)/(remaining)
        probability["MBD"] = round((1 - probability["MBD"]) * 100, 2)
        return probability

    def __call__(self):
        while True:
            print(self)
            command = input("Please enter a command ")
            if command == "reset" or self.deck == 0:
                break
            self.deck -= 1




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

print(test.probabilities(5))
# Calculate probability of having at least one Dragon + 1 Thunder



# Deck  |  MBD%  |  Dragon%  |  Thunder%  | Equip | Trap |