# N-Queens Genetic Algorithm

This code implements a genetic algorithm to solve the N-Queens problem. The goal is to find a configuration of N queens on an N×N chessboard such that no two queens threaten each other.

## Description

The code uses a genetic algorithm to evolve populations of queen configurations. Each population consists of several individuals, where each individual represents a possible configuration of queens on the chessboard. The algorithm applies genetic operators such as selection, crossover, and mutation to create new generations of populations.

The code starts by generating four initial populations randomly. Each population is represented as a list of integers, where each integer represents the row position of a queen in the corresponding column.

The fitness of each individual in a population is evaluated based on the number of conflicts between queens. A higher fitness value indicates a better solution.

The algorithm selects the two fittest individuals from the populations as parents for the next generation. It performs crossover to create two child individuals by combining the genetic material of the parents. Then, mutation is applied to introduce random changes in the child individuals.

The process of selection, crossover, and mutation is repeated until a solution with no conflicts is found or a maximum number of iterations is reached.

## Usage

To run the code, follow these steps:

1. Make sure you have Python installed (version 3.x).

2. Run the script using the Python interpreter:

python n_queens_genetic.py


3. The code will output the populations and their corresponding fitness values. It will also display the crossover and mutation effects.

4. The algorithm will continue to evolve the populations until a solution is found or a maximum number of iterations is reached. The final population with the best fitness value will be displayed.

## Results

The code prints the chessboard representation of each population, indicating the positions of the queens. It also shows the fitness value of each population, which represents the number of non-conflicting pairs of queens.

If a solution is found (fitness value equals the board size), the code will display the final queen configuration.

Happy coding!


