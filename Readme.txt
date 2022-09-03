**************************************************************************************************** AP2 project (2nd year of College) ****************************************************************************************************

Authors : Geoffrey Laforest, Achraf Azalmad, Oumeima El Gharbi.
L2 Maths, group 1


						*** Resume of the project ***


This is the project we realized for the Algorithm and programmation (AP2) class during the first semestre of the 2nd year of College.
There were several subjects. I convinced my fellow comrades to chose this one called "algogen", because of my strong interest in 
evolutionary processes and in the links between biology and machine learning.

We had to code a genetic algorithm designed to solve each of the four problems given by the teachers. 

Additional information (in french) on the project can be found on the website of the University : 

https://www.fil.univ-lille1.fr/~L2S3API/CoursTP/Projets/AlgoGen/index.html


						*** How does a genetic algorithm work ***


A genetic algorithm is an algorithm based on the principles of evolutionary biology that is able to solve a wide range of problems. We generate a random 
population with each individual having a random genome. Individuals compete against each other regarding their fitness, i.e a  
measurement of how well their genome gives an answer to the problem we try to solve. The most fitted individuals reproduce and give 
birth to a new generation. At each step, when a new generation is produced, the genome of each individual can mutate, according to
a given mutation probability.

The process is iterated a certain number of times, with the hope that the algorithm converges to a good solution.


						*** Architecture of the code *** 


In the main directory you'll find this readme.text explaining the project.

The CommandLineArgumentsInWindows.txt was made to help the user launching a script through the command line in Windows.

There are also the sourcecode directory, conf.py and Makefile that are related to the production of the docstring and that the 
teachers wanted us to use.

The fast_launchers directory contains .bat files, i.e executables, to launch quickly the different scripts for the different problems.

The src directory contains the source code of the project. 

It is split in 3 main directories. 

The general_interface has the scripts for running the algogen, and the principal and most general architecture for the code related to
each individual and each problem interface.

Main_files contain all the main scripts related to each problem, the script concerning a specific problem being run when we want to 
solve this particular problem. 
The managing_command_line_args.py file was designed in order to deal with the command line arguments given when a problem is solved 
using the genetic algorithm.

Finally, the problems directory is composed of 4 subdirectories, each one related to one of the four problems.

For problem_function and problem_secret, each folder contain two files, one for dealing with the specific problem and one for the 
peculiarities of the individual interface also linked to the given problem. 
For problem_haunted and problem_maze, the folder include one more python file, for generating the haunted field and the maze 
respectively.
 

						*** User guide to pass command line arguments ***


	main_function.py : number of generations / population size / mutation probability / genome size  / xmin / xmax

	main_secret.py : number of generations / population size / mutation probability
	
	main_maze.py :  number of generations / population size / mutation probability / Number of the labyrinth (problem maze) ; if number = 1, it will generate maze1.txt

	main_haunted.py :  number of generations / population size / mutation probability / height / width / number of monsters / N (number of iterations to create different haunted fields). 

	
	Be aware that we had some problems lauching the main_maze through command line with Ubuntu, but it works fine on Windows.


Be careful that on some editors, like Pycharm, some import path references are not resolved and should be change to be run from the 
editor. A change could nevertheless cause the .bat files and command line not to work  anymore, but without any change it should work 
perfectly as it is supposed to.

Also don't hesitate to check the CommandLineArgumentsInWindows.txt to know how to launch a script by command line in Windows.

   