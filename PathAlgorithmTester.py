from WeightedGraph import WeightedGraph
from PathAlgorithm import *

def test_prim(graph):
    print("***** Testing prim *****")
    mst = prim(graph)
    for edge in mst:
        print(f"{edge[0]} {edge[1]}")
        

def test_totalWeight(graph, mst):
    print("\n***** Testing totalWeight *****")
    total_weight = totalWeight(mst, graph)
    print(f"The total weight of the MST is: {total_weight}")

def test_edgeNames(graph, mst):
    print("\n***** Testing edgeNames *****")
    print("The names of the edges in the MST are:")
    edge_names = edgeNames(mst, graph)
    for edge in edge_names:
        print(edge[0],edge[1])

def main():
    exGraph = WeightedGraph("example.txt")
    exGraph2 = WeightedGraph("graphex.txt")
    

    # Test Prim's Algorithm
    print("The edges for the graph in example.txt are given by the following edges:")    
    test_prim(exGraph)
    print()
    print("The edges for the graph in graphex.txt are given by the following edges:")  
    test_prim(exGraph2)

    # Get MST using Prim's Algorithm
    mst = prim(exGraph)
    mst2 = prim(exGraph2)

    # Test totalWeight function
    test_totalWeight(exGraph, mst)
    print("example.txt")    
    test_totalWeight(exGraph2, mst2)
    print("graphex.txt") 

    # Test edgeNames function
    test_edgeNames(exGraph, mst)
    print("The edge names of example.txt") 
    test_edgeNames(exGraph2, mst2)
    print("The edge names of graphex.txt") 
    
    print("\n***** Prints MST, Total Weight, and Edge Names of Example.txt*****")
    exGraph = WeightedGraph("example.txt")
    mst = prim(exGraph)
    print("MST:", mst)
    print("Total Weight:", totalWeight(mst, exGraph))
    print("Edge Names:", edgeNames(mst, exGraph))  
    print("-"*50)
    print("\n***** Prints MST, Total Weight, and Edge Names of Graphex.txt*****")
    exGraph = WeightedGraph("graphex.txt")
    mst = prim(exGraph)
    print("MST:", mst)
    print("Total Weight:", totalWeight(mst, exGraph))
    print("Edge Names:", edgeNames(mst, exGraph))    
        
    
main()
