# Data structure with Python 
This repo contains the implementation of the most used data structures built <br /> by using python programming language. <br />
You can use this repo to understand the various 
- data structures
- built them on your own  
- Use them in your projects.
<br />

The datastructure.py contains implementaion of :
- Stack
- Queue 
- Max Priority Queue
- Min Priority Queue 
- Min Heap
- Max Heap
- Double Ended Queue 
- Bloom Filter 
- Binary Search Tree 
- Link List 
- Circular Link List 
- Un-Directed Graphs
- Directed Graphs

Datastructures implemented seperately :
- Binary Tree 

Next Implmentation to add 
- Treaps
- Directed Graphs 
- Undirected Graphs 
- K Dimentional Tree 
- skip list 

# Refer this for Help

- stack 
  - .put(value_to_add) - allows you to add element in the stack !
  - .pop(return_pop_element=False) - allows you to remove the top element of the stack also returns if return true !
  - .print_stack() - prints the stack if not empty !
  - .put_multiple(n) - allows you to add n elements in the stack !
  - .put_list(list) - allows you to add a list of elements into the stack !
  - .bottom_of_stack(return_element(boolean)) - returns or prints the bottom of the stack !
  - .top_of_stack(return_element(boolean)) - returns or prints the top of the stack !
  
- queue
  - .enqueue(value_to_add) - allows you to add element in the queue !
  - .dequeue(return_pop_element=False) - allows you to remove the start element of the queue also returns if return true !
  - .print_queue() - prints the queue if not empty !
  - .put_multiple(n) - allows you to add n elements in the queue !
  - .put_list(list) - allows you to add a list of elements into the queue !
  - .last_of_queue(return_element(boolean)) - returns or prints the bottom of the queue 
  - .start_of_queue(return_element(boolean)) - returns or prints the top of the queue !
  - .size_of_queue() - returns the size of the queue
  
- max priority queue 
  - .enqueue(value_to_add) - allows you to add element in the queue !
  - .dequeue(return_pop_element=False) - allows you to remove the max element of the queue also returns if return true !
  - .print_queue() - prints the queue if not empty !
  - .put_multiple(n) - allows you to add n elements in the queue !
  - .put_list(list) - allows you to add a list of elements into the queue !
  - .last_of_queue(return_element(boolean)) - returns or prints the bottom of the queue !
  - .start_of_queue(return_element(boolean)) - returns or prints the top of the queue !
  
- min priority queue 
  - .enqueue(value_to_add) - allows you to add element in the queue !
  - .dequeue(return_pop_element=False) - allows you to remove the min element of the queue also returns if return true !
  - .print_queue() - prints the queue if not empty !
  - .put_multiple(n) - allows you to add n elements in the queue !
  - .put_list(list) - allows you to add a list of elements into the queue !
  - .last_of_queue(return_element(boolean)) - returns or prints the bottom of the queue !
  - .start_of_queue(return_element(boolean)) - returns or prints the top of the queue !
  
- double ended queue 
  - .enqueue_start(value_to_add) - allows you to add element in the start of the queue !
  - .enqueue_end(value_to_add) - allows you to add element in the end of the queue !
  - .dequeue_start(return_pop_element=False) - allows you to remove the start element of the queue also returns if return true !
  - .dequeue_end(return_pop_element=False) - allows you to remove the end element of the queue also returns if return true !
  - .print_queue() - prints the queue if not empty !
  - .put_multiple(n,reverse=False) - allows you to add n elements in the queue !,reverse allows to add from the start of the queue
  - .put_list(list,reverse=False) - allows you to add a list of elements into the queue !reverse allows to add from the start of the queue
  - .last_of_queue(return_element(boolean)) - returns or prints the bottom of the queue !
  - .start_of_queue(return_element(boolean)) - returns or prints the top of the queue !
  
- bloom filter 
  - You can use the .insert() method to insert into the filter !
  - You can use the .check() method to check into the filter !

- LinkList 
  - You can intialize the link list by #from datastructure import linklist and then s = linklist(rootval)
  - You can use the add_node_start(val) to add value to the start of the link list
  - You can use the add_node_end(val) to add value to the end of the link list 
  - You can use the print_lisk_list() to print the link list 
  - You can use the delete_start() to delete the node from start of linklist 
  - You can use the delete_end() to delete the node from end of linklist 
  - You can use the delete_between(val) to delete the node in between of linklist 
  - You can use the reverse_link_list() to reverse the link list 
 
- Binary Tree
  - You can use the different traversals to print the tree in your desired order 
      - level_order_traversal()
      - in_order_traversal()
      - post_order_traversal()
      - pre_order_traversal()
  - You can use height() to get the height of binary tree 
  - insert_auto() inserts node in the binary tree by checking on the root value 
  - insert_right() inserts in the right sub tree 
  - insert_left() inserts in the left sub tree 

- Min Heap <br />
  You can use minheap as <br />
  from datastructure import minheap <br />
  mheap = minheap() <br />
  mheap.add_node() -- adds node to the min heap <br />
  mheap.delete() -- deletes the min node from the heap <br />
  mheap.size_of_heap() -- prints the size of the heap <br />
  mheap.print_heap() --prints the heap <br />
  mheap.peak() -- prints the min value of the heap <br /> 
  
- Max Heap <br />
  You can use maxheap as <br />
  from datastructure import maxheap <br />
  mheap = maxheap() <br />
  mheap.add_node() -- adds node to the max heap <br />
  mheap.delete() -- deletes the max node from the heap <br />
  mheap.size_of_heap() -- prints the size of the heap <br />
  mheap.print_heap() --prints the heap <br />
  mheap.peak() -- prints the min value of the heap <br /> 
  depth_of_heap() -- returns the depth of heap <br />

- Binary Search Tree 
  You can use Binary Search Tree as <br />
  from datastructure import BinarySearchTree <br />
  bst = BinarySearchTree(val) -- initialize the bst with root val <br />
  bst.add_node(val) -- to add node to the bst <br />
  bst.in_order_traversal() --prints the inorder traversal of the tree <br />
  bst.delete_node(val) -- deletes nodes and rearranges it <br />
  bst.height() -- prints the height of the tree <br />

- Circular Link List 
  You can use the Circular Link list as follows <br />
  from datastructure import circularlinklist <br />
  cll = circularlinklist(val) -- initialize linklist with head val <br />
  cll.add_start(val) -- Adds a node to the start of the  circular link list <br />
  cll.add_start(end) -- Adds a node to the end of the circular link list <br />
  cll.delete_start() -- Deletes a node from the start of the circular link list <br />
  cll.delete_end() -- Deletes a node from the end of the circular link list <br />
  cll.print_link_list() -- Prints the Link list <br />

- Undirected Graphs <br />
  You can use the undirected graphs as follows <br />
  from datastructure import udgraph <br />
  g = udgraph() <br />
  g.add_node(value) => Adds a node <br />
  g.add_edge(one_node,another_node) => Adds a edge between one_node and another node <br />
  g.delete_node(node) => Deletes a node from the graph <br />
  g.delete_edge(node,another_node) => deletes the edge specified <br />
  g.find_paths(node,another_node) => Returns all the possible paths from one_node to another <br />
  g.show_all_nodes() => Prints all the nodes <br />
  g.show_all_edges() => prints all the edges <br />
  g.show_edges_from_node(node) => prints all the edges from a particular node <br />
  g.find_isolated_nodes(node=None) => If none returns all the isolated nodes else checks if the node entered is isolated or not <br />
  g.degree_node(node) => prints the degree of the specified node <br />

- Directed Graphs <br />
  You can use the directed graphs as follows <br />
  from datastructure import dgraph <br />
  g = dgraph() <br />
  g.add_node(value) => Adds a node <br />
  g.add_edge(one_node,another_node) => Adds a edge between one_node and another node <br />
  g.delete_node(node) => Deletes a node from the graph <br />
  g.delete_edge(node,another_node) => deletes the edge specified <br />
  g.find_paths(node,another_node) => Returns all the possible paths from one_node to another <br />
  g.show_all_nodes() => Prints all the nodes <br />
  g.show_all_edges() => prints all the edges <br />
  g.show_edges_from_node(node) => prints all the edges from a particular node <br />

# You can use import the datastructure .py in your program as 
from datastructure import stack ... 
s = stack() 
*with every function you can use the .help() method to access the help method 