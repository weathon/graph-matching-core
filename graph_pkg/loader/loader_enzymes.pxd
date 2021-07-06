from graph_pkg.graph.label.label_base cimport LabelBase
from graph_pkg.graph.label.label_edge cimport LabelEdge
from graph_pkg.graph.label.label_node_enzymes cimport LabelNodeEnzymes
from graph_pkg.loader.loader_base cimport LoaderBase


cdef class LoaderEnzymes(LoaderBase):

    cpdef int _format_idx(self, str idx)

    cpdef LabelBase _formatted_lbl_node(self, attr)

    cpdef LabelBase _formatted_lbl_edge(self, attr)
