from graph_pkg.edit_cost.edit_cost cimport EditCost
from graph_pkg.graph.graph cimport Graph
from graph_pkg.graph.node cimport Node
from graph_pkg.graph.edge cimport Edge

cdef class GED:

    cdef:
        int _n, _m
        readonly int[::1] phi
        double _free_edge_sub
        readonly double[:, ::1] C, C_star

        Graph graph_source, graph_target
        EditCost edit_cost


    cdef void _create_c_matrix(self)

    cdef void _create_c_star_matrix(self)

    cdef double _compute_cost_node_edit(self, int[::1] phi)

    cdef double _compute_cost_edge_edit(self, int[::1] phi)

    cpdef double compute_edit_distance(self, Graph graph_source, Graph graph_target)