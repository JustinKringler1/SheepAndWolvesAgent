"""
File Name: TestEfficiency.py
Aurthor: Justin Kringler
Last Updated: 1/24/2025

Description: Contains functions and plots for testing the efficiency of the solve function
             from the SemanticNetsAgent.py script.

Problem: You are a shepherd tasked with getting sheep and wolves across a river for some reason. 
         If the wolves ever outnumber the sheep on either side of the river, the wolves will overpower
         and eat the sheep. You have a boat, which can only take one or two animals in it at a time,
         and must have at least one animal in it because you’ll get lonely (and because the problem
         is trivial otherwise). How do you move all the animals from one side of the river to the other?

Notes: Generates and saves four plots comparing three sets of tests. 
       First set calculates the time when there is one less wolf than sheep.
       Second set calculates the time when there is 50% the amount of wolves than sheep.
       Third set calculates the time when there is 75% the amount of wolves than sheep.

       Each plot will plot the results for their respective set, the last plot is all three of the
       sets overlayed on top of each other.


"""

##### Loading Modules -----

import os
import time
from SemanticNetsAgent import SemanticNetsAgent
import matplotlib.pyplot as plt

##### Efficiency Function -----

# Define a function to test the efficiency of the solve function
def test_efficiency(test_cases):
    agent = SemanticNetsAgent()
    
    results = []  # To store results for each test case

    for sheep, wolves in test_cases:
        start_time = time.time()
        solution = agent.solve(sheep, wolves)
        end_time = time.time()

        elapsed_time = end_time - start_time

        results.append({
            "Sheep": sheep,
            "Wolves": wolves,
            "Solution": solution,
            "Time (s)": elapsed_time
        })

        print(f"Test Case (Sheep: {sheep}, Wolves: {wolves}) - Time: {elapsed_time:.6f}s - Solution: {solution}")

    return results


##### Plot All Results Function -----

# Function to plot all three results on the same plot
def plot_combined_results(results_1, results_2, results_3, filename):
    plt.figure()

    # Plot first set
    sheep_counts_1 = [result["Sheep"] for result in results_1]
    times_1 = [result["Time (s)"] for result in results_1]
    plt.plot(sheep_counts_1, times_1, marker='o', label="Wolves = Sheep - 1")

    # Plot second set
    sheep_counts_2 = [result["Sheep"] for result in results_2]
    times_2 = [result["Time (s)"] for result in results_2]
    plt.plot(sheep_counts_2, times_2, marker='o', label="Wolves = 0.5 * Sheep")

    # Plot third set
    sheep_counts_3 = [result["Sheep"] for result in results_3]
    times_3 = [result["Time (s)"] for result in results_3]
    plt.plot(sheep_counts_3, times_3, marker='o', label="Wolves = 0.75 * Sheep")

    plt.title("Combined Time vs Sheep Count")
    plt.xlabel("Number of Sheep")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()


##### Plot Set function -----

# Function to plot the results of a single set of test cases
def plot_results(results, title, filename):
    sheep_counts = [result["Sheep"] for result in results]
    times = [result["Time (s)"] for result in results]

    plt.plot(sheep_counts, times, marker='o')
    plt.title(title)
    plt.xlabel("Number of Sheep")
    plt.ylabel("Time (s)")
    plt.grid(True)
    plt.savefig(filename)
    plt.show()


##### Main -----

if __name__ == "__main__":

    # Create a data folder if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")

    # First set of test cases (Wolves close to Sheep count)
    test_cases_1 = [
        (100, 99),
        (200, 199),
        (300, 299),
        (400, 399),
        (500, 499),
        (600, 599),
        (700, 699),
        (800, 799),
        (900, 899),
        (1000, 999),
    ]

    # Second set of test cases (Wolves half the Sheep count)
    test_cases_2 = [
        (100, 50),
        (200, 100),
        (300, 150),
        (400, 200),
        (500, 250),
        (600, 300),
        (700, 350),
        (800, 400),
        (900, 450),
        (1000, 500),
    ]

    # Third set of test cases (Wolves in the middle of first and second set)
    test_cases_3 = [
        (100, 75),
        (200, 150),
        (300, 225),
        (400, 300),
        (500, 375),
        (600, 450),
        (700, 525),
        (800, 600),
        (900, 675),
        (1000, 750),
    ]

    # Print 1st set
    print("Running first set of test cases.")
    results_1 = test_efficiency(test_cases_1)

    # Print 2nd set
    print("Running second set of test cases.")
    results_2 = test_efficiency(test_cases_2)

    # Print 3rd set
    print("Running third set of test cases.")
    results_3 = test_efficiency(test_cases_3)

    # Plot results for all sets
    plot_results(results_1, "Time vs Sheep Count (Wolves = Sheep - 1)", "data/plot_wolves_close.png")
    plot_results(results_2, "Time vs Sheep Count (Wolves = 0.5 * Sheep)", "data/plot_wolves_half.png")
    plot_results(results_3, "Time vs Sheep Count (Wolves = 0.75 * Sheep)", "data/plot_wolves_middle.png")

    # Plot combined results
    plot_combined_results(results_1, results_2, results_3, "data/plot_combined.png")

    # Save results
    with open("data/efficiency_results.txt", "w") as file:
        file.write("First Set of Test Cases:\n")
        for result in results_1:
            file.write(f"Test Case (Sheep: {result['Sheep']}, Wolves: {result['Wolves']}):\n")
            file.write(f"Time Taken: {result['Time (s)']:.6f}s\n\n")

        file.write("Second Set of Test Cases:\n")
        for result in results_2:
            file.write(f"Test Case (Sheep: {result['Sheep']}, Wolves: {result['Wolves']}):\n")
            file.write(f"Time Taken: {result['Time (s)']:.6f}s\n\n")

        file.write("Third Set of Test Cases:\n")
        for result in results_3:
            file.write(f"Test Case (Sheep: {result['Sheep']}, Wolves: {result['Wolves']}):\n")
            file.write(f"Time Taken: {result['Time (s)']:.6f}s\n\n")

    print("Efficiency testing complete. Results saved to efficiency_results.txt.")
