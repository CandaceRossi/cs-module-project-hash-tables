class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


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
        self.capacity = capacity
        self.hash_table = [None] * self.capacity
        self.totalItems = 0
        self.max_Load_Factor =  0.70
        self.min_Load_Factor = 0.20


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        #count everytime we add an item
        #remove when we delete
        return len(self.hash_table)
        
    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        #return count % hash_table
        #triggers a resize
        return self.totalItems / self.get_num_slots()
        
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF
    #basic hashing function from scratch
    # def my_hash(s):
    #     string_utf = s.encode()

    #     total = 0
    #     for char in string_utf:
    #         total += char
    #         total &= 0xffffffff # limit total to 32 bits
    #     return total

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity
        #from scratch hash_index
        # hash_num = my_hash(key)
        # return hash_num % len(hash_table)

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        #basic hash function (not linked list version)
        # i = self.hash_index(key)
        # self.hash_table[i] = value

        #Linked list version
        #hash the key and get an index
        #find the start of the linked list using the index
        #if the key already exists in the link list
            #replace value
        #else
            #add new hashtable entry to the head of link list
        i = self.hash_index(key)
        current_node = self.hash_table[i]
        while current_node != None and current_node.key != key:
            current_node = i.next
            
        if current_node != None:
            self.hash_table[i] = value
            
            current_node = current_node.next
            self.get_load_factor()

        else: #if current_node is None:
            new_node = HashTableEntry(key, value)
            new_node.next = self.hash_table[i]
            self.hash_table[i] = new_node
            self.totalItems += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)

                
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # i = self.hash_index(key)
        # self.hash_table[i] = None
        
        #linked list version
        i = self.hash_index(key)
        current_node = self.hash_table[i]
        previous_node = None 

        while current_node != None and current_node.key != key:
            previous_node = current_node
            current_node = previous_node.next
            
        if current_node == None:
            #if current node is not there
            print("node does not exist")

        else: #if current_node is None:
            #if previous node is not there
            if previous_node is None:
                self.hash_table[i] = current_node.next 
            else: 
                previous_node.next = current_node.next 
            if self.get_load_factor() < self.min_Load_Factor:
                #have to have at least one byte in array / have to have at least 8 in hashtable
                if self.capacity > MIN_CAPACITY:
                    #change capacity
                    new_capacity = self.capacity // 2 
                    if new_capacity < MIN_CAPACITY:
                        new_capacity = MIN_CAPACITY
                    self.resize(new_capacity)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # i = self.hash_index(key) 
        # return self.hash_table[i]

        #linked list version
        i = self.hash_index(key)
        node = self.hash_table[i]
        while node != None:
            print("Hey There", node.key)
            if node.key == key:
                print("node key", node.value, key)
                return node.value
            node = node.next
        # index = self.hash_index(key) 
        
        # node = self.hash_table[index]
        # print("this is node", node)
        # while node:
        #     if node.key == key:
        #         print("Node value: ", node.value)
        #         return node.value
        #     node = node.next

               
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # return (self.capacity * 2) % totalItems

        # if load factor is too high, resize
        #too high == industry standard is over 0.7
        #check load factor after every insertion
        # if load factor is too small, downsize under 0.2

        #make a new array that is double the current size
        # newSize = self.capacity * 2
        # newHashTable = HashTable(newSize)
        #new array now needs to be populated with the data
        #go through each linked list in array
        #go through each item and rehash it
        new_arr = []
        old_hashtable = self.hash_table
        self.capacity = new_capacity
        self.hash_table = [None] * self.capacity
        current_node = None 
        old_totalItems = self.totalItems
        for item in old_hashtable:
            current_node = item
            while current_node is not None:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next
        self.totalItems = old_totalItems
                #insert the items into their new locations
        # self.capacity = newSize
        #forget about old array or delete or something ??

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
