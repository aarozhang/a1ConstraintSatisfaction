class State():
    def __init__(self, name):
        self.name = name
        self.adjStates = []
        self.color = None
        self.possibleColors = []

    def setColor(self, c):
        self.color = c

    def setAdjacents(self, s):
        self.adjStates.append(s)

    def setPossibleColors(self, colors):
        self.possibleColors = colors
