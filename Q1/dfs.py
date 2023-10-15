from utils import *

maximum_depth = 20
is_goal_reached = False
states_to_explore = list()
visited_states = set()


def depth_first_search():
    initial_prob_state = (3, 3, 1)
    visited_states.add(initial_prob_state)
    states_to_explore = [initial_prob_state]
    root_node_id = "0" + str(initial_prob_state) + "0"

    initial_next_states = get_next_states_with_boat_on_left(initial_prob_state)
    explore_next_depth(initial_next_states, 1, states_to_explore, root_node_id)


def handle_goal_reached(prob_state, state_stack):
    global is_goal_reached
    state_stack.append(prob_state)
    print("Solution found!")
    print("The following sequence of states leads to a solution:")
    for state in state_stack:
        print(state)
    is_goal_reached = True


def get_next_possible_states(prob_state):
    next_states = []
    if boat_on_left(prob_state):
        next_states = get_next_states_with_boat_on_left(prob_state)
    elif boat_on_right(prob_state):
        next_states = get_next_states_with_boat_on_right(prob_state)
    return next_states


def handle_failure(prob_state, state_stack, current_depth, parent_node_id):
    state_stack.append(prob_state)
    next_states = get_next_possible_states(prob_state)
    non_duplicate_states = []
    for next_state in next_states:
        if next_state not in visited_states:
            visited_states.add(next_state)
            non_duplicate_states.append(next_state)
    explore_next_depth(non_duplicate_states, current_depth + 1, state_stack, parent_node_id)
    state_stack.pop()


def explore_next_depth(states_at_same_level, current_depth, state_stack, parent_node_id):
    global is_goal_reached
    for index, prob_state in enumerate(states_at_same_level):
        if not is_goal_reached:
            visited_states.add(prob_state)
            current_node_id = generate_current_node_id(prob_state, current_depth, index, parent_node_id)
            if is_successful_state(prob_state):
                handle_goal_reached(prob_state, state_stack)
            elif current_depth < maximum_depth:
                handle_failure(prob_state, state_stack, current_depth, current_node_id)


def generate_current_node_id(prob_state, current_depth, index, parent_node_id):
    current_node_id = parent_node_id + str(current_depth) + str(prob_state) + str(index)
    return current_node_id


if __name__ == "__main__":
    depth_first_search()
