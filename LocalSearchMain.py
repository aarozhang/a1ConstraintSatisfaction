import sys
import random
from State import State
from LocalSearch import LocalSearch

colors = []
states = []

def main():
    global colors
    global states
    inFile = sys.argv[1]
    setVariables(inFile)

    # store possible colors in states & randomly assign states a color
    for state in states:
        possibleColors = colors.copy()
        state.setPossibleColors(possibleColors)
        state.color = random.choice(colors)
    
    # call local search
    aLocalSearch = LocalSearch(states, colors)
    aLocalSearch.colorTheStates()

# read and store colors, states, and adjacent states
def setVariables(fileName):
    global colors
    global states

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
            states.append(newState)

    # store adjacents
    for line in f:
        if not line.strip():
            break
        else:
            splitStrings = line.split()
            mainState = splitStrings[0]
            adjState = splitStrings[1]
            for state1 in states:
                if state1.name == mainState:
                    for state2 in states:
                        if state2.name == adjState:
                            state1.setAdjacents(state2)
                            state2.setAdjacents(state1)


if __name__ == "__main__":
    main()