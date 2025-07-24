# AI Assignment - Search-Based Problem Solving


**Student Name:** Sai Shiva Thatipalli  
**Department:** CSE (3rd Year)  
**Subject:** Artificial Intelligence  

---

## 🧠 Problem 1: Rabbit Leap Problem

### 📌 Problem Statement:
Three east-bound rabbits and three west-bound rabbits stand in a line with a single empty stone between them. They need to cross each other using stones placed in a line. Each rabbit can:
- Move forward by 1 step if the next position is empty.
- Jump over exactly one rabbit into an empty space.
- Cannot jump over two rabbits.
- Can only move in their direction (E ➡, W ⬅).

**Initial Configuration:**  
`E E E _ W W W`  
**Goal Configuration:**  
`W W W _ E E E`

### 💡 Objective:
Find a valid sequence of moves that transitions the rabbits from the initial state to the goal state **without any deadlock**.

### 🚀 Solution Approach:
Implemented both **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to explore the state space.

### 🔧 Implementation Highlights:
- `State` class represents the arrangement of rabbits.
- `move_gen()` generates all legal moves based on current configuration.
- `bfs()` and `dfs()` explore the state space and reconstruct the shortest solution path.
- `removeSeen()` filters already-visited states from expansion.
- `reconstructPath()` backtracks from goal to start.

---

## 🧠 Problem 2: Bridge and Torch Problem

### 📌 Problem Statement:
Amogh, Ameya, Grandmother, and Grandfather must cross a bridge within 60 minutes to catch a train. It's raining and only one umbrella is available (can be used by two people at once). Nobody wants to get wet.

**Individual crossing times:**
- Amogh: 5 minutes  
- Ameya: 10 minutes  
- Grandmother: 20 minutes  
- Grandfather: 25 minutes  

### 💡 Objective:
Find a sequence of valid crossings such that **all four cross the bridge in 60 minutes or less**, respecting constraints.

### 🛠️ Constraints:
- At most 2 people can cross at a time.
- Umbrella must be used both ways.
- Time is counted as the **maximum** of the two crossing people.
- Total time must be within 60 minutes.

### 🚀 Solution Approach:
Modeled as a state-space search problem using BFS and DFS:
- Each `State` tracks positions of people, umbrella, and time remaining.
- `move_gen()` generates valid forward (2 people) and return (1 person) moves.
- Search continues until all are on the other side within the allowed time.

### 🔧 Implementation Highlights:
- `State` holds each person's side (0: left, 1: right), umbrella side, and remaining time.
- `move_gen()` uses `itertools.combinations()` to simulate possible moves.
- `removeSeen()` ensures previously visited configurations are not repeated.
- `reconstructPath()` backtracks the valid transition path if a solution is found.





