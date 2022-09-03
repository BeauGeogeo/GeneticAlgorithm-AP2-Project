class Maze(object):
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, filename):
        """
        each cell of a maze receives a number from 0 to the number of cells -1, cells by cells, line by line
        maze is represented by a dictionary whose keys are the cell numbers and values the list of possible DIRECTIONS
        from this cell start cell is number 0 (top, left) and exit cell is the last one (bottom, right)

        :param filename:  the name file containing the maze description
        :type filename; string
        """
        self.init_cells(filename)
        self.__start = 0  # index of starting cell
        self.__exit = len(self.__cells) - 1

    def init_cells(self, filename):
        """
        read a text file describing the maze from a "picture" made of | + - and spaces
        cells are stored in a dictionary, the key is the cell number (built line by line) the value is the string made
        of N,S,E,W corresponding to available directions for leaving the cell

        :param filename: the name of the file containing the maze description
        :type filename: string
        :return: the dictionary corresponding to the maze description
        :rtype: dictionary (int : list(DIRECTIONS))
        """

        CSV_SEPARATOR = ';'

        def read_content(input_stream):

            HOLE = ' '  # a HOLE means a path

            def handle_horizontal_path(chaine):
                for col in range(1, self.__width):
                    car = chaine[2 * col]
                    if car == HOLE:
                        cells[line * self.__width + col - 1] += 'E'
                        cells[line * self.__width + col] += 'W'

            def handle_vertical_path(chaine):
                for col in range(0, self.__width):
                    car = chaine[2 * col + 1]
                    if car == HOLE:
                        cells[line * self.__width + col] += 'S'
                        cells[(line + 1) * self.__width + col] += 'N'

            # read_content body
            line = input_stream.readline().rstrip().split(CSV_SEPARATOR)  # first line of file
            self.__width, self.__height = int(line[0]), int(line[1])  # define __width and __height fields
            cells = dict((i, '') for i in range(self.__width * self.__height))
            lines = input_stream.readlines()  # all other lines
            for line in range(self.__height):
                handle_horizontal_path(lines[2 * line + 1])  # odd lines => horizontal path
                handle_vertical_path(lines[2 * line + 2])  # even lines => vertical path
            return cells

        # init_cells body
        try:
            with open(filename, 'r', encoding="utf-8") as input_stream:
                self.__cells = read_content(input_stream)
        except FileNotFoundError:
            raise FileNotFoundError('fichier inconnu')

    def get_size(self):
        """
        :return: the number of cells of this maze
        :rtype: int
        """
        return self.__width * self.__height

    def get_width(self):
        return self.__width

    def try_path(self, path):
        """
        path is tried from entry point, step by step.
        Course stops either as soon as a wall is met, or it returns to an already visited cell, or reaches the exit.
        Successful steps are steps until stop.

        :param path: a sequence of DIRECTIONS corresponding to moves.
        :type path: a sequence (actually a string but could be list) of DIRECTIONS
        :return: a tuple containing number of successful steps using path and manhattan distance between reached cell
        and the exit
        :rtype: (int, int)
        """
        visited = []
        nb_steps = 0
        current_cell = self.__start
        while current_cell != self.__exit and \
                nb_steps < len(path) and \
                current_cell not in visited and \
                path[nb_steps] in self.__cells[current_cell]:
            visited.append(current_cell)
            current_cell = current_cell + self.offset(path[nb_steps])
            nb_steps = nb_steps + 1
        return nb_steps, self.manhattan_distance(current_cell, self.__exit)

    def offset(self, direction):
        """
        consider a move towards DIRECTION,
        and compute the offset to apply to the current cell number to obtain the destination cell number

        :param direction: the direction to convert
        :type direction: an element of DIRECTIONS
        :return: the offset corresponding to direction
        :rtype:int
        """
        if direction == 'E':
            return + 1
        elif direction == 'N':
            return - self.__width
        elif direction == 'W':
            return - 1
        elif direction == 'S':
            return + self.__width

    def manhattan_distance(self, first, second):
        """
        :param first: coordinate of first cell
        :type first: (int, int)
        :param second: coordinate of second cell
        :type second: (int, int)
        :return: the manhattan distance between coordinates first and second
        :rtype: int
        """
        col_first, line_first = first % self.__width, first // self.__width
        col_second, line_second = second % self.__width, second // self.__width
        return abs(col_first - col_second) + abs(line_first - line_second)


if __name__ == "__main__":
    m = Maze('maze2.txt')
    print(m.try_path("SSSSSSESNSNSWEWNWEEENWNSSS"))
    # dépasse pas ça : Score du + adapté : 91, Génome du + adapté : SSSSSSENESSNENNSNWSENWNSNW
    print("\n5000, 100")
    print(m.try_path("SSSSSSENESSNENNSNWSENWNSNW"))
    print("\n1000, 50")
    print(m.try_path("SSSSSSESWSWWNESNWWNWSNWWSN"))
    print("\n1000, 150")
    print(m.try_path("ESSESWSEENWNSSSWNWSESSWESN"))
    print("\n1000 gen et 20 pop")  # assez mauvais ici
    print(m.try_path("SSEESESEEWSEWWEWSEWWWENNEN"))
    print("\n1000 gen et 100 pop")
    print(m.try_path("EEESSENNEESSNSWNEEWNESSSSE"))
    # avec 1000 et 500, fitness score 93
    print("\nAvec 1000 et 500")
    print(m.try_path("SSEESWSEESEWNESNWWEESNNSEN"))
    # Avec population + petite et tjs 500 générations ça plafonne a 73 le score de fitness
    # idem pour 200 de pop... ah un petit 91 pour finir
    print("\n500 gen et pop entre 200 et moins")
    print(m.try_path("ESSESWSEESSNEEWWESWSNWWWEW"))
    print(m.try_path("SSSSSSENENWESSENEEWSWENNSW"))
    # Avec generation de 500, pop 100, proba 0.05
    # ok bcp de génération augmente un peu le score. Voyons en diminuant la population
    print("\nAvec generation de 500, pop 20, proba 0.05")
    print(m.try_path("SSSSSSEESENESWEWESNNESEEWN"))
    # Avec generation de 100, pop 100, proba 0.05
    # Notons que ça progresse très peu...
    print("\nAvec generation de 100, pop 20, proba 0.05")
    print(m.try_path("ESEESENSNWNWENNENWSWEWWNWW"))
    # Avec generation de 100, pop 100, proba 0.05
    print("\nAvec generation de 100, pop 20, proba 0.05")
    print(m.try_path("SSSSSSWEWNNEWEWNNEWWSSNWNN"))
    print("\nLes trois suivants avec 20 generation, pop 20, proba 0.05")
    # Les trois suivants avec 20 generation, pop 20, proba 0.05
    print(m.try_path("SSSSSSWEEENWESNWWSSNWSNNEN"))
    print(m.try_path("ESSESSWNSSNSNEWNWSSNNWWSSS"))
    print(m.try_path("SSSSSWNWSEWSWEESSWENNWNNEE"))
    print(m.try_path('EEESWWSESWSEESENEESENENNNS'))
    print(m.try_path('EEESWWSESWSEESENEES'))
    print(m.try_path('SSENEESENNEESWSSE'))
    print(m.try_path("WWNEWSNNNNNSSNNNSNWNNWWNSS"))
