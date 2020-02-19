import random
import time

class LocalSearch():
    def __init__(self, states, colors):
        self.states = states
        self.colors = colors

    # localsearch method to color the inputted states
    def colorTheStates(self):
        startTime = time.time()
        states = self.states
        colors = self.colors
        numberOfSteps = 0
        conflictedStates = []
        adjStates = []
        currentState = random.choice(states)
        
        # loop to continually traverse until goal reached
        while not (self.isFinished(states)):
            self.checkRunTime(startTime)

            numberOfSteps += 1
            currStateColor = currentState.color
            adjStates = currentState.adjStates
            conflictedStates.clear()
            
            # find and store color-conflicted neighbors
            for adj in adjStates:
                if (currStateColor == adj.color):
                    conflictedStates.append(adj)

            # if no conflicts move onto a random adj state
            if not conflictedStates:
                # if state has no adj then pick from states list (ie. tasmania)
                if not adjStates:
                    currentState = random.choice(states)
                else:
                    currentState = random.choice(adjStates)
            # else move to a random conflicted state and change color
            else:
                currentState = random.choice(conflictedStates)
                self.changeColor(currentState, colors, currStateColor)

        self.printOutput(states, numberOfSteps)

    # checks if goal has been reached
    def isFinished(self, states):
        errors = 0
        for state in states:
            for adj in state.adjStates:
                if (state.color == adj.color):
                    errors += 1
            
        if (errors == 0):
            return True
        
        return False

    # changes conflicting state's color to some non-conflicting color
    def changeColor(self, currentState, colors, notThisColor):
        colorChange = random.choice(colors)
        while (colorChange == notThisColor):
            colorChange = random.choice(colors)
        
        currentState.color = colorChange

    # prints output
    def printOutput(self, states, numberOfSteps):
        print('LocalSearch Output:')
        print('Number of Steps = ' , str(numberOfSteps))
        for state in states:
            print(state.name + ' ' + state.color)

    # monitors runtime to avoid infinite looping
    def checkRunTime(self, startTime):
        elapsedTime = startTime - time.time()
        if (elapsedTime > 60):
            print('Runtime has exceeded maximum time allowance. Please rerun the program.')
            exit()