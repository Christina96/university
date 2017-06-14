"""
The programm open the file with the fragments and creates the  synthesis of a
chain of unknown DNA.
author: Christina Chaniotaki
"""
import argparse  # The library for Parser command-line


def open_file(filename):
    """
    Open the file with the fragments and create a list
    :param filename: the file with fragments
    :return: A list with fragments
    """
    fragments = []
    with open(filename) as piece:
        for line in piece:
            parts = line.split(' ')
            parts[-1] = parts[-1].strip()
            fragments.append(parts[0])
    return fragments


def create_graph(fragments):
    """
    Create the graph with the fragments
    :param fragments: A list with fragments
    :return: The graph with the fragments and the starting node
    """
    k = len(fragments[0])
    graph = {}
    for fragment in fragments:
        # The directed graph with nodes as keys and their neighbors in list
        part1 = fragment[0:k - 1]
        part2 = fragment[1:]
        if part1 not in graph:
            graph[part1] = [part2]
            starting_node = part1
        else:
            if part2 not in graph[part1]:
                graph[part1].append(part2)
    return graph, starting_node


def cycle_finding(starting_node, graph):
    """
    Finds the dna cycle
    :param starting_node: the starting node from the graph
    :param graph: The graph with the fragments
    :return: The changed graph and the circular path
    """
    circular_path = [starting_node]
    # The node that we use to find the next node by using the graph
    next_acme = graph[starting_node][0]
    for i in range(len(graph[starting_node])):
        # Delete the node from graph
        if graph[starting_node][i] == next_acme:
            del graph[starting_node][i]
            break
    if not graph[starting_node]:
        # Delete the node from graph if node has not neighbor
        del graph[starting_node]
    circular_path.append(next_acme)  # Add the node in circularPath list
    while starting_node != next_acme:
        # I do the same thing using instead of the variable starting_node the
        # variable neighbor until it reaches the node that is the same with
        # starting node
        neighbor = graph[next_acme][0]
        if neighbor != starting_node:
            circular_path.append(neighbor)
        for i in range(len(graph[next_acme])):
            if graph[next_acme][i] == neighbor:
                del graph[next_acme][i]
                break
        if not graph[next_acme]:
            del graph[next_acme]
        next_acme = neighbor
    return graph, circular_path


def create_sequence_list(graph, starting_node):
    """
    Creates the sequence list from the graph
    :param graph: The graph with the fragments
    :param starting_node: he starting node from the graph
    :return: The sequence list
    """
    start = 0
    while graph:  # While the graph is not empty
        if start == 0:  # Runs only the first time
            (graph, auxiliary_cycle) = cycle_finding(starting_node, graph)
            sequence_list = auxiliary_cycle
            start += 1
        else:
            position = 0  # Save the location of the new starting node
            for node in sequence_list:
                if node in graph.keys():
                    # The new starting node is a node that i visited but has
                    # and other neighbor
                    starting_node = node
                    break
                position += 1
            (graph, auxiliary_cycle) = cycle_finding(starting_node, graph)
            # Insert the new following in sequenceList
            for node in auxiliary_cycle:
                sequence_list.insert(position, node)
                position += 1
    return sequence_list


def output(sequence_list):
    """
    The string with the dna
    :param sequence_list: List with sequence from dna
    """
    dna = ""
    for_start = 0
    # Remove the same piece and save the result as a string
    for node in sequence_list:
        if for_start == 0:
            # Runs only the first time
            dna = node[-1]
            for_start += 1
        else:
            dna += node[-1]
    print(dna)


def main():
    """Main of the project"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="name of input file")
    args = parser.parse_args()
    fragments = open_file(args.filename)
    graph, starting_node = create_graph(fragments)
    sequence_list = create_sequence_list(graph, starting_node)
    output(sequence_list)


if __name__ == "__main__":
    main()
