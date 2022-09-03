from math import ceil
from copy import deepcopy
from general_interface.problem_interface import ProblemInterface
from problems.problem_haunted.individual_haunted import IndividualHaunted, USED


STATES = ["success", "monster", "stuck", "alive"]


class ProblemHaunted(ProblemInterface):
    MAX_OR_MIN = True

    def __init__(self, haunted_field, list_haunted_fields):
        self.__list_haunted_fields = list_haunted_fields
        self.__original_haunted_field = deepcopy(haunted_field)
        self.__haunted_field = haunted_field
        self.__genome_length = 243
        self.__height = haunted_field.get_height()
        self.__width = haunted_field.get_width()

    def evaluate_fitness(self, individual):
        """
        computes the fitness of individual for this problem.

        :param individual: the individual whose fitness is being computed
        :type individual: an Individual object
        :return: the fitness score of the individual passed as parameter
        :rtype: int
        """
        fitness_score = 0
        individual.reinit_res()
        for haunted_field in self.__list_haunted_fields:
            self.__haunted_field = deepcopy(haunted_field)
            self.__original_haunted_field = deepcopy(haunted_field)
            fitness_score += self.haunted_fitness(individual)
        return fitness_score

    def haunted_fitness(self, individual):
        """
        computes the fitness of individual for this problem, for one given haunted field.

        :param individual: the individual whose fitness is being computed
        :type individual: an Individual object
        :return: the fitness score of the individual passed as parameter
        :rtype: int
        """
        height = self.__height
        width = self.__width
        self.crossing_haunted_field(individual)
        fitness_score = individual.get_used() + individual.get_line() * self.__height
        if individual.get_state() == "success":
            fitness_score = fitness_score + (height * width - individual.get_used()) * 10
        elif individual.get_state() == "stuck":
            fitness_score = fitness_score + (height - individual.get_line()) * 2
        elif individual.get_state() == "monster":
            fitness_score = fitness_score + (height - individual.get_line()) * 20
        individual.reinitialize_attributes()
        individual.init_column(self.__original_haunted_field)
        return fitness_score

    def create_individual(self):
        """
        creates a randomly generated individual for this problem.

        :return: a randomly generated individual for this problem
        :rtype: an Individual object
        """
        individu = IndividualHaunted()
        individu.init_column(self.__haunted_field)
        return individu

    def get_haunted_field(self):
        """
        gives the haunted field of the problem that the genetic algorithm is trying to solve.

        :return: a haunted field object
        :rtype: HauntedField
        """
        return self.__haunted_field

    def get_genome_length(self):
        """
        gives the length of the string representing the genome of an individual, i.e self.__genome.

        :return: the length of the genome of an individual object
        :rtype: int
        """
        return self.__genome_length

    def crossing_haunted_field(self, individual):
        """
        manages the crossing of a haunted field by an individual, mainly in order to compute its fitness with the
        evaluate_fitness function.

        :param individual: the individual that will cross the haunted field
        :type individual: an Individual object
        :return: None
        :rtype: NoneType
        """
        individual.init_column(self.__haunted_field)  # obligé de faire cela sinon la colone était initialisée à 0 et
        # on a pas trouvé pourquoi.
        self.__haunted_field.set_cell(individual.get_line(), individual.get_column(), USED)  # pour marquer la case de
        # départ
        while not individual.get_state() in STATES:
            individual.next_step(self.__haunted_field, self.__original_haunted_field)
        individual.add_res()
        self.__haunted_field = deepcopy(self.__original_haunted_field)



