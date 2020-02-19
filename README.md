# a1ConstraintSatisfaction

a1ConstraintSatisfaction is assignment 1 for comp560 at UNC

HOW TO RUN:
My project consists of 5 main files:
    - BackTracker.py
    - BackTrackerMain.py
    - LocalSearch.py
    - LocalSearchMain.py
    - State.py
    
I have separated each search implementation into its own "main" file. For example, to run the backtracker, you must run BackTrackerMain.py.
The "main" files read the input file and create a search object located in either BackTracker.py or LocalSearch.py.
The searches are run in either BackTracker.py or LocalSearch.py.
State.py is simply a file housing the State object.

To run Backtracker in the shell, use the command:
    python BackTrackerMain.py filename.txt

Or for LocalSearch:
    python LocalSearchMain.py filename.txt:
    
filename.txt is the name of the input file you wish to run my code on.
Please note that I have included test files in my repository that should be the same format as the official test files.

My programs output directly to the terminal.
The following is the output format:
    SearchName Output:
    Number of Steps = ###
    State Color
    State Color
    State Color
    State Color
    etc.
    
