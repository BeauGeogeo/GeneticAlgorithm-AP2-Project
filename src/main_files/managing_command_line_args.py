import sys
import inspect
from problems.problem_haunted.haunted_field import HauntedField
from problems.problem_haunted.problem_haunted import ProblemHaunted
from problems.problem_maze.problem_maze import ProblemMaze
from problems.problem_maze.maze import Maze


def manage_command_args():
    """
    gets the arguments from the command line and initializes the parameters required for the different objects to solve
    a problem using the genetic algorithm. Raises errors and exceptions if the arguments given through command line
    don't meet the requirements they should.

    :return: list of arguments made from those given in command line.
    :rtype: list
    """
    frame_records = inspect.stack()[1]
    calling_module = inspect.getmodulename(frame_records[1])

    list_args = []

    if calling_module == "main_maze":
        if len(sys.argv) != 5:
            print('Bad number of arguments for this problem (ProblemMaze)!', file=sys.stderr)
            usage(calling_module)
        else:
            try:
                MAZE = "..\\problems\\problem_maze\\mazes\\maze" + str(sys.argv[4]) + ".txt"
                MAZE_TO_SOLVE = Maze(MAZE)
                PROBLEM_MAZE = ProblemMaze(MAZE_TO_SOLVE)
                list_args.append(PROBLEM_MAZE)
            except FileNotFoundError:
                print("Verify that the file does exist", file=sys.stderr)
                usage(calling_module)
            except ValueError:
                print("The 'maze' argument must be a string or an integer representing the number of the"
                      " maze you want the genetic algorithm to solve.", file=sys.stderr)
                usage(calling_module)

    elif calling_module == "main_function":
        if len(sys.argv) != 7:
            print('Bad number of arguments for this problem (ProblemFunction)!', file=sys.stderr)
            usage(calling_module)
        else:
            try:
                GENOME_LENGTH = int(sys.argv[4])
                list_args.append(GENOME_LENGTH)
            except ValueError:
                print("Genome length (xmin) must be an integer!", file=sys.stderr)
            try:  # we could go even further in the management of the different exceptions that could occur
                XMIN = int(sys.argv[5])
                list_args.append(XMIN)
            except ValueError:
                print("Minimum value of the interval (xmin) must be an integer!", file=sys.stderr)
            try:
                XMAX = int(sys.argv[6])
                list_args.append(XMAX)
            except ValueError:
                print("Maximum value of the interval (xmax) must be an integer!", file=sys.stderr)

    elif calling_module == "main_haunted":
        if len(sys.argv) != 8:
            print('Bad number of arguments for this problem (ProblemHaunted)!', file=sys.stderr)
            usage(calling_module)
        else:
            try:
                HEIGHT = int(sys.argv[4])
            except ValueError:
                print('Height of the haunted field must be an integer!', file=sys.stderr)
                usage(calling_module)
            try:
                WIDTH = int(sys.argv[5])
            except ValueError:
                print('Width of the haunted field must be an integer!', file=sys.stderr)
                usage(calling_module)
            try:
                MONSTERS = int(sys.argv[6])
                list_args.append(MONSTERS)
            except ValueError:
                print('Number of monsters must be an integer!', file=sys.stderr)
            try:
                N = int(sys.argv[7])
                list_args.append(N)
            except ValueError:
                print("N must be an integer")
            HAUNTED_FIELD = HauntedField(HEIGHT, WIDTH)
            list_args.append(HAUNTED_FIELD)

    elif len(sys.argv) != 4:
        print('Bad number of arguments!', file=sys.stderr)
        usage(calling_module)

    try:
        GENERATIONS = int(sys.argv[1])
    except ValueError:
        print('Number of generations must be an integer!', file=sys.stderr)
        usage(calling_module)

    try:
        POPULATION_SIZE = int(sys.argv[2])
    except ValueError:
        print('Population size must be an integer!', file=sys.stderr)
        usage(calling_module)
    try:
        PROBABILITY = float(sys.argv[3])
    except ValueError:
        print('Probability of mutation must be a float', file=sys.stderr)
        usage(calling_module)

    return [GENERATIONS, POPULATION_SIZE, PROBABILITY] + list_args


def usage1():
    """
    prints usage conditions related to main_function.py file, i.e the first problem.

    :return: None
    :rtype: NoneType
    """
    print('Usage: {:s} <generation> <population size> <mutation probability> <genome length> <xmin = lower bound '
          'of the interval> <xmax = upper bound of the interval>'.format(sys.argv[0]),
          file=sys.stderr)
    print('with\n\t<generation> = number of generations you want to generate', file=sys.stderr)
    print('\t<population size> = size of the population on which genetic algorithm is applied', file=sys.stderr)
    print('\t<mutation probability> = probability for a gene of the genome of an individual to randomly mutate',
          file=sys.stderr)
    print('\t<genome length> = length of the genome of an individual',
          file=sys.stderr)
    print('\t<xmin> = lower bound of the interval on which you want to test the genetic algorithm for this problem',
          file=sys.stderr)
    print('\t<xmax> = upper bound of the interval on which you want to test the genetic algorithm for this problem',
          file=sys.stderr)


def usage2():
    """
    prints usage conditions related to main_secret.py file, i.e the SecretCode problem.

    :return: None
    :rtype: NoneType
    """
    print('Usage: {:s} <generation> <population size> <mutation probability>'.format(sys.argv[0]),
          file=sys.stderr)
    print('with\n\t<generation> = number of generations you want to generate', file=sys.stderr)
    print('\t<population size> = size of the population on which genetic algorithm is applied', file=sys.stderr)
    print('\t<mutation probability> = probability for a gene of the genome of an individual to randomly mutate',
          file=sys.stderr)


def usage3():
    """
    prints usage conditions related to main_maze.py file, i.e the ProblemMaze problem.

    :return: None
    :rtype: NoneType
    """
    print('Usage: {:s} <generation> <population size> <mutation probability> <maze to solve>'.format(sys.argv[0]),
          file=sys.stderr)
    print('with\n\t<generation> = number of generations you want to generate', file=sys.stderr)
    print('\t<population size> = size of the population on which genetic algorithm is applied', file=sys.stderr)
    print('\t<mutation probability> = probability for a gene of the genome of an individual to randomly mutate',
          file=sys.stderr)
    print('\t<maze to solve> = the maze on which you want to test the algorithm',
          file=sys.stderr)


def usage4():
    """
    prints usage conditions related to main_haunted.py file, i.e the ProblemHaunted problem.

    :return: None
    :rtype: NoneType
    """
    print('Usage: {:s} <generation> <population size> <mutation probability> <height> <width> <number of monsters> <N>'
          .format(sys.argv[0]),
          file=sys.stderr)
    print('with\n\t<generation> = number of generations you want to generate', file=sys.stderr)
    print('\t<population size> = size of the population on which genetic algorithm is applied', file=sys.stderr)
    print('\t<mutation probability> = probability for a gene of the genome of an individual to randomly mutate',
          file=sys.stderr)
    print('\t<height> = the height of the haunted field on which you want to test the algorithm',
          file=sys.stderr)
    print('\t<width> = the width of the haunted field on which you want to test the algorithm',
          file=sys.stderr)
    print('\t<number of monsters> = the number of monsters per line of the haunted field on which you want to test the '
          'algorithm', file=sys.stderr)
    print('\t<N> = the number of multiple randomly generated haunted fields on which you want to test the algorithm',
          file=sys.stderr)


def usage(module_name):
    """
    prints usage conditions related to the particular problem to be solved by the genetic algorithm, in case the
    arguments given in command line don't meet the requirement they should or are insufficient in number.

    :return: None
    :rtype: NoneType
    """
    if module_name == "main_function":
        usage1()
    elif module_name == "main_secret":
        usage2()
    elif module_name == "main_maze":
        usage3()
    elif module_name == "main_haunted":
        usage4()
    exit(1)
