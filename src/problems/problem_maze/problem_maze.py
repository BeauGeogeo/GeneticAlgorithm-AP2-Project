from math import ceil
from general_interface.problem_interface import ProblemInterface
from problems.problem_maze.individual_maze import IndividualMaze


class ProblemMaze(ProblemInterface):
    MAX_OR_MIN = True

    def __init__(self, maze_to_solve):
        self.__maze_to_solve = maze_to_solve
        self.__genome_length = self.__maze_to_solve.get_size()

    def evaluate_fitness(self, individual):
        """
        computes the fitness of individual for this problem.

        :param individual: the individual whose fitness is being computed
        :type individual: an Individual object
        :return: the fitness score of the individual passed as parameter
        :rtype: int
        """
        steps_nb, distance = self.__maze_to_solve.try_path(individual.get_value())
        x = ceil(self.__maze_to_solve.get_width() / 2) - distance
        fitness_score = max(0, x) ** 2 + steps_nb
        if distance == 0:
            fitness_score += 1000
        return fitness_score

    def create_individual(self):
        """
        creates a randomly generated individual for this problem.

        :return: a randomly generated individual for this problem
        :rtype: an Individual object
        """
        individu = IndividualMaze(self.__genome_length)
        return individu

    def get_maze(self):
        """
        gives the maze of the problem that the genetic algorithm is trying to solve.

        :return: the particular maze of a Maze object, attached to the ProblemMaze object that the genetic algorithm is
        trying to solve.
        :rtype: Maze
        """
        return self.__maze_to_solve

    def get_genome_length(self):
        """
        gives the length of the string representing the genome of an individual, i.e self.__genome.

        :return: the length of the genome of an individual object
        :rtype: int
        """
        return self.__genome_length
