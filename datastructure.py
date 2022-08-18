import os,sys
from collections import deque

# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore print 
def enablePrint():
    sys.stdout = sys.__stdout__

class stack:
    def __init__(self):
        self.s = []
        print("Use .help() to see all the functions definitions ")
    def put(self,inpu):
        self.s.insert(0,inpu)
        print(f"{inpu} added to the stack succesfully")
    def pop(self,rett = False):
        if rett:
            if len(self.s)==0:
                print("stack is empty ! Cannot Pop")
            else:
                a = self.s[0]
                print(f"{a} element pop successfully and returned")
                self.s.pop(0)
                return a 
        else:
            if len(self.s)==0:
                print("stack is empty ! Cannot Pop")
            else:
                print(f"{self.s[0]} element pop successfully")
                self.s.pop(0)
    def print_stack(self):
        if len(self.s)==0:
            print("stack is empty")
        else:
            print("TOP",end="\n")
            for i in self.s:
                print(f"|{i}|",end="\n")
            print(" End ")
    def put_multiple(self,n):
        for _ in range(n):
            i = float(input())
            self.put(i)
    def put_list(self,l):
        for ele in l :
            self.put(ele)
    def bottom_of_stack(self,rett = False):
        if rett:
            return self.s[-1] 
        else:
            print(f"{self.s[-1]} is at the bottom of the stack !")
    def top_of_stack(self,rett = False):
        if rett:
            return self.s[0] 
        else:
            print(f"{self.s[0]} is at the bottom of the stack !")
    def help(self):
        print(".put(value_to_add) - allows you to add element in the stack !")
        print(".pop(return_pop_element=False) - allows you to remove the top element of the stack also returns if return true !")
        print(".print_stack() - prints the stack if not empty !")
        print(".put_multiple(n) - allows you to add n elements in the stack !")
        print(".put_list(list) - allows you to add a list of elements into the stack !")
        print(".bottom_of_stack(return_element(boolean)) - returns or prints the bottom of the stack !")
        print(".top_of_stack(return_element(boolean)) - returns or prints the top of the stack !")

class queue:
    def __init__(self):
        self.q = []
        print("Use .help() to see all the functions definitions ")
    def enqueue(self,inpu):
        self.q.insert(len(self.q),inpu)
        print(f"{inpu} added to the queue succesfully")
    def dequeue(self,rett = False):
        if rett:
            if len(self.q)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                a  = self.q[0]
                print(f"{a} element dequeue successfully")
                self.q.pop(0)
                return a 
        else:   
            if len(self.q)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                print(f"{self.q[0]} element dequeue successfully")
                self.q.pop(0)
    def print_queue(self):
        if len(self.q)==0:
            print("queue is empty")
        else:
            print("START|",end="")
            for i in self.q:
                print(f"{i}",end="|")
            print("End")
    def put_multiple(self,n):
        for _ in range(n):
            i = float(input())
            self.enqueue(i)
    def put_list(self,l):
        for ele in l :
            self.enqueue(ele)
    def last_of_queue(self,rett = False):
        if rett:
            return self.q[-1] 
        else:
            print(f"{self.q[-1]} is at the last of the queue !")
    def start_of_queue(self,rett = False):
        if rett:
            return self.q[0] 
        else:
            print(f"{self.q[0]} is at the start of the queue !")
    
    def size_of_queue(self):
        return len(self.q)
    
    def help(self):
        print(".enqueue(value_to_add) - allows you to add element in the queue !")
        print(".dequeue(return_pop_element=False) - allows you to remove the start element of the queue also returns if return true !")
        print(".print_queue() - prints the queue if not empty !")
        print(".put_multiple(n) - allows you to add n elements in the queue !")
        print(".put_list(list) - allows you to add a list of elements into the queue !")
        print(".last_of_queue(return_element(boolean)) - returns or prints the bottom of the queue !")
        print(".start_of_queue(return_element(boolean)) - returns or prints the top of the queue !")

class max_priority_queue:
    def __init__(self):
        self.mq = []
        print("Use .help() to see all the functions definitions ")
    def enqueue(self,inpu):
        self.mq.insert(len(self.mq),inpu)
        print(f"{inpu} added to the queue succesfully")
    def dequeue(self,rett=False):
        if rett:
            if len(self.mq)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                m = max(self.mq)
                print(f"{m} element dequeue successfully")
                self.mq.remove(m)
                return m
        else:
            if len(self.mq)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                m = max(self.mq)
                print(f"{m} element dequeue successfully")
                self.mq.remove(m)
    def print_queue(self):
        if len(self.mq)==0:
            print("queue is empty")
        else:
            print("START|",end="")
            for i in self.mq:
                print(f"{i}",end="|")
            print("End")
    def put_multiple(self,n):
        for _ in range(n):
            i = float(input())
            self.enqueue(i)
    def put_list(self,l):
        for ele in l :
            self.enqueue(ele)
    def last_of_queue(self,rett = False):
        if rett:
            return self.mq[-1] 
        else:
            print(f"{self.mq[-1]} is at the last of the queue !")
    def start_of_queue(self,rett = False):
        if rett:
            return self.mq[0] 
        else:
            print(f"{self.mq[0]} is at the start of the queue !")
    def help(self):
        print(".enqueue(value_to_add) - allows you to add element in the queue !")
        print(".dequeue(return_pop_element=False) - allows you to remove the max element of the queue also returns if return true !")
        print(".print_queue() - prints the queue if not empty !")
        print(".put_multiple(n) - allows you to add n elements in the queue !")
        print(".put_list(list) - allows you to add a list of elements into the queue !")
        print(".last_of_queue(return_element(boolean)) - returns or prints the bottom of the queue !")
        print(".start_of_queue(return_element(boolean)) - returns or prints the top of the queue !")
    
class min_priority_queue:
    def __init__(self):
        self.miq = []
        print("Use .help() to see all the functions definitions ")
    def enqueue(self,inpu):
        self.miq.insert(len(self.miq),inpu)
        print(f"{inpu} added to the queue succesfully")
    def dequeue(self,rett=False):
        if rett:
            if len(self.miq)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                m = min(self.miq)
                print(f"{m} element dequeue successfully")
                self.miq.remove(m)
                return m
        else:
            if len(self.miq)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                m = min(self.miq)
                print(f"{m} element dequeue successfully")
                self.miq.remove(m)
    def print_queue(self):
        if len(self.miq)==0:
            print("queue is empty")
        else:
            print("START|",end="")
            for i in self.miq:
                print(f"{i}",end="|")
            print("End")
    def put_multiple(self,n):
        for _ in range(n):
            i = float(input())
            self.enqueue(i)
    def put_list(self,l):
        for ele in l :
            self.enqueue(ele)
    def last_of_queue(self,rett = False):
        if rett:
            return self.miq[-1] 
        else:
            print(f"{self.miq[-1]} is at the last of the queue !")
    def start_of_queue(self,rett = False):
        if rett:
            return self.miq[0] 
        else:
            print(f"{self.miq[0]} is at the start of the queue !")
    def help(self):
        print(".enqueue(value_to_add) - allows you to add element in the queue !")
        print(".dequeue(return_pop_element=False) - allows you to remove the min element of the queue also returns if return true !")
        print(".print_queue() - prints the queue if not empty !")
        print(".put_multiple(n) - allows you to add n elements in the queue !")
        print(".put_list(list) - allows you to add a list of elements into the queue !")
        print(".last_of_queue(return_element(boolean)) - returns or prints the bottom of the queue !")
        print(".start_of_queue(return_element(boolean)) - returns or prints the top of the queue !")

class double_ended_queue:
    def __init__(self):
        self.dqueue = []
        print("Use .help() to see all the functions definitions !")
    def enqueue_start(self,inpu):
        self.dqueue.insert(0,inpu)
        print(f"{inpu} added to the queue succesfully")
    def enqueue_end(self,inpu):
        self.dqueue.insert(len(self.dqueue),inpu)
        print(f"{inpu} added to the queue succesfully")
    def dequeue_start(self,rett=False):
        if rett:
            if len(self.dqueue)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                a  = self.dqueue[0]
                print(f"{a} element dequeue successfully")
                self.dqueue.pop(0)
                return a 
        else:   
            if len(self.dqueue)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                print(f"{self.dqueue[0]} element dequeue successfully")
                self.dqueue.pop(0)
    def dequeue_end(self,rett=False):
        if rett:
            if len(self.dqueue)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                a  = self.dqueue[-1]
                print(f"{a} element dequeue successfully")
                self.dqueue.pop(-1)
                return a 
        else:   
            if len(self.dqueue)==0:
                print("queue is empty ! Cannot dequeue")
            else:
                print(f"{self.dqueue[-1]} element dequeue successfully")
                self.dqueue.pop(-1)
    def print_queue(self):
        if len(self.dqueue)==0:
            print("queue is empty")
        else:
            print("START|",end="")
            for i in self.dqueue:
                print(f"{i}",end="|")
            print("End")
    def put_multiple(self,n,ulta=False):
        if ulta:    
            for _ in range(n):
                i = float(input())
                self.enqueue_start(i)
        else:
            for _ in range(n):
                i = float(input())
                self.enqueue_end(i)
    def put_list(self,l,ulta=False):
        if ulta:
            for ele in l :
                self.enqueue_start(ele)
        else:
            for ele in l :
                self.enqueue_end(ele)
    def last_of_queue(self,rett = False):
        if rett:
            return self.dqueue[-1] 
        else:
            print(f"{self.dqueue[-1]} is at the last of the queue !")
    def start_of_queue(self,rett = False):
        if rett:
            return self.dqueue[0] 
        else:
            print(f"{self.dqueue[0]} is at the start of the queue !")
    def help(self):
        print(".enqueue_start(value_to_add) - allows you to add element in the start of the queue !")
        print(".enqueue_end(value_to_add) - allows you to add element in the end of the queue !")
        print(".dequeue_start(return_pop_element=False) - allows you to remove the start element of the queue also returns if return true !")
        print(".dequeue_end(return_pop_element=False) - allows you to remove the end element of the queue also returns if return true !")
        print(".print_queue() - prints the queue if not empty !")
        print(".put_multiple(n,reverse=False) - allows you to add n elements in the queue !,reverse allows to add from the start of the queue")
        print(".put_list(list,reverse=False) - allows you to add a list of elements into the queue !reverse allows to add from the start of the queue")
        print(".last_of_queue(return_element(boolean)) - returns or prints the bottom of the queue !")
        print(".start_of_queue(return_element(boolean)) - returns or prints the top of the queue !")

class bloomfilter:
    def __init__(self):
        self.filtersize = int(input("please enter the size of the filter:"))
        self.bloom = [0 for _ in range(self.filtersize)]
        print("You can use the .help() method")

    def hash1(self,num):
        return num % self.filtersize

    def hash2(self,num):
        return (2*num+3) % self.filtersize

    def insert(self,num):
        h1 = self.hash1(num)
        h2 = self.hash2(num)
        self.bloom[h1] = 1 
        self.bloom[h2] = 1 
        print(f"{num} inserted successfully !")

    def check(self,num):
        h1 = self.hash1(num)
        h2 = self.hash2(num)
        if self.bloom[h1] == 1 and self.bloom[h2] == 1 :
            print(f"False Positive !\n{num} was probably present ")
        else :
            print(f"{num} is surely not present !")

    def help(self):
        print("You can use the .insert() method to insert into the filter !")
        print("You can use the .check() method to check into the filter !")

class minheap:
    def __init__(self):
        self.heap = []
        self.heap.append("root")
    
    def index_of_parent(self,index):
        return int(index // 2)

    def swap(self,index,parent):
        temp = self.heap[index]
        self.heap[index] = self.heap[parent]
        self.heap[parent] = temp
    
    def add_node(self,val):
        self.heap.append(val)
        if len(self.heap) == 2:
            return 
        index = len(self.heap) - 1 
        parent = self.index_of_parent(index)
        while self.heap[index] < self.heap[parent]:
            self.swap(index,parent)
            index = parent 
            parent = self.index_of_parent(index)
            if index == 1:
                break

    def delete(self):
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        index = 1
        left = index * 2
        right = (index * 2 ) + 1
        while True:
            try:
                if self.heap[index] > self.heap[left]:
                    self.swap(index,left)
                    index = left
                    left = index * 2
                    right = (index * 2 ) + 1
                    if left > len(self.heap) - 1 :
                        break
                    if right > len(self.heap) - 1 :
                        break
                    continue
                if self.heap[index] > self.heap[right]:
                    self.swap(index,right)
                    index = right
                    left = index * 2
                    right = (index * 2 ) + 1
                    if left > len(self.heap) - 1 :
                        break
                    if right > len(self.heap) - 1 :
                        break
                    continue
            except:
                pass
            
    def size_of_heap(self):
        print(f"There are {len(self.heap)} in the Heap !")
    
    def print_heap(self):
        print(self.heap[1:])

    def depth_of_heap(self):
        blockPrint()
        q = queue()
        index = 1
        try:
            while True:
                q.enqueue(self.heap[index])
                index = index * 2
        except:
            pass
        enablePrint()
        return q.size_of_queue()
        
    def peek(self):
        print("Min value is : ",self.heap[1])

class maxheap:
    def __init__(self):
        self.heap = []
        self.heap.append("root")
    
    def index_of_parent(self,index):
        return int(index // 2)

    def swap(self,index,parent):
        temp = self.heap[index]
        self.heap[index] = self.heap[parent]
        self.heap[parent] = temp
    
    def depth_of_heap(self):
        blockPrint()
        q = queue()
        index = 1
        try:
            while True:
                q.enqueue(self.heap[index])
                index = index * 2
        except:
            pass
        enablePrint()
        return q.size_of_queue()
        
    def add_node(self,val):
        self.heap.append(val)
        if len(self.heap) == 2:
            return 
        index = len(self.heap) - 1 
        parent = self.index_of_parent(index)
        while self.heap[index] > self.heap[parent]:
            self.swap(index,parent)
            index = parent 
            parent = self.index_of_parent(index)
            if index == 1:
                break

    def delete(self):
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        index = 1
        left = index * 2
        right = (index * 2 ) + 1
        while True:
            try:
                if self.heap[index] < self.heap[left]:
                    self.swap(index,left)
                    index = left
                    left = index * 2
                    right = (index * 2 ) + 1
                    if left > len(self.heap) - 1 :
                        break
                    if right > len(self.heap) - 1 :
                        break
                    continue
                if self.heap[index] < self.heap[right]:
                    self.swap(index,right)
                    index = right
                    left = index * 2
                    right = (index * 2 ) + 1
                    if left > len(self.heap) - 1 :
                        break
                    if right > len(self.heap) - 1 :
                        break
                    continue
            except:
                pass
            
    def size_of_heap(self):
        print(f"There are {len(self.heap)} in the Heap !")
    
    def print_heap(self):
        print(self.heap[1:])

    def peek(self):
        print("Max value is : ",self.heap[1])

class BinarySearchTree:
    def __init__(self,val):
        self.root = self.Node(val)

    class Node:
        def __init__(self,data):
            self.data = data 
            self.left = None 
            self.right = None 

    def add_node(self,val):
        curr = self.root 
        while True:
            if val <= curr.data :
                if not curr.left :
                    curr.left = self.Node(val)
                    break
                else:
                    curr = curr.left 
                    continue
            if val > curr.data :
                if not curr.right :
                    curr.right = self.Node(val)
                    break
                else:
                    curr = curr.right 
                    continue

    def in_order_traversal(self):
        s = deque()
        curr = self.root
        while s or curr :
            if curr:
                s.append(curr)
                curr = curr.left
            else:
                curr = s.pop()
                print(curr.data,end=" ")
                curr = curr.right
        print("\n")

    def Maxi(self,treeee):
        curr = treeee
        prev = None 
        while True :
            if curr.left :
                prev = curr
                try:
                    curr = curr.left 
                except:
                    pass
            else:
                if prev:
                    prev.left = None 
                else:
                    treeee = None 
                break
        return curr

    def height(self):
        q=deque()
        q.append(self.root)
        ht=0
        while q :
            size=len(q)
            while size>0:
                curr=q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                size=size-1
            ht=ht+1
        print("Height of tree is :",ht) 

    def delete_node(self,val):
        curr = self.root 
        while True :
            if val == curr.data :
                if not curr.left and not curr.right:
                    if right:
                        prev.right = None 
                    if left:
                        prev.left = None 
                    break

                if curr.left and curr.right :
                    tree_subtree_left = curr.left
                    tree_subtree_right = curr.right
                    if right:
                        l = self.Maxi(tree_subtree_right)
                        prev.right = l
                        if not l.left or l.right :
                            pass
                        else:
                            l.right = tree_subtree_right
                        l.left = tree_subtree_left
                        break
                    if left:
                        l = self.Maxi(tree_subtree_right)
                        prev.left = l
                        if not l.left or l.right :
                            pass
                        else:
                            l.right = tree_subtree_right
                        l.left = tree_subtree_left
                        break 

                else:
                    if right:
                        prev.right = None 
                    if left:
                        prev.left = None 
                    if curr.left :
                        to_add = curr.left
                        curr.left = None 
                    else:
                        to_add = curr.right
                        curr.right = None  
                    self.add_node(to_add.data)
                    break

            if val > curr.data :
                prev = curr 
                curr = curr.right
                right = True 
                left = False

            if val < curr.data :
                right = False 
                left = True
                prev = curr 
                curr = curr.left

class circularlinklist:
    def __init__(self,val):
        self.head = self.node(val)
        self.head.next = self.head

    class node:
        def __init__(self,val,next=None):
            self.data = val 
            self.next = next

    def add_start(self,val):
        i = self.head
        temp = self.head
        while True:
            if i.next == self.head:
                new_node = self.node(val)
                i.next = new_node
                self.head = new_node 
                new_node.next = temp
                break
            i = i.next
        
    def add_end(self,val):
        i = self.head
        temp = self.head
        while True:
            if i.next == self.head:
                new_node = self.node(val)
                i.next = new_node
                new_node.next = temp
                break
            i = i.next

    def print_link_list(self):
        i  = self.head 
        print("Head->",end="")
        n=0
        while i:
            n+=1
            print(i.data,end="->")
            if i.next == self.head:
                break
            i = i.next
        print("Head")

    def delete_start(self):
        to_point = self.head.next
        i = self.head
        while True:
            if i.next == self.head:
                i.next = to_point
                self.head = to_point
                break
            i = i.next 

    def delete_end(self):
        temp = self.head 
        i = self.head
        prev = None
        while True:
            if i.next == temp:
                prev.next = temp
                del i 
                break
            prev = i 
            i = i.next 

    def help(self):
        print("""
        Circular Link List with Python 
        You can use the Circular Link list as follows 
        from datastructure import circularlinklist
        cll = circularlinklist(val) -- initialize linklist with head val 
        cll.add_start(val) -- Adds a node to the start of the  circular link list 
        cll.add_start(end) -- Adds a node to the end of the circular link list 
        cll.delete_start() -- Deletes a node from the start of the circular link list 
        cll.delete_end() -- Deletes a node from the end of the circular link list 
        cll.print_link_list() -- Prints the Link list 
        """)

class linklist:
    def __init__(self,root_val):
        self.root = self.node(root_val)
    
    class node:
        def __init__(self,data,next_node = None):
            self.data = data
            self.next_node = next_node
    
    def add_node_start(self,val):
        n = self.node(val,self.root) 
        self.root = n   
    
    def print_link_list(self):
        if self.root is None :
            print("LL empty !")
        i  = self.root 
        while i:
            print(i.data,end="->")
            i = i.next_node
        print("End\n")
    
    def add_node_end(self,val):
        i = self.root 
        while i:
            if i.next_node is None:
                i.next_node = self.node(val)
                break
            i = i.next_node
    
    def delete_start(self):
        i = self.root 
        self.root = i.next_node
        del i 
    
    def delete_end(self):
        i = self.root
        while i:
            if i.next_node is None:
                prev.next_node = None 
                del i 
                break
            prev = i 
            i = i.next_node
    
    def delete_between(self,val):
        i = self.root
        while i :
            if i.data == val :
                prev.next_node = i.next_node
                del i 
                break
            prev = i 
            i = i.next_node
    
    def reverse_link_list(self):
        current = self.root
        prev = None
        while current :
            next_node = current.next_node
            current.next_node = prev
            prev = current
            if next_node is None:
                self.root = current 
            current = next_node
    
    def help(self):
        print("""- You can intialize the link list by #from slinklist import linklist and then s = linklist(rootval)
  - You can use the add_node_start(val) to add value to the start of the link list
  - You can use the add_node_end(val) to add value to the end of the link list 
  - You can use the print_lisk_list() to print the link list 
  - You can use the delete_start() to delete the node from start of linklist 
  - You can use the delete_end() to delete the node from end of linklist 
  - You can use the delete_between(val) to delete the node in between of linklist 
  - You can use the reverse_link_list() to reverse the link list """)

# Undirected Graph           
class udgraph:
    def __init__(self):
        self.d = {}

    def add_node(self,node):
        if node in self.d.keys():
            print("Collision Trying to add the same node twice !")
            return 
        self.d[node] = []

    def add_edge(self,node,another_node):
        if self.check(node,another_node):
    
            self.d[node].append(another_node)
            self.d[another_node].append(node)

    def delete_edge(self,node,another_node):
        if self.check(node,another_node):
            self.d[node].remove(another_node)
            self.d[another_node].remove(node)

    def check(self,node,another_node):
        if node not in self.d.keys():
            print("first Node not in graph , please add node in graph first !")
            return None
        if another_node not in self.d.keys():
            print("Second Node not in graph , please add node in graph first !")
            return None 
        return True

    def delete_node(self,node):
        a =[]
        for i in self.d[node]:
            a.append(i)
        for i in a:
            self.delete_edge(node,i) 
        del self.d[node]

    def degree_node(self,node):
        print(len(self.d[node]))

    def find_isolated_nodess(self,node= None):
        isolated_nodes = []
        for i,j in self.d.items():
            if not j:
                isolated_nodes.append(i)
        if node:
            if node in isolated_nodes:
                print(f"The node {node} is isolated ! add edges ")
            else:
                print("Not Isolated")
        else:
            print("isolated nodes :")
            for i in isolated_nodes:
                print(i)

    def show_all_nodes(self):
        for yo in self.d.keys():
            print(f"Node {yo}")

    def bfs(self,start):
        visited = []
        queue = []
        queue.append(start)
        visited.append(start)
        while queue:
            print(visited)
            s = queue.pop(0)
            print(s,end=" ")
            for node in self.d[s] :
                if node in visited:
                    pass
                else:
                    queue.append(node)
                    visited.append(node)

    def show_all_edges(self):
        for i,j in self.d.items():
            print(f"Edges from Node {i}")
            for edge in j :
                print(i,"==>",edge)
            print("")

    def show_edges_from_node(self,node):
        print(f"Edges from Node {node}")
        for i in self.d[node]:
            print(node,"==>",i)

    def find_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.d
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_paths(vertex, 
                                               end_vertex, 
                                               path)
                for p in extended_path:
                    paths.append(p)
        return paths
    
# Directed Graph
class dgraph:
    def __init__(self):
        self.d = {}

    def add_node(self,node):
        if node in self.d.keys():
            print("Node already exists !")
            return 
        self.d[node] = []

    def add_edge(self,node,another_node):
        if node not in self.d.keys() or another_node not in self.d.keys():
            print("Node Not in Graph Please add node first")
            return 
        self.d[node].append(another_node)
        print(f"Edge from Node {node} to Node {another_node} added succesfully !")

    def delte_node(self,node):
        for i in self.d.keys():
            if node in self.d[i]:
                self.d[i].remove(node)
        del self.d[node]

    def delete_edge(self,node,another_node):
        if node not in self.d.keys() or another_node not in self.d.keys():
            print("Node Not in Graph Please add node first")
            return
        self.d[node].remove(another_node)

    def show_all_nodes(self):
        print("Nodes in the graph are :")
        for i in self.d.keys():
            print("Node ",i)
      
    def show_all_edges(self):
        for i,j in self.d.items():
            print("Node ",i)
            for edges in j:
                print(i," ==> ",edges)
            print("")

    def show_edges_from_a_node(self,node):
        for edges in self.d[node]:
                print(node," ==> ",edges)
    
    def bfs(self,start):
        visited = []
        queue = []
        queue.append(start)
        visited.append(start)
        while queue:
            s = queue.pop(0)
            print( s , end=" ")
            for node in self.d[s]:
                if node in visited:
                    pass 
                else:
                    visited.append(node)
                    queue.append(node)

    def find_path(self,node,another_node,path=[]):
        graph = self.d
        path = path + [node]
        if node == another_node:
            return [path]
        if node not in graph:
            return []
        paths = []
        for vertex in graph[node]:
            if vertex not in path:
                extended_path = self.find_path(vertex,another_node,path)
                for p in extended_path:
                    paths.append(p)
        return paths

# Directed Weighted Graph
class dweightedgraph:
    def __init__(self):
        self.d = {}

    def add_node(self,node):
        if node in self.d.keys():
            print("Node already exists !")
            return 
        self.d[node] = []

    def add_edge(self,node,another_node,weight):
        if node not in self.d.keys() or another_node not in self.d.keys():
            print("Node Not in Graph Please add node first")
            return 
        self.d[node].append((another_node,weight))
        print(f"Edge from Node {node} to Node {another_node} with {weight} added succesfully !")

    def show_all_edges(self):
        for i,j in self.d.items():
            print("Node ",i)
            for edges in j:
                print(i," ==> ",edges[0]," weight ==> ",edges[1])
            print("")

    def show_edges_from_a_node(self,node):
        for edges in self.d[node]:
                print(node," ==> ",edges[0]," weight ==> ",edges[1])

    def delte_node(self,node):
        for i,j in self.d.items():
            for edges in j:
                if edges[0] == node:
                    self.d[i].remove(edges)
        del self.d[node]
            
    def delete_edge(self,node,another_node):
        if node not in self.d.keys() or another_node not in self.d.keys():
            print("Node Not in Graph Please add node first")
            return

        for edges in self.d[node]:
            if edges[0] == another_node:
                self.d[node].remove(edges)
                break

    def show_all_nodes(self):
        print("Nodes in the graph are :")
        for i in self.d.keys():
            print("Node ",i)
      
    def dijkstras_algorithm(self,start,end):
        inf = sys.maxsize
        node_data = {}
        for i in self.d.keys():
            node_data[i] = {'cost':inf,'pred':[]}   
        node_data[start]['cost'] = 0  
        visited = []
        temp = start 
        nextt = None  
        minn = inf
        for i in range(len(self.d.keys())):
            if temp not in visited:
                visited.append(temp)
                for j in range(len(self.d[temp])):
                    a = self.d[temp][j][0]
                    if a not in visited:
                        cost = node_data[temp]['cost'] + self.d[temp][j][1]
                        if cost < node_data[a]['cost']:
                            node_data[a]['cost'] = cost
                            node_data[a]['pred'] = node_data[temp]['pred'] + [temp]
                        if cost < minn :
                            minn = cost 
                            nextt = a
            temp = nextt            
        print("Shortest Distance:",node_data[end]['cost'])
        print("Shortest Path: ",node_data[end]['pred']+[end])