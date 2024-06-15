class Node:
    def __init__(self, name: str, killer: str = None, next_node: 'Node' = None):
        self.name = name
        self.killer = killer
        self.next = next_node
    

    
    