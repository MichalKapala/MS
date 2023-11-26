import numpy as np

class State:
    def __init__(self, fund: int, winProb: float):
        self.fund = fund
        self.winProb = winProb

    def isBancrupt(self) -> bool:
        return self.fund <= 0

    def decreaseFund(self):
        self.fund -= 1

    def increaseFund(self):
        self.fund += 1

class GameStatistics:
    def __init__(self):
        self.roundsNumber = 0
        self.playerWon = None


class Game:
    def __init__(self, playerA: State, playerB: State, statistics : GameStatistics):
        self.playerA = playerA
        self.playerB = playerB
        self.gameStatistics = statistics

    def round(self):
        randomNumber = np.random.uniform(0.0, 1.0, 1)[0]
        if randomNumber <= self.playerA.winProb:
            self.playerB.decreaseFund()
            self.playerA.increaseFund()
        else:
            self.playerA.decreaseFund()
            self.playerB.increaseFund()


    def play(self):
        while not (self.playerA.isBancrupt() or self.playerB.isBancrupt()):
            self.round()
            self.gameStatistics.roundsNumber += 1

        if self.playerA.isBancrupt():
            self.gameStatistics.playerWon = "B"
        else:
            self.gameStatistics.playerWon = "A"
