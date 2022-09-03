from random import randint, choice, random, randrange
from general_interface.individual_interface import IndividualInterface

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
# Si la chaîne est de longueur 30, il existe alors 27^30 chaînes possibles.

secret = 'ceci est un secret a retrouver'


class IndividualSecret(IndividualInterface):
    MAX_OR_MIN = False

    def __init__(self, genome_length=30):
        self.__genome_length = genome_length
        super(IndividualSecret, self).__init__()

    def init_value(self):
        """
        randomly initializes the genome value of self.

        :return: None
        :rtype: NoneType
        """
        return "".join([choice(LETTERS) for _ in range(self.__genome_length)])

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
        values for the genome of the subclass of the individual which is derived from IndividualInterface
        :rtype: str
        """
        return choice([genes for genes in LETTERS if genes != gene])
