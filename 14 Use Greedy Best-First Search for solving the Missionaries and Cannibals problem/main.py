# Define the problem as a graph with nodes, edges and heuristic values
graph = {
    "start": {"A": 2, "B": 5, "h": 7},
    "A": {"C": 1, "D": 2, "h": 4},
    "B": {"D": 6, "E": 2, "h": 6},
    "C": {"F": 1, "h": 3},
    "D": {"F": 4, "G": 3, "h": 3},
    "E": {"G": 6, "h": 4},
    "F": {"goal": 3, "h": 0},
    "G": {"goal": 4, "h": 0},
    "goal": {"h": 0}
}

# Define the initial and goal states
initial_state = "start"
goal_state = "goal"

# Define a function to find the lowest heuristic node in a list
def find_lowest_heuristic_node(nodes):
    lowest_heuristic = float("inf")
    lowest_heuristic_node = None
    for node in nodes:
        heuristic = graph[node]["h"]
        if heuristic < lowest_heuristic:
            lowest_heuristic = heuristic
            lowest_heuristic_node = node
    return lowest_heuristic_node

# Define a function to perform Greedy Best-First Search algorithm
def gbfs(graph, initial_state, goal_state):
    # Initialize an empty list to store the path
    path = []

    # Initialize the current node as the initial state
    current_node = initial_state

    # Loop until the current node is the goal state or None
    while current_node != goal_state and current_node is not None:
        # Append the current node to the path
        path.append(current_node)

        # Get the neighbors of the current node from the graph
        neighbors = graph[current_node]

        # Remove the heuristic value from the neighbors dictionary
        neighbors.pop("h")

        # Find the next lowest heuristic node from the neighbors
        current_node = find_lowest_heuristic_node(neighbors)

    # If the goal state is reached, append it to the path and return it, otherwise return None
    if current_node == goal_state:
        path.append(goal_state)
        return path
    
    else:
        return None

# Test the function with an example
path = gbfs(graph, initial_state, goal_state)
print(f"The optimal path is {path}")

# Explanation:

# The graph is represented as a dictionary where each node is a key and its value is another dictionary that contains its neighbors as keys and their corresponding edge weights, as well as the heuristic value of the node. The heuristic value is an estimate of the distance from the node to the goal state, which is used to guide the search towards the goal.

# The initial and goal states are defined as strings.

# The find_lowest_heuristic_node function takes a list of nodes and returns the node with the lowest heuristic value. It iterates through each node in the list and retrieves its heuristic value from the graph. If the heuristic value is lower than the current lowest heuristic, it updates the lowest heuristic and stores the node with that heuristic value.

# The gbfs function takes the graph, initial state, and goal state as inputs. It initializes an empty list to store the path, sets the current node as the initial state, and loops until the current node is the goal state or None.

# In each iteration, the current node is appended to the path. The neighbors of the current node are retrieved from the graph, and the heuristic value is removed from the dictionary of neighbors. The find_lowest_heuristic_node function is then used to find the next lowest heuristic node from the neighbors. If the current node is the goal state, it is appended to the path and the path is returned. Otherwise, None is returned.

# Finally, the gbfs function is called with the provided graph, initial_state, and goal_state. The optimal path is then printed to the console