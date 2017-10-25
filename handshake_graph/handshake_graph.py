"""
Handshakes Graph Construction Problem
author: Christina Chaniotaki
"""
import random as rd
import networkx as nx
import matplotlib.pyplot as plt


def handshakes_graph(handshakes):
    """
    Creates the handshakes graph by using NetworkX
    :param handshakes: list with handshakes for each person including
    Melania Trump
    :return: a NetworkX graph with handshakes
    """
    graph = nx.Graph()
    length = len(handshakes)
    # Add length + 1 nodes in the graph because we have Donald Trump too
    graph.add_nodes_from([i for i in range(0, length + 1)])
    for person in range(0, length):
        for handshake in range(0, handshakes[person]):
            check = True
            while check:
                # a random person who had handshake with person
                handshake_person = rd.randint(0, length)
                if handshake_person == length:
                    graph.add_edge(person, handshake_person)
                    check = False
                elif handshake_person \
                        not in list(graph.adj[person]) \
                        and len(list(graph.adj[person])) < \
                        handshakes[handshake_person]:
                    graph.add_edge(person, handshake_person)
                    check = False
    return graph


def main():
    """ The beginning of the program that calls the functions."""
    handshakes = [i for i in range(0, 8)]
    graph = handshakes_graph(handshakes)
    plt.figure(figsize=(16, 16))
    nx.draw_circular(graph, arrows=True, node_color='#A0CBE2', width=1,
                     with_labels=True)
    plt.show()


if __name__ == '__main__':
    main()
