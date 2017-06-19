'''Prompt:
You have simple linked list that specifies paths through a graph. For example;  [(node1, node2), (node2, node3)]
node 1 connects to node 2 and node 2 connects to node 3. Write a program that traverses the list and breaks any cycles.
So if node 1 links to both node 2 and node 2374, one link should be broken and reset. Give the first link formed priority.
You can use helper methods .get(index) and .set(index, (new_value)) to get and set new links in the list or write your own
'''

'''Explanation:
Given the constraints, there are basically two cases that we want to control for: cycles and multiple links. Will be
maintaining 2 lists in addition to the original: one to store previously seen values, one to return.
1. Iterate through the list of edges, check if the source node (n1 in (n1, n2)) is already in the seen nodes dict
2. If it's not in the seen nodes dict, add it to the dict and make sure n1's pointer doesn't create a cycle or is the
second edge from that node. If those are both true, append the edge to the return list
3. If it is in the dict, check if there is a cycle by comparing to the previous edge. If a cycle is present, append an edge
containing (n1, n4), where original two edges were [(n1, n2)(n3, n4)], effectively skipping the node creating the cycle
4. All other cases are skipped, as they are not the original edges from a particular source node
'''

from operator import itemgetter

class linked_list(object):
    def __init__(self, edge_list):
        self.edge_list = edge_list

    def get(self, index):
        return self.edge_list[index]

    def set(self, index, new_value):
        self.edge_list[index] = new_value
        return self.edge_list

    def list_iter(self):
        ret_list = []
        seen_dict = {}
        for i, edge in enumerate(self.edge_list):
            node_from, node_to = itemgetter(0, 1)(edge)
            if node_from not in seen_dict:
                # new node addition to seen dict
                seen_dict[node_from] = True
                if node_to not in seen_dict:
                    # source and destination nodes are unique and create no cycles
                    ret_list.append(edge)
            else:
                prev_node_from, prev_node_to = itemgetter(0, 1)(self.edge_list[i-1])
                if prev_node_to == node_from:
                    # cycling case - skips the cycled node to preserve path continuity
                    ret_list.append((prev_node_from, node_to))
        return sorted(list(set(ret_list)))

input_list = [('n1', 'n2'), ('n2', 'n3'), ('n3', 'n1'), ('n1', 'n4'), ('n4', 'n5'), ('n1', 'n123')]
x = linked_list(input_list)
print(x.list_iter())
