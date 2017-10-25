"""
Handshakes Graph Construction Problem
author: Christina Chaniotaki
"""
import operator
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
    sorted_person_list = sort_people(handshakes)
    graph = nx.Graph()
    length = len(handshakes)
    # Add length + 1 nodes in the graph because we have Donald Trump too
    graph.add_nodes_from([i for i in range(0, length + 1)])
    for person in sorted_person_list:
        for handshake in range(0, handshakes[person]):
            if handshakes[person] == len(list(graph.adj[person])):
                break
            check = True
            while check:
                # a random person who had handshake with person
                handshake_person = rd.randint(0, length)
                if handshake_person == length and handshake_person not in list(
                        graph.adj[person]) and handshake_person != person:
                    graph.add_edge(person, handshake_person)
                    check = False
                elif handshake_person not in list(graph.adj[person]) \
                        and len(list(graph.adj[handshake_person])) < \
                                handshakes[handshake_person] \
                        and handshake_person != person:
                    graph.add_edge(person, handshake_person)
                    check = False
    return graph


def sort_people(handshakes):
    """
    Sort the people by their handshakes
    :param handshakes: list we the handshakes for each person
    :return: sorted people by the number of handshakes
    """
    people_handshakes = {}
    for i in range(0, len(handshakes)):
        people_handshakes[i] = handshakes[i]
    sorted_handshakes_person = sorted(people_handshakes.items(),
                                      key=operator.itemgetter(1), reverse=True)
    sorted_person_list = []
    for i in sorted_handshakes_person:
        sorted_person_list.append(i[0])
    return sorted_person_list


def main():
    """" The beginning of the program that calls the functions."""
    handshakes = [i for i in range(0, 101)]
    graph = handshakes_graph(handshakes)
    nx.draw_circular(graph, arrows=True, node_color='#A0CBE2', width=1,
                     with_labels=True)
    plt.show()


if __name__ == '__main__':
    main()
