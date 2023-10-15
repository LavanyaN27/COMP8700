from Node import Node

class HillClimbing:
    def __init__(self, state):
        super().__init__()
        self.initial_node = Node(state)

    def steepest_ascent(self, max_sidesteps=0):
        current_node = self.initial_node
        current_cost = current_node.get_heuristic_cost()
        moves = 0
        sidesteps = 0
        while True:
            if max_sidesteps == 0:
                next_successor, next_cost = current_node.lowest_cost_successor()
            else:
                next_successor, next_cost = current_node.first_choice_successor()
            if(next_cost > current_cost):
                return current_node.state, current_cost, (next_cost == current_cost), moves
            if(next_cost == current_cost):
                sidesteps += 1
                if sidesteps > max_sidesteps:
                    return current_node.state, current_cost, (next_cost == current_cost), moves
            else:
                sidesteps = 0
            current_node, current_cost = next_successor, next_cost
            moves += 1
