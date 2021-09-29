"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old = head;
        if old == None:
            return old
        newN = Node(old.val, None,None)
        self.visited[old] = newN
        
        def helper(node):
            if node:
                if node in self.visited:
                    return self.visited[node]
                else:
                    newN = Node(node.val, None, None)
                    self.visited[node] = newN
                    return self.visited[node]
            
        while old != None:
            newN.next = helper(old.next)
            newN.random = helper(old.random)
            old = old.next
            newN = newN.next
        return self.visited[head]
            
            
            
            
        
