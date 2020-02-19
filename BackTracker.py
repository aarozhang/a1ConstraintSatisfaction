class BackTracker():

    def __init__(self, coloredStates, uncoloredStates):
        self.coloredStates = coloredStates
        self.uncoloredStates = uncoloredStates
        self.numberOfSteps = 1

    # backtracker search to color the inputted states
    def colorTheStates(self):
        coloredStates = self.coloredStates
        uncoloredStates = self.uncoloredStates

        # check for completion (print & exit if done)
        if not uncoloredStates:
            if self.isFinished(coloredStates):
                print('BackTracker Output:')
                print('Number of Steps = ' , str(self.numberOfSteps))
                self.printColoredStates(coloredStates)
                exit()
            else:
                print ('ERROR(S) IN OUTPUT')

        state = self.selectUncoloredState(uncoloredStates)
        possibleColors = state.possibleColors
        adjStates = state.adjStates

        # if no possible colors for current state, backtrack
        if not possibleColors:
            return

        # loop to explore each possible color choice (if needed)
        for selectedColor in possibleColors:
            # tracks number of colors explored
            self.numberOfSteps += 1

            # verify color assignment
            if not self.verify(selectedColor, adjStates):
                continue

            # if verified, update list data and forward check
            state.setColor(selectedColor)
            coloredStates.append(state)
            uncoloredStates.remove(state)
            self.forwardCheck(state.color, adjStates)

            # recursive call
            self.colorTheStates()

            # if returned from failed path, reset changes and continue to next color path
            state.setColor('')
            coloredStates.remove(state)
            uncoloredStates.append(state)
            self.reverseForwardCheck(selectedColor, adjStates)

        # backtrack if no colors work
        return

    # returns an uncolored state
    def selectUncoloredState(self, uncoloredStates):
        chosenState = uncoloredStates[0]
        return chosenState

    # verifies color assignment
    def verify(self, color, adjStates):
        for adjState in adjStates:
            if (color == adjState.color):
                return False
        return True

    # implements forward checking
    def forwardCheck(self, selectedColor, adjStates):        
        # check all surrounding nodes and prune
        for adjState in adjStates:
            try:
                adjState.possibleColors.remove(selectedColor)
            except:
                continue

    # reverses effects of forward checking
    def reverseForwardCheck(self, selectedColor, adjStates):
        for adjState in adjStates:
            adjState.possibleColors.append(selectedColor)

    # prints output
    def printColoredStates(self, coloredStates):
        for state in coloredStates:
            print(state.name + ' ' + state.color)

    # checks final output for errors
    def isFinished(self, coloredStates):
            errors = 0
            for state in coloredStates:
                for adj in state.adjStates:
                    if (state.color == adj.color):
                        errors += 1
                
            if (errors == 0):
                return True