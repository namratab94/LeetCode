'''
Problem Number: 146
Difficulty level: Hard
Link: https://leetcode.com/problems/lru-cache/
Author: namratabilurkar
'''
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache_dict = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache_dict:
            val = self.cache_dict[key]
            del self.cache_dict[key]
            self.cache_dict[key] = val
            return val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache_dict:
            if len(self.cache_dict) >= self.capacity:
                self.cache_dict.popitem(last=False)
            self.cache_dict[key] = value
        else:
            del self.cache_dict[key]
            self.cache_dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)