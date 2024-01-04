#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


from route import Node
from route import Frontier


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""
    node = Node(problem.start)
    if problem.is_goal(node.loc):
        return node
    frontier = Frontier(node, 'f')
    reached = set()
    if repeat_check:
        reached.add(node.loc)

    while frontier.is_empty() == False:
        node = frontier.pop()
        if problem.is_goal(node.loc):
            return node
        for child in node.expand(h.problem):
            child_loc = child.loc
            if (child_loc not in reached) and (frontier.contains(child) is False):
                if repeat_check:
                    reached.add(child_loc)
                frontier.add(child)
            else:
                if frontier.contains(child):
                    if (child.path_cost + child.h_eval) < frontier.__getitem__(child):
                        if repeat_check and (child_loc not in reached):
                            reached.add(child_loc)
                        frontier.__delitem__(child)
                        frontier.add(child)
    return None


