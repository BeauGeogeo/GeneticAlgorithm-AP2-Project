from random import choice
from problems.problem_haunted.haunted_field import HauntedField, EMPTY, MONSTER, OBSTACLE, USED
from general_interface.individual_interface import IndividualInterface


HAUNTED_FIELD_ALPHABET = [EMPTY, MONSTER, OBSTACLE, USED]
HAUNTED_DICT = {EMPTY: 0, MONSTER: 1, OBSTACLE: 2}
DIRECTIONS = ["U", "D", "L", "R"]


class IndividualHaunted(IndividualInterface):
    MAX_OR_MIN = True

    def __init__(self, genome_length=243):
        self.__genome_length = genome_length
        self.__line = 1
        self.__column = 0
        self.__used = 1
        self.__state = ''
        self.__nb_step = 0
        self.__res = []
        super(IndividualHaunted, self).__init__()

    def init_value(self):
        """
        randomly initializes the genome value of self.

        :return: a string composed of letters representing different directions and which is the genome of an
        individual.
        :rtype: str
        """
        return "".join([choice(DIRECTIONS) for i in range(self.__genome_length)])

    def init_column(self, haunted_field):
        """
        initializes the value of the attribute column of self to the width of the haunted field divided by 2. This is
        the column where an individual starts its crossing of the haunted field.

        :param haunted_field: the haunted field to be crossed by the individual
        :type haunted_field: a HauntedField object
        :return: None
        :rtype: NoneType

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_column()
        0
        >>> haunted_field = HauntedField(6,6)
        >>> individu.init_column(haunted_field)
        >>> individu.get_column()
        3
        """
        self.__column = haunted_field.get_width() // 2

    def get_genome_length(self):
        """
        gives the length of the string representing the genome of an individual, i.e self.__genome.

        :return: the length of the genome of an individual object
        :rtype: int
        """
        return self.__genome_length

    def get_line(self):
        """
        returns the line of the cell reached by the individual represented by the parameter self

        :return: the line number of the cell on which the individual currently is
        :rtype: int

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_line()
        1
        """
        return self.__line

    def get_column(self):
        """
        returns the column of the cell reached by the individual represented by the parameter self.

        :return: the column number of the cell on which the individual currently is
        :rtype: int

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_column()
        0
        """
        return self.__column

    def get_state(self):
        """
        returns the current state of the individual represented by the parameter self.

        :return: the current state of the individual
        :rtype: str

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_state()
        """
        return self.__state

    def get_used(self):
        """
        returns the number of boxes of the haunted field already visited by the individual represented by the self
        parameter.

        :return: number fo boxes visited by a given individual for a given haunted field
        :rtype: int

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_used()
        1
        """
        return self.__used

    def get_nb_step(self):
        """
        returns the nb of steps done by the individual.

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_nb_step()
        0
        """
        return self.__nb_step

    def get_res(self):
        """
        returns the results of an individual, i.e the different states it got when it crossed the haunted fields.

        :return: a list of the different final states an individual had after each crossing of an haunted field
        :rtype: list

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_res()
        []
        """
        return self.__res

    def set_state(self, new_state):
        """
        set the state of the individual represented by the parameter self to the value corresponding to the string
        passed as parameter.

        :return: None
        :rtype: NoneType

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_state()
        ''
        >>> individu.set_state("success")
        >>> individu.get_state()
        success
        """
        self.__state = new_state

    def update_nb_step(self):
        """
        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_nb_step()
        0
        >>> individu.update_nb_step()
        >>> individu.get_nb_step()
        1
        """
        self.__nb_step += 1

    def make_vision_pattern(self, original_haunted_field):
        """
        establishes the vision pattern of the individual, i.e the 5 visible boxes alongside and in front of him.

        :param original_haunted_field: a HauntedField object
        :type original_haunted_field: HauntedField
        :return: a vision pattern
        :rtype: str
        """
        visible_boxes = [original_haunted_field.get_cell(self.__line + i, self.__column + j) for i in range(2) for j in
                         range(-1, 2) if (i, j) != (0, 0)]
        vision_pattern = "".join(visible_boxes)
        return vision_pattern

    def get_move(self, original_haunted_field):
        """
        returns the move for an individual to do inside a haunted field, according to the score linked to the vision of
        this individual inside the haunted field. The move returned corresponds to the letter of the genome of the
        individual at the index corresponding to the number representing the vision pattern of the individual.

        :param original_haunted_field: the haunted_field to be crossed by the individual represented by self
        :type original_haunted_field: a HauntedField object
        :return: a letter of the genome of the individual
        :rtype: str
        """
        vision_pattern = self.make_vision_pattern(original_haunted_field)
        vision_pattern_score = IndividualHaunted.compute_vision(vision_pattern)
        return self.get_value()[vision_pattern_score]  # ok ici on doit utiliser get_value car le self.__genome est
        # attribut de IndividualInterface et on peut donc pas y accéder directement ici

    def add_res(self):
        """
        adds the result of the crossing of an haunted field by an individual.

        :return: None
        :rtype: NoneType

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_res()
        []
        >>> individu.set_state("success")
        >>> individu.add_res()
        >>> individu.get_res()
        ["success"]
        """
        self.__res += [self.__state]

    def reinit_res(self):
        """
        reinitializes the list of results of an individual

        :return: None
        :rtype: NoneType

        Examples:

        >>> individu = IndividualHaunted()
        >>> individu.get_res()
        []
        >>> individu.set_state("success")
        >>> individu.add_res()
        >>> individu.get_res()
        ["success"]
        """
        self.__res = []

    def make_move(self, original_haunted_field):
        """
        operates a move for an individual inside a haunted field.

        :param original_haunted_field: the haunted_field to be crossed by the individual represented by self
        :type original_haunted_field: a HauntedField object
        :return: None
        :rtype: NoneType
        """
        move = self.get_move(original_haunted_field)
        if move == "U":
            self.__line -= 1
        elif move == "D":
            self.__line += 1
        elif move == "L":
            self.__column -= 1
        elif move == "R":
            self.__column += 1

    def modify_state(self, original_haunted_field):
        """
        checks the content of the cell on which the individual actually is during its crossing of the haunted field,
        and modifies

        :param original_haunted_field: the haunted_field to be crossed by the individual represented by self
        :type original_haunted_field: a HauntedField object
        :return: None
        :rtype: NoneType
        """
        if original_haunted_field.is_monster(self.__line, self.__column):
            self.__state = "monster"
        elif original_haunted_field.is_obstacle(self.__line, self.__column):
            self.__state = "stuck"
        elif self.__nb_step >= original_haunted_field.get_width() * original_haunted_field.get_height() // 2:
            self.__state = "alive"
        elif self.__line == original_haunted_field.get_height():
            self.__state = "success"

    def update_used(self, haunted_field):
        """
        updates the number of boxes visited by an individual crossing the haunted field.

        :return: None
        :rtype: NoneType
        """
        if haunted_field.is_empty(self.__line, self.__column):
            self.__used += 1

    def next_step(self, haunted_field, original_haunted_field):
        """
        manages the crossing of an individual in the haunted field by dealing with the next step to accomplish inside
        it, i.e. calling the function to operate the next move and update the attributes of the individual
        consecutively.

        :param haunted_field: the haunted_field to be crossed by the individual represented by self
        :type haunted_field: a HauntedField object
        :param original_haunted_field: same haunted_field, only used to make the crossing while the over is used to
        establish used boxes without affecting the make_vision_pattern function
        :return: None
        :rtype: NoneType
        """
        self.make_move(original_haunted_field)
        self.modify_state(original_haunted_field)
        self.update_used(haunted_field)
        self.update_nb_step()
        haunted_field.set_cell(self.__line, self.__column, USED)

    def reinitialize_attributes(self):  # à voir si pas plus malin à faire avec le haunted field backup restore...
        """
        reinitializes the attributes of self. It is intended to be able to compute the fitness of the individuals of the
        next generations created by the genetic algorithm, otherwise the newly created individuals may have
        inherited of the attributes of the ones from which they descend or the individuals selected by tournament and
        coming from previous generations could have kept their attributes values incremented while being tested again on
        the haunted field.

        :return: None
        :rtype: NoneType
        """
        self.__column = 0
        self.__line = 1
        self.__used = 0
        self.__nb_step = 0
        self.__state = ''

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
        return choice([genes for genes in DIRECTIONS if genes != gene])

    @staticmethod
    def compute_vision(vision_pattern):
        """
        computes the number corresponding to a pattern_vision

        :param vision_pattern: a string representing the vision that an individual has of the 5 boxes alongside and in
        front of him
        :type vision_pattern: str
        :return: a number computed on the basis of the string given as parameter
        :rtype: int

        Examples:

        >>> vision_pattern = '_____'
        >>> compute_vision(vision_pattern)
        0
        >>> vision_pattern = '_M_**'
        >>> compute_vision(vision_pattern)
        219
        """
        assert len(vision_pattern) == 5, "pattern_vision must have a length of 5"
        return sum([HAUNTED_DICT[vision_pattern[i]] * 3 ** i for i in range(len(vision_pattern))])

