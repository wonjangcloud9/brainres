class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError
