from functools import wraps


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None

    def ensure_node_exists(func):
        @wraps(func)
        def wrapper(self, index, *args, **kwargs):
            n = self.head
            pos = 0
            while(n != None and pos != index):
                pos += 1
                n = n.next
            if n:
                return func(self, index, *args, **kwargs)
                
            print("Index not present")        

        return wrapper
    
    def __repr__(self):
        n = self.head
        nodes = []
        while(n):
            nodes.append(str(n.data))
            n = n.next
        return f"[{', '.join(nodes)}]"
 
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    
    @ensure_node_exists
    def update(self, index, value):
        n = self.head
        pos = 0
        while(pos != index):
            pos += 1
            n = n.next
        
        n.data = value
