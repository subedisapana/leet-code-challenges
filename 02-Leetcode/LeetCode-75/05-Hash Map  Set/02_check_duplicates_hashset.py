"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

def find_duplicates(keys):
    hashset = set()
    for key in keys:
        if key in hashset:
            return True
        hashset.add(key)
    return False

# Example usage:
keys = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 4]
print("Duplicates exist:", find_duplicates(keys))


