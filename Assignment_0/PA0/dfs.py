#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# YOUR COMMENTS INCLUDING CITATIONS AND ACKNOWLEDGMENTS
#
# Arvind Kumar - 9/29/2023
# 


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    #Initializes new Node
    node = Node(problem.start)
    #Initializes frontier, doesnt check repeat check
    stck = Frontier(node, True)
    #Keeps track of locations explored
    reached = set()
    #Starts a loop until frontier is empty
    while not stck.is_empty():
        #Removes and returns node from frontier for exploration
        node = stck.pop()
        #Checks if current node's location is goal state, then returns node indicating goal being found
        if problem.is_goal(node.loc):
            return node
        #Expands current node to generate child nodes in problem space
        nunode = node.expand(problem)
        #Adds current node's location to set of explored states
        reached.add(node.loc)
        #Iterates through child nodes
        for child in nunode:
            #Checks whether child node's location is not explored before
            if repeat_check == True:
                # adds child node to frontier and set of explored places
                if child.loc not in reached:
                    stck.add(child)
                    reached.add(child.loc)
            else:
                stck.add(child)
                # Adds child node to frontier without checking for repeated states
                pass
    return None
