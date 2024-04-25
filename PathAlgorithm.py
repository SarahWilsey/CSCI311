from WeightedGraph import WeightedGraph
import sys

def prim(graph):
    # Initialize variables
    edgeSet = []             # Initialize edgeSet
    mst = []                 # Minimum spanning tree
    visitedNodes = set()     # Set of visited nodes
    firstNode = 0            # Start node
    visitedNodes.add(firstNode) # Add start node to visited nodes
    nodeCount = graph.getSize() # Total number of nodes

   
    # Create initial edge set with edges connected to the start node
    for nearest in range(nodeCount):
        distance = graph.getDistance(firstNode, nearest)
        if distance != -1: # If there is a connection
            edgeSet.append((distance, firstNode, nearest)) # Add edge to edgeSet
            # #3 visitedNodes = {nearest}
            #if distance <  graph.getDistance(1, nearest):
                #edgeSet.append((distance, firstNode, nearest)) # Add edge to edgeSet
            #else: 
                #distance = graph.getDistance(1, nearest)
                #edgeSet.append((distance, 1, nearest))
                # #1 the commented out section is to find the closest node, but it doesnt work.
   
    # While there are unvisited nodes
    while len(visitedNodes) < nodeCount:
        infinity = sys.maxsize()
        minWeightEdge = None # Initialize edge with minimum weight
        minWeight = infinity # Initialize minimum weight
       
        # Find edge with minimum weight in the edge set
        for edge in edgeSet:
            if edge[0] < minWeight:
                minWeight = edge[0] # Update minimum weight
                minWeightEdge = edge # Update edge with minimum weight
       
        edgeSet.remove(minWeightEdge) # Remove edge from edge set
       
        distance = minWeightEdge[0]
        node1 = minWeightEdge[1]
        node2 = minWeightEdge[2]

        # If the second node of the edge is not visited, add it to the MST
        if node2 not in visitedNodes:
            mst.append([node1, node2]) # Add edge to MST
            visitedNodes.add(node2)     # Mark second node as visited

        # Update edge set with new edges from the newly visited node
        for nearest in range(nodeCount):
            distance = graph.getDistance(node2, nearest)
            if distance != -1:
                if nearest not in visitedNodes:
                    edgeSet.append((distance, node2, nearest))
               
    return mst

# Calculate total weight of MST
def totalWeight(mst, graph):
    totalWeight = 0
    for edge in mst:
        (node1, node2) = edge
        #node1 = edge[0]
        #node2 = edge[1]
        totalWeight = totalWeight + graph.getDistance(node1, node2)
    return totalWeight
    
# Get edge names of MST
def edgeNames(mst, graph):
    edgeNames = []
    for edge in mst:
        (node1, node2) = edge
        #node1 = edge[0]
        #node2 = edge[1]
        edgeNames.append([graph.getNodeName(node1), graph.getNodeName(node2)])
    return edgeNames

# Example usage:
def main():
    exampleGraph = WeightedGraph("example.txt")
    mst = prim(exampleGraph)
    print("MST:", mst)
    print("Total Weight:", totalWeight(mst, exampleGraph))
    print("Edge Names:", edgeNames(mst, exampleGraph))
    print("mst array:", mst[1][0])
    
main()
