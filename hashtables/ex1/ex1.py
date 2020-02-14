#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Loop through wieghts and add to hashtable
    for index in range(len(weights)):
        # make the weight the key and the index the value
        hash_table_insert(ht, weights[index], index)
    
    # Compare the wieghts to the hashtable to find limit or 0
    for index in range(len(weights)):
        # variable to checking if its a match
        zero_check = limit - weights[index]
        # See if the zero_check is in the table as a key
        if hash_table_retrieve(ht, zero_check):
            # Set a var to the value for a matched key
            good_pair = hash_table_retrieve(ht, zero_check)
            # print(index, good_pair)
            print(good_pair, index)
            # Return the found value and the index that it was found at
            return(good_pair, index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

'''
Plan
Im goint to need to insert data into the hash table
Ill have to retrive it to check it against the data

two different for loops, one to insert one to check

the weights should be inserts as values and the limit could be the key

'''