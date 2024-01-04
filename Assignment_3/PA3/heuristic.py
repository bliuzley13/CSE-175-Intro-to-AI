#
# heuristic.py
#
# This Python script file provides two functions in support of minimax search
# using the expected value of game states. First, the file provides the
# function "expected_value_over_delays". This function takes as an argument
# a state of game play in which the current player has just selected an
# action. The function calculates the expected value of the state over all
# possible random results determining the amount of time before the
# Guardian changes gaze direction. This function calculates this value
# regardless of whose turn it is. The value of game states that result from
# different random outcomes is determined by calling "value". Second, the
# file provides a heuristic evaluation function for non-terminal game states.
# The heuristic value returned is between "max_payoff" (best for the
# computer player) and negative one times that value (best for the opponent).
# The heuristic function may be applied to any state of play. It uses
# features of the game state to predict the game payoff without performing
# any look-ahead search.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE
#
# Arvind Kumar 12/1/2023
#


from parameters import *
from minimax import probability_of_time
from minimax import value


def expected_value_over_delays(state, ply):
    """Calculate the expected utility over all possible randomly selected
    Guardian delay times. Return this expected utility value."""
    val = 0.0
    #Iterates over a range of delay times

    for i in range(min_time_steps, max_time_steps+1):
        #Calculates probability of that time
        prob_Time = probability_of_time(i)
        #Ensures state is updated
        state.time_remaining = i
        #Calculates value of current state
        res_Value = value(state, ply)
        #Gets a result that is the expected utility over all possible delay times
        val = val + res_Value * prob_Time
    # PLACE YOUR CODE HERE
    # Note that the value of "ply" must be passed along, without
    # modification, to any function calls that calculate the value 
    # of a state.

    return val


def heuristic_value(state):
    """Return an estimate of the expected payoff for the given state of
    game play without performing any look-ahead search. This value must
    be between the maximum payoff value and the additive inverse of the
    maximum payoff."""
    val = 0.0
    #Variables representing the positions of the computer player and actual player in game state
    comp_player = state.w_loc
    act_player = state.e_loc
    #Calculates normalized position of the winninng player based on minimum divided by max act steps
    win_position = float((min((comp_player*-1), act_player)) / max_act_steps)
    #Calculates the difference between positions of actual player and computer player
    diff = float(act_player + comp_player)
    #Normalizes difference between the positions by dividing it by win_position and ensuring result is
    #between -1 and 1
    norm_diff = max(-1, min(1, diff/win_position))
    #Calculates heuristic value as a weighted product
    # PLACE YOUR CODE HERE
    val = ((max_payoff * 0.97) * norm_diff)

    return val