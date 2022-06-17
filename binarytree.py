
from collections import deque
class BinaryTree:
    def __init__(self,data):
        self.root = self.tree_node(data)

    class tree_node:
        def __init__(self,data,left=None,right=None):
            self.data = data 
            self.left = left 
            self.right = right 

    def level_order_traversal(self):
        q = deque()
        q.append(self.root)
        while q :
            curr = q.popleft()
            print(curr.data,end=" ")
            if curr.left:
                q.append(curr.left)
            if curr.right :
                q.append(curr.right)

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

    def post_order_traversal(self):
        s = deque()
        q = deque()
        q.append(self.root)
        while q:
            curr = q.pop()
            s.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        while s:
            print(s.pop(),end=" ")
        
    def pre_order_traversal(self):
        s= deque()
        s.append(self.root)
        while s :
            curr = s.pop()
            print(curr.data)
            if curr.right:
                s.append(curr.right)
            if curr.left:
                s.append(curr.left)    
    
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

    def insert_auto(self,data):
        curr = self.root
        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left = self.tree_node(data)
                    break
                else:
                    curr = curr.left 
            if data > curr.data:
                if curr.right is None :
                    curr.right = self.tree_node(data)
                    break
                else:
                    curr = curr.right

    def insert_right(self,data):
        curr = self.root.right
        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left = self.tree_node(data)
                    break
                else:
                    curr = curr.left 
            if data > curr.data:
                if curr.right is None :
                    curr.right = self.tree_node(data)
                    break
                else:
                    curr = curr.right

    def insert_left(self,data):
        curr = self.root.left
        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left = self.tree_node(data)
                    break
                else:
                    curr = curr.left 
            if data > curr.data:
                if curr.right is None :
                    curr.right = self.tree_node(data)
                    break
                else:
                    curr = curr.right
