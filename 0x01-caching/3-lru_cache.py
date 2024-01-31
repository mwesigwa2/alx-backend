#!/usr/bin/env python3
'''
    Create a class LRUCache that inherits from BaseCaching
    and is a caching system:

    You must use self.cache_data - dictionary from the parent
    class BaseCaching
    You can overload def __init__(self): but don’t forget to
    call the parent init: super().__init__()
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value
    for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that
    BaseCaching.MAX_ITEMS:
    you must discard the least recently used item (LRU algorithm)
    you must print DISCARD: with the key discarded and following
    by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data,
    return None.
'''
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''
        class LRUCache that inherits from BaseCaching
        and is a caching system
    '''
    def __init__(self):
        '''
            initializes class
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
            Adds an item in the cache.
        '''
        if key is not None and item is not None:
            if key in self.cache_data:
                '''
                    If the key already exists, move it to the end to
                    mark it as most recently used
                '''
                self.cache_data.move_to_end(key)
            else:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    discarded_key, _ = self.cache_data.popitem(last=False)
                    print(f"DISCARD: {discarded_key}")

                self.cache_data[key] = item

    def get(self, key):
        '''
            Retrieves an item by key.
        '''
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end to mark it as most recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        else:
            return None
