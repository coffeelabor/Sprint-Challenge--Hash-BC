#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Loop through the tickets
    for ticket in tickets:
        # they will be inserted with hash_table, key = source, value = destination)
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    # Start off the trip with the destination of None so the loop knows where to start
    # route[0] = hash_table_retrieve(hashtable, "None")
    route[0] = hash_table_retrieve(hashtable, "NONE")

    # Loop through the length of the trip
    # for index in range(length):
    # for index in range(0, length):
    for index in range(1, length):
        # Make the key of the current place = the value of last stop
        key_source = route[index-1]
        # Find the value of the current place using the key var
        value_destination = hash_table_retrieve(hashtable, key_source)
        # for the current index, the destination should be set to the value
        print('value_destination/index', value_destination)
        route[index] = value_destination

    return route



'''
I need to set up up kinda like the last one
One loop for inserting the tickets in the hash table
The flights need to start at source None and end at destination None
I can match up the flights by either looking forward to where destination is source or the other way around
 
 '''


 '''
# Loop through the tickets
    for ticket in tickets:
        # they will be inserted with hash_table, key = source, value = destination)
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    # Loop through the length of the trip
    # for index in range(length):
    for index in range(0, length):
        # Make the key of the current place = the value of last stop
        key_source = route[index-1]
        # Find the value of the current place using the key var
        value_destination = hash_table_retrieve(hashtable, key_source)
        # for the current index, the destination should be set to the value
        print('value_destination/index', value_destination)
        route[index] = value_destination

    return route

 '''