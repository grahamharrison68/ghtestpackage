import networkx as nx

#from pycausalwhy.common import BaseCollection

class Node():
    """Encapusulates the functionality of a node in the directed acyclic graph
        """

    def __init__(self, name: str, dag: "DirectedAcyclicGraph"):
        self._name = name
        self._dag = dag

    @property
    def name(self) -> str:
        """The name of the ID

            Returns:
                str: The name of the treatment node
            """
        return self._name

    @property
    def is_treatment(self) -> bool:
        """Indicates if the node is the treatment node

            Returns:
                bool: True if the node is the treatment node, otherwise false
            """
        return self.name == self._dag._treatment

    @property
    def is_outcome(self) -> bool:
        """Indicates if the node is the outcome node

            Returns:
                bool: True if the node is the outcome node, otherwise false
            """
        return self.name == self._dag._outcome

    @property
    def is_unobserved(self) -> bool:
        """Indicates if the node is unobserved

            Returns:
                bool: True if the node is the unobserved node, otherwise false
            """
        return self.name in self._dag._unobserved_confounders

    @property
    def parents(self) -> "Nodes":
        """Returns the nodes that are parents of the current node

            Returns:
                Nodes: A Nodes collection of the parent nodes
            """
        #return Nodes(node_names=list(self._dag._digraph.predecessors(self.name)), dag=self._dag)
        return {node_name: Node(name=node_name, dag=self._dag) for node_name in list(self._dag._digraph.predecessors(self.name))}

    @property
    def ancestors(self) -> "Nodes":
        """Returns the nodes that are ancestors of the current node

            Returns:
                Nodes: A Nodes collection of the ancestor nodes
            """
        #return Nodes(node_names=list(nx.ancestors(self._dag._digraph, self.name)), dag=self._dag)
        return {node_name: Node(name=node_name, dag=self._dag) for node_name in list(nx.ancestors(self._dag._digraph, self.name))}

    @property
    def children(self) -> "Nodes":
        """Returns the nodes that are children of the current node

            Returns:
                Nodes: A Nodes collection of the children nodes
            """
        #return Nodes(node_names=list(self._dag._digraph.successors(self.name)), dag=self._dag)
        return {node_name: Node(name=node_name, dag=self._dag) for node_name in list(self._dag._digraph.successors(self.name))}

    @property
    def descendants(self) -> "Nodes":
        """Returns the nodes that are descendants of the current node

            Returns:
                Nodes: A Nodes collection of the ancestor nodes
            """
        #return Nodes(node_names=list(nx.descendants(self._dag._digraph, self.name)), dag=self._dag)
        return {node_name: Node(name=node_name, dag=self._dag) for node_name in list(nx.descendants(self._dag._digraph, self.name))}

    @property
    def non_descendants(self) -> "Nodes":
        """Returns the nodes that are non-descendants of the current node

            Returns:
                Nodes: A Nodes collection of the non-descendant nodes

            Notes:
                Non-descendants are all observed nodes MINUS descendants MINUS the current node MINUS immediate parents and they are used in Pearlean checks for missing links
            """
        # return list(set(self.observed_nodes) - set(self.descendants(node_name=node_name)) - set([node_name]) - set(self.parents(node_name=node_name)))
        observed_node_names = {node.name for node in self._dag.nodes.values() if ~node.is_unobserved}
        descendant_node_names = {node.name for node in self.descendants.values()}
        node_name = {self.name}
        parent_node_names = {node.name for node in self.parents.values()}

        non_descendant_node_names = observed_node_names - descendant_node_names - node_name - parent_node_names

        #return Nodes(node_names=list(observed_node_names - descendant_node_names - node_name - parent_node_names), dag=self._dag)
        return {node_name: node for node_name, node in self._dag.nodes.items() if node_name in non_descendant_node_names}

    def __repr__(self):
        return f"Node(name={self.name}, is_treatment={self.is_treatment}, is_outcome={self.is_outcome}, unobserved={self.is_unobserved})"

# class Nodes(BaseCollection):
#     """Holds a list of all the nodes
#         """
#     def __init__(self, node_names: list, dag: "DirectedAcyclicGraph"):
#         """Constructor

#             Args:
#                 nodes (dict): A dict containing the nodes and their positions

#             Example:
#                 >>> nodes = Nodes(nodes={'X': [1, 1], 'Z1': [1, 3], 'W': [2, 1.25], 'Z3': [2, 2.25], 'Y': [3, 1], 'Z2': [3, 3]})
#                 >>> nodes[0]
#                 >>> ('X', Node(name=X, pos=Pos(x=1, y=1)))

#                 >>> nodes["Z1"]
#                 >>> Node(name=Z1, pos=Pos(x=1, y=3))
#             """
#         # region comments
#         # {item[0]: Node(item[0], item[1][0], item[1][1]) for item in list(nodes_dict.items())}
#         # converts ...
#         # {'X': [1, 1], 'Z1': [1, 3], 'W': [2, 1.25], 'Z3': [2, 2.25], 'Y': [3, 1], 'Z2': [3, 3]}
#         # into ...
#         # {'X': Node(name=X, pos=Pos(x=1, y=1)), 'Z1': Node(name=Z1, pos=Pos(x=1, y=3)), 'W': Node(name=W, pos=Pos(x=2, y=1.25)), 'Z3': Node(name=Z3, pos=Pos(x=2, y=2.25)), 'Y': Node(name=Y, pos=Pos(x=3, y=1)), 'Z2': Node(name=Z2, pos=Pos(x=3, y=3))}
#         # endregion
#         self._dag = dag
#         super().__init__({node_name: Node(name=node_name, dag=self._dag) for node_name in node_names})

#     def __repr__(self):
#         return_string = ""
#         for node in self:
#             return_string += f"{node.__repr__()}\n"
#         return return_string
