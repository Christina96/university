"""
Read a file from command prompt, create a dictionary with the parts of file and
finding the trusses between neighbors.
"""

import argparse  # read the file


def open_file(file_name):
    """Open the file and create a dictionary with acme as a key and list with
    neighbours"""
    adjacency_list = {}
    with open(file_name) as graph:  # open the file
        for line in graph:
            parts = line.split(' ')
            parts[-1] = parts[-1].strip()
            parts = [int(i) for i in parts]
            point = parts[0] in adjacency_list
            if point:
                # create a dictionary with key acme and a list with neighbours
                adjacency_list[parts[0]].append(parts[1])
            else:
                adjacency_list[parts[0]] = [parts[1]]
            point = parts[1] in adjacency_list
            if point:
                adjacency_list[parts[1]].append(parts[0])
            else:
                adjacency_list[parts[1]] = [parts[0]]
    return adjacency_list.copy()


def find_trusses(adjacency_list, number_of_trusses):
    """Find the trusses from the list"""
    copy_list = adjacency_list.copy()  # copy from Adjacency List
    change = True
    while change:  # start to find the trusses
        for acme, neighbours in list(copy_list.items()):
            # two loops for each pair
            copy_list = del_same_acme(acme, neighbours,
                                      copy_list, number_of_trusses)
        # Check if the adjacency list has changed with the copy.
        # (PS: the adjacency list changes at each iteration
        # with the values of copyList)
        copy_list_2 = sorted(copy_list.items())
        sorted_adjacency_list = sorted(adjacency_list.items())
        if copy_list_2 == sorted_adjacency_list:
            change = False
        else:
            adjacency_list = copy_list.copy()
            change = True
    return adjacency_list


def del_same_acme(acme1, neighbours1, copy_list, number_of_trusses):
    """Delete the same Acme from list"""
    for acme2, neighbours2 in list(copy_list.items()):
        if acme1 != acme2:  # we don't want to see the same acme
            total1 = set(neighbours1)  # conversion into sets
            total2 = set(neighbours2)
            intersection = total1 & total2  # the intersection of two sets
            if len(intersection) < number_of_trusses - 2:  # condition testing
                try:  # remove if exists
                    copy_list[acme1].remove(acme2)
                except ValueError:
                    pass
                except KeyError:
                    pass
                try:  # remove if exists
                    copy_list[acme2].remove(acme1)
                except ValueError:
                    pass
        if not copy_list[acme2]:
            del copy_list[acme2]
    return copy_list


def output(adjacency_list):
    """Create the output"""
    trusses = {}  # preparing output
    count = 0
    for acme, neighbours in adjacency_list.items():
        trusses[count] = [acme]
        trusses[count].extend(neighbours)
        trusses[count] = sorted(trusses[count])
        count += 1
    trusses_set = set()
    for line in trusses.values():
        trusses_set.add(tuple(sorted(line)))
    total_trusses = [x for x in trusses_set]
    total_trusses.sort()
    return total_trusses


def main():
    """Main of the project"""
    parser = argparse.ArgumentParser()
    # name for file
    parser.add_argument("file_name", help="Name of input file")
    # give a name and default number for number
    parser.add_argument("number_of_trusses", help="Number of trusses",
                        type=int, default=3)
    args = parser.parse_args()
    number_of_trusses = args.number_of_trusses
    adjacency_list = open_file(args.file_name)
    adjacency_list = find_trusses(adjacency_list, number_of_trusses)
    total_trusses = output(adjacency_list)
    for values in total_trusses:  # show results
        print(values)


if __name__ == "__main__":
    main()
