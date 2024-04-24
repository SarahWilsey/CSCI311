from WeightedGraph import WeightedGraph
from PathAlgorithm import prim, totalWeight, edgeNames

def test_prim(graph):
    print("***** Testing prim *****")
    print("The edges for the graph in example.txt are given by the following edges:")
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
        print(f"{edge[0]} {edge[1]}")

if __name__ == "__main__":
    example_graph = WeightedGraph("example.txt")

    # Test Prim's Algorithm
    test_prim(example_graph)

    # Get MST using Prim's Algorithm
    mst = prim(example_graph)

    # Test totalWeight function
    test_totalWeight(example_graph, mst)

    # Test edgeNames function
    test_edgeNames(example_graph, mst)
    
    example_graph = WeightedGraph("example.txt")
    mst = prim(example_graph)
    print("MST:", mst)
    print("Total Weight:", totalWeight(mst, example_graph))
    print("Edge Names:", edgeNames(mst, example_graph))    

