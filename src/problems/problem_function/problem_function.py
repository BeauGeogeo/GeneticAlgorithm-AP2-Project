from math import ceil
from general_interface.problem_interface import ProblemInterface
from problems.problem_function.individual_function import IndividualFunction
import numpy as np


class ProblemFunction(ProblemInterface):
    MAX_OR_MIN = True

    def __init__(self, genome_length, xmin, xmax):
        assert genome_length > 0, "length of the genome must be superior than zero"
        self.__genome_length = genome_length
        self.__xmin = xmin
        self.__xmax = xmax

    def evaluate_fitness(self, individual):
        """
        computes the fitness of individual for this problem.

        :param individual: the individual whose fitness is being computed
        :type individual: an Individual object
        :return: the fitness score of the individual passed as parameter
        :rtype: int
        """
        Nmax = int('1' * self.__genome_length, 2)
        N = int(individual.get_value(), 2)
        x = self.__xmin + N*((self.__xmax-self.__xmin)/Nmax)
        return f(x)

    def create_individual(self):
        """
        creates a randomly generated individual for this problem.

        :return: a randomly generated individual for this problem
        :rtype: an Individual object
        """
        individu = IndividualFunction(self.__genome_length)
        return individu

    def get_genome_length(self):
        """
        gives the length of the string representing the genome of an individual, i.e self.__genome.

        :return: the length of the genome of an individual object
        :rtype: int
        """
        return self.__genome_length


def f(x):
    return x**2*np.sin(x)*np.cos(x)
