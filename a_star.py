from utils import *

cost_so_far = dict()
reached_goal = False
current_side = 1

def a_star_search():
    initial_prob_state = (3, 3, 1)
    frontier_states = set()
    frontier_states.add(initial_prob_state)
    cost_so_far[initial_prob_state] = 0
    explore_states(frontier_states, 1, 0)

def explore_states(frontier_states, current_cost_so_far, current_depth):
    global reached_goal
    while not reached_goal:
        best_frontier_state, best_frontier_fn = find_best_frontier(frontier_states, current_side, calculate_fn)
        toggle_side()

        print("Frontiers: " + str(frontier_states))
        print("Best State: " + str(best_frontier_state))
        print("Best Value: " + str(best_frontier_fn))
        print("")
        frontier_states.remove(best_frontier_state)

        if is_successful_state(best_frontier_state):
            print("Success! Goal state: " + str(best_frontier_state))
            reached_goal = True
        elif boat_on_left(best_frontier_state):
            a_states = get_next_states_with_boat_on_left(best_frontier_state)
            add_new_states_to_frontier(frontier_states, a_states, current_cost_so_far)
        elif boat_on_right(best_frontier_state):
            b_states = get_next_states_with_boat_on_right(best_frontier_state)
            add_new_states_to_frontier(frontier_states, b_states, current_cost_so_far)
        explore_states(frontier_states, current_cost_so_far + 1, current_depth + 1)

def add_new_states_to_frontier(frontier_states, new_states, current_cost_so_far):
    for state in new_states:
        cost_so_far[state] = current_cost_so_far
        frontier_states.add(state)

def toggle_side():
    global current_side
    if current_side == 1:
        current_side = 0
    else:
        current_side = 1

def calculate_fn(prob_state):
    return calculate_gn(prob_state) + calculate_hn(prob_state)

def calculate_hn(prob_state):
    return prob_state[0] + prob_state[1]

def calculate_gn(prob_state):
    return cost_so_far[prob_state]

if __name__ == "__main__":
    a_star_search()
