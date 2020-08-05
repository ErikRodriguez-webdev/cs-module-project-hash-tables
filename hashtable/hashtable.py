class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8

# linked list to help prevent collisions of multiple hash nodes at an index in our hashtable
class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_tail(self, node):
        # check if linkedlist is empty and add node
        if self.head == None:
            self.head = node

        # linkedlist is not empty
        # set current to self.head
        current = self.head

      # while loop (while true)
        while True:
            # check if current.key is equal to key
            if current.key == node.key:
                # then update by setting current.value to node.value
                current.value = node.value
                print('Found existing node and updated value')
                break
            # check if current.next is None
            if current.next is None:
                # then insert by setting current.next to node
                current.next = node
                print('Successfully added new node to tail')
                break

            # now set current to current.next
            current = current.next

    def remove(self, key):
        # check if linkedlist is empty return because there is nothing to remove
        if self.head == None:
            return

        # check if linklist head pointer is the item to remove
        if self.head.key == key:
            self.head = self.head.next

        # linkedlist is more than two items
        # set current to self.head
        current = self.head

      # while loop (while true)
        while True:
            # check if current.next is None
            if current == None:
                print('Key not found')
                break
            # check if current.next.key is equal to key
            if current.next.key == key:
                # set current.next = current.next.next
                current.next = current.next.next
                print('Existing node was deleted')
                break

            # now set current to current.next
            current = current.next

    def find_value(self, key):
        # check if self.head == none
        if self.head == None:
            # return because no nodes in link
            return

        # linkedlist is not empty
        # set current to self.head
        current = self.head

      # while loop (while true)
        while True:
            # check if current.key is equal to key
            if current.key == key:
                # then return current value
                return current.value
            # check if current.next is None
            if current.next is None:
                # then return with print saying not found
                return print('Key not found')

            # now set current to current.next
            current = current.next


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # this creates our list multiplied with the capacity passed in
        self.capacity = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # return length of capacity
        return len(self.capacity)

    def get_load_factor(self):
        pass
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    # def fnv1(self, key):
    #     pass
    #     """
    #     FNV-1 Hash, 64-bit

    #     Implement this, and/or DJB2.
    #     """
    #     # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # hash is 5381
        hash = 5381

        # loop through all letters in key passed in
        for letter in key:
            # hash is now set to 5381 * 33 and add method ord to letter
            hash = (hash * 33) + ord(letter)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % length of self.capacity
        return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # set new_hash to create new hashtableentry and pass in key and value arguments to initialize
        new_hash = HashTableEntry(key, value)

        # set hash_index_num to self.hash_index and pass in new_hash.key
        hash_index_num = self.hash_index(key)

        # check if self.capacity[hash_index_num] is None
        if self.capacity[hash_index_num] == None:
            # initialize a linked list and set it to empty capacity index
            linked_list = LinkedList()
            linked_list.add_to_tail(new_hash)
            # now self.capacity[hash_index] is set to the new_hash created which will store both the key, value and next which points to none
            self.capacity[hash_index_num] = linked_list
        # else, then insert node to linkedlist at index
        else:
            self.capacity[hash_index_num].add_to_tail(new_hash)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # set hash_index_num to self.hash_index(key)
        hash_index_num = self.hash_index(key)

        # check if self.capacity[hash_index_num] is None, then no key found
        if self.capacity[hash_index_num] == None:
            return print("Key was not found")
        else:
            # then use self.capacity[hash_index_num] remove method on linked list to find key
            linked_list = self.capacity[hash_index_num]
            linked_list.remove(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # set hash_index_num to hash_index(key)
        hash_index_num = self.hash_index(key)

        # check if self.capacity[hash_index_num] is not None
        if self.capacity[hash_index_num] is not None:
            # then return the value from key
            return self.capacity[hash_index_num].find_value(key)

        # else, return none because key was not found
        else:
            return None

    def resize(self, new_capacity):
        pass
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
