import numpy as np
from HillClimbing import HillClimbing
import warnings
import sys

NUM_STATES = 1000
ALGOS = ['Steepest-Ascent Hill Climbing', 'Steepest-Ascent Hill Climbing (with 100 sidesteps)']

def generate_random_state():
    return np.random.randint(8, size=8)

def print_analysis_results(success_moves, failed_moves):
    print("\nAnalysis Results:")
    for algo_name in ALGOS:
        print(algo_name)
        print('-' * 15)
        success_rate = len(success_moves[algo_name]) / NUM_STATES * 100
        avg_success_moves = np.mean(success_moves[algo_name])
        avg_failed_moves = np.mean(failed_moves[algo_name])
        result_string = "Solved {} of {} instances (Success rate - {:.2f}%).\nAverage # of moves when it succeeds: {:.0f}\nAverage # of moves when it fails: {:.0f}\n".format(
            len(success_moves[algo_name]), NUM_STATES, success_rate, avg_success_moves, avg_failed_moves)
        print(result_string)

def update_progress_bar(progress, total):
    percent = progress / total * 100
    sys.stdout.write('\r[{}] {:.2f}% {}/{} cases'.format('*' * int(percent / 5) + '-' * (20 - int(percent / 5)), percent, progress, total))

if __name__ == "__main__":
    np.random.seed(42)

    success_moves = {algo: [] for algo in ALGOS}
    failed_moves = {algo: [] for algo in ALGOS}

    # Generate random states
    states = [generate_random_state() for i in range(NUM_STATES)]

    print("Running analysis...")
    for i, state in enumerate(states):
        # Solve with Hill Climbing
        hill_climbing = HillClimbing(state)
        # Steepest Ascent
        end_state, end_cost, is_plateau, moves = hill_climbing.steepest_ascent()
        if end_cost == 0:
            success_moves[ALGOS[0]].append(moves)
        else:
            failed_moves[ALGOS[0]].append(moves)
        # Steepest Ascent with 100 sidesteps
        end_state, end_cost, is_plateau, moves = hill_climbing.steepest_ascent(100)
        if end_cost == 0:
            success_moves[ALGOS[1]].append(moves)
        else:
            failed_moves[ALGOS[1]].append(moves)

        update_progress_bar(i + 1, NUM_STATES)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        print_analysis_results(success_moves, failed_moves)
