import os
import inspect
import sys
from random import randint
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from general_interface.algogen import AlgoGen
from main_files.managing_command_line_args import manage_command_args
from problems.problem_haunted.problem_haunted import ProblemHaunted
from problems.problem_haunted.haunted_field import HauntedField


def count_success(list_res):
    """
    counts number of times an individual has successfully crossed a haunted field

    :param list_res: list containing the results/the states of an individual after each crossing of a haunted field.
    :type list_res: list
    :return: the number of times an individual has successfully crossed a haunted field
    :rtype: int

    Examples:

    >>> list_res = ['monster', 'monster', 'monster', 'monster', 'monster', 'success', 'alive', 'alive', 'monster',
    'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster',
    'monster']
    >>> count_success(list_res)
    1
    """
    return list_res.count("success")


def count_without_exploding(list_res):
    """
    counts number of times an individual has crossed a haunted field without exploding.

    :param list_res: list containing the results/the states of an individual after each crossing of a haunted field.
    :type list_res: list
    :return: the number of times an individual has crossed a haunted field without exploding
    :rtype: int

    Examples:

    >>> list_res = ['monster', 'monster', 'monster', 'monster', 'monster', 'success', 'alive', 'alive', 'monster',
    'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster',
    'monster']
    >>> count_without_exploding(list_res)
    3
    """
    return count_success(list_res) + list_res.count("alive")


def success_rate(list_res, N):
    """
    returns the success rate of an individual based on the number of times it successfully crossed a haunted field for
    N crossing of this field.

    :param list_res: list containing the results/the states of an individual after each crossing of a haunted field.
    :type list_res: list
    :param N: number of crossings completed by the individual for which we compute the success rate
    :type N: int
    :return: the success rate of an individual
    :rtype: float

    Examples:

    >>> list_res = ['monster', 'monster', 'monster', 'monster', 'monster', 'success', 'alive', 'alive', 'monster',
    'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster',
    'monster']
    >>> N = 20
    >>> success_rate(list_res, N)
    5.0
    """
    return count_success(list_res) * 100 / N


def generate_random_haunted_field():
    """
    generates a random haunted field.

    :return: a randomly generated haunted field
    :rtype: a HauntedField object
    """
    haunted_field = HauntedField(randint(4, 9), randint(4, 9))
    haunted_field.init_monsters(randint(2, haunted_field.get_width() - 1))
    haunted_field.backup_field()
    return haunted_field


if __name__ == '__main__':
    list_args = manage_command_args()
    N = list_args[4]
    haunted_field = list_args[5]
    haunted_field.backup_field()
    monsters = list_args[3]
    haunted_field.init_monsters(monsters)
    list_haunted_fields = [haunted_field] + [generate_random_haunted_field() for i in range(N-1)]
    Pb_Haunted = ProblemHaunted(haunted_field, list_haunted_fields)
    population_size = list_args[1]
    probability = list_args[2]
    SolvingProblem = AlgoGen(Pb_Haunted, population_size, probability)
    SolvingProblem.GENERATIONS = list_args[0]
    SolvingProblem.solving_problem()

    population = SolvingProblem.get_population()
    best_individual = Pb_Haunted.best_individual(population)
    list_res = best_individual.get_res()

    print("\nBest individual has crossed {} different haunted fields. Best individual has crossed haunted fields {}"
          "\ntimes without exploding. Moreover, it has successfully crossed the field {} times. Its success rate is "
          "\n{:.2f}%."
          .format(N, count_without_exploding(list_res), count_success(list_res), success_rate(list_res, N)))

    best_individual.reinit_res()

    for i in range(N):

        best_individual.reinitialize_attributes()

        haunted_field.restore_field()
        haunted_field.backup_field()
        haunted_field.init_monsters(monsters)
        best_individual.init_column(haunted_field)

        Pb_Haunted = ProblemHaunted(haunted_field, list_haunted_fields)
        Pb_Haunted.haunted_fitness(best_individual)

    list_res = best_individual.get_res()

    print("\nBest individual has crossed {} times haunted fields. Best individual has crossed haunted fields {} times "
          "\nwithout exploding. Moreover, it has successfully crossed the field {} times. Its success rate is "
          "\n{:.2f}%."
          .format(N, count_without_exploding(list_res), count_success(list_res), success_rate(list_res, N)))
    best_individual.reinit_res()

    # the following snippet of code is to use for the original test in the project, i.e when you test the individual on
    # the same haunted field N times with same configuration (same height and width) and you want to print the relevant
    # informations.

    # print("\nBest individual on {} crossing of the same haunted field (same height, width and number of monsters but "
    #       "\nrandom positions for the last ones) has successfully crossed the field {} times.\nIts success rate is "
    #       "\n{:.2f}%"
    #       .format(N, count_success(list_res), success_rate(list_res, N)))




