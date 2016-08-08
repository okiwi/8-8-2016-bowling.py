class Bowling():
    def __init__(self):
        self.score = 0
        self.estSpare = False

    def tour(self, premier, second):
        somme = premier + second + self.estSpare * premier
        self.estSpare = premier + second == 10
        self.score = self.score + somme
        return self.score

