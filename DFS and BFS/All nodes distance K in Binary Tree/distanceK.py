#Problem Statement:Given the root of a binary tree, the value
# of a target node target, and an integer k, return an array of the values
# of all nodes that have a distance k from the target node. You can return 
# the answer in any order.

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Solution:
#First make a adjacency list graph out of the Binary Tree
#Then From the target Node we travesrse to the the list and return elements at K      
def distanceK(self, root: TreeNode, target: TreeNode, k: int):
    if not root:
        return []
    
    graph = collections.defaultdict(list)
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()

        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node)
            queue.append(node.left)
        
        if node.right:
            graph[node].append(node.right)
            graph[node.right].append(node)

            queue.append(node.right)
    
    results =[]

    visited =set([target])
    queue = collections.deque([(target,0)])

    while queue:
        node,distance = queue.popleft()
        if distance ==k:
            results.append(node.val)
        else:
            for edge in graph[node]:
                if edge not in visited:
                    visited.add(edge)
                    queue.append((edge,distance+1))
    
    return results
