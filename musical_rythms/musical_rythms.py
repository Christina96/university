"""
Finds the musical rhythm checks if it exists in the json file and if it is then
displays the description. If it is also an Euclidean String or Reverse
Euclidean String prints an appropriate message
author: Christina Chaniotaki
"""

import argparse
import copy
import json


def euclid(first_sub_list, last_sub_list, euclid_list):
    """
    Recursive function that finds the Euclidean rhythm.
    :param first_sub_list: The first item from the list
    :param last_sub_list: The last item from the list
    :param euclid_list: The list with the rhythm
    :return: euclid list
    """
    if last_sub_list == 0:
        return euclid_list
    else:
        for number in range(0, first_sub_list):
            if last_sub_list != 0:
                # put the last item at the end of the first item of the list
                euclid_list[number].extend(euclid_list[len(
                    euclid_list) - 1])
                # Remove the last item from the list.
                euclid_list.remove(euclid_list[len(euclid_list) - 1])
                last_sub_list -= 1
            else:
                break
        first_sub_list, len_from_first_list = 0, len(euclid_list[0])
        for number in range(0, len(euclid_list)):
            if len_from_first_list == len(euclid_list[number]):
                first_sub_list += 1
                # Find the number of smaller lists.
                last_sub_list, len_from_last_list = 0, len(
                    euclid_list[len(euclid_list) - 1])
        if len_from_last_list != len(euclid_list[0]):
            for number in range(0, len(euclid_list)):
                if len_from_last_list == len(euclid_list[number]):
                    last_sub_list += 1
        if last_sub_list == 1:
            return euclid_list
        return euclid(first_sub_list, last_sub_list, euclid_list)


def vector_space_f(euclid_list):
    """
    Function creates rhythm with the form of vector space.
    :param euclid_list: The list with the euclid rhythm
    :return: The vector space
    """
    vector_space = []
    for step in range(0, len(euclid_list)):
        vector = 1
        if euclid_list[step] == 1:
            while step + vector < len(euclid_list) and \
                            euclid_list[step + vector] == 0:
                vector += 1
            vector_space.append(vector)
    return vector_space


def euclid_string(vector_space):
    """
    The function finds if the rhythm is Euclidean strings.
    :param vector_space: The vector space
    :return: True or False if is a euclid string or not
    """
    if len(vector_space) > 1:
        reverse_vector_space_f = copy.copy(vector_space)
        reverse_number = len(reverse_vector_space_f)
        reverse_vector_space_f[0], reverse_vector_space_f[reverse_number - 1] \
            = reverse_vector_space_f[0] + 1, \
              reverse_vector_space_f[reverse_number - 1] - 1
        reverse_vector_space_f.reverse()
        return reverse_vector_space_f == vector_space
    return False


def recognize(rhythm, aces, length):
    """
    The fuction recognize if the rhythm is a Euclidean rhythm.
    :param rhythm: The musical rhythm
    :param aces: The number of aces
    :param length: The length of the rhythm
    :return: Return True if the Euclidean rhythm is the same with rhythm.
                Else return False
    """
    euclid_rhythm = [[1] for counter in range(aces)]
    for i in range(length - aces):
        euclid_rhythm.append([0])
    # Find the Euclidean rhythm.
    euclid_rhythm = euclid(aces, length - aces, euclid_rhythm)
    euclid_rhythm = [item for i in euclid_rhythm for item in i]
    return rhythm == euclid_rhythm


def hamming_distance(rhythms_1, rhythms_2):
    """
    Find the hamming distance from two rhythms
    :param rhythms_1: First rhythms
    :param rhythms_2: Second rhythm
    :return: The hamming distance
    """
    if len(rhythms_1) != len(rhythms_2):
        raise ValueError("Undefined for sequence of unequal length")
    return sum(bool(ord(ch_1) - ord(ch_2)) for ch_1, ch_2 in
               zip(rhythms_1, rhythms_2))


def display_message(euclid_rhythm, aces, length, musical_rhythm):
    """
    The display message.
    :param euclid_rhythm: The euclid rhythm
    :param aces: The number of aces
    :param length: The length from the rhythm
    :param musical_rhythm: The musical rhythm
    """
    # List rhythm to string rhythm.
    rhythm_string = "".join(str(euclid_rhythm[i]) for i in range(
        len(euclid_rhythm)))
    vector_space = vector_space_f(euclid_rhythm)  # Create the vector space.
    vector_space_string = "".join(str(vector_space[number]) for number in
                                  range(len(vector_space)))
    function = 'E({0},{1})'.format(aces, length)
    if function in musical_rhythm.keys():  # Check if has or not description.
        print('{0} = [{1}] = ({2}) {3}'.format(function, rhythm_string,
                                               vector_space_string,
                                               musical_rhythm[str(function)]))
    else:
        print('{0} = [{1}] = ({2})'.format(function, rhythm_string,
                                           vector_space_string))
    if euclid_string(vector_space):  # Check if is a Euclidean string.
        print('It is a Euclidean string.')
    vector_space.reverse()
    if euclid_string(vector_space):  # Check if is a reverse Euclidean string.
        print('It is a reverse Euclidean string.')


def all_euclid_rhythms(length, distance_dictionary, list_rhythms):
    """
    Find all the Euclidean rhythms.
    :param length: The length of the dictionary
    :param distance_dictionary: The distance between rhythms
    :param list_rhythms: List with the rhythms
    :return: distance_dictionary with all the Euclidean rhythms
    """
    for aces in range(1, length):  # Find all the Euclidean rhythms.
        euclid_list = [[1] for i in range(aces)]
        for counter in range(length - aces):
            euclid_list.append([0])
        # Find the Euclidean rhythm.
        euclid_list = euclid(aces, length - aces, euclid_list)
        euclid_rhythm = [value for i in euclid_list for value in i]
        rhythm_string = "".join(str(euclid_rhythm[i]) for i in range(
            len(euclid_rhythm)))
        # Find the distance between similar rhythms.
        distance = hamming_distance(list_rhythms, rhythm_string)
        # Create a dictionary: key=dictionary and value=list with rhythms.
        if distance in distance_dictionary.keys():
            distance_dictionary[distance].append(rhythm_string)
        else:
            distance_dictionary[distance] = [rhythm_string]
    return distance_dictionary


def display_message_similar_rhythm(distance_dictionary, length, musical_rhythm):
    """
    Display the message for similar rhythm
    :param distance_dictionary: The distance between rhythms
    :param length: The length of dictionary
    :param musical_rhythm: The musical rhythm
    :return:
    """
    for i in list(distance_dictionary.keys()):  # Sort the list in dictionary.
        distance_dictionary[i].sort(key=None, reverse=False)
    for distance in sorted(distance_dictionary.keys()):  # Display message.
        for rhythm in distance_dictionary[distance]:
            print("Distance =", distance)
            aces = 0
            for i in rhythm:
                if int(i) == 1:
                    aces += 1
            euclid_rhythm = [int(i) for i in rhythm]
            display_message(euclid_rhythm, aces, length, musical_rhythm)


def main():
    """Main of the project"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--SLOTS", type=int, help="the size of rhythm.")
    parser.add_argument("-p", "--PULSES", type=int, help="the number of hits.")
    parser.add_argument("-r", "--RECOGNIZE", type=str,
                        help="a rhythm in binary form for recognition "
                             "Euclidean rhythm.")
    parser.add_argument("-l", "--LIST_RhYTHMS", type=str,
                        help="a rhythm in binary to find similar rhythms.")
    args = parser.parse_args()
    # open the file and create dictionary
    file = open('musical_rythms.json', 'r')
    musical_rhythm = json.load(file)
    file.close()
    # The beginning of the program that calls the functions.
    if args.SLOTS and args.PULSES:  # Create the Euclidean rhythm.
        aces, length = args.PULSES, args.SLOTS
        euclid_list = [[1] for i in range(aces)]  # Create a list with aces.
        for i in range(length - aces):  # Add zeros to the list.
            euclid_list.append([0])
        # Create the Euclidean rhythm.
        euclid_list = euclid(aces, length - aces, euclid_list)
        rhythm = [x for i in euclid_list for x in i]
        # Display the message.
        display_message(rhythm, aces, length, musical_rhythm)
    elif args.RECOGNIZE:
        # Recognize if the rhythm is a Euclidean rhythm or not.
        rhythm = [int(i) for i in args.RECOGNIZE]
        # From string create a list with integers.
        aces, length = 0, len(rhythm)
        for i in rhythm:
            if int(i) == 1:
                aces += 1
        if recognize(rhythm, aces, length):
            display_message(rhythm, aces, length, musical_rhythm)
        else:
            print("Not a Euclidean rhythm.")
    elif args.LIST_RhYTHMS:  # Find similar rhythms.
        length, distance_dictionary = len(args.LIST_RhYTHMS), {}
        distance_dictionary = all_euclid_rhythms(length, distance_dictionary, args.LIST_RhYTHMS)
        display_message_similar_rhythm(distance_dictionary, length, musical_rhythm)
    else:  # No parameters.
        print("E(0,0) = [] = ()")


if __name__ == "__main__":
    main()
