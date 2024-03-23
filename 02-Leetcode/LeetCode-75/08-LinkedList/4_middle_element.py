class Solution(object):
    def FindLength(self,head):
        temp = head
        cnt = 0
        while temp:
            cnt+=1
            temp=temp.next
        return cnt
    def middleNode(self, head):
        length = self.FindLength(head)
        mid = length//2
        cnt = 0
        temp = head
        while temp:
            if cnt==mid:
                return temp
            cnt+=1
            temp = temp.next