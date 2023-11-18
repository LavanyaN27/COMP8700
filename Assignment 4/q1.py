import numpy as np

# Create a general game
class Game:
    def current_player(self, state):
        return state.current_player

    def helper_util(self, state, player):
        raise NotImplementedError

    def tasks(self, state):
        raise NotImplementedError

    def goal_state(self, state, move):
        raise NotImplementedError

    def is_terminal(self, state):
        return not self.tasks(state)

# Define the two-ply game in fig 5.2
class TwoPlyGame(Game):
    start = "A"
    utilities = {
        "B1": 3,
        "B2": 12,
        "B3": 8,
        "C1": 2,
        "C2": 4,
        "C3": 6,
        "D1": 14,
        "D2": 5,
        "D3": 2
    }
    paths = {
        "A": {
            "a1": "B",
            "a2": "C",
            "a3": "D"
        },
        "B": {
            "b1": "B1",
            "b2": "B2",
            "b3": "B3"
        },
        "C": {
            "c1": "C1",
            "c2": "C2",
            "c3": "C3"
        },
        "D": {
            "d1": "D1",
            "d2": "D2",
            "d3": "D3"
        }
    }

    def current_player(self, state):
        return 'min' if state in 'BCD' else 'max'

    def helper_util(self, state, player):
        if player == 'max':
            return self.utilities[state]
        else:
            return -self.utilities[state]
    
    def tasks(self, state):
        return list(self.paths.get(state, {}).keys())

    def goal_state(self, state, move):
        return self.paths[state][move]

    def is_terminal(self, state):
        return state not in ('A', 'B', 'C', 'D')

class FourPlyGame1(Game):
    start = "A"
    utilities = {
        "B111": 10,
        "B112": 18,
        "B121": 19,
        "B122": 4,
        "B211": 15,
        "B212": 5,
        "B221": 2,
        "B222": 5,
        "C111": 6,
        "C112": 2,
        "C121": 3,
        "C122": 4,
        "C211": 15,
        "C212": 9,
        "C221": 1,
        "C222": 7,
        "D111": 15,
        "D112": 18,
        "D121": 7,
        "D122": 19,
        "D211": 17,
        "D212": 11,
        "D221": 19,
        "D222": 5
    }
    paths = {
        "A": {
            "a1": "B",
            "a2": "C",
            "a3": "D"
        },
        "B": {
            "b1": "B1",
            "b2": "B2",
        },
        "C": {
            "c1": "C1",
            "c2": "C2",
        },
        "D": {
            "d1": "D1",
            "d2": "D2",
        },
        "B1": {
            "b11": "B11",
            "b12": "B12",
        },
        "B2": {
            "b21": "B21",
            "b22": "B22",
        },
        "C1": {
            "c11": "C11",
            "c12": "C12",
        },
        "C2": {
            "c21": "C21",
            "c22": "C22",
        },
        "D1": {
            "d11": "D11",
            "d12": "D12",
        },
        "D2": {
            "d21": "D21",
            "d22": "D22",
        },
        "B11": {
            "b111": "B111",
            "b112": "B112",
        },
        "B12": {
            "b121": "B121",
            "b122": "B122",
        },
        "B21": {
            "b211": "B211",
            "b212": "B212",
        },
        "B22": {
            "b221": "B221",
            "b222": "B222",
        },
        "C11": {
            "c111": "C111",
            "c112": "C112",
        },
        "C12": {
            "c121": "C121",
            "c122": "C122",
        },
        "C21": {
            "c211": "C211",
            "c212": "C212",
        },
        "C22": {
            "c221": "C221",
            "c222": "C222",
        },
        "D11": {
            "d111": "D111",
            "d112": "D112",
        },
        "D12": {
            "d121": "D121",
            "d122": "D122",
        },
        "D21": {
            "d211": "D211",
            "d212": "D212",
        },
        "D22": {
            "d221": "D221",
            "d222": "D222",
        }
    }

    def current_player(self, state):
        return 'min' if state in ('B', 'C', 'D', 'B11', 'B12', 'B21', 'B22', 'C11', 'C12', 'C21', 'C22', 'D11', 'D12', 'D21', 'D22') else 'max'

    def helper_util(self, state, player):
        if player == 'max':
            return self.utilities[state]
        else:
            return -self.utilities[state]
    
    def tasks(self, state):
        return list(self.paths.get(state, {}).keys())

    def goal_state(self, state, move):
        return self.paths[state][move]

    def is_terminal(self, state):
        return state not in ('A', 'B', 'C', 'D', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'B11', 'B12', 'B21', 'B22', 'C11', 'C12', 'C21', 'C22', 'D11', 'D12', 'D21', 'D22')

class FourPlyGame2(Game):
    start = "A"
    utilities = {
        "B111": 10,
        "B112": 49,
        "B121": 41,
        "B122": 14,
        "B211": 3,
        "B212": 5,
        "B221": 24,
        "B222": 4,
        "C111": 34,
        "C112": 44,
        "C121": 29,
        "C122": 34,
        "C211": 38,
        "C212": 13,
        "C221": 27,
        "C222": 6,
        "D111": 39,
        "D112": 8,
        "D121": 45,
        "D122": 21,
        "D211": 43,
        "D212": 31,
        "D221": 13,
        "D222": 47
    }
    paths = {
        "A": {
            "a1": "B",
            "a2": "C",
            "a3": "D"
        },
        "B": {
            "b1": "B1",
            "b2": "B2",
        },
        "C": {
            "c1": "C1",
            "c2": "C2",
        },
        "D": {
            "d1": "D1",
            "d2": "D2",
        },
        "B1": {
            "b11": "B11",
            "b12": "B12",
        },
        "B2": {
            "b21": "B21",
            "b22": "B22",
        },
        "C1": {
            "c11": "C11",
            "c12": "C12",
        },
        "C2": {
            "c21": "C21",
            "c22": "C22",
        },
        "D1": {
            "d11": "D11",
            "d12": "D12",
        },
        "D2": {
            "d21": "D21",
            "d22": "D22",
        },
        "B11": {
            "b111": "B111",
            "b112": "B112",
        },
        "B12": {
            "b121": "B121",
            "b122": "B122",
        },
        "B21": {
            "b211": "B211",
            "b212": "B212",
        },
        "B22": {
            "b221": "B221",
            "b222": "B222",
        },
        "C11": {
            "c111": "C111",
            "c112": "C112",
        },
        "C12": {
            "c121": "C121",
            "c122": "C122",
        },
        "C21": {
            "c211": "C211",
            "c212": "C212",
        },
        "C22": {
            "c221": "C221",
            "c222": "C222",
        },
        "D11": {
            "d111": "D111",
            "d112": "D112",
        },
        "D12": {
            "d121": "D121",
            "d122": "D122",
        },
        "D21": {
            "d211": "D211",
            "d212": "D212",
        },
        "D22": {
            "d221": "D221",
            "d222": "D222",
        }
    }

    def current_player(self, state):
        return 'min' if state in ('B', 'C', 'D', 'B11', 'B12', 'B21', 'B22', 'C11', 'C12', 'C21', 'C22', 'D11', 'D12', 'D21', 'D22') else 'max'

    def helper_util(self, state, player):
        if player == 'max':
            return self.utilities[state]
        else:
            return -self.utilities[state]
    
    def tasks(self, state):
        return list(self.paths.get(state, {}).keys())

    def goal_state(self, state, move):
        return self.paths[state][move]

    def is_terminal(self, state):
        return state not in ('A', 'B', 'C', 'D', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'B11', 'B12', 'B21', 'B22', 'C11', 'C12', 'C21', 'C22', 'D11', 'D12', 'D21', 'D22')

class FourPlyGame3(Game):
    start = "A"
    utilities = {
        "B111": 748,
        "B112": 786,
        "B121": 846,
        "B122": 777,
        "B211": 146,
        "B212": 501,
        "B221": 528,
        "B222": 766,
        "C111": 124,
        "C112": 871,
        "C121": 958,
        "C122": 743,
        "C211": 336,
        "C212": 217,
        "C221": 742,
        "C222": 476,
        "D111": 335,
        "D112": 422,
        "D121": 745,
        "D122": 419,
        "D211": 820,
        "D212": 151,
        "D221": 136,
        "D222": 557
    }
    paths = {
        "A": {
            "a1": "B",
            "a2": "C",
            "a3": "D"
        },
        "B": {
            "b1": "B1",
            "b2": "B2",
        },
        "C": {
            "c1": "C1",
            "c2": "C2",
        },
        "D": {
            "d1": "D1",
            "d2": "D2",
        },
        "B1": {
            "b11": "B11",
            "b12": "B12",
        },
        "B2": {
            "b21": "B21",
            "b22": "B22",
        },
        "C1": {
            "c11": "C11",
            "c12": "C12",
        },
        "C2": {
            "c21": "C21",
            "c22": "C22",
        },
        "D1": {
            "d11": "D11",
            "d12": "D12",
        },
        "D2": {
            "d21": "D21",
            "d22": "D22",
        },
        "B11": {
            "b111": "B111",
            "b112": "B112",
        },
        "B12": {
            "b121": "B121",
            "b122": "B122",
        },
        "B21": {
            "b211": "B211",
            "b212": "B212",
        },
        "B22": {
            "b221": "B221",
            "b222": "B222",
        },
        "C11": {
            "c111": "C111",
            "c112": "C112",
        },
        "C12": {
            "c121": "C121",
            "c122": "C122",
        },
        "C21": {
            "c211": "C211",
            "c212": "C212",
        },
        "C22": {
            "c221": "C221",
            "c222": "C222",
        },
        "D11": {
            "d111": "D111",
            "d112": "D112",
        },
        "D12": {
            "d121": "D121",
            "d122": "D122",
        },
        "D21": {
            "d211": "D211",
            "d212": "D212",
        },
        "D22": {
            "d221": "D221",
            "d222": "D222",
        }
    }

    def current_player(self, state):
        return 'min' if state in ('B', 'C', 'D', 'B11', 'B12', 'B21', 'B22', 'C11', 'C12', 'C21', 'C22', 'D11', 'D12', 'D21', 'D22') else 'max'

    def helper_util(self, state, player):
        if player == 'max':
            return self.utilities[state]
        else:
            return -self.utilities[state]
    
    def tasks(self, state):
        return list(self.paths.get(state, {}).keys())

    def goal_state(self, state, move):
        return self.paths[state][move]

    def is_terminal(self, state):
        return state not in ('A', 'B', 'C', 'D', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'B11', 'B12', 'B21', 'B22', 'C11', 'C12', 'C21', 'C22', 'D11', 'D12', 'D21', 'D22')


def maximum_val(game, state, player):
    if game.is_terminal(state):
        return game.helper_util(state, player)
    v = -np.inf
    for a in game.tasks(state):
        v2 = minimum_val(game, game.goal_state(state, a), player)
        if v2 > v:
            v = v2
    return v

def minimum_val(game, state, player):
    if game.is_terminal(state):
        return game.helper_util(state, player)
    v = np.inf
    for a in game.tasks(state):
        v2 = maximum_val(game, game.goal_state(state, a), player)
        if v2 < v:
            v = v2
    return v

# Takes a game and state as input and provides an action as output
def minimax_search(game, state):
    player = game.current_player(state)
    move = max(game.tasks(state), key=lambda a: minimum_val(game, game.goal_state(state, a), player))
    return move

def maximum_value_abp(game, state, alpha, beta, player):
    if game.is_terminal(state):
        return game.helper_util(state, player)
    v = -np.inf
    for a in game.tasks(state):
        v = max(v, minimum_value_abp(game, game.goal_state(state, a), alpha, beta, player))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def minimum_value_abp(game, state, alpha, beta, player):
    if game.is_terminal(state):
        return game.helper_util(state, player)
    v = np.inf
    for a in game.tasks(state):
        v = min(v, maximum_value_abp(game, game.goal_state(state, a), alpha, beta, player))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def alpha_beta_pruning(game, state):
    player = game.current_player(state)
    best_val = -np.inf
    beta = np.inf
    best_action = None
    for a in game.tasks(state):
        v = minimum_value_abp(game, game.goal_state(state, a), best_val, beta, player)
        if v > best_val:
            best_val = v
            best_action = a
    return best_action

def main():
    twoplygame = TwoPlyGame()
    print("Result of 2 ply game:- ")
    print()
    print("Result from minimax search: ")
    print(minimax_search(twoplygame, 'A'))
    print()
    print("Result from alpha-beta pruning: ")
    print(alpha_beta_pruning(twoplygame, 'A'))
    print('------------------------------------')

    fourplygame1 = FourPlyGame1()
    print("Result of first 4 ply game:- ")
    print()
    print("Result from minimax search: ")
    print(minimax_search(fourplygame1, 'A'))
    print()
    print("Result from alpha-beta pruning: ")
    print(alpha_beta_pruning(fourplygame1, 'A'))
    print('------------------------------------')

    fourplygame2 = FourPlyGame2()
    print("Result of second 4 ply game:- ")
    print()
    print("Result from minimax search: ")
    print(minimax_search(fourplygame2, 'A'))
    print()
    print("Result from alpha-beta pruning: ")
    print(alpha_beta_pruning(fourplygame2, 'A'))
    print('------------------------------------')

    fourplygame3 = FourPlyGame3()
    print("Result of third 4 ply game:- ")
    print()
    print("Result from minimax search: ")
    print(minimax_search(fourplygame3, 'A'))
    print()
    print("Result from alpha-beta pruning: ")
    print(alpha_beta_pruning(fourplygame3, 'A'))
    

if __name__ == '__main__':
    main()