import os
import inspect
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from general_interface.algogen import AlgoGen
from main_files.managing_command_line_args import manage_command_args
from problems.problem_secret.problem_secret import ProblemSecret

if __name__ == '__main__':
    list_args = manage_command_args()
    genome_length = 30
    problem_secret = ProblemSecret(genome_length)
    population_size = list_args[1]
    probability = list_args[2]
    SolvingProblem = AlgoGen(problem_secret, population_size, probability)
    SolvingProblem.GENERATIONS = list_args[0]
    SolvingProblem.solving_problem()
