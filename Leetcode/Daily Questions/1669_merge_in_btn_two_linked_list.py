class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        pointer1 = list1
        count = 1
        while count != a:
            pointer1 = pointer1.next
            count += 1
        
        pointer2 = pointer1.next
        while count != b + 1:
            pointer2 = pointer2.next
            count += 1
        
        pointer1.next = list2
        temp = list2
        while temp.next is not None:
            temp = temp.next
        
        temp.next = pointer2
        
        return list1

# soln = Solution()
# result = soln.mergeInBetween([10,1,13,6,9,5], 3, 4, [1000000,1000001,1000002])
# print(result)