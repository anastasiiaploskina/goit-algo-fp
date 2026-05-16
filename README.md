# GOIT Algorithms Final Project

## Overview

This repository contains solutions for a series of algorithmic and data structure tasks implemented in Python.

The project demonstrates practical usage of:

- Linked lists
- Sorting algorithms
- Recursion and fractals
- Graph algorithms
- Binary heaps and tree visualization
- Tree traversal algorithms
- Greedy algorithms
- Dynamic programming
- Monte Carlo simulations

The project was created as part of the GOIT algorithmic programming assignments.

---

# Project Structure

```text
.
├── task1.py   # Linked lists, sorting, merging
├── task2.py   # Recursive Pythagoras Tree fractal
├── task3.py   # Dijkstra shortest path algorithm
├── task4.py   # Binary heap visualization
├── task5.py   # DFS and BFS tree traversal visualization
├── task6.py   # Greedy algorithm vs dynamic programming
├── task7.py   # Monte Carlo dice simulation
├── pyproject.toml
└── README.md
```

---

# Requirements

- Python 3.13+
- matplotlib
- networkx

Dependencies are defined in `pyproject.toml`.

## Install dependencies

Using pip:

```bash
pip install matplotlib networkx
```

Or using uv:

```bash
uv sync
```

---

# Task 1 — Linked Lists and Sorting

## Description

Implementation of a singly linked list with the following functionality:

- Insert elements
- Delete nodes
- Search elements
- Reverse linked list
- Merge sort for linked lists
- Merge two sorted linked lists

## Features

### Reverse Linked List

The `reverse()` method reverses the list by changing node references.

### Merge Sort

The linked list is sorted using the merge sort algorithm:

1. Finds the middle node
2. Splits the list recursively
3. Merges sorted halves

### Merge Sorted Lists

Two sorted linked lists are merged into one sorted list.

## Example

```python
first_list.reverse()

first_list.head = first_list.merge_sort(first_list.head)

merged = first_list.merge_sorted_lists(first_list, second_list)
```

---

# Task 2 — Recursive Pythagoras Tree Fractal

## Description

A recursive visualization of the **Pythagoras Tree fractal** using `matplotlib`.

The user specifies the recursion depth, and the program recursively draws branches at different angles.

## Features

- Recursive fractal generation
- Adjustable recursion depth
- Graphical visualization
- Dynamic branch scaling

## Run

```bash
python task2.py
```

Example input:

```text
Enter the recursion depth:
```

---

# Task 3 — Dijkstra Algorithm with Binary Heap

## Description

Implementation of Dijkstra’s shortest path algorithm using:

- Weighted graph
- Priority queue (`heapq`)
- Binary heap optimization

The graph is visualized using `networkx` and `matplotlib`.

## Features

- Efficient shortest path calculation
- Priority queue optimization
- Weighted graph support
- Graph visualization

## Algorithm Complexity

```text
O((V + E) log V)
```

## Example Output

```python
{'A': 0, 'B': 4, 'C': 7, 'E': 8, 'F': 8, 'D': 12, 'G': 10, 'H': 11}
```

---

# Task 4 — Binary Heap Visualization

## Description

Visualization of a binary heap as a tree structure.

The program:

1. Builds a heap using `heapq`
2. Converts the heap into a binary tree
3. Draws the tree using `networkx`

## Features

- Heap construction
- Recursive tree building
- Binary tree visualization

## Example

```python
heap_list = [1, 3, 5, 7, 9, 2]
heapq.heapify(heap_list)
```

---

# Task 5 — DFS and BFS Tree Traversal Visualization

## Description

Visualization of binary tree traversal algorithms:

- DFS (Depth-First Search)
- BFS (Breadth-First Search)

Traversal order is visualized using dynamically generated node colors.

## Requirements Implemented

- Stack used for DFS
- Queue used for BFS
- No recursion used for traversal
- Unique color for each visited node
- RGB hex color generation

## Features

### DFS Traversal

Uses a stack to simulate depth-first traversal.

### BFS Traversal

Uses `collections.deque` as a queue for breadth-first traversal.

### Dynamic Coloring

Node colors gradually change depending on traversal order.

---

# Task 6 — Greedy Algorithm and Dynamic Programming

## Description

Comparison of two approaches for maximizing calories within a limited budget:

1. Greedy algorithm
2. Dynamic programming

Food items contain:

- Cost
- Calories

## Dataset

```python
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
```

## Greedy Algorithm

Chooses items with the best calorie-to-cost ratio.

### Complexity

```text
O(n log n)
```

## Dynamic Programming

Finds the optimal solution using a DP table.

### Complexity

```text
O(n * budget)
```

---

# Task 7 — Monte Carlo Dice Simulation

## Description

Monte Carlo simulation for calculating probabilities of sums when rolling two dice.

The program:

1. Simulates dice rolls
2. Calculates probability distribution
3. Compares experimental and analytical probabilities
4. Displays results in tables and charts

## Features

- Random simulations
- Statistical analysis
- Probability comparison
- Visualization with bar charts

## Example

```python
simulate_dice_rolls(100000)
```

## Sample Output

```text
--- Порівняння для 100,000 кидків ---
Сума  | Монте-Карло  | Аналітична   | Різниця   
--------------------------------------------------
2     | 2.67       % | 2.78       % | 0.11     %
3     | 5.60       % | 5.56       % | 0.04     %
4     | 8.45       % | 8.33       % | 0.11     %
5     | 11.09      % | 11.11      % | 0.02     %
6     | 13.73      % | 13.89      % | 0.16     %
7     | 16.57      % | 16.67      % | 0.09     %
8     | 13.88      % | 13.89      % | 0.01     %
9     | 11.24      % | 11.11      % | 0.13     %
10    | 8.31       % | 8.33       % | 0.02     %
11    | 5.57       % | 5.56       % | 0.02     %
12    | 2.88       % | 2.78       % | 0.10     %
--------------------------------------------------
```

---

# Technologies Used

- Python 3.13
- matplotlib
- networkx
- heapq
- collections.deque
- uuid

---

# Running the Project

Run any task individually:

```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
python task6.py
python task7.py
```

---

# Learning Objectives

This project demonstrates understanding of:

- Data structures
- Graph theory
- Tree traversal
- Recursive algorithms
- Heap structures
- Dynamic programming
- Greedy optimization
- Simulation methods
- Data visualization

---

# License

This project is intended for educational purposes.
