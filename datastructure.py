import os,sys

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
    
