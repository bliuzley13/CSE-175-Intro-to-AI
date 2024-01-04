#
# greedy.py
#
# This file provides a function implementing greedy best-first search for
# a route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier. Also, this function uses heuristic function objects defined
# in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


from route import Node
from route import Frontier

from route import Node, Frontier


def greedy_search(problem, heuristic, repeat_check=False):
    """Perform greedy best-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # Initialize the start node
    start_node = Node(problem.start)
    if problem.is_goal(start_node.loc):
        return start_node

    # Initialize the frontier with the start node and heuristic values
    frontier = Frontier(start_node, 'h')
    # Keep track of explored locations
    reached = set()

    if repeat_check:
        reached.add(start_node.loc)

    while not frontier.is_empty():
        # Remove and return the node from frontier for exploration
        start_node = frontier.pop()
        # Check if the current node's location is the goal state
        if problem.is_goal(start_node.loc):
            return start_node
        # Iterate through child nodes
        start_nodes = start_node.expand(heuristic.problem)
        for child in start_nodes:
            child_loc = child.loc
            # Check if the child node's location is not explored before


            if (child.loc not in reached) and (frontier.contains(child) is False):
                if repeat_check:
                    reached.add(child_loc)
                frontier.add(child)

                 

    return None  # No solution found


