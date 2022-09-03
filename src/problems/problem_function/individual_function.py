import random
from general_interface.individual_interface import IndividualInterface

nb = ['0', '1']


class IndividualFunction(IndividualInterface):
    MAX_OR_MIN = True

    def __init__(self, genome_length):
        self.__genome_length = genome_length
        super(IndividualFunction, self).__init__()

    def init_value(self):
        """
        randomly initializes the genome value of self.

        :return: None
        :rtype: NoneType
        """
        return "".join([random.choice(nb) for i in range(self.__genome_length)])

    def get_genome_length(self):
        """
        gives the length of the string representing the genome of an individual, i.e self.__genome.

        :return: the length of the genome of an individual object
        :rtype: int
        """
        return self.__genome_length

    @staticmethod
    def gene_mutation(gene):
        """
        makes the gene passed as parameter mutate.

        :param gene: a str of length 1 representing a gene of the genome of an individual
        :type gene: str
        :return: a new gene, different from the gene passed as parameter, randomly chosen among the different allowed
        values for the genome of the subclass of the individual which is derivated from IndividualInterface
        :rtype: str
        """
        return random.choice([genes for genes in nb if genes != gene])
