#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem
        locations = self.problem.map.connection_dict
        speedMax = 0
        for location in locations:
            keys = (self.problem.map.connection_dict[location].keys())
            values = (self.problem.map.connection_dict[location].values())
            for key, value in zip(keys, values):
                dist = self.problem.map.euclidean_distance(location, key)
                if (dist/value)>speedMax:
                    self.speedMax = dist/value
        self.speedMax = speedMax

    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            distance = self.problem.map.euclidean_distance(loc, self.problem.goal)
            value = distance / self.speedMax
            return value

