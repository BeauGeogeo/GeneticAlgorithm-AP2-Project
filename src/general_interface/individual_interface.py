from random import random, randint


class IndividualInterface(object):
    """
    An Individual in genetic algorithm problem

    The value (or genome) of an individual is a sequence (e.g string or list) of a fixed size

    An individual has a fitness score
    """

    def __init__(self):
        """
        :param genome_length: the size of the genome of an individual
        :type genome_length: an integer
        :return: None
        :rtype: NoneType
        """
        self.__genome = self.init_value()
        self.__fitness = None

    def copy(self):
        """
        builds a copy of self, the genome is a copy of self’s genome.

        :return: a new Individual which is a « clone » of self
        :rtype: an Individual object
        """
        other = type(self)(self.get_genome_length())
        other.set_value(self.get_value())
        other.set_score(self.get_score())
        return other

    def cross_with(self, other):
        """
        performs a 1 point crossover between self and other, two new built individuals are returned.

        :param other: the individual to cross with
        :type other: an Individual object
        :return: the two new Individuals built by 1 point crossover operation
        :rtype: tuple of individuals
        """
        first = self.copy()
        second = other.copy()
        crossed_genomes = self.one_point_crossover(self, other)
        first.set_value(crossed_genomes[0])
        second.set_value(crossed_genomes[1])
        return first, second

    def evaluate(self, problem):
        """
        sets the fitness score with the fitness computed by problem for self.

        :param problem: the problem for which we want to evaluate the fitness of the individual
        :rtype problem: a subclass of the class ProblemInterface
        :return: None
        :rtype: NoneType
        """
        self.set_score(problem.evaluate_fitness(self))

    def get_score(self):
        """
        returns the fitness score of the individual represented by self.

        :return: the fitness score of self
        :rtype: float
        """
        return self.__fitness

    def get_genome_length(self):
        """
        gives the length of the string representing the genome of an individual, i.e self.__genome.

        :return: the length of the genome of an individual object
        :rtype: int
        """
        pass

    def get_value(self):
        """
        gives the string representing the genome of an individual object.

        :return: the genome of self
        :rtype: sequence
        """
        return self.__genome

    def mutate(self, probability):
        """
        Applies mutation operation to self : each element of the geome sequence is randomly changed with given
        probability.

        Side effect : self’s genome is modified

        :param probability: the probability of mutation for every gene
        :type probability: float
        :return: None
        :rtype: NoneType
        """
        new_genome = ''
        for gene in self.__genome:
            if self.can_mutate(probability):
                new_genome += self.gene_mutation(gene)
            else:
                new_genome += gene
        self.__genome = new_genome

    def set_score(self, new_score):
        """
        changes the fitness score of self.

        :return: None
        :rtype: NoneType
        """
        self.__fitness = new_score

    def set_value(self, new_value):
        """
        changes the genome value of self by the value of the argument new_value given into the function.

        :return: None
        :rtype: NoneType
        """
        self.__genome = new_value

    def init_value(self):
        """
        randomly initializes the genome value of self.

        :return: None
        :rtype: NoneType
        """
        pass

    @staticmethod
    def gene_mutation(gene):
        """
        makes the gene passed as parameter mutate.

        :param gene: a str of length 1 representing a gene of the genome of an individual
        :type gene: str
        :return: a new gene, different from the gene passed as parameter, randomly chosen among the different allowed
        values for the genome of the subclass of the individual which is derived from IndividualInterface
        :rtype: str
        """
        pass

    @staticmethod
    def can_mutate(probability):
        """
        allows a gene to mutate if the probability of mutation passed as parameter si higher or equal to a randomly
        generated number.

        :return: True if the randomly generated number si inferior or equal to the probability of mutation, False
        otherwise
        :rtype: bool
        """
        return random() <= probability

    @staticmethod
    def one_point_crossover(first_individual, second_individual):
        """
        takes the genomes of 2 individuals and creates 2 genomes using the methode of the one_point_crossover.

        :param first_individual: the first individual from whom we want the genome to be crossed with the second
        :type first_individual: an Individual object
        :param second_individual: the second individual from whom we want the genome to be crossed with the first
        :type second_individual: an Individual object
        :return: tuple of new genomes obtained with the methode of one point crossover
        :rtype: str
        """
        crossover_point = randint(1, len(first_individual.get_value())-2)
        first_genome = first_individual.get_value()[:crossover_point] + second_individual.get_value()[crossover_point:]
        second_genome = second_individual.get_value()[:crossover_point] + first_individual.get_value()[crossover_point:]
        return first_genome, second_genome

    def __repr__(self):
        """
        special method to print an individual object.

        :return: a string representing the genome of an individual object.
        :rtype: str
        """
        return self.__genome
