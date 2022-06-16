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

# You can use import the datastructure .py in your program as 
from datastructure import stack ... 
s = stack() 
*with every function you can use the .help() method to access the help method 

Next Implmentation :
- Singly Link List 
- Binary tree 
- Heap 
- Binary Search Tree 
- Treaps
- Directed Graphs 
- Undirected Graphs 
- K Dimentional Tree 

