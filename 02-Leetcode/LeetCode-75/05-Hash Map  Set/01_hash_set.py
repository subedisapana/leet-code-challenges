class MyHashSet:
    def __init__(self):
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset

# Example usage:
myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))  # Output: True
print(myHashSet.contains(3))  # Output: False
myHashSet.add(2)
print(myHashSet.contains(2))  # Output: True
myHashSet.remove(2)
print(myHashSet.contains(2))  # Output: False
