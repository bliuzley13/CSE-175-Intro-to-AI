#
# ucost.py
#
# This file provides a function implementing uniform cost search for a
# route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#

from route import Node
from route import Frontier


def uniform_cost_search(problem, repeat_check=False):
    """Perform uniform cost search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # Initializes new Node
    start_node = Node(problem.start)
    if problem.is_goal(start_node):
        return start_node
    # Initializes frontier, doesn't check repeat check
    frontier = Frontier(start_node, 'g')
    # Keeps track of locations explored
    reached_set = set()
    if repeat_check:
        reached_set.add(start_node.loc)
    # Starts a loop until frontier is empty
    while not frontier.is_empty():
        # Removes and returns node from frontier for exploration
        current_node = frontier.pop()
        # Checks if current node's location is the goal state, then returns node indicating goal being found
        if problem.is_goal(current_node.loc):
            return current_node
        # Expands current node to generate child nodes in problem space
        child_nodes = current_node.expand(problem)
        # Iterates through child nodes
        for child in child_nodes:
            child_loc = child.loc
            # Checks whether child node's location is not explored before
            if repeat_check:
                if child_loc in reached_set:
                    if child in frontier:
                        if Node.value(child) < Node.value(current_node):
                            frontier.remove(current_node)
                            frontier.add(child)
                else:
                    frontier.add(child)
                    reached_set.add(child_loc)
            else:
                frontier.add(child)
                reached_set.add(child_loc)
    return None
