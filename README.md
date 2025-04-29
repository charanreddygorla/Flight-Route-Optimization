# Flight-Route-Optimization

This Python program optimizes flight routes using Dijkstra’s algorithm, with additional features like displaying all possible flight paths, graph visualization, and booking functionality.

## Features

1)Find the fastest flight route between two cities.

2)Display all possible flight paths with distances and costs.

3)Visualize the flight graph with the shortest path highlighted.

4)Book flights using multiple payment methods.

## Installation and Setup

### 1)Prerequisites

  Python 3.6 or later

  Graphviz library (Python package)

  Graphviz software (system installation)

### 2)Installing Libraries

Use pip to install the required libraries:
pip install graphviz

### 3) Installing Graphviz Software

Download and install Graphviz from the official site.

Add Graphviz to your PATH (e.g., C:\Program Files\Graphviz\bin).

Verify installation by running dot -V in the Command Prompt.

## Menu Options

Option 1: Display fastest route and book flight (Dijkstra’s algorithm).

Option 2: Display all paths and book flight.

Option 3: Visualize flight graph with highlighted shortest path.

Option 4: Exit.

## Example Input/Output

### Input:

    Source: Delhi

    Destination: Mumbai

### Output:

    Fastest Flight: 2.05 hours, $513

    All Paths: Delhi -> Mumbai (2.05 hours, $513)
    
### Graph

A PNG file (highlighted_flight_graph.png) is generated showing the flight network with the shortest path.

## Notes

Ensure Graphviz is added to the PATH variable before running.

The program dynamically generates the flight graph and allows for interactive flight selection and booking.

      

