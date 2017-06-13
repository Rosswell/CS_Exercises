class Node(object):
    '''
    Creating a node with a value and a list of edges - nodes that it's connected to
    '''
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    '''
    Connection between two nodes with a value
    '''
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    '''
    Initializes an empty Graph with space for edges and nodes
    '''
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        '''
        :param new_node_val: value of the node to insert
        :return: updated nodes list
        '''
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        '''
        Take new edge params for a directed edge and return updated edges list
        :param new_edge_val: value of the new edge
        :param node_from_val: value of the new edge's source
        :param node_to_val: value of the new edge's destination
        :return: updated edges list
        '''
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        '''
        Iterate through the edge list and return a new list of edges.
        :return: edge list with values, source, and destination nodes for each edge
        '''
        edge_list = []
        for edge in self.edges:
            edge_list.append((edge.value, edge.node_from.value, edge.node_to.value))
        return edge_list

    def get_adjacency_list(self):
        '''
        Iterate over the nodes, and return a list of the all the node's edges, where the edge list's element index
        in the outer list is the node's value.
        :return: adjacency list of all nodes in the graph
        '''
        adj_list = [None] * (max([node.value for node in self.nodes]) + 1)
        for node in self.nodes:
            temp_list = [(edge.node_to.value, edge.value) for edge in self.edges if node.value == edge.node_from.value]
            if temp_list != []:
                adj_list[node.value] = temp_list
        return adj_list

    def get_adjacency_matrix(self):
        '''
        Create an (m x m) matrix, where m is the number of nodes in the graph. The index of the outer list is the value
        of a node, and the index of the inner list is the node to test for the presence of an edge between. Returns the
        edge's presence within the matrix as binary.
        :return: adjacency matrix for all nodes and edges in the graph.
        '''
        adj_mat = [[0] * y for x, y in zip(range(len(self.nodes) + 1), len(self.nodes) + 1)]
        for node in range(len(adj_mat)):
            for edge in self.edges:
                if edge.node_from.value == node:
                    adj_mat[node][edge.node_to.value] = edge.value
        return adj_mat


graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print(graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())