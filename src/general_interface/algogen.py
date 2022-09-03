from general_interface.individual_interface import IndividualInterface
from random import shuffle
import numpy as np


class AlgoGen(object):

    GENERATIONS = 0
    """
    A prototype class for « problems » in genetic algorithm

    An Individual class must be associated to a problem to represent the individuals
    """

    def __init__(self, problem, population_size, mutation_probability):
        """
        builds a genetic algorithm to solve problem using a population of size population_size and a probability of
        mutation of mutation_probability.

        :UC: population_size must be even and mutation_probability must be 0<= and <1
        :param problem: the problem we want to be solved
        :type problem: subclass of the class ProblemInterface
        :param population_size: the size of the population of the problem considered
        :type population_size: integer
        :param mutation_probability: the probability for the genom of the individuals to mutate
        :type mutation_probability: float
        :return: None
        :rtype: NoneType
        """
        assert population_size % 2 == 0, "population_size must be an even number."
        assert 0 <= mutation_probability < 1, "mutation probability must be between 0 and 1."
        assert population_size > 5, "population size must be more than 5."
        self.__population = [problem.create_individual() for _ in range(population_size)]
        self.__population_size = population_size
        self.__problem = problem
        self.__mutation_probability = mutation_probability

    def solving_problem(self):
        """
        solves the problem corresponding to self.__problem.

        :return: None
        :rtype: NoneType
        """

        self.please_wait()
        self.evaluate_population_fitness(self.__population)
        self.intermediate_step(0)

        for i in range(self.GENERATIONS):
            next_gen = self.generate_next_gen()
            self.mutate_population(next_gen)
            self.evaluate_population_fitness(next_gen)
            self.__problem.sort_population(next_gen)
            self.__problem.sort_population(self.__population)
            best = self.__population[:5]
            new_population = best + next_gen[:-5]
            shuffle(new_population)
            self.change_population(new_population)
            if i + 1 != self.GENERATIONS:
                self.intermediate_step(i + 1)
            else:
                fittest_individual = self.__problem.best_individual(self.__population)
                print("FINAL STEP - STEP n° {}".format(i + 1))
                print("The fittest individual has the following properties :\n\nGENOME : {}\n\nFITNESS SCORE : {}"
                      .format(fittest_individual.get_value(), fittest_individual.get_score()))

    def mutate_population(self, population):
        """
        makes the population of self mutate, i.e the mutation function is applied to each individual of the population
        passed as parameter.

        :param population: list of individual objects
        :type population: list
        :return: None
        :rtype: NoneType
        """
        for individual in population:
            individual.mutate(self.__mutation_probability)

    def evaluate_population_fitness(self, population_to_evaluate):
        """
        evaluates and set the fitness score for each individual of the population passed as parameter.

        :param population_to_evaluate: list of individuals
        :type population_to_evaluate: list
        :return:
        """
        for individual in population_to_evaluate:
            individual.set_score(self.__problem.evaluate_fitness(individual))

    def create_next_gen1(self):
        """
        creates a next generation of size self.__population_size/2, obtained by tournament.

        :return: a list of length self.__population_size/2 of new individuals obtained by tournament
        :rtype: list
        """
        next_gen1 = []
        for i in range(0, self.__population_size, 2):
            winner = self.__problem.tournament(self.__population[i], self.__population[i+1])
            next_gen1.append(winner)
        return next_gen1

    def create_next_gen2(self):  # marche correctement les individus ont tout
        """
        creates a next generation of size self.__population_size/2, obtanied by crossover.

        :return: a list of length self.__population_size/2 of new individuals obtained by crossover
        :rtype: list
        """
        next_gen2 = []
        for i in range(0, self.__population_size, 2):
            new_individuals = IndividualInterface.cross_with(self.__population[i], self.__population[i+1])
            new_individual = self.__problem.tournament(*new_individuals)
            next_gen2.append(new_individual)
        return next_gen2

    def please_wait(self):
        """
        This procedure prints a message asking kindly to be patient during the solving process of the problem.

        :return: None
        :rtype: NoneType
        """
        if self.GENERATIONS + self.__population_size >= 200:
            print("\nPlease wait while the problem is being processed...\n")

    def generate_next_gen(self):
        """
        creates a next generation of individuals by combining the lists coming from the two function create_next_gen1
        and create_next_gen2.

        :return: a list of Individual objects
        :rtype: list
        """
        return self.create_next_gen1() + self.create_next_gen2()

    def get_mutation_probability(self):
        """
        gives the probability of mutation which will be applied to individuals when we make them mutate.

        :return: the value of the mutation probability
        :rtype: float
        """
        return self.__mutation_probability

    def get_population_size(self):
        """
        gives the size of the population of the problem which is being solved.

        :return: a number representing the size of the population
        :rtype: int
        """
        return self.__population_size

    def get_problem(self):
        """
        gives the problem that the genetic algorithm is trying to solve.

        :return: a Problem object
        :rtype: a problem of one of the subclass derived from the class ProblemInterface
        """
        return self.__problem

    def get_population(self):
        """
        gives the list of individuals representing the population of the problem that the genetic algorithm is
        trying to solve.

        :return: a list of Individual objects
        :rtype: list
        """
        return self.__population

    def change_population(self, new_population):
        """
        changes the value of the attribute population of self by the value of the parameter new_population.

        :param new_population: a list of newly generated individuals, aimed to replace the current population attribute
        of self.
        :type new_population: list
        :return: None
        :rtype: NoneType
        """
        self.__population = new_population

    def average_fitness(self):
        """
        computes the average fitness, i.e. the mean fitness value, for the population fo self.

        :return: the average fitness score of the individual of the population for which the genetic algorithm is
        trying to solve the current problem.
        :rtype: float
        """
        return np.mean([individual.get_score() for individual in self.__population])

    def intermediate_step(self, iter_nb):
        """
        prints for the initial step and then for each intermediate step before the end of the run of the genetic
        algorithm, the score and the value of the genome of the fittest individual of the population of self.

        :param iter_nb: a number representing the step reached by the genetic algorithm while processing the problem
        :type iter_nb: int
        :return: None
        :rtype: NoneType
        """
        best_individual = self.__problem.best_individual(self.__population)
        best_score = best_individual.get_score()
        best_genome = best_individual.get_value()
        average_fitness = self.average_fitness()
        if iter_nb == 0:
            step = "INTERMEDIATE STEP - "
        else:
            step = "INTERMEDIATE "
        print(step + "STEP n° {}.\n\nThe fittest individual has a score of {}.\nIts genome is {}.\nAverage "
              "fitness of the current population is {}\n".format(iter_nb, best_score, best_genome, average_fitness))

    def get_info(self):
        """
        a function mainly used to debug the program and print the most relevant information to do so.

        :return: None
        :rtype: NoneType
        """
        for i in range(self.__population_size):
            info = "Individu {}. Genome {}. Score {}".format(i, self.__population[i].get_value(),
                                                             self.__population[i].get_score())
            print(info)


