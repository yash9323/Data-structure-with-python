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
            


            


                

             
        