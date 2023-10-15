import numpy as np
from itertools import product

class Node:
    state = np.array([0,1,2,3,4,5,6,7])

    def __init__(self, column_positions):
        super().__init__()
        self.state = np.array(column_positions)
        
    def get_heuristic_cost(self):
        return Node.heuristic_cost(self.state)

    @staticmethod
    def heuristic_cost(state):
        cost = 0
        for index, queen in enumerate(state):
            cost += (np.count_nonzero(state == queen) - 1)
            cost += (np.count_nonzero(abs(state - queen) ==  abs(np.arange(8) - index)) - 1)
        return (cost // 2)

    def get_successor_states(self):
        successors = []
        for index, queen in product(range(8), range(8)):
            if(queen != self.state[index]):
                new_state = self.state.copy()
                new_state[index] = queen
                successors.append(new_state)
        return successors

    def random_successor(self):
        new_state = self.state.copy()
        index = np.random.randint(8)
        choices = [a for a in range(8) if a != self.state[index]]
        new_state[index] = np.random.choice(choices)
        return Node(new_state), Node.heuristic_cost(new_state)

    def first_choice_successor(self):
        cost = self.get_heuristic_cost()
        successors = self.get_successor_states()
        np.random.shuffle(successors)
        side_state, side_cost = None, None
        for successor in successors:
            successor_cost = Node.heuristic_cost(successor)
            if successor_cost < cost:
                return Node(successor), successor_cost
            if side_state is None and successor_cost == cost:
                side_state, side_cost = successor, successor_cost
        if side_state is not None:
            return Node(side_state), side_cost
        return Node(successor), successor_cost

    def lowest_cost_successor(self):
        successors = self.get_successor_states()
        costs = [Node.heuristic_cost(successor) for successor in successors]
        best_successor_index = np.argmin(costs)
        return Node(successors[best_successor_index]), costs[best_successor_index]
