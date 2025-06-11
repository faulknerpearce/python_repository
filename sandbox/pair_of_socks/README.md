# Pair of Socks Simulation

This script simulates the process of drawing socks from a drawer to find the first matching pair. It uses random shuffling and repeats the experiment multiple times to estimate the average number of attempts needed to get a pair.

## Features

- Generates a list of socks with customizable colors
- Simulates drawing socks until a pair is found
- Repeats the experiment multiple times for statistical analysis
- Calculates and prints the average number of attempts needed to get a pair

## Functions

`create_socks_list(colours)`
- Generates a list containing ten socks for each specified color.

`find_pair(socks_draw)`
- Simulates drawing socks from the list until a pair is found and returns the number of draws needed.

`generate_tires_arr(socks, amount_of_tries)`
- Runs the pair-finding simulation multiple times and records the number of attempts for each run.

`calculate_average(arr)`
- Calculates and returns the rounded average of an array of numbers.

## Usage

1. Adjust the number of sock colors in the main program if desired.
2. Run the script:
3. The script will print the average number of attempts needed to get a pair of socks.