# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description
# RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.
# Implement the RandomizedCollection class:
# RandomizedCollection() Initializes the empty RandomizedCollection object.
# bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
# bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
# int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of the same values the multiset contains.
# You must implement the functions of the class such that each function works on average O(1) time complexity.
# Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection.

# Example 1:

# Input
# ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
# [[], [1], [1], [2], [], [1], []]
# Output
# [null, true, false, true, 2, true, 1]
# Explanation
# RandomizedCollection randomizedCollection = new RandomizedCollection();
# randomizedCollection.insert(1);   // return true since the collection does not contain 1.
#                                   // Inserts 1 into the collection.
# randomizedCollection.insert(1);   // return false since the collection contains 1.
#                                   // Inserts another 1 into the collection. Collection now contains [1,1].
# randomizedCollection.insert(2);   // return true since the collection does not contain 2.
#                                   // Inserts 2 into the collection. Collection now contains [1,1,2].
# randomizedCollection.getRandom(); // getRandom should:
#                                   // - return 1 with probability 2/3, or
#                                   // - return 2 with probability 1/3.
# randomizedCollection.remove(1);   // return true since the collection contains 1.
#                                   // Removes 1 from the collection. Collection now contains [1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 or 2, both equally likely.
# --- My solution
import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []                    # flat list of all values
        self.indices = defaultdict(set)   # val -> set of indices in nums

    def insert(self, val: int) -> bool:
        is_new = len(self.indices[val]) == 0
        self.indices[val].add(len(self.nums))
        self.nums.append(val)
        return is_new

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False

        # Pick any index that holds val, and get the last element
        remove_idx = next(iter(self.indices[val]))
        last_val   = self.nums[-1]
        last_idx   = len(self.nums) - 1

        # Overwrite remove_idx with the last element
        self.nums[remove_idx] = last_val

        # Update index sets
        self.indices[val].discard(remove_idx)
        self.indices[last_val].discard(last_idx)

        # Only re-add if we actually moved the last element somewhere new
        if remove_idx != last_idx:
            self.indices[last_val].add(remove_idx)

        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
# --- Test
randomizedCollection = RandomizedCollection()
print(randomizedCollection.insert(1))   
print(randomizedCollection.insert(1))   
print(randomizedCollection.insert(2))   
print(randomizedCollection.getRandom()) 
print(randomizedCollection.remove(1))   
print(randomizedCollection.getRandom()) 