
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None 

    def __str__(self): 
        output = ''
        current_node = self.head  
        while current_node is not None: 
            output += f'{current_node.value} ->'
            current_node = current_node.next_node
        return output

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def isEmpty(self, value):
        return True if self.head.value is None else False

    def get_max(self, value):
        if (self.isEmpty(self.head.value)):
            return str(-maxsize - 1)


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.hash_table = LinkedList()


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code 
        self.capacity = " "


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # len(MIN_CAPACITY)
        #  hash_table = [None] * 8
    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
    #    return __ % capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
    hash_bits = 64
    PNV_prime = 240 + 28 + 0xb3 = 1099511628211 
    offset_basis = 0
    offset_str = key 
    hash_mod = 2^hash_bits
    str_len = len(offset_str)
    for i=1; 1< str_len; ++i 
        offset_basis = (offset_basis * FNV_prime) % hash_mod
        offset_basis = xor(offset_basis, ord(substr(offset_str,i,1)))
    
    print hash_bits, offset_basis
      
      
    #   hash = offset_basis
    #         for each octet_of_data to be hashed
    #         hash = hash * FNV_prime
    #         hash = hash xor octet_of_data
    #         return hash

    #     64 bit FNV_prime = 240 + 28 + 0xb3 = 1099511628211    
    #     64 bit offset_basis = 14695981039346656037


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity
        index = HashTable(key, len(hash_table))
        hash_table[index] = key


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
    curr_node = self.hash_table.head
    if curr_node is not None:
        while curr_node.next is not None:
            for k in curr_node.value:
                if k == key:
                    node = curr_node
                    break
            curr_node = curr_ode.next

        if node == None:
            hash_table.append({key: value})
        else:
            node.value[key] = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
    curr_node = self.hash_table.head
    if curr_node is not None:
        while curr_node.next is not None:
            for k in curr_node.value:
                if k == key:
                    node = curr_tNode
                    break
            curr_node = curr_node.next

        if not node == None:
            return hash_table.remove_head(curr_node.value)

        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        node_storage = []
        curr_node = self.hash_table.head

        if curr_node is not None: 
            while curr_node.next is not None:
                node_storage.append(curr_node.value)
                curr_node = curr_node.next 
            node_storage.append(curr_node.value)
        return node_storage

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        return value % new_capacity


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
