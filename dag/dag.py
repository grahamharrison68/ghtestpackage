from typing import Iterable

import numpy as np

from pygraphviz import AGraph
import networkx as nx

from pycausalwhy.dag import Node

class DirectedAcyclicGraph():
    """_summary_
    """

    def __init__(self, treatment : str, outcome : str, edges : list = [], unobserved_confounders : list = [], pos : dict = None, digraph_string : str = "", gmlgraph_string : str = "", adj_matrix : Iterable = [], nodes: list = []):

        self._treatment = treatment
        self._outcome = outcome

        if digraph_string != "":
            edges = AGraph(digraph_string).edges() # AGraph can ingest a DiGraph string and automatically convert it to a model with nodes and edges so no additional work is necessary

        if gmlgraph_string != "":
            edges = list(nx.parse_gml(gmlgraph_string).edges)

        if adj_matrix != []:
            adj_matrix = np.array(adj_matrix)
            edges = [(nodes[r], nodes[c]) for r in range(adj_matrix.shape[0]) for c in range(adj_matrix.shape[1]) if adj_matrix[r, c] != 0]

        self._digraph = nx.DiGraph()
        self._digraph.add_nodes_from(sorted({node for edge in edges for node in edge})) # Use {} sets to pick the nodes out in alphabetical order - this helps when auto-rendering a circular layout from an adjacency matrix
        self._digraph.add_edges_from(edges)

        self._unobserved_confounders = unobserved_confounders

        self._pos = nx.circular_layout(self._digraph) if pos == None else pos

        self._nodes = {node_name: Node(name=node_name, dag=self) for node_name in list(self._digraph.nodes)}

    @property
    def nodes(self) -> dict:
        """The name of the ID

        Returns:
            str: The name of the treatment node
        """
        return self._nodes
