from copy import deepcopy


class ProblemInterface(object):

    def best_individual(self, population):
        """
        returns the best fitted individual from population. Depending on the problem, it can correspond to the
        individual with the highest or the lowest fitness value.

        :param population: the list of individuals to sort
        :type population: list
        :return: the best fitted individual of population
        :rtype: an Individual object
        """

        temp_population = deepcopy(population)
        self.sort_population(temp_population)
        return temp_population[0]

    def create_individual(self):
        """
        creates a randomly generated individual for this problem.

        :return: a randomly generated individual for this problem
        :rtype: an Individual object
        """
        pass

    def evaluate_fitness(self, individual):
        """
        computes the fitness of individual for this problem.

        :param individual: the individual to consider
        :type individual: an Individual object
        :return: the fitness of individual for this problem
        :rtype: an Individual object
        """
        pass

    def sort_population(self, population):
        """
        sorts population from best fitted to worst fitted individuals. Depending on the problem, it can correspond to
        ascending or descending order with respect to the fitness function.

        :param population: a list of Individual objects
        :type population: list
        :return: None
        :rtype: NoneType
        """
        if self.MAX_OR_MIN:
            population.sort(key=lambda t: t.get_score(), reverse=True)
        else:
            population.sort(key=lambda t: t.get_score())

    def tournament(self, first, second):
        """
        performs a tournament between two individuals, the winner is the most fitted one, it is returned.

        :param first: an individual
        :type first: an Individual object
        :param second: an individual
        :type second: an Individual object
        :return: the winner of the tournament
        :rtype: an Individual object
        """
        if self.MAX_OR_MIN:
            if first.get_score() > second.get_score():
                return first.copy()
            else:
                return second.copy()
        else:
            if first.get_score() < second.get_score():
                return first.copy()
            else:
                return second.copy()
