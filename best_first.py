from utils import *

maximum_depth = 20
is_goal_reached = False
current_side = 1


def best_first_search():
    initial_prob_state = (3, 3, 1)
    frontier_states = list()
    frontier_states.append(initial_prob_state)
    explore_states(frontier_states, 0)


def explore_states(frontier_states, current_depth):
    global is_goal_reached
    while not is_goal_reached:
        best_frontier_state, best_frontier_value = find_best_frontier(frontier_states, current_side, calculate_value)
        toggle_side()

        print("Frontiers: " + str(frontier_states))
        print("Best State: " + str(best_frontier_state))
        print("Best Value: " + str(best_frontier_value))
        print("")
        frontier_states.remove(best_frontier_state)

        if is_successful_state(best_frontier_state):
            print("Success! Goal state: " + str(best_frontier_state))
            is_goal_reached = True
        elif boat_on_left(best_frontier_state):
            add_new_states_to_frontier(frontier_states, get_next_states_with_boat_on_left(best_frontier_state))
        elif boat_on_right(best_frontier_state):
            add_new_states_to_frontier(frontier_states, get_next_states_with_boat_on_right(best_frontier_state))

        explore_states(frontier_states, current_depth + 1)


def add_new_states_to_frontier(frontier_states, new_states):
    frontier_states += new_states


def toggle_side():
    global current_side
    if current_side == 1:
        current_side = 0
    else:
        current_side = 1


def calculate_value(prob_state):
    return calculate_heuristic_value(prob_state)


def calculate_heuristic_value(prob_state):
    return prob_state[0] + prob_state[1]


if __name__ == "__main__":
    best_first_search()
