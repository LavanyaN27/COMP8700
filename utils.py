import numpy as np
import math

def is_successful_state(probability_state):
    return probability_state[0] == probability_state[1] == 0

def boat_on_left(probability_state):
    return probability_state[2] == 1

def boat_on_right(probability_state):
    return probability_state[2] == 0

def get_next_states_with_boat_on_left(probability_state):
    new_states = []
    for missionary in range(probability_state[0] + 1):
        for cannibal in range(probability_state[1] + 1):
            if missionary + cannibal < 1 or missionary + cannibal > 2:
                continue
            new_state = (probability_state[0] - missionary,
                         probability_state[1] - cannibal,
                         0)
            if 0 < new_state[0] < new_state[1]:
                continue
            if 0 < 3 - new_state[0] < 3 - new_state[1]:
                continue
            new_states.append(new_state)
    return new_states

def get_next_states_with_boat_on_right(probability_state):
    new_states = []
    for missionary in range(3 - probability_state[0] + 1):
        for cannibal in range(3 - probability_state[1] + 1):
            if missionary + cannibal < 1 or missionary + cannibal > 2:
                continue
            new_state = (probability_state[0] + missionary,
                         probability_state[1] + cannibal,
                         1)
            if 0 < new_state[0] < new_state[1]:
                continue
            if 0 < 3 - new_state[0] < 3 - new_state[1]:
                continue
            new_states.append(new_state)

    return new_states

def find_best_frontier(frontier_states, side, compute_fn):
    min_value = 100000
    min_state = -1
    for state in frontier_states:
        if state[2] != side:
            continue
        fn = compute_fn(state)
        if fn < min_value:
            min_value = fn
            min_state = state
    return min_state, min_value
