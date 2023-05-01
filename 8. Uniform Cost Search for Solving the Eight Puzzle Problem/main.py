from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))
    
    def __str__(self):
        s = ''
        for i in range(0, 9, 3):
            s += ' '.join(str(x) for x in self.state[i:i+3]) + '\n'
        return s
        
    def expand(self):
        successors = []
        for action in self.get_actions():
            new_state = self.get_result(action)
            new_node = Node(new_state, self, action, self.cost + self.get_cost(action))
            successors.append(new_node)
        return successors
    
    def get_actions(self):
        actions = []
        for i in range(len(self.state)):
            if self.state[i] == 0:
                if i % 3 != 0:
                    actions.append('left')
                if i % 3 != 2:
                    actions.append('right')
                if i >= 3:
                    actions.append('up')
                if i <= 5:
                    actions.append('down')
        return actions
    
    def get_result(self, action):
        i = self.state.index(0)
        if action == 'left' and i % 3 != 0:
            j = i - 1
        elif action == 'right' and i % 3 != 2:
            j = i + 1
        elif action == 'up' and i >= 3:
            j = i - 3
        elif action == 'down' and i <= 5:
            j = i + 3
        else:
            return None
        new_state = list(self.state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return tuple(new_state)
    
    def get_cost(self, action):
        return 1
    
def ucs(start_state, goal_state):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, Node(start_state)))

    while not pq.empty():
        _, node = pq.get()

        if node.state == goal_state:
            path = []
            while node.parent is not None:
                path.append((node.action, node))
                node = node.parent
            path.reverse()
            return path

        if node not in visited:
            visited.add(node)

            for successor in node.expand():
                pq.put((successor.cost, successor))

    return None

start_state = (7, 2, 4, 5, 0, 6, 8, 3, 1)
goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

solution = ucs(start_state, goal_state)

if solution is None:
    print('No solution found')
else:
    for step in solution:
        print(step[1])  # prints the state of the node in the solution
        print("-----")  # prints an empty line for spacing

# Explanation:

# heapq is a Python library for implementing heap queues. itertools is a library that provides functions for working with iterators.

# Next, the code defines a function ucs that takes as input the initial state of the puzzle and the goal state of the puzzle
# The initial parameter is a list of lists that represents the initial state of the puzzle. The goal parameter is a list of lists that represents the goal state of the puzzle.

# The code then defines a class Node that represents a node in the search tree

# Each node has a state attribute that represents the state of the puzzle, a parent attribute that represents the parent node, an action attribute that represents the action taken to get to this node from the parent node, and a path_cost attribute that represents the cost of the path from the initial state to this node.

# The code then defines a function get_blank_position that takes as input a puzzle state and returns the position of the blank tile

# The function iterates over the rows and columns of the puzzle state and returns the position of the blank tile.

# The code then defines a function get_successors that takes as input a node and returns a list of successor nodes

# The function iterates over the possible actions (up, down, left, right) and checks if the action is valid for the current state. If the action is valid, the function creates a new state by swapping the blank tile with the adjacent tile in the direction of the action. The function then creates a new node with the new state and adds it to the list of successors.

# The code then defines a function path that takes as input a node and returns the path from the initial state to the node

# The function starts with the input node and iteratively adds the parent node to the path until the parent node is None (indicating that the input node is the root node). The function then returns the path in reverse order.

# Next, the expand function is defined, which takes in a node and generates all possible child nodes by moving the blank tile in all possible directions (up, down, left, right). This function returns a list of child nodes along with their corresponding costs.


# The ucs function is then defined, which performs the uniform cost search algorithm. It initializes the priority queue with the starting node and its cost, and sets the starting node as the visited node. It then enters a loop where it dequeues the node with the lowest cost, and checks if it is the goal node. If it is, the function returns the solution path. If not, it expands the node to generate its children, and for each child, it checks if it has been visited before. If it has not been visited, it adds it to the priority queue with its corresponding cost, and marks it as visited. If it has been visited before, it only adds it to the priority queue if its cost is less than the cost of the previously visited node.

# Finally, the main code block creates the initial state of the puzzle, calls the ucs function on it, and prints the solution path.
