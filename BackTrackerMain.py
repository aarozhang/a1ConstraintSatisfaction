import sys
from State import State
from BackTracker import BackTracker

colors = []
uncoloredStates = []
coloredStates = []

def main():
    global colors
    global uncoloredStates
    inFile = sys.argv[1]
    setVariables(inFile)

    # store possible colors in states & assign states with no adj a color (ie. tasmania)
    for state in uncoloredStates:
        possibleColors = colors.copy()
        state.setPossibleColors(possibleColors)
        if not state.adjStates:
            state.color = colors[0]
            coloredStates.append(state)
            uncoloredStates.remove(state)

    # call backTracking search
    aBackTrackerSearch = BackTracker(coloredStates, uncoloredStates)
    aBackTrackerSearch.colorTheStates()

# read and store colors, states, and adjacent states
def setVariables(fileName):
    global colors
    global uncoloredStates

    f = open(fileName, 'r')

    # store colors
    for line in f:
        if not line.strip(): #checks for empty line
            break
        else:
            colorName = line.strip()
            colors.append(colorName)

    # create/store state objs
    for line in f:
        if not line.strip():
            break
        else:
            stateName = line.strip()
            newState = State(stateName)
            uncoloredStates.append(newState)

    # store adjacents
    for line in f:
        if not line.strip():
            break
        else:
            splitStrings = line.split()
            mainState = splitStrings[0]
            adjState = splitStrings[1]
            for state1 in uncoloredStates:
                if state1.name == mainState:
                    for state2 in uncoloredStates:
                        if state2.name == adjState:
                            state1.setAdjacents(state2)
                            state2.setAdjacents(state1)


if __name__ == "__main__":
    main()