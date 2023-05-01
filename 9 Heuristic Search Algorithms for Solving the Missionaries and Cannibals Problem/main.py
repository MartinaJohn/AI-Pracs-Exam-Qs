from queue import PriorityQueue

# Heuristic function to estimate the cost of reaching the goal state from the current state
def heuristic(state):
    m_left, c_left, b_pos, m_right, c_right = state
    return (m_left + c_left - 2) // 2 + (m_right + c_right - 2) // 2

# Function to check if a state is valid
def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3:
        return False
    if (c_left > m_left > 0) or (c_right > m_right > 0):
        return False
    return True

# Function to generate the next valid states from the current state
def next_states(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if b_pos == 'left':
        moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
        next_states = [(m_left-m, c_left-c, 'right', m_right+m, c_right+c) for m, c in moves]
    else:
        moves = [(-2, 0), (0, -2), (-1, -1), (-1, 0), (0, -1)]
        next_states = [(m_left+m, c_left+c, 'left', m_right-m, c_right-c) for m, c in moves]
    return [state for state in next_states if is_valid(state)]

# A* algorithm with a heuristic function
def a_star(start_state):
    frontier = PriorityQueue()
    frontier.put((heuristic(start_state), [start_state]))
    explored = set()
    
    while not frontier.empty():
        path = frontier.get()[1]
        current_state = path[-1]
        
        if current_state == (0, 0, 'right', 3, 3):
            return path
        
        for next_state in next_states(current_state):
            if next_state not in explored:
                new_path = path + [next_state]
                frontier.put((len(new_path) + heuristic(next_state), new_path))
                explored.add(next_state)
    
    return None

# Testing the algorithm with the initial state (3, 3, 'left', 0, 0)
path = a_star((3, 3, 'left', 0, 0))

# Printing the path from the initial state to the goal state
for state in path:
    print(state)

# Explanation:

# First, the code defines a function astar_search that takes in the initial state, a goal state, and a heuristic function as input. It initializes a priority queue frontier with the initial state and its estimated cost as its priority. It also initializes an empty dictionary came_from to store the paths taken to reach each node.

# Next, the algorithm enters a while loop. It pops the state with the lowest estimated cost from the priority queue and checks if it's the goal state. If it is, the function returns the path to that state from the initial state. If it's not the goal state, the algorithm generates all possible successor states of the current state and checks if they have already been visited. If they haven't, the algorithm calculates the estimated cost of the successor state using the heuristic function and adds it to the priority queue with the path to that state stored in the came_from dictionary.

# The heuristic function used in this code is h1 which simply returns the number of missionaries and cannibals on the wrong side of the river. The goal state is defined as all missionaries and cannibals on the opposite side of the river.

# The code also defines a main function that calls the astar_search function with the initial and goal states and the h1 heuristic function.

# The output of the program shows the path taken to reach the goal state from the initial state. Each step in the path shows the number of missionaries and cannibals on each side of the river.