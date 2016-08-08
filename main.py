class Bowling():
    def __init__(self):
        self.score = 0
        self.estSpare = False
        self.estStrike = False

    def tour(self, premier, second):
        somme = premier + second + self.estSpare * premier + self.estStrike * second
        self.estSpare = premier + second == 10
        self.estStrike = self.estStrike or premier == 10
        self.score = self.score + somme
        return self.score

    def _estSpare(self, premier, second):
        return premier + second == 10

