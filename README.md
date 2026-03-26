# shuttle-network-graph-analysis
# Discovering Connections: Using Graph Theory to Optimize SU's Shuttle Network

**Syracuse University — SOURCE Explorers Program | January 2025 – February 2025**

**Researchers:** Sabrina Smokler, Darika Djusupova, Daniel Johnson, and Alexander Delgado (me)

**Research Mentors:** Brianna Gillfillian and Bryan Bueno

---

## Overview

This research project applied **graph theory**, **Breadth-First Search (BFS)**, and **Depth-First Search (DFS)** algorithms to model and analyze Syracuse University's trolley (shuttle) network. Using Python and NetworkX, we represented each trolley stop as a vertex and each route as a weighted directed edge, then analyzed connectivity patterns to make data-driven recommendations for improving campus transportation efficiency.

---

## Tools & Technologies

- **Python** — core programming language
- **NetworkX** — graph construction, traversal, and analysis
- **Matplotlib** — graph visualization
- **SciPy** — supporting data analysis
- **Collections (deque)** — BFS/DFS queue implementation

---

## Repository Structure

```
source-explore-graph-theory/
├── README.md
├── code/
│   ├── Shuttle Loops.py        # Models all 5 SU trolley routes as directed graphs
│   ├── routes.py               # MultiDiGraph with colored routes, BFS & DFS path finding
│   ├── shortest routes.py      # BFS shortest path from College Place to all stops
│   └── main.py                 # Initial graph prototype and weighted edge visualization
│   └── practice.py             # BFS tree exploration (experimental)
├── results/
│   └── research_poster.png     # Full research poster presented at SOURCE Explorers
```

---

## Code Breakdown

### `Shuttle Loops.py` — Main Route Visualization
Models all **5 SU trolley loops** as separate directed graphs and overlays them on a shared layout:

| Route | Color | Key Stops |
|---|---|---|
| South Campus Loop | Purple | CP → Comstock Lot → Colvin Lot → Skytop → Goldstein |
| Orange Loop | Orange | CP → Flint → Shaw → BBB → Irving Garage → NVRC → Dellplain |
| Blue Loop | Blue | CP → Comstock Ave → NVRC → BBB → Irving Garage → Shaw |
| Warehouse Loop | Red | CP → BBB → Syracuse Stage → Peck Hall → Warehouse |
| Euclid Loop | Green | CP → Genesee Irving → Genesee Crouse → Westcott Euclid |

Runs a BFS tree from College Place across the combined graph and prints traversal order.

### `routes.py` — Multi-Route Graph with BFS & DFS Path Finding
Uses a `MultiDiGraph` to allow multiple overlapping edges between the same stops. Implements both:
- **BFS path finding** — explores shortest hops from College Place across all routes
- **DFS path finding** — explores all possible deep paths from College Place

### `shortest routes.py` — BFS Shortest Path Analysis
Implements a clean BFS shortest path function that calculates the minimum number of hops from **College Place** to every other stop in the network. This was core to identifying which stops are hardest to reach.

### `main.py` — Initial Graph Prototype
Early-stage prototype used to learn and validate the NetworkX workflow with simplified weighted edges before scaling to the full shuttle network.

---

## Methodology

### Graph Construction
- Each SU trolley stop → **vertex**
- Each route segment → **weighted directed edge** (weight = travel time in minutes)
- Each trolley line → distinct color for visual differentiation

### BFS Traversal
BFS was run starting from **College Place (CP)** as the root node. Each layer of traversal represents stops that are one additional hop away, allowing us to measure how reachable each stop is relative to the central hub.

### DFS Traversal
DFS was used to enumerate all possible paths from College Place, helping identify the full extent of each route and where routes diverge or terminate.

---

## Key Findings

| Stop | Connectivity | BFS Layer | Interpretation |
|---|---|---|---|
| College Place (CP) | 5 connections | Layer 0 (root) | Primary hub — on every route |
| BBB | 3 connections | Early layer | Important transfer point |
| Irving Garage, Colvin Lot, NVRC, Comstock Ave, Flint, Barnes, Forestry Gate, Herny St. Lot, Shaw | 2 connections | Mid layers | Moderate connectivity |
| Skytop Offices (SKYO) | Low | Layer 7 | Least frequently visited |
| Goldstein Student Center (GSS) | Low | Layer 8 | Longest travel time from hub |

---

## Recommendations

1. **Add more routes serving South Campus** — Skytop and Goldstein appear at the deepest BFS layers, making them the hardest stops to reach from the central hub
2. **Preserve College Place frequency** — Its high connectivity is a structural necessity, not an inefficiency; it is the only stop shared by all 5 routes
3. **Use BFS depth as a planning metric** — Future route changes should target stops with high BFS layer numbers to reduce campus accessibility gaps

---

## About SOURCE Explorers

The [SOURCE Explorers Program](https://surface.syr.edu/source/) at Syracuse University is a faculty-mentored undergraduate research initiative supporting students in applied research across STEM disciplines.

---

## Author

**Alexander Delgado**  
B.S. Computer Engineering, Syracuse University (Class of 2027)  
[LinkedIn](https://linkedin.com/in/alexd1222/) | adelga11@syr.edu
