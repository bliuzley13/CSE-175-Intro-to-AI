#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS AND ACKNOWLEDGMENTS
#
# Arvind Kumar - 9/26/2023
#


from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    #Initializes new Node
    node = Node(problem.start)
    #Initializes frontier, doesnt check repeat check
    qew = Frontier(node,False)
    #Keeps track of locations explored
    reached = set()
    #Starts a loop until frontier is empty
    while not qew.is_empty():
        #Removes and returns node from frontier for exploration
        node = qew.pop()
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
                    qew.add(child)
                    reached.add(child.loc)
            #Adds child node to frontier without checking for repeated states
            else:
                qew.add(child)
    return None

    # function SEARCH(problem) returns a solution node or failure
    # node < - a node containing the initial state of problem
    # if node contains a goal state of problem then return node
    # initialize the frontier to contain node
    # initialize the reached set to contain node
    # while frontier is not empty
    #     node < - a leaf node removed from frontier
    #     if node contains a goal state of problem then return node
    #     expand node
    #     for each child of node
    #     add child to frontier
    #         and add child to the reached set,
    #         only if not already in the reached set
    # return failure
