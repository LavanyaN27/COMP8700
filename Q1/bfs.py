from utils import *

def get_next_possible_states(prob_state):
    if boat_on_left(prob_state):
        return get_next_states_with_boat_on_left(prob_state)
    else:
        return get_next_states_with_boat_on_right(prob_state)

def breadth_first_search():
    state_stack = list()
    visited_states = set()
    initial_state = (3, 3, 1)
    visited_states.add(initial_state)
    states = [initial_state]
    all_states = [states]

    success = False
    while not success:
        print("States: " + str(states))
        new_states = []
        for prob_state in states:
            print("Current State: " + str(prob_state))
            state_stack.append(prob_state)
            if is_successful_state(prob_state):
                print("Success! Goal state: " + str(prob_state))
                success = True
                break
            future_states = get_next_possible_states(prob_state)
            for future_state in future_states:
                if future_state not in visited_states:
                    new_states.append(future_state)
                    visited_states.add(future_state)
                    print("Next State: " + str(future_state))
            print()
        print("Visited states: " + str(visited_states))
        print()
        if not success:
            states = new_states
            all_states.append(states)
    print()
    print()
    print("All States:")
    for p_state in all_states:
        print(p_state)

if __name__ == "__main__":
    breadth_first_search()
