'''Prompt:
You have simple linked list that specifies paths through a graph. For example;  [(node1, node2), (node2, node3)]
node 1 connects to node 2 and node 2 connects to node 3. Write a program that traverses the list and breaks any cycles.
So if node 1 links to both node 2 and node 2374, one link should be broken and reset. Give the first link formed priority.
You can use helper methods .get(index) and .set(index, (new_value)) to get and set new links in the list or write your own
'''

'''Explanation:
Given the constraints, there are basically two cases that we want to control for: cycles and multiple links.
Cycles will be in the following format: [(n1, n2),...(nx, n1)]
In this case, we want to:
1. check to see if there is a link after the loop occurs
2. if no, set the loop edge pointer to Null
3. if yes, skip the node causing the loop
Multiple links will be in the following format: [(n1, n2),...(n1, nx)]
In this case, we want to:
1. check to see if there is a link after the multiple links occur
2. if yes, delete the link and 
'''