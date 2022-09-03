from general_interface.problem_interface import ProblemInterface
from problems.problem_secret.individual_secret import IndividualSecret, LETTERS, secret


class ProblemSecret(ProblemInterface):
    MAX_OR_MIN = False

    def __init__(self, genome_length):
        assert genome_length > 0, "length of the genome must be superior than zero"
        self.__genome_length = genome_length

    def evaluate_fitness(self, individual):
        """
        computes the fitness of individual for this problem
        Measures the distance between the secret string and the string representing the genome of the individual

        :param individual: the individual to consider
        :type individual: an Individual object
        :return: the fitness of individual for this problem
        :rtype: int
        """
        s1, s2 = secret, individual.get_value()
        assert self.__genome_length == len(s1), "lengths of the genome and of the secret message must be equal."

        distance = 0
        for i in range(self.__genome_length):
            distance += abs(LETTERS.index(s1[i]) - LETTERS.index(s2[i]))
        return distance

    def create_individual(self):
        """
        creates a randomly generated individual for this problem.

        :return: a randomly generated individual for this problem
        :rtype: an Individual object
        """
        individu = IndividualSecret(self.__genome_length)
        return individu

    def get_genome_length(self):
        """
        gives the length of the string representing the genome of an individual, i.e self.__genome.

        :return: the length of the genome of an individual object
        :rtype: int
        """
        return self.__genome_length

