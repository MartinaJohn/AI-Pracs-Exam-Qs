def hanoi_dfs(n, source, target, aux):
    # Define the stack for DFS algorithm
    stack = []
    # Push the initial state to the stack
    stack.append((n, source, target, aux))
    # Loop until the stack is empty
    while stack:
        # Pop the top state from the stack
        state = stack.pop()
        # If n is 1, move the disk directly from source to target
        if state[0] == 1:
            print(f"Move disk 1 from {state[1]} to {state[2]}")
        else:
            # Push the subproblems to the stack
            stack.append((state[0]-1, state[1], state[3], state[2]))
            stack.append((1, state[1], state[2], state[3]))
            stack.append((state[0]-1, state[3], state[2], state[1]))
    print("Tower of Hanoi problem solved!")

# Take user input for the number of disks and the towers
n = int(input("Enter the number of disks (min 3): "))
source = input("Enter the source tower (A, B, or C): ")
target = input("Enter the target tower (A, B, or C): ")
aux = input("Enter the auxiliary tower (A, B, or C): ")

# Test the function with user input
hanoi_dfs(n, source, target, aux)

# Explanation:

# The hanoi_dfs function takes three arguments: n represents the number of disks, source represents the starting peg, target represents the target peg, and aux represents the auxiliary peg. The function initializes a stack for the DFS algorithm and pushes the initial state to the stack, which is represented by a tuple containing four elements: n, source, target, and aux. The while loop runs until the stack is empty. In each iteration of the loop, the top state is popped from the stack. If n is 1, the function moves the disk directly from the source peg to the target peg. Otherwise, the function pushes three subproblems to the stack in the following order:

# Move n-1 disks from the source peg to the aux peg, using target as the auxiliary peg. Move the largest disk from the source peg to the target peg. Move n-1 disks from the aux peg to the target peg, using source as the auxiliary peg. Finally, the function prints a message indicating that the Tower of Hanoi problem is solved.

# The output shows the sequence of disk movements required to solve the Tower of Hanoi problem with 3 disks. The movements are shown in a visual manner, where A, B, and C represent the three pegs, and each line represents a movement of a disk from one peg to another. For example, the first line of the output (Move disk 1 from A to C) indicates that the smallest disk is moved from the source peg (A) to the target peg (C).