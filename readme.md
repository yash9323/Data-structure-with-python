# Data structure with Python 
This repo contains the implementation of the most used data structure with python 
You can use this repo to understand the various data structures and built them with python 
The datastructure.py contains implementaion of :
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
  - You can intialize the link list by #from slinklist import linklist and then s = linklist(rootval)
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

# You can use import the datastructure .py in your program as 
from datastructure import stack ... 
s = stack() 
*with every function you can use the .help() method to access the help method 

Next Implmentation :
- Heap 
- Binary Search Tree 
- Treaps
- Directed Graphs 
- Undirected Graphs 
- K Dimentional Tree 

