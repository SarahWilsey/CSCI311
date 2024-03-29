# WeightedGraph.py
#
# Created by: Sarah Wilsey and Tess Adams
# Date: 03/29/2024
#
# This is the WeightedGraph class. This class conatins methods 
# that makes positive-weight graph objects.
#
# WeightedGraph class.
class WeightedGraph:
    # constructor
    def __init__(self, filename):
        # instance variables
        self.adjMatrix = []
        self.nodeNames = []
        self.size = 0
        
        # open file for reading
        file = open(filename, 'r') 
        lines = file.readlines()
        nodes = lines[0].strip().split(',')
        self.nodeNames = nodes
        self.size = len(nodes)
        
        # loop through to set values to -1
        for index in range(self.size):
            row = [-1] * self.size
            self.adjMatrix.append(row)
            
        # loop through to populate matrix   
        for line in lines[1:]:
            parts = line.strip().split(',')
            
            node1 = parts[0]
            node2 = parts[1]
            weight = int(parts[2])

            i = nodes.index(node1)
            k = nodes.index(node2)
            self.adjMatrix[i][k] = int(weight)
            self.adjMatrix[k][i] = int(weight)
            
        # set value to 0 if nodes are the same.       
        for i in range(self.size):
            self.adjMatrix[i][i] = 0
            
    # Get distance method. Returns the length of the edge between i and k,
    #-1 if it does not exist, and 0 if i and k are the same.
    def getDistance(self, i, k):
        return self.adjMatrix[i][k]
    
    # Direct link method. Returns True if an edge exists between i and k
    # or if i and k are the same, and False otherwise.
    def directLink(self, i, k):
        
        # to handle out of index error
        if i < 0 or i>= self.size or k < 0 or k >= self.size:
            return False
        # if i and k are the same or an edge exists
        elif self.adjMatrix[i][i] or self.adjMatrix[i][k] != -1:
            return True
        #else
        else:
            return False
    
    # Get node name method. Returns the name of the node associated with with 
    # the index.
    def getNodeName(self, i):
        return self.nodeNames[i]

    # Returns the number of nodes in the graph.
    def getSize(self):
        return self.size
    
    # DONT FORGET TO DELETE BEFORE SUBMISSION!!!!
    def printMatrix(self):
        print("Weighted adjacency Matrix:")
        for row in self.adjMatrix:
            print(" ".join(str(cell) for cell in row))
