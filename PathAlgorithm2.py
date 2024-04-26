from WeightedGraph import WeightedGraph
import sys

def prim(graph):
    size = graph.getSize()
    nearest = [0] * size
    distance = [0] * size
    smallest = sys.maxsize
    smallestIndex = 0
    nodeSet = [False] * size
    edgeSet = []
               
    for i in range(size - 1):
        edgeSet.append([0,0])

    for i in range(size - 1):
        if i > 0:
            distance[i] = graph.getDistance(0, i)
        else:
            distance[0] = -1
        nodeSet[i] = False
        nearest[i] = 0

    nodeSet[0] = True

    for j in range(size - 1):
        smallest = sys.maxsize
        # Find node v closest to nodeSet using distance
        for i in range(size):
            if distance[i] < smallest and not nodeSet[i] and distance[i] > 0:
                smallest = distance[i]
                smallestIndex = i

        # Add edge from v to nearest[v] to edgeSet
        edgeSet[j][0] = nearest[smallestIndex]
        edgeSet[j][1] = smallestIndex
        nodeSet[smallestIndex] = True

        # Update distance[v] to indicate v is in nodeSet
        distance[smallestIndex] = -1

        # Update distances from other nodes to v, if shorter
        for i in range(size):
            # if matrix[i][smallestIndex] is smaller than distance[i], shorter path is found
            if not nodeSet[i] and (graph.getDistance(i, smallestIndex) < distance[i] or distance[i] == -1):
                distance[i] = graph.getDistance(i, smallestIndex)
                nearest[i] = smallestIndex

    return edgeSet

def totalWeight(mst, graph):
    totalWeight = 0
    for edge in mst:
        node1, node2 = edge
        totalWeight += graph.getDistance(node1, node2)
    return totalWeight

def edgeNames(mst, graph):
    edgeNames = []
    for edge in mst:
        node1, node2 = edge
        edgeNames.append([graph.getNodeName(node1), graph.getNodeName(node2)])
    return edgeNames

def main():
    exampleGraph = WeightedGraph("example.txt")
    mst = prim(exampleGraph)
    print("MST:", mst)
    print("Total Weight:", totalWeight(mst, exampleGraph))
    print("Edge Names:", edgeNames(mst, exampleGraph))

main()
