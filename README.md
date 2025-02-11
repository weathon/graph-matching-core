# Graph Matching Framework

This is a Cython framework to perform graph matching.
It uses the flexibility of python and the efficiency of compiled c code to 
package contains the core files to perform graph matching.

## Installation

#### Prerequisites
- Python 3.9
- Numpy
- A C++ compatible compiler


#### Install
```bash
# Clone repo
git clone https://github.com/CheshireCat12/graph-matching-core.git [folder-name]
# Move to repo directory
cd [folder-name]

#Create python virtual environment with python
python -m venv venv
source venv/bin/activate

# Install Numpy
pip install numpy

# Compile and install the code
pip install -e .
```

#### Run tests
```bash
python -m pytest tests
```

## How to use
```python
# More example available in ./tests/

from graph_pkg_core.algorithm.graph_edit_distance import GED
from graph_pkg_core.edit_cost.edit_cost_vector import EditCostVector
from graph_pkg_core.graph.edge import Edge
from graph_pkg_core.graph.graph import Graph
from graph_pkg_core.graph.label.label_edge import LabelEdge
from graph_pkg_core.graph.label.label_node_vector import LabelNodeVector
from graph_pkg_core.graph.node import Node
from graph_pkg_core.loader.loader_vector import LoaderVector

ged = GED(EditCostVector(1., 1., 1., 1., 'euclidean'))

n, m = 4, 3
graph_source = Graph('gr_source', 'gr_source.gxl', n)
graph_target = Graph('gr_target', 'gr_targe.gxl', m)

# Init graph source: add nodes and edges
graph_source.add_node(Node(0, LabelNodeVector(np.array([1.]))))
graph_source.add_node(Node(1, LabelNodeVector(np.array([2.]))))
graph_source.add_node(Node(2, LabelNodeVector(np.array([1.]))))
graph_source.add_node(Node(3, LabelNodeVector(np.array([3.]))))
graph_source.add_edge(Edge(0, 1, LabelEdge(0)))
graph_source.add_edge(Edge(1, 2, LabelEdge(0)))
graph_source.add_edge(Edge(1, 3, LabelEdge(0)))
graph_source.add_edge(Edge(2, 3, LabelEdge(0)))

# Init graph target: add nodes and edges
graph_target.add_node(Node(0, LabelNodeVector(np.array([3.]))))
graph_target.add_node(Node(1, LabelNodeVector(np.array([2.]))))
graph_target.add_node(Node(2, LabelNodeVector(np.array([2.]))))
graph_target.add_edge(Edge(0, 1, LabelEdge(0)))
graph_target.add_edge(Edge(1, 2, LabelEdge(0)))

edit_cost = ged.compute_edit_distance(graph_source, graph_target)
```

#### Parallelization
```python
[...]
from graph_pkg_core.algorithm.matrix_distances import MatrixDistances

ged = GED(EditCostVector(1., 1., 1., 1., 'euclidean'))

# List of graphs
source_graphs = [grs1, grs2, ..., grsm]
target_graphs = [grt1, grt2, ..., grtn]


mat_dist = MatrixDistances(ged, parallel=True)

mat_edit_dist = mat_dist.calc_matrix_distances(source_graphs,
                                                target_graphs,
                                                heuristic=True)
```
