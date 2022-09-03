import os
import inspect
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from general_interface.algogen import AlgoGen
from main_files.managing_command_line_args import manage_command_args

if __name__ == '__main__':
    list_args = manage_command_args()
    Pb_Maze = list_args[3]
    population_size = list_args[1]
    probability = list_args[2]
    SolvingProblem = AlgoGen(Pb_Maze, population_size, probability)
    SolvingProblem.GENERATIONS = list_args[0]
    SolvingProblem.solving_problem()
